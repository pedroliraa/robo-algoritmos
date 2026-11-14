import unittest

from robo.contagem import contar_chamadas

EXEMPLO = [[2, 1, 9, 9, 9],
           [3, None, 1, 1, 9],
           [1, 1, 1, None, 2],
           [9, 9, 1, 1, 1]]


def grade_de_uns(linhas, colunas):
    return [[1] * colunas for _ in range(linhas)]


class TestContagem(unittest.TestCase):

    def test_2x3(self):
        self.assertEqual(contar_chamadas(grade_de_uns(2, 3)), 9)

    def test_3x3(self):
        self.assertEqual(contar_chamadas(grade_de_uns(3, 3)), 19)

    def test_6x6(self):
        self.assertEqual(contar_chamadas(grade_de_uns(6, 6)), 923)

    def test_10x10(self):
        self.assertEqual(contar_chamadas(grade_de_uns(10, 10)), 184755)

    def test_1x10(self):
        self.assertEqual(contar_chamadas(grade_de_uns(1, 10)), 10)

    def test_exemplo(self):
        self.assertEqual(contar_chamadas(EXEMPLO), 43)


if __name__ == "__main__":
    unittest.main()
