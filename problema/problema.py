class Problema_Cidades(object):

    def __init__(self, c_inicio, c_objetivo):
        self.inicio = c_inicio
        self.objetivo = c_objetivo

    def acoes(self, estado):
        raise NotImplementedError

    def verifica_objetivo(self, estado_atual):
        raise NotImplementedError
