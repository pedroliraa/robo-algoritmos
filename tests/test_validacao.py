"""Testes de entrada inválida (Pessoa 2 completa)."""

import unittest

from robo.resolver import resolver
from robo.validacao import validar


class TestValidacao(unittest.TestCase):

    def test_json_quebrado_e_invalido(self):
        mapa, erro = validar('{"custos": [[1, 2]')   # falta fechar ] e }
        self.assertIsNone(mapa)
        self.assertIsNotNone(erro)

    def test_resolver_devolve_entrada_invalida(self):
        resposta = resolver('isto nao e json')
        self.assertEqual(resposta["status"], "entrada_invalida")
        self.assertIn("erro", resposta)

    # TODO (Pessoa 2): um teste para cada entrada inválida da tabela do
    # enunciado (são 11) + 1 inventado pelo grupo.


if __name__ == "__main__":
    unittest.main()
