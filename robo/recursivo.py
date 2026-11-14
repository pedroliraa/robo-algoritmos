def recursivo(mapa) -> int | None:
    linhas = len(mapa)
    colunas = len(mapa[0])

    def custo(i, j):
        # fora da grade ou obstáculo
        if i >= linhas or j >= colunas or mapa[i][j] is None:
            return float("inf")
        # chegada
        if i == linhas - 1 and j == colunas - 1:
            return mapa[i][j]
        # caso geral
        return mapa[i][j] + min(custo(i, j + 1), custo(i + 1, j))

    resultado = custo(0, 0)
    return None if resultado == float("inf") else resultado