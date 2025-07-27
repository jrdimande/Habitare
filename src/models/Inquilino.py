class Inquilino:
    def __init__(self, id,  nome, contacto, data_de_entrada, id_imovel):
        self.id = id
        self.nome = nome
        self.contacto = contacto
        self.data_de_entrada = data_de_entrada
        self.imovel = id_imovel
        self.pagamentos = []
