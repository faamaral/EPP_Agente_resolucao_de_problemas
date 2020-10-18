import os

from collections import defaultdict

class CidadeNo:
    def __init__(self, cidade, distancia):
        self.cidade = cidade
        self.distancia = distancia


titulo = None



def extrair_dados(nome_arquivo):
    grafo = defaultdict()
    with open(os.path.abspath(nome_arquivo), 'r') as file:
        file.readline()
        quant_v = file.readline().strip().split('VERTICES: ')
        quant_a = file.readline().strip().split('ARESTAS: ')
        linhas_rest = file.readlines()
        for linha in linhas_rest:
            line = linha.split(', ')

            cidade1 = line[0]
            cidade2 = line[1]
            custo= line[2].strip()

            grafo.setdefault(cidade1, []).append(CidadeNo(cidade2, custo))
            grafo.setdefault(cidade2, []).append(CidadeNo(cidade1, custo))

    return grafo


if __name__ == '__main__':

    grafo = extrair_dados('grafo_8_cidades.txt')




