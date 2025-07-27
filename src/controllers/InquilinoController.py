import json
from src.models.Inquilino import Inquilino
from src.utils.validators import validar_inquilino
from src.utils.idCreator import gerar_inq_id
from src.storage.imovel_json import load, dump

class InquilinoController:
    def __init__(self):
        self.inquilinos = []


    def ocupar_imovel(self, id_imovel, nome):
        filename = "imoveis.json"
        dados = load()

        for i in range(len(dados["imoveis"])):
            if dados["imoveis"][i]["id"] == id_imovel:
                dados["imoveis"][i]["estado"] = True
                dados["imoveis"][i]["ocupante"] = nome

        with open(filename, "w") as f:
            json.dump(dados, f, indent=4)

    def desocupar_imovel(self, id_imovel):
        filename = "imoveis.json"
        dados = load()

        for i in range(len(dados["imoveis"])):
            if dados["imoveis"][i]["id"] == id_imovel:
                dados["imoveis"][i]["estado"] = False
                dados["imoveis"][i]["ocupante"] = None

        with open(filename, "w") as f:
            json.dump(dados, f, indent=4)

    def adicionar_inquilino(self, id, nome, contacto, data_de_entrada, id_imovel):
        """ Adiciona um novo inquilino à lista de inquilinos, se for válido """

        if validar_inquilino(nome, contacto, data_de_entrada):
            if not id:
                id = gerar_inq_id()

            inquilino = Inquilino(id, nome, contacto, data_de_entrada, id_imovel)
            self.inquilinos.append(inquilino)
            self.ocupar_imovel(id_imovel, nome)
            return True
        return False


    def buscar_inquilino(self, id):
        """ Busca e retorna o inquilino com o ID especificado """
        for inquilino in self.inquilinos:
            if inquilino.id == id:
                return inquilino
        return False


    def remover_inquilino(self, id):
        """ Remove o inquilino com o ID especificado """
        inquilino = self.buscar_inquilino(id)
        if inquilino:
            self.inquilinos.remove(inquilino)

            filename = "imoveis.json"
            dados = load()
            id_imovel = inquilino.imovel
            self.desocupar_imovel(id_imovel)


    def atualizar_inquilino(self,id, nome, contacto, id_imovel):
        """ Atualiza os atributos do inquilino com o ID especificado """
        inquilino = self.buscar_inquilino(id)
        if inquilino:
            inquilino.nome = nome
            inquilino.contacto = contacto
            inquilino.casa= id_imovel
            return True
        return False
    def adicionar_pagamento(self, pagamento):
        """ Adiciona pagamento à lista de pagamentos do inquilino """
        inquilino = self.buscar_inquilino(pagamento.id_inquilino)
        if inquilino:
            inquilino.pagamentos.append(pagamento)
            return True
        return False

    def remover_pagamento(self, pagamento):
        """ Remove pagamento na lista de pagamentos do inquilino """
        inquilino = self.buscar_inquilino(pagamento.id_inquilino)
        if inquilino:
            inquilino.pagamentos.remove(pagamento)
