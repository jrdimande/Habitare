import json
import os
from src.controllers.ImovelController import ImovelController

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILENAME = os.path.join(BASE_DIR, "storage", "imoveis.json")

def dump(controller: ImovelController):
    """Salvar dados em arquivo json"""
    os.makedirs(os.path.dirname(FILENAME), exist_ok=True)

    dados = {"imoveis": []}

    for imovel in controller.imoveis:
        atual = {
            "id": imovel.id,
            "endereco": imovel.endereco,
            "preco": imovel.preco,
            "tipo": imovel.tipo,
            "estado": imovel.estado,
            "ocupante": imovel.ocupante
        }
        dados["imoveis"].append(atual)

    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)


def load():
    "Carregar dados do arquivo json"
    os.makedirs(os.path.dirname(FILENAME), exist_ok=True)

    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump({"imoveis": []}, f, indent=4)

    with open(FILENAME, "r", encoding="utf-8") as f:

        imoveis = json.load(f)
    return imoveis
