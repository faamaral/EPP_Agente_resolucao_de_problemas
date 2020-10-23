'''
    arquivo: dados.py
'''
import os
from collections import defaultdict
from estado.estado import Estado

class Arquivo:

    def extrair_dados(nome_arquivo):
        #coloca os dados do arquivo em um dicionario
        #{chave: [valores]}
        grafo = defaultdict(list)

        #abre o arquivo com fechamento automatico após o
        #fim do bloco with
        with open(os.path.abspath(nome_arquivo), 'r') as file:
            file.readline() # lê a primeira linha e descarta

            # tambem é descartado pois não é necessario em dicionario
            quant_v = file.readline().strip().split('VERTICES: ')
            quant_a = file.readline().strip().split('ARESTAS: ')

            # transforma as linhas restantes em uma lista
            linhas_rest = file.readlines()
            for linha in linhas_rest:
                #divide a linha em um 'array' com tres posições
                line = linha.strip().split(', ')

                cidade1 = line[0]
                cidade2 = line[1]
                custo= line[2]

                #cria uma especie de lista de adjacencias no grafo
                grafo[cidade1].append({cidade2: int(custo)})
                grafo[cidade2].append({cidade1: int(custo)})
        # retorna a estrutura do grafo a ser usada na classe estado
        return grafo

    # def desestruturar(dict):
    #     for chave, valor in dict.items():
    #         cidade = chave
    #         list = []
    #         tupla = tuple()
    #         for k in valor:
    #             dic = k
    #             for key, value in dic.items():
    #                 cidade1 = key
    #                 peso = value
    #                 tupla = (cidade1, peso)
    #                 list.append(tupla)
    #         e = Estado(cidade, list)
    #         print(e)

    def desestruturar(dict):
        e = Estado()
        for chave, valor in dict.items():
            cidade = chave
            list = []
            tupla = tuple()
            for k in valor:
                dic = k
                for key, value in dic.items():
                    cidade1 = key
                    peso = value
                    tupla = (cidade1, peso)
                    list.append(tupla)
            e.nome = cidade
            e.lista_estados = list


if __name__ == '__main__':

    grafo = Arquivo.extrair_dados('grafo_8_cidades.txt')
    Arquivo.desestruturar(grafo)

    #print(grafo)



