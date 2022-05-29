from typing import Dict, List

from docarray import DocumentArray
from now_common import options

from now.apps.base.app import JinaNOWApp
from now.constants import Modalities
from now.run_backend import finetune_flow_setup


class image_to_text(JinaNOWApp):
    @property
    def description(self) -> str:
        return 'Image to text search'

    @property
    def input_modality(self) -> str:
        return Modalities.IMAGE

    @property
    def output_modality(self) -> str:
        return Modalities.TEXT

    @property
    def options(self) -> List[Dict]:
        return [options.QUALITY_CLIP]

    def setup(self, da: DocumentArray, user_config: Dict, kubectl_path) -> Dict:
        return finetune_flow_setup(self, da, user_config, kubectl_path)