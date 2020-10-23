
class Espaco_de_Estados(object):

    def __init__(self, grafo_estados = None):

        if grafo_estados == None:
            grafo_estados = {}
        self.espaco_de_estados = grafo_estados
    '''
        Retorna a lista de cidades
    '''
    def get_cidades(self):
        return [self.espaco_de_estados.keys()]
        # ou return list(self.espaco_de_estados)

    def visinhancas(self):
        return self.monta_visinhanca()
    '''
        Adiciona uma nova cidade aspaço de estados
        A principio ela fica sem cidades visinhas
    '''
    def add_cidade(self, vertice):
        if vertice not in self.espaco_de_estados:
            self.espaco_de_estados[vertice] = []

    def add_visinhanca(self, aresta):
        aresta = set(aresta) # Cria um conjunto de arestas

        (cidade1, cidade2, peso) = tuple(aresta)

        if cidade1 in self.espaco_de_estados:
            self.espaco_de_estados[cidade1].append({cidade2: int(peso)})
        else:
            self.espaco_de_estados[cidade1] = [{cidade2: int(peso)}]

    def monta_visinhanca(self):

        borda = []

        for cidade in self.espaco_de_estados:
            for visinho in self.espaco_de_estados[cidade]:
                if {visinho, cidade} not in borda:
                    borda.append({cidade, visinho})
        return borda

    def __repr__(self):
        return f'{self.espaco_de_estados}'

    def __str__(self):
        string = 'Cidades: '
        for cidades in self.espaco_de_estados:
            string += str(cidades) + ' '
        string += '\nVizinhancas: '
        for arestas in self.monta_visinhanca():
            string += str(arestas) + ' '
        return string