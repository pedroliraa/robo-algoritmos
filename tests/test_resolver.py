"""Testes de ponta a ponta: ok e sem_caminho (Pessoa 3 completa)."""

import unittest

from robo.resolver import resolver

EXEMPLO = '{"custos": [[2,1,9,9,9],[3,null,1,1,9],[1,1,1,null,2],[9,9,1,1,1]]}'


class TestResolver(unittest.TestCase):

    def test_exemplo_do_enunciado(self):
        self.assertEqual(resolver(EXEMPLO), {"status": "ok", "custo": 11})

    # TODO (Pessoa 3): casos da tabela do enunciado (custo 7, 6, 4, 11, 6
    # e os 4 sem caminho) + 3 casos criados pelo grupo.


if __name__ == "__main__":
    unittest.main()
