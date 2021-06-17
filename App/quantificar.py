#!/usr/bin/env python3

"""Quantificador de cores de imagens utilizando algoritmos de busca local"""

import sys, buscas
from problemas import ProblemaQuantificacao
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
    """
    Funcao que inicializa estruturas de dados e invoca algoritmo de busca local
    por por algoritmo genético.
    """
    ### Após iniciar estruturas de dados, remova o comentario da linha abaixo
    #buscas.busca_genetica(populacao, fitness)
    raise NotImplementedError
    

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
    except IOError as err:
        print("Erro ao acessar arquivo: {0}".format(err))
    # Copiar imagem para poder comparar ambas ao final.    
    reduzida = original.copy()
    # Obtendo acesso aos pixels da cópia. Cada posicao é uma tupla (R, G, B)
    # R, G e B tem domínio em [0,255], ou seja, 0 <= x <= 255
    pixels = reduzida.load()

    algoritmo(argumento=argumento, cores=cores, pixels=pixels)
    
    original.show()
    reduzida.show()
    reduzida.save(nome_arquivo.split(".")[0] + ".png")
    
    exit()

else:
    raise ImportError("Este módulo só pode funcionar como o principal.")