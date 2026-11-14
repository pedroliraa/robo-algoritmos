INF = float('inf')


def contar_chamadas(mapa):
    """Quantas vezes a função recursiva foi chamada para esse mapa.
    Regra usada: só chama o vizinho se ele estiver dentro da grade
    (chamadas 'fora da grade' não são contadas)."""
    linhas, colunas = len(mapa), len(mapa[0])
    chamadas = 0

    def custo(i, j):
        nonlocal chamadas
        chamadas += 1

        if mapa[i][j] is None:
            return INF
        if i == linhas - 1 and j == colunas - 1:
            return mapa[i][j]

        melhor = INF
        if j + 1 < colunas:
            melhor = min(melhor, custo(i, j + 1))
        if i + 1 < linhas:
            melhor = min(melhor, custo(i + 1, j))
        return mapa[i][j] + melhor

    custo(0, 0)
    return chamadas
