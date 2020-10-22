import os
from estado.estado import Estado
from collections import defaultdict


class Arquivo:


    def extrair_dados(nome_arquivo):
        temp = defaultdict(list)
        with open(os.path.abspath(nome_arquivo), 'r') as file:

            file.readline() #descarta a primeira linha
            quantidadeV = file.readline().strip().split('Vertices:')
            quantidadeA = file.readline().strip().split(('Arestas: '))

            for line in file.readlines():
                linha = line.strip().split(', ')
                cidade1 = linha[0]
                cidade2 = linha[1]
                custo = int(linha[2])

                temp[Estado.set_cidade(cidade1)].append({Estado.set_lista_visinhos(cidade2, custo)})
                temp[Estado.set_cidade(cidade2)].append({Estado.set_lista_visinhos(cidade1, custo)})
        return temp

    def desestruturar(self, dict):

        for chave, valor in dict.items():
            cidade = chave
            for c, v in valor:
                (cidade1, peso) = c, v
            Estado(cidade, (cidade1, peso))



if __name__ == '__main__':
    grafo = Arquivo.extrair_dados('grafo_8_cidades.txt')
    print(grafo)
