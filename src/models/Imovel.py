class Imovel:
    def __init__(self, id, endereco, preco, tipo, estado=False):
        self.id = id
        self.endereco = endereco
        self.preco = preco
        self.tipo = tipo
        self.estado = estado

