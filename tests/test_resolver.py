
"""Testes de ponta a ponta: ok e sem_caminho (Pessoa 3 completa)."""

import json
import unittest

from robo.recursivo import recursivo
from robo.resolver import resolver


EXEMPLO = '{"custos": [[2,1,9,9,9],[3,null,1,1,9],[1,1,1,null,2],[9,9,1,1,1]]}'


def entrada(mapa):
    return json.dumps({"custos": mapa})


class TestResolver(unittest.TestCase):

    def assertOk(self, mapa, esperado):
        self.assertEqual(
            resolver(entrada(mapa)),
            {"status": "ok", "custo": esperado}
        )

    def assertSemCaminho(self, mapa):
        self.assertEqual(
            resolver(entrada(mapa)),
            {"status": "sem_caminho", "custo": None}
        )

    # --- Casos do enunciado ---

    def test_exemplo_do_enunciado(self):
        self.assertEqual(
            resolver(EXEMPLO),
            {"status": "ok", "custo": 11}
        )

    def test_ok_uma_casa(self):
        self.assertOk([[7]], 7)

    def test_ok_uma_linha(self):
        self.assertOk([[1, 2, 3]], 6)

    def test_ok_uma_coluna(self):
        self.assertOk([[1], [2], [3]], 6)

    def test_ok_2x3(self):
        mapa = [
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assertOk(mapa, 4)

    def test_ok_desvia_de_obstaculo_oficial(self):
        mapa = [
            [1, 1, None],
            [2, None, 1],
            [1, 1, 1]
        ]
        # Caminho: 1 + 2 + 1 + 1 + 1 = 6
        self.assertOk(mapa, 6)

    # --- Testes adicionais com caminho ---

    def test_ok_2x2_escolhe_o_mais_barato(self):
        # Direita: 1+2+1 = 4
        # Baixo: 1+3+1 = 5
        self.assertOk([[1, 2], [3, 1]], 4)

    def test_ok_desvia_de_obstaculo(self):
        # Caminho: 1 -> 2 -> 3 -> 1 = 7
        self.assertOk(
            [[1, 2, None],
             [None, 3, 1]],
            7
        )

    # --- Casos sem caminho ---

    def test_sem_caminho_chegada_e_obstaculo(self):
        self.assertSemCaminho(
            [[1, 1, 1],
             [None, None, 1],
             [1, 1, None]]
        )

    def test_sem_caminho_partida_e_obstaculo(self):
        self.assertSemCaminho(
            [[None, 1],
             [1, 1]]
        )

    def test_sem_caminho_parede_de_obstaculos(self):
        self.assertSemCaminho(
            [[1, None],
             [None, 1]]
        )

    def test_sem_caminho_uma_casa_bloqueada(self):
        self.assertSemCaminho([[None]])

    def test_sem_caminho_preso_no_meio(self):
        self.assertSemCaminho(
            [[2, 3, 1],
             [None, 4, None],
             [1, None, 5]]
        )

    # --- Casos criados pelo grupo ---

    def test_grupo_3x3_conferido_a_mao(self):
        mapa = [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]
        # Melhor: direita, direita, baixo, baixo
        # Custo: 1 + 3 + 1 + 1 + 1 = 7
        self.assertOk(mapa, 7)

    def test_grupo_3x3_com_obstaculo_no_centro(self):
        mapa = [
            [1, 2, 3],
            [4, None, 1],
            [5, 6, 1]
        ]
        # Por cima: 1+2+3+1+1 = 8
        # Por baixo: 1+4+5+6+1 = 17
        self.assertOk(mapa, 8)

    def test_grupo_caminho_com_menor_custo(self):
        mapa = [
            [1, 9, 9],
            [1, 9, 9],
            [1, 1, 1]
        ]
        # Desce pela primeira coluna e segue à direita
        # Custo: 1+1+1+1+1 = 5
        self.assertOk(mapa, 5)

    # --- Testes complementares ---

    def test_recursivo_devolve_none_e_inteiro(self):
        self.assertIsNone(
            recursivo([[1, None], [None, 1]])
        )
        self.assertIsInstance(
            recursivo([[1, 2], [3, 1]]),
            int
        )

    def test_entrada_invalida_passa_pelo_resolver(self):
        resposta = resolver('{"custos": [[1, "a"]]}')
        self.assertEqual(
            resposta["status"],
            "entrada_invalida"
        )


if __name__ == "__main__":
    unittest.main()
