import json
from src.models.Pagamento import Pagamento
from src.utils.idCreator import gerar_pay_id
from src.storage.inquilino_json import load
from src.storage.pagamento_json import load as load_pagamentos



class PagamentoController():
    def __init__(self):
        self.pagamentos = []
        dados_inquilinos = load()


    def adicionar_pagamento(self, id_pagamento, id_inquilino, valor, data_de_pagamento):
        "Adiciona um novo pagamento à lista de pagamentos , se for válido"
        if not id_pagamento:
            id_pagamento = gerar_pay_id()

        if not id_inquilino or not valor or not data_de_pagamento:
            return False
        dados_inquilinos = load()
        inquilinos = dados_inquilinos["inquilinos"]
        inquilino_existe = False

        for iquilino in range(len(inquilinos)):
            if inquilinos[iquilino]["id"] == id_inquilino:
                inquilino_existe = True

        if inquilino_existe:
            pagamento = Pagamento(id_pagamento, id_inquilino, valor, data_de_pagamento)
            self.pagamentos.append(pagamento)



    def buscar_pagamento(self, id_pagamento):
        "Retorna o pagamento com o ID especificado"
        for pagamento in self.pagamentos:
            if pagamento.id_pagamento == id_pagamento:
                return pagamento
        return False

    def remover_pagamento(self, id_pagamento, id_inquilino):
        "Remove pagamento com ID,s especificados"

        dados_inquilinos = load()
        inquilinos = dados_inquilinos["inquilinos"]
        inquilino_existe = False

        for iquilino in range(len(inquilinos)):
            if inquilinos[iquilino]["id"] == id_inquilino:
                inquilino_existe = True

        pagamento = self.buscar_pagamento(id_pagamento)

        if inquilino_existe:
            self.pagamentos.remove(pagamento)