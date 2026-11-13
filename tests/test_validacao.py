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
    def test_valor_zero(self):
        mapa, erro = validar('{"custos": [[0, 2]]}')
        self.assertIsNone(mapa)
        self.assertIsNotNone(erro)
    def test_texto_vazio(self):
        mapa, erro = validar("")
        self.assertIsNone(mapa)
        self.assertIsNotNone(erro)

    def test_raiz_e_lista(self):
        mapa, erro = validar('[[1, 2]]')
        self.assertIsNone(mapa)
        self.assertIsNotNone(erro)

    def test_chave_matriz(self):
        mapa, erro = validar('{"matriz": [[1, 2]]}')
        self.assertIsNone(mapa)
        self.assertIsNotNone(erro)

    def test_custos_vazio(self):
        mapa, erro = validar('{"custos": []}')
        self.assertIsNone(mapa)
        self.assertIsNotNone(erro)

    def test_linha_vazia(self):
        mapa, erro = validar('{"custos": [[]]}')
        self.assertIsNone(mapa)
        self.assertIsNotNone(erro)

    def test_linhas_tamanhos_diferentes(self):
        mapa, erro = validar('{"custos": [[1, 2], [3]]}')
        self.assertIsNone(mapa)
        self.assertIsNotNone(erro)

    def test_valor_string(self):
        mapa, erro = validar('{"custos": [[1, "a"]]}')
        self.assertIsNone(mapa)
        self.assertIsNotNone(erro)

    def test_valor_string_numerica(self):
        mapa, erro = validar('{"custos": [["1", 2]]}')
        self.assertIsNone(mapa)
        self.assertIsNotNone(erro)

    def test_valor_decimal(self):
        mapa, erro = validar('{"custos": [[1.5, 2]]}')
        self.assertIsNone(mapa)
        self.assertIsNotNone(erro)

    def test_valor_negativo(self):
        mapa, erro = validar('{"custos": [[-1, 2]]}')
        self.assertIsNone(mapa)
        self.assertIsNotNone(erro)

    def test_valor_true(self):
        mapa, erro = validar('{"custos": [[true, 2]]}')
        self.assertIsNone(mapa)
        self.assertIsNotNone(erro)

    def test_custos_nao_e_lista(self):
        mapa, erro = validar('{"custos": 5}')
        self.assertIsNone(mapa)
        self.assertIsNotNone(erro)

    # --- inventados pelo grupo ---
    def test_inventado_nan(self):
        mapa, erro = validar('{"custos": [[1, NaN]]}')
        self.assertIsNone(mapa)
        self.assertIsNotNone(erro)

    def test_inventado_lista_dentro_de_lista(self):
        mapa, erro = validar('{"custos": [[[1], 2]]}')
        self.assertIsNone(mapa)
        self.assertIsNotNone(erro)
    

if __name__ == "__main__":
    unittest.main()
