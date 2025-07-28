def validar_inquilino(nome, contacto, data_de_entrada):
    """ Validar os dados do inquilino"""
    if len(nome) > 2 and len(contacto) == 9 and data_de_entrada:
        return True
    return False


 # def validar_id(id, controller):
 #


def validar_imovel(endereco, preco, tipo):
    """ Validar imóveis"""
    if endereco and preco > 0 and tipo:
        return True
    return False

# def validar_pagamento(valor):
#     """ Validar pagamentos"""
#     valor = float(valor)
#     if valor > 0:
#         return True
#     return False


