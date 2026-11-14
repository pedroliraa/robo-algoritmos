import unittest

from robo.guloso import guloso

EXEMPLO = [[2, 1, 9, 9, 9],
           [3, None, 1, 1, 9],
           [1, 1, 1, None, 2],
           [9, 9, 1, 1, 1]]

# Grade própria: o guloso escolhe o 1 (barato agora) e entra na linha de 8 e 9.
# Ótimo: 2 -> 3 -> 2 -> 1 -> 1 = 9.  Guloso: 2 -> 1 -> 8 -> 9 -> 1 = 21.
GRADE_PROPRIA = [[2, 1, 8],
                 [3, 9, 9],
                 [2, 1, 1]]


class TestGuloso(unittest.TestCase):

    def test_exemplo_da_26(self):
        self.assertEqual(guloso(EXEMPLO), 26)

    def test_grade_propria_guloso_erra(self):
        self.assertEqual(guloso(GRADE_PROPRIA), 21)  # o ótimo seria 9

    def test_fica_preso(self):
        self.assertIsNone(guloso([[1, None], [None, 1]]))

    def test_partida_obstaculo(self):
        self.assertIsNone(guloso([[None, 1], [1, 1]]))

    def test_empate_vai_para_direita(self):
        # direita 2 = baixo 2: vai para a direita e depois desce
        self.assertEqual(guloso([[1, 2], [2, 1]]), 4)

    def test_grade_1x1(self):
        self.assertEqual(guloso([[5]]), 5)


if __name__ == "__main__":
    unittest.main()
