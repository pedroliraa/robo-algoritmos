"""Validação da entrada."""


def validar(texto: str):
    """Recebe o texto JSON. Devolve (mapa, None) se válido,
    ou (None, "mensagem de erro") se inválido.

    Exemplo válido:   '{"custos": [[2, 1], [3, 4]]}'  ->  ([[2, 1], [3, 4]], None)
    Exemplo inválido: '{"custos": [[1, "a"]]}'        ->  (None, "mensagem")
    """
    raise NotImplementedError("Pessoa 2: implementar validar()")
