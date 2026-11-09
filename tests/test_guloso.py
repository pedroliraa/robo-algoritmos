"""Testes da regra gulosa (Pessoa 4 completa)."""

import unittest

from robo.guloso import guloso

EXEMPLO = [[2, 1, 9, 9, 9],
           [3, None, 1, 1, 9],
           [1, 1, 1, None, 2],
           [9, 9, 1, 1, 1]]


class TestGuloso(unittest.TestCase):

    def test_exemplo_do_enunciado_da_26(self):
        self.assertEqual(guloso(EXEMPLO), 26)

    # TODO (Pessoa 4): grade própria (até 4x4) onde o guloso erra
    # + um caso em que o guloso fica preso (deve devolver None).


if __name__ == "__main__":
    unittest.main()
