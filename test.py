from esp_estado.espaco_estado import Espaco_de_Estados
from dados.dados import Arquivo

if __name__ == '__main__':
    grafo = Arquivo.extrair_dados('grafo_8_cidades.txt')
    esp = Espaco_de_Estados('Salinas','MOC',grafo)


    print(esp.get_cidades())
    #print(esp.get_visinhancas())
    #print(esp.visinhancas_com_peso())
    print(esp.busca_dls(esp.inicio,esp.objetivo,5))
    print(esp.dls(5))