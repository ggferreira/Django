from typing import List

from django.db.models import Prefetch

from pypro.modulos.models import Modulo, Aula


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista modulos ordenados por titulos
    :return:
    """
    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_aulas_de_modulo_ordenadas(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())


def encontrar_aula(slug: str):
    return Aula.objects.select_related('modulo').get(slug=slug)


def listar_modulos_com_aulas():
    aula_ordenadas = Aula.objects.order_by('order')
    return Modulo.objects.order_by('order').prefetch_related(
        Prefetch('aula_set', queryset=aula_ordenadas, to_attr='aulas')
    ).all()
