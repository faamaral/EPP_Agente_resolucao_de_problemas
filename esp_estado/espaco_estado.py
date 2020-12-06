
# Arquivo: espaco_estado.py
from problema.problema import Problema_Cidades


class Espaco_de_Estados(Problema_Cidades):

    def __init__(self, inicio, objetivo ,grafo_estados):
        '''
        Essa classe tratará o espaço de estados como um dicionário \
        onde receberá um dicionário, se nada for passado ao construtor \
        será criado um dicionário vazio.
        Caso contrario a classe receberá o grafo extraido do arquivo.
        '''
        super().__init__(inicio, objetivo)
        self.espaco_de_estados = grafo_estados

    def verifica_objetivo(self, estado_atual):
        if estado_atual == self.objetivo:
            return True
        return False

    def acoes(self, estado_atual):
        '''
        Retorna os próximos estados acessíveis a partir do estado atual
        '''
        possiveis_estados = []
        for l in self.get_vizinhancas():
            for i, j in l:
                if estado_atual == i:
                    possiveis_estados.append(j)
                if estado_atual == j:
                    possiveis_estados.append(i)
        return possiveis_estados

    def get_cidades(self):
        '''
        Retorna a lista de cidades
        '''
        return [self.espaco_de_estados.keys()]
        # ou return list(self.espaco_de_estados)

    def get_vizinhancas(self):
        '''
        Retorna uma lista de vizinhanças, ou seja, todas as arestas do grafo
        '''
        return self.monta_vizinhanca()

    def get_vizinhancas_com_peso(self):
        '''
        Retorna uma lista de vizinhanças com as distancias, ou seja, todas as arestas do grafo + peso
        '''
        return self.monta_vizinhaca_com_peso()

    def add_cidade(self, vertice):
        '''
        Adiciona uma nova cidade ao espaço de estados
        A principio ela fica sem cidades vizinhas
        '''
        if vertice not in self.espaco_de_estados:
            self.espaco_de_estados[vertice] = []

    def add_vizinhanca(self, aresta):
        '''
        Adiciona uma nova aresta de cidades no espaço de estados
        :param aresta: pode ser uma lista, tupla ou conjunto contendo as cidades e a distancia entre elas
        :return: None
        '''
        aresta = set(aresta)

        (cidade1, cidade2, peso) = tuple(aresta)

        if cidade1 in self.espaco_de_estados:
            self.espaco_de_estados[cidade1].append({cidade2: int(peso)})
        else:
            self.espaco_de_estados[cidade1] = [{cidade2: int(peso)}]

    def monta_vizinhanca(self):
        '''
        Esse método percorre o grafo e cria uma lista com das vizinhanças entre as cidades
        :return: a lista de vizinhos
        '''
        borda = []

        for cidade, vizinho in self.espaco_de_estados.items():
            for k in vizinho:
                for c, p in k.items():
                    if {c, cidade} not in borda:
                        borda.append((cidade, c))
        return borda

    def monta_vizinhaca_com_peso(self):
        '''
        cria a lista de vizinhos, mas acrescentando a distancia entre cada uma
        :return: lista de vizinhos
        '''
        borda = []

        for cidade, vizinho in self.espaco_de_estados.items():
            for k in vizinho:
                for c, p in k.items():
                    if {c, cidade, p} not in borda:
                        borda.append((cidade, c, p))
        return borda

    def encontrar_caminho(self, inicio, fim, caminho=None):
        '''
        Método auxiliar para obter o percurso de um cidade a outra
        :param inicio: cidade inicial
        :param fim: cidade objetivo
        :param caminho: lista com as cidades que foram visitadas até chegar no destino
        :return: o caminho que foi percorrido
        '''
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
        '''
        Método auxiliar para obter o percurso de um cidade a outra e a distancia percorrida
        :param inicio: cidade de partida
        :param fim: cidade objetivo
        :param caminho: percurso percorrido
        :param peso: distancia percorrida
        :return: o caminho + custo ou none caso falha
        '''
        if caminho == None:
            caminho = []
        cidades = self.espaco_de_estados
        caminho = caminho + [inicio]
        custo = peso
        if inicio == fim:
            return (caminho, custo)
        if inicio not in cidades:
            return None
        for cidade in cidades[inicio]:
            for c, v in cidade.items():
                if c not in caminho:
                    caminho_extendido = self.encontrar_caminho_com_custo(c, fim, caminho, custo+v)
                    if caminho_extendido:
                        return caminho_extendido
        return None


    def busca_dls(self, inicio, fim, limite, caminho = None):

        if caminho==None:
            caminho = []

        cidades = self.espaco_de_estados
        caminho = caminho+[inicio]
        if inicio == fim or limite <= 0:
            return caminho
        if inicio not in cidades:
            return None


        for cidade in cidades[inicio]:
            for c in cidade.keys():
                if c not in caminho:
                    caminho_extendido = self.busca_dls(c, fim, limite-1, caminho)
                    if caminho_extendido:
                        return caminho_extendido
        return None


    def dls(self, limite):
        profundidade=0
        visitados = []
        pilha = [self.inicio]
        cidades = self.espaco_de_estados

        if self.inicio == self.objetivo:
            return "Inicio e objetivo são a mesma cidade"
        if limite<=0:
            return 'Valor para limite não permitido'

        while pilha:
            if profundidade <= limite:
                cidade_atual = pilha.pop()
                visitados.append(cidade_atual)
                visinhos = cidades[cidade_atual]
                for visinho in visinhos:
                    for k in visinho.keys():
                        if k not in visitados:
                            if (self.verifica_objetivo(k)):
                                visitados.append(k)
                                return visitados
                            pilha.append(k)
            else:
                return "Busca interrompida, O limite de profundidade foi atingido"
            profundidade = profundidade+1
        return None









    def __repr__(self):
        '''
        representação do objeto como string
        :return: o objeto em formato string
        '''
        return f'{self.espaco_de_estados}'

    def __str__(self):
        '''
        Representação personalizada do objeto
        :return: o objeto como string de forma mais legível
        '''
        string = 'Cidades: '
        for cidades in self.espaco_de_estados:
            string += str(cidades) + ' '
        string += '\nVizinhanças: '
        for arestas in self.monta_visinhanca():
            string += str(arestas) + ' '
        return string