"""Validação da entrada."""

import json


def validar(texto: str):
    """Recebe o texto JSON. Devolve (mapa, None) se válido,
    ou (None, "mensagem de erro") se inválido.
    """
    if not isinstance(texto, str):
        return None, "a entrada deve ser um texto JSON"

    try:
        dados = json.loads(texto)
    except json.JSONDecodeError:
        return None, "JSON inválido"

    if not isinstance(dados, dict):
        return None, 'a entrada deve ser um objeto com a chave "custos"'
    if "custos" not in dados:
        return None, 'falta a chave "custos"'

    mapa = dados["custos"]
    if not isinstance(mapa, list) or len(mapa) == 0:
        return None, '"custos" deve ser uma lista não vazia'

    colunas = len(mapa[0]) if isinstance(mapa[0], list) else None
    for i, linha in enumerate(mapa):
        if not isinstance(linha, list) or len(linha) == 0:
            return None, f"a linha {i} deve ser uma lista não vazia"
        if len(linha) != colunas:
            return None, f"a linha {i} tem tamanho diferente"
        for j, v in enumerate(linha):
            if v is not None and not (type(v) is int and v > 0):
                return None, f"valor inválido na posição ({i}, {j})"

    return mapa, None