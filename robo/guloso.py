def guloso(mapa):
    """Vai sempre para o vizinho livre mais barato (direita no empate).
    None se ficar preso."""
    linhas, colunas = len(mapa), len(mapa[0])
    i, j = 0, 0

    if mapa[0][0] is None:
        return None

    total = mapa[0][0]

    while (i, j) != (linhas - 1, colunas - 1):
        direita = mapa[i][j + 1] if j + 1 < colunas else None
        baixo = mapa[i + 1][j] if i + 1 < linhas else None

        if direita is None and baixo is None:
            return None  # preso

        if baixo is None or (direita is not None and direita <= baixo):
            j += 1
            total += direita
        else:
            i += 1
            total += baixo

    return total
