# Robô na grade: rota de menor custo

Projeto de Algoritmos. Calcula o custo da rota mais barata de um robô numa grade
(só anda para a direita ou para baixo, desviando de obstáculos) usando **recursão pura**,
e compara com uma **regra gulosa**.

- **Entrega 1:** recursão sem memoização, contagem de chamadas e regra gulosa.
- **Entrega 2:** (a definir) deve evoluir a partir deste mesmo código.

## Integrantes

| Pessoa | Parte | Nome |
|---|---|---|
| 1 | Base, `resolver`, integração e montagem do relatório | |
| 2 | Descrição do problema + `validar` e testes de entrada inválida | |
| 2 | `recursivo`, testes ok/sem_caminho e "por que funciona" | |
| 1 | `contar_chamadas` e `guloso` | |

## Requisitos

- Python 3.10 ou mais novo. Só biblioteca padrão (`json`, `unittest`): **nada para instalar**.

## Como rodar

No Windows, se `python` não funcionar, use `py` no lugar.

```bash
python -m unittest discover -v   # roda todos os testes
python main.py                   # exemplo do enunciado + tabela de contagem
```

## Estrutura

```
robo/
├── validacao.py   validar(texto)          -> Pessoa 2
├── recursivo.py   recursivo(mapa)         -> Pessoa 3
├── resolver.py    resolver(entrada)       -> Pessoa 1
├── contagem.py    contar_chamadas(mapa)   -> Pessoa 4
└── guloso.py      guloso(mapa)            -> Pessoa 4
tests/             test_validacao.py, test_resolver.py, test_guloso.py
main.py            exemplo + tabela de contagem
relatorio/         rascunhos de cada um + PDF final
```

## Regras da dupla

- **Não mudar nomes nem assinaturas** do contrato (`validar`, `recursivo`, `resolver`,
  `contar_chamadas`, `guloso`, e os campos `status`, `custo`, `erro`) sem avisar no grupo.
- **Entrega 1 proíbe memoização:** nada de cache, dicionário de resultados, `global`
  guardando resultados ou `@lru_cache`. O contador de chamadas pode usar variável externa.
- "Impossível" dentro da recursão = `float('inf')`; só no final vira `None`.
- `main` = versão de entrega. `develop` = integração. Cada pessoa cria a sua branch
  **a partir da `develop`** e abre Pull Request **para a `develop`**:
  `feature/validacao`, `feature/recursivo`, `feature/contagem-guloso`.
- Antes de começar: `git checkout develop` e `git pull`.
- Todo mundo precisa entender o código inteiro: o professor usa a apresentação como evidência.
