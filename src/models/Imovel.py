class Imovel:
    def __init__(self, id, endereco, preco, tipo, estado=False, ocupante=None):
        self.id = id
        self.endereco = endereco
        self.preco = preco
        self.tipo = tipo
        self.estado = estado
        self.ocupante = ocupante

