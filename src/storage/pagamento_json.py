import json


filename = "pagamentos.json"

def dump(PagamentoController):
    """ Salvar os dados no arquivo .json """

    PagamentoController = PagamentoController

    dados = {"pagamentos" : []}

    for pagamento in PagamentoController.pagamentos:
        actual = {"id" : pagamento.id_pagamento,
                  "id_inquilino" : pagamento.id_inquilino,
                  "valor" : pagamento.valor,
                  "data" : pagamento.data_de_pagamento
                  }
        dados["pagamentos"].append(actual)

    with open(filename, "w") as f:
        json.dump(dados, f, indent=4)


def load():
    """ Carregar os dados n arquivo .json"""
    try:
        with open(filename, "r") as f:
            pagamentos = json.load(f)
        return pagamentos
    except Exception:
        return {"pagamentos" : []}

