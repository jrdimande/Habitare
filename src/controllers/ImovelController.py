from src.models.Imovel import Imovel
from src.utils.validators import validar_imovel
from src.utils.idCreator import gerar_id

class ImovelController:
    def __init__(self):
        self.imoveis = []

    def adicionar_imovel(self, endereco, preco, tipo):
        """" Adiciona um novo imóvel à lista, se for válido"""

        if validar_imovel(endereco, preco, tipo):
            id = gerar_id(endereco)                # <- lógica provisória para ID
            imovel = Imovel(id, endereco, preco, tipo)
            self.imoveis.append(imovel)

    def buscar_imovel(self, id):
        """ Busca e retorna o imóvel com o ID especificado"""
        for imovel in self.imoveis:
            if imovel.id == id:
                return imovel

    def remover_imovel(self, id):
        """ Remove o imóvel com o ID especificado"""
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








