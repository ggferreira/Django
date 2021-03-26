import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    [
        'Abertura do Curso',
        'Video Aperitivo: Motivação',
    ]
)
def test_title_video(resp, titulo):
    assert_contains(resp, titulo)


@pytest.mark.parametrize(
    'slug',
    [
        'abertura',
        'motivacao',
    ]
)
def test_link_video(resp, slug):
    assert_contains(resp, reverse('aperitivos:video', args=(slug,)))
