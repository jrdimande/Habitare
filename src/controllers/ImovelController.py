from src.models.Imovel import Imovel
from src.utils.validators import validar_imovel, validar_id

class ImovelController:
    def __init__(self):
        self.imoveis = []

    def adicionar_imovel(self, endereco, preco, tipo):
        """" Adiciona um novo imóvel à lista, se for válido"""

        if validar_imovel(endereco, preco, tipo):
            id = len(self.imoveis) + 1                 # <- lógica provisória para ID
            imovel = Imovel(id, endereco, preco, tipo)
            self.imoveis.append(imovel)

    def buscar_imovel(self, id):
        """ Busca e retorna o imóvel com o ID especificado"""
        if validar_id(id):
            for imovel in self.imoveis:
                if imovel.id == id:
                    return imovel

    def remover_imovel(self, id):
        """ Remove o imóvel com o ID especificado"""
        if validar_id(id):
            imovel = self.buscar_imovel(id)
            self.imoveis.remove(imovel)

    def atualizar_estado(self, id):
        """" Atualiza o estado do imóvel com o ID especificado """
        if validar_imovel(id):
            imovel = self.buscar_casa(id)

            if imovel.estado == False:
                imovel.estado = True
            else:
                imovel.estado = False







