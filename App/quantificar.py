#!/usr/bin/env python3

"""Quantificador de cores de imagens utilizando algoritmos de busca local"""
from scipy.spatial import distance
import sys
import buscas
from problemas import ProblemaQuantificacao, ProblemaLocal
from PIL import Image

__author__ = "Nome do aluno"
__copyright__ = "Copyleft"
__credits__ = ["Ricardo Inácio Álvares e Silva"]
__license__ = "GPLv3"
__version__ = "1.0"
__maintainer__ = "Ricardo Inácio Álvares e Silva"
__email__ = "ricardo.silva@unifil.br"
__status__ = "Desenvolvimento"


def quantificar_subida_encosta(**kwargs):

    no_atual = estado_inicial
    filhos = no_atual.pegarValor(1)

    while(True):
        no_vizinho = max(filhos)
        if no_vizinho.pegarValor(2) <= no_atual.pegarValor(2):
            return no_atual
        no_atual = no_vizinho
        

    """
    Funcao que inicializa estruturas de dados e invoca algoritmo de busca local
    por subida de encosta.
    """
    ### Após iniciar estruturas de dados, remova o comentario da linha abaixo
    #buscas.subida_encosta(problema)
    raise NotImplementedError

def quantificar_feixe_local(**kwargs):
    """
    Funcao que inicializa estruturas de dados e invoca algoritmo de busca em
    feixe local.
    """
    ### Após iniciar estruturas de dados, remova o comentario da linha abaixo
    #buscas.feixe_local(problema, k)
    raise NotImplementedError

def quantificar_geneticamente(**kwargs):
    popInit = [] #população inicial declarada como vazia, a variavel argumento irá definir o tamanho da população

    for i in range(int(argumento)):
        print(i)
        popInit.append(ProblemaLocal(cores, pixels, tamanhoImg)) #enche a população com paletas aleatorias onde o numero de cores é definido pela variavel cores
    
    res = buscas.busca_genetica(popInit, ProblemaLocal.heuristica) #inicia a busca genetica pela paleta
    print(res)
    for i in range(tamanhoImg[0]):
        for j in range(tamanhoImg[1]):
            #mc = res.paleta[0]

            pixels[i,j] = getBest(res.paleta, pixels[i,j])
            '''for cor in res.paleta:
                if(distance.euclidean(pixels[i,j],mc) < distance.euclidean(pixels[i,j],cor)):
                    mc = cor'''
            #pixels[i,j] = mc

    #precisa aplicar a paleta a imagem apos obter resposta


    """
    Funcao que inicializa estruturas de dados e invoca algoritmo de busca local
    por por algoritmo genético.
    """
    ### Após iniciar estruturas de dados, remova o comentario da linha abaixo
    #buscas.busca_genetica(populacao, fitness)
    
def getBest(paleta, pixel):
    best = []
    for i in range(len(paleta)):
        if (len(best) == 0 or best[1] > distance.euclidean(paleta[i],pixel)):
            best = [paleta[i], distance.euclidean(paleta[i],pixel)]

    return best[0]

if __name__ == "__main__":

    print("Olá meu caro mansebo, vamos dar os argumentos para o funcionamento do nosso quantizador")
    print("Digite o nome do algoritimo desejado")
    algoritmo = input("SUBIDA | FEIXE | GENÉTICO" + '\n').lower()
    argumento = input("Digite o argumento que acompanha o algoritimo" + '\n')
    cores = int(input("Quantidade de cores"  + '\n'))
    nome_arquivo = input("Caminho e nome do arquivo com a imagem a ser processada"  + '\n' )
    # Define algoritmo a ser aplicado
    if algoritmo == "subida":
        algoritmo = quantificar_subida_encosta
    elif algoritmo == "feixe":
        algoritmo = quantificar_feixe_local
    elif algoritmo == "genetico":
        algoritmo = quantificar_geneticamente
    else:
        print("Algoritmo especificado inválido: {0}".format(algoritmo))
        print("Algoritmos válidos são: {0}, {1}, {2}"
              .format("subida", "feixe", "genetico"))
        exit()
    #Verifica o numero de cores
    if cores < 1:
        print("Quantidade de cores pós-quantizacão deve ser no mínimo 1.")
        exit()
    # Abrir a imagem especificada
    try:
        original = Image.open(nome_arquivo)
        tamanhoImg = original.size
    except IOError as err:
        print("Erro ao acessar arquivo: {0}".format(err))
    # Copiar imagem para poder comparar ambas ao final.    
    reduzida = original.copy()
    # Obtendo acesso aos pixels da cópia. Cada posicao é uma tupla (R, G, B)
    # R, G e B tem domínio em [0,255], ou seja, 0 <= x <= 255
    pixels = reduzida.load()
    
    

    algoritmo(argumento=argumento, cores=cores, pixels=pixels, tamanhoImg=tamanhoImg) #esses argumentos vao entrar com esses nomes nos algoritmos
    
    original.show()
    reduzida.show()
    reduzida.save(nome_arquivo.split(".")[0] + ".png")
    
    exit()

else:
    raise ImportError("Este módulo só pode funcionar como o principal.")
