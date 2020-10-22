
class Estado(object):

    def __init__(self, nome, lista_cidades):
        self.nome = nome
        self.lista_estados = lista_cidades

    def set_cidade(self, nome):
        self.nome = nome

    def set_lista_visinhos(self, cidade, custo):
        self.lista_estados = (cidade, custo)

    def get_cidade(self):
        return self.nome

    def __repr__(self):
        return f'{self.nome} -> {self.lista_estados}'

    def get_lista_visinhos(self):
        return self.lista_estados