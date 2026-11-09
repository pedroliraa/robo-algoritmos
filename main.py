
from robo.contagem import contar_chamadas
from robo.guloso import guloso
from robo.resolver import resolver

EXEMPLO_TEXTO = '{"custos": [[2,1,9,9,9],[3,null,1,1,9],[1,1,1,null,2],[9,9,1,1,1]]}'
EXEMPLO_MAPA = [[2, 1, 9, 9, 9],
                [3, None, 1, 1, 9],
                [1, 1, 1, None, 2],
                [9, 9, 1, 1, 1]]


def grade_de_uns(linhas, colunas):
    """Grade só com 1s, usada na tabela de contagem."""
    return [[1] * colunas for _ in range(linhas)]


def tentar(funcao, *args):
    """Chama a função; se ainda não foi implementada, avisa em vez de quebrar."""
    try:
        return funcao(*args)
    except NotImplementedError:
        return "pendente"


def main():
    print("=== Exemplo do enunciado ===")
    print("resolver:", tentar(resolver, EXEMPLO_TEXTO), "  (esperado: custo 11)")
    print("guloso:  ", tentar(guloso, EXEMPLO_MAPA), "  (esperado: 26)")

    print()
    print("=== Contagem de chamadas da recursão ===")
    print(f"{'Grade':<10}{'Chamadas':>12}{'Referência':>14}")
    grades = [
        ("2x3", grade_de_uns(2, 3), "9"),
        ("3x3", grade_de_uns(3, 3), "19"),
        ("6x6", grade_de_uns(6, 6), "923"),
        ("10x10", grade_de_uns(10, 10), "184.755"),
        ("1x10", grade_de_uns(1, 10), "10"),
        ("exemplo", EXEMPLO_MAPA, "43*"),
    ]
    for nome, grade, referencia in grades:
        chamadas = tentar(contar_chamadas, grade)
        if isinstance(chamadas, int):
            chamadas = f"{chamadas:,}".replace(",", ".")
        print(f"{nome:<10}{str(chamadas):>12}{referencia:>14}")
    print("* 43 contando também as chamadas que caem em obstáculo (ver escopo).")


if __name__ == "__main__":
    main()
