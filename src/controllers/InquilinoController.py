from src.models.Inquilino import Inquilino
from src.utils.validators import validar_inquilino
from src.utils.idCreator import gerar_inq_id
class InquilinoController:
    def __init__(self):
        self.inquilinos = []

    def adicionar_inquilino(self, id, nome, contacto, data_de_entrada, casa):
        """ Adiciona um novo inquilino à lista de inquilinos, se for válido """
        if validar_inquilino(nome, contacto, data_de_entrada):
            if not id:
                id = gerar_inq_id()
            inquilino = Inquilino(id, nome, contacto, data_de_entrada, casa)
            self.inquilinos.append(inquilino)


    def buscar_inquilino(self, id):
        """ Busca e retorna o inquilino com o ID especificado """
        for inquilino in self.inquilinos:
            if inquilino.id == id:
                return inquilino

    def remover_inquilino(self, id):
        """ Remove o inquilino com o ID especificado """
        inquilino = self.buscar_inquilino(id)
        self.inquilinos.remove(inquilino)

    def atualizar_inquilino(self,id, nome, contacto, casa):
        """ Atualiza os atributos do inquilino com o ID especificado """
        inquilino = self.buscar_inquilino(id)
        inquilino.nome = nome
        inquilino.contacto = contacto
        inquilino.casa= casa
    def adicionar_pagamento(self, pagamento):
        """ Adiciona pagamento à lista de pagamentos do inquilino """
        inquilino = self.buscar_inquilino(pagamento.id_inquilino)
        inquilino.pagamentos.append(pagamento)

    def remover_pagamento(self, pagamento):
        """ Remove pagamento na lista de pagamentos do inquilino """
        inquilino = self.buscar_inquilino(pagamento.id_inquilino)
        inquilino.pagamentos.remove(pagamento)





