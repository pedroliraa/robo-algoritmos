"""Junta as peças: valida a entrada e calcula o custo."""

from robo.recursivo import recursivo
from robo.validacao import validar


def resolver(entrada: str) -> dict:
    """{"status": "ok", "custo": 11}
    {"status": "sem_caminho", "custo": None}
    {"status": "entrada_invalida", "erro": "mensagem"}
    """
    mapa, erro = validar(entrada)
    if erro is not None:
        return {"status": "entrada_invalida", "erro": erro}

    custo = recursivo(mapa)
    if custo is None:
        return {"status": "sem_caminho", "custo": None}

    return {"status": "ok", "custo": custo}
