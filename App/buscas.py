#!/usr/bin/env python3

import random

"""Módulo que abriga os algoritmos de quantificacao de imagens"""

__author__ = "Nome do aluno"
__copyright__ = "Copyleft"
__credits__ = ["Ricardo Inácio Álvares e Silva"]
__license__ = "GPLv3"
__version__ = "0.1"
__maintainer__ = "Aluno"
__email__ = "seu@email.com"
__status__ = "Desenvolvimento"

def subida_encosta(problema):
    """
    Busca local por subida de encosta.
    
    :param problema: objeto da classe ProblemaLocal
    :return: estado final de um pico do problema (global ou local).
    """
    raise NotImplementedError

def feixe_local(problema, k=8):
    """
    Busca por feixe local.
    
    :param problema: objeto da classe ProblemaLocal
    :param k: quantidade de estados a passarem de uma geracão à outra
    :return: estado final de um pico do problema (global ou local).
    """
    raise NotImplementedError

def busca_genetica(populacao, fn_fitness):
    """
    Busca local por algoritmo genético.
    
    :param populacao: lista de strings, cada string são os "genes" de um individuo
    :param fn_fitness: funcao capaz de avaliar a qualidade de um individuo
    :return: um individuo com a funcao_fitness desejada
    """    
    ngen = int(input("informe quantas gerações deseja: "))
    for cont in range(ngen):
        print(f"geração: {cont}")
        fitness = []
        peso = []
        for individuo in populacao:
            fitness.append(fn_fitness(individuo, individuo.getPaleta()))
            
        
        fitnessGeral = sum(fitness)
        for fit in fitness:
            peso.append( fit/fitnessGeral)

        ng = random.choices(populacao, peso, k=len(populacao))
        
            #print(f"pósseleção: {i.paleta}")
        for i in range(0, len(ng), 2):
            pos = random.randint(1, len(ng[i].getPaleta())-1)
            for j in range(0, pos):
                ng[i].paleta[j], ng[i+1].paleta[j] = ng[i+1].paleta[j], ng[i].paleta[j]
        
            #print(f"póscrusamento: {i.paleta}")
        alpha = 0.1
        for i in ng:
            #print(i.paleta)
            for j in range(len(i.paleta)):
                rng = random.random()
                #print(rng)
                if(rng <= alpha):
                    i.aplicarMutacao(j, i.gerarCorAleatoria())
            #print(i.paleta)
    
        populacao = ng
        

    populacao.sort(key=lambda x: fn_fitness(individuo, individuo.getPaleta()))
    return populacao[0]




    

if __name__ == "__main__":
    print("Este módulo não deve ser utilizado como o principal ou inicial")
    exit()
