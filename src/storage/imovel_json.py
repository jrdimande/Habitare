import json
from src.controllers.ImovelController import ImovelController

def dump(ImovelController):
    "Salvar dados em arquivo JSON"
    ImovelController = ImovelController
    filename = "imoveis.json"

    dados = {"imoveis" : [] }

    for imovel in ImovelController.imoveis:
        actual = {
            "id" : imovel.id,
            "endereco" : imovel.endereco,
            "preco" : imovel.preco,
            "tipo" : imovel.tipo,
            "estado": imovel.estado,
            "ocupante" : imovel.ocupante

        }
        dados["imoveis"].append(actual)

    with open(filename, "w") as f:
        json.dump(dados, f, indent=4)


def load():
    " Carregar dados do ficheiro JSON "
    filename = "imoveis.json"

    try:
        with open(filename, "r") as f:
            imoveis = json.load(f)
        return imoveis
    except FileNotFoundError:
        return {"imoveis" : [] }
