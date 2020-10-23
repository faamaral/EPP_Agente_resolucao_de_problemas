
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

    def visinhancas_com_peso(self):
        return self.monta_visinhaca_com_peso()
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

        for cidade, visinho in self.espaco_de_estados.items():
            for k in visinho:
                for c, p in k.items():
                    if {c, cidade} not in borda:
                        borda.append({cidade, c})
        return borda

    def monta_visinhaca_com_peso(self):
        borda = []

        for cidade, visinho in self.espaco_de_estados.items():
            for k in visinho:
                for c, p in k.items():
                    if {c, cidade, p} not in borda:
                        borda.append({cidade, c, p})
        return borda

    def encontrar_caminho(self, inicio, fim, caminho=None):
        if caminho==None:
            caminho = []

        cidades = self.espaco_de_estados
        caminho = caminho+[inicio]
        if inicio == fim:
            return caminho
        if inicio not in cidades:
            return None
        for cidade in cidades[inicio]:
            for c in cidade.keys():
                if c not in caminho:
                    caminho_extendido = self.encontrar_caminho(c, fim, caminho)
                    if caminho_extendido:
                        return caminho_extendido
        return None

    def encontrar_caminho_com_custo(self, inicio, fim, caminho=None, peso=0):
        if caminho == None:
            caminho = []
        cidades = self.espaco_de_estados
        caminho = caminho + [inicio]
        custo = peso
        if inicio == fim:
            return caminho
        if inicio not in cidades:
            return None
        for cidade in cidades[inicio]:
            for c, v in cidade.items():
                if c not in caminho:
                    caminho_extendido = self.encontrar_caminho_com_custo(c, fim, caminho, custo+v)
                    if caminho_extendido:
                        custo_caminho = {
                            'Caminho': caminho_extendido,
                            'Custo': custo
                        }
        return None

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