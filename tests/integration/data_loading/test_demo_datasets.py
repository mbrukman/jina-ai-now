"""
This suite tests that the demo datasets are available
behind their URLs.
"""
import pytest
import requests
from starlette import status

from now.constants import (
    AVAILABLE_DATASET,
    DEMO_DATASET_DOCARRAY_VERSION,
    Modalities,
    Qualities,
)
from now.data_loading.utils import get_dataset_url


@pytest.mark.parametrize(
    'modality, ds_name',
    [(m, d[0]) for m in Modalities() for d in AVAILABLE_DATASET[m]],
)
@pytest.mark.parametrize('quality', [q for q in Qualities()])
def test_dataset_is_available(
    ds_name: str,
    modality: Modalities,
    quality: Qualities,
):
    url = get_dataset_url(ds_name, quality, modality)

    assert requests.head(url).status_code == status.HTTP_200_OK


@pytest.mark.parametrize(
    'ds_url',
    [
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/jpeg/nft-monkey.img10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/jpeg/deepfashion.img10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/jpeg/nih-chest-xrays.img10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/jpeg/stanford-cars.img10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/jpeg/bird-species.img10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/jpeg/best-artworks.img10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/jpeg/geolocation-geoguessr.img10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/text/rock-lyrics.txt10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/text/pop-lyrics.txt10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/text/rap-lyrics.txt10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/text/indie-lyrics.txt10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/text/metal-lyrics.txt10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/jpeg/deepfashion.txt10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/jpeg/nih-chest-xrays.txt10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/jpeg/stanford-cars.txt10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/jpeg/bird-species.txt10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/jpeg/best-artworks.txt10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/jpeg/geolocation-geoguessr.txt10-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/music/music-genres-mid-song5-{}.bin",
        "https://storage.googleapis.com/jina-fashion-data/data/one-line/datasets/music/music-genres-mix-song5-{}.bin",
    ],
)
def test_sample_data_is_available(ds_url: str):
    assert (
        requests.head(url=ds_url.format(DEMO_DATASET_DOCARRAY_VERSION)).status_code
        == status.HTTP_200_OK
    )
