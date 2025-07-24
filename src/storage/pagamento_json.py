import json
from src.controllers.PagamentoController import PagamentoController

def dump(PagamentoController):
    """ Salvar os dados no arquivo .json """
    PagamentoController = PagamentoController()
    filename = "dados.json"

    dados = {"Pagamentos" : []}

    for pagamento in PagamentoController.pagamentos:
        actual = {"id" : pagamento.id_pagamento,
                  "id_inquilino" : pagamento.id_inquilino,
                  "valor" : pagamento.valor,
                  "data" : pagamento.data_de_pagamento
                  }
        dados["Pagamentos"].append(actual)

    with open(filename, "w") as f:
        json.dump(dados, f, indent=4)


def load():
    """ Carregar os dados n arquivo .json"""
    filename = "dados.json"
    try:
        with open(filename, "r") as f:
            pagamentos = json.load(f)
        return pagamentos
    except FileNotFoundError:
        return {"Pagamentos" : []}
