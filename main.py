from robo.resolver import resolver
from robo.contagem import contar_chamadas
from robo.guloso import guloso
from robo.recursivo import recursivo

EXEMPLO = [[2, 1, 9, 9, 9],
           [3, None, 1, 1, 9],
           [1, 1, 1, None, 2],
           [9, 9, 1, 1, 1]]

GRADE_PROPRIA = [[2, 1, 8],
                 [3, 9, 9],
                 [2, 1, 1]]


def grade_de_uns(linhas, colunas):
    return [[1] * colunas for _ in range(linhas)]


def main():
    print("=== Grade do exemplo ===")
    entrada = '{"custos": [[2,1,9,9,9],[3,null,1,1,9],[1,1,1,null,2],[9,9,1,1,1]]}'
    print("resolver :", resolver(entrada))
    print("guloso   :", guloso(EXEMPLO), "(recursivo:", recursivo(EXEMPLO), ")")

    print("\n=== Grade própria onde o guloso erra ===")
    print("recursivo (ótimo):", recursivo(GRADE_PROPRIA))
    print("guloso           :", guloso(GRADE_PROPRIA))

    print("\n=== Contagem de chamadas ===")
    print(f"{'Grade':<10}{'Chamadas':>10}")
    for l, c in [(2, 3), (3, 3), (6, 6), (10, 10), (1, 10)]:
        print(f"{l}x{c:<8}{contar_chamadas(grade_de_uns(l, c)):>10,}".replace(",", "."))
    print(f"{'Exemplo':<10}{contar_chamadas(EXEMPLO):>10}")


if __name__ == "__main__":
    main()
