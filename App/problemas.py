#!/usr/bin/env python3
from scipy.spatial import distance
import random
"""Módulo com implementacao da modelagem do problema abordado"""

__author__ = "Nome do aluno"
__copyright__ = "Copyleft"
__credits__ = ["Ricardo Inácio Álvares e Silva"]
__license__ = "GPLv3"
__version__ = "0.1"
__maintainer__ = "Aluno"
__email__ = "seu@email.com"
__status__ = "Desenvolvimento"


class ProblemaLocal():
    """Classe abstrata com interfaces para implementacao de busca local"""
    
    def __init__(self, quantidadeCores, pixeis, tamanho):
        self.pixeis = pixeis
        self.alt, self.lar = tamanho
        
        self.paleta = self.gerarPaletaAleatoria(quantidadeCores)
        print(self.paleta)
        
        self.h = self.heuristica(self.paleta)
    
    
    def heuristica(self, paleta):
        h = 0
        for p in paleta:
            for i in range(self.alt):
                for j in range(self.lar):
                    h += distance.euclidean(p, self.pixeis[i,j])
        
        h /= self.alt*self.lar
        
        return h

    def aplicarMutacao(self, posicao, novaCor):
        self.paleta[posicao] = novaCor

    def gerarCorAleatoria(self):
        novacor = -1
        while(novacor in self.paleta or novacor == -1):
            ht, wt = random.randint(0,self.alt-1),random.randint(0,self.lar-1)
            novacor = self.pixeis[ht,wt]
        return (novacor)

    
    def gerarPaletaAleatoria(self, quantidadeCores):
        paleta = []
        for i in range(quantidadeCores):
            cor = self.pixeis[random.randint(0,self.alt-1),
            random.randint(0,self.lar-1)]
            #cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            paleta.append(cor)
        return paleta

    
    def getPaleta(self):
        return self.paleta

    def getHeuristica(self):
        return self.h


    
    def acoes(self, s):
        raise NotImplementedError()
    
    def resultado(self, s, a):
        raise NotImplementedError()


class ProblemaQuantificacao(ProblemaLocal):
    """Aqui você implementará a modelagem da busca local em quantizacao de
    imagens"""

    
    pass


if __name__ == "__main__":
    print("Este módulo não deve ser utilizado como o principal ou inicial")
    exit()
