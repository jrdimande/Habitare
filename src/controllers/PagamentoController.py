from src.models.Pagamento import Pagamento
from src.utils.validators import validar_pagamento
from src.utils.idCreator import gerar_pay_id
class PagamentoController:
    def __init__(self, InquilinoController):
        self.InquilinoController = InquilinoController
        self.pagamentos = []

    def adicionar_pagamento(self, id_inquilino, valor, data_pagamentos):
        """ Adiciona pagamento à lista de pagamentos """
        if  not validar_pagamento(valor):
            return "Pagamento inválido"

        inquilino = InquilinoController.buscar_inquilino(id_inquilino)

        if not inquilino:
            return "Inquilino não encontrado"

        id_pagamento = gerar_pay_id
        pagamento = Pagamento(id_pagamento, id_inquilino, valor, data_pagamentos)
        self.pagamentos.append(pagamento)
        self.InquilinoController.adicionar_pagamento(pagamento)

    def buscar_pagamento(self, id_pagamento):
        " Busca e retorna o pagamento com o ID especificado"
        for pagamento in self.pagamentos:
            if pagamento.id == id_pagamento:
                return pagamento


    def remover_pagamento(self, id_pagamento):
        """ Remove pagamento com o ID especificado """
        pagamento = self.buscar_pagamento(id_pagamento)
        self.pagamentos.remove(pagamento)


    def atualizar_pagamento(self, id_pagamento):
        pass






