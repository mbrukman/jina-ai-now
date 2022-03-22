import os.path
from os.path import join as osp
from time import sleep

import requests
from yaspin import yaspin

from now.deployment.deployment import apply_replace
from now.deployment.flow import cmd, wait_for_lb


def run(
    data,
    gateway_host,
    gateway_port,
    gateway_host_internal,
    gateway_port_internal,
    docker_frontend_tag,
    tmpdir,
    kubectl_path,
    **kwargs,
):
    # deployment
    with yaspin(text="Deploy frontend", color="green") as spinner:
        deploy_path = osp(tmpdir, 'src/deployment')
        if not os.path.exists(deploy_path):
            os.makedirs(deploy_path)
        apply_replace(
            deploy_path + '/k8s_frontend-deployment.yml',
            {
                'data': data,
                'gateway_host': gateway_host_internal,
                'gateway_port': gateway_port_internal,
                'docker_frontend_tag': docker_frontend_tag,
            },
            kubectl_path,
        )

        if gateway_host == 'localhost':
            cmd(f'{kubectl_path} apply -f {deploy_path}/k8s_frontend-svc-node.yml')
            while True:
                try:
                    url = 'http://localhost:30080'
                    requests.get(url)
                    break
                except Exception:
                    sleep(1)
            frontend_host = 'http://localhost'
            frontend_port = '30080'
        else:
            cmd(f'{kubectl_path} apply -f {deploy_path}/k8s_frontend-svc-lb.yml')
            frontend_host = f'http://{wait_for_lb("frontend-lb", "nowapi")}'
            frontend_port = '80'

        spinner.ok('🚀')
        return frontend_host, frontend_port


if __name__ == '__main__':
    run(
        'best-artworks',
        'remote',
        None,
        'gateway.nowapi.svc.cluster.local',
        '8080',
        docker_frontend_tag='0.0.1',
    )
    # 31080