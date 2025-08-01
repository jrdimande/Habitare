import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filename = os.path.join(BASE_DIR, "storage", "pagamentos.json")

def dump(PagamentoController):
    """Salvar os dados nor arquivo .json"""
    dados = {"pagamentos": []}

    for pagamento in PagamentoController.pagamentos:
        actual = {
            "id": pagamento.id_pagamento,
            "id_inquilino": pagamento.id_inquilino,
            "valor": pagamento.valor,
            "data": pagamento.data_de_pagamento
        }
        dados["pagamentos"].append(actual)

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)


def load():
    """Carregar os dados n arquivo .json"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    try:
        with open(filename, "r", encoding="utf-8") as f:
            pagamentos = json.load(f)
        return pagamentos
    except FileNotFoundError:
        return {"pagamentos": []}
