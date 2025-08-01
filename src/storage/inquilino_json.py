import json
import os
from src.controllers.InquilinoController import InquilinoController

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILENAME = os.path.join(BASE_DIR, "storage", "inquilinos.json")

def dump(inc):
    "Salvar dados no arquivo json"
    InquilinoController = inc

    dados = {"inquilinos": []}

    for inquilino in InquilinoController.inquilinos:
        actual = {
            "id": inquilino.id,
            "nome": inquilino.nome,
            "contacto": inquilino.contacto,
            "data_de_entrada": inquilino.data_de_entrada,
            "imovel": inquilino.imovel,
            "pagamentos": inquilino.pagamentos
        }
        dados["inquilinos"].append(actual)

    os.makedirs(os.path.dirname(FILENAME), exist_ok=True)

    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)

def load():
    "Carregar dados no arauivo json"
    os.makedirs(os.path.dirname(FILENAME), exist_ok=True)

    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            inquilinos = json.load(f)
        return inquilinos
    except FileNotFoundError:
        return {"inquilinos": []}

def open_and_dump(data):
    os.makedirs(os.path.dirname(FILENAME), exist_ok=True)
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
