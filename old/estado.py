from dados import Arquivo

class Estado(object):
    '''

    '''
    def __init__(self, cidadeInicial, objetivo, nome_arq):
        self.grafo = Arquivo.extrair_dados(nome_arq)
        self.cidadeInicial = self.grafo[cidadeInicial]
        self.objetivo = self.grafo[objetivo]
    '''
        Esse metodo testa se o estado atual é o estado objetivo
        recebe o estado atual como parametro e retorna verdadeiro caso 
        o estado atual é estado objetivo e falso caso contrario
    '''
    def verifica_objetivo(self, estado_atual):

        if estado_atual == self.objetivo:
            return True
        return False


    '''
        Este metodo realiza uma busca no grafo, retornado uma lista
        de pares (ação, resultado) no grafo de estados 
    '''
    def estados_sucessores(self, estado):

        return [(sucessor, sucessor) for sucessor in self.grafo.get(estado).keys()]


