import json
from src.controllers.InquilinoController import InquilinoController

def dump(inc):
    """ Salvar os dados no arquivo .json """
    InquilinoController = inc
    filename = "inquilinos.json"

    dados = {"inquilinos" : []}

    for inquilino in InquilinoController.inquilinos:
        actual = {"id" : inquilino.id,
                  "nome" : inquilino.nome,
                  "contacto" : inquilino.contacto,
                  "data_de_entrada" : inquilino.data_de_entrada,
                  "imovel" : inquilino.casa
                  }
        dados["inquilinos"].append(actual)

    with open(filename, "w") as f:
        json.dump(dados, f, indent=4)

def load():
    """ Carregar os dados no arquivo .json """
    filename = "inquilinos.json"
    try:
        with open(filename, "r") as f:
            inquilinos = json.load(f)
        return inquilinos
    except FileNotFoundError:
        return {"inquilinos": []}

