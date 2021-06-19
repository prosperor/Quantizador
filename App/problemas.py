#!/usr/bin/env python3
from scipy.spatial import distance
import random


class ProblemaLocal():
    
    def __init__(self, quantidadeCores, pixeis):
        self.paleta = self.gerarPaletaAleatoria(quantidadeCores)
        self.pixeis = pixeis
        self.h = self.heuristica(pixeis, self.paleta)
    
    @staticmethod
    def heuristica(original, paleta):
        h = 0
        for p in paleta:
            for i in original:
                for j in i:
                    h += distance.euclidean(p, j)
        
        return h

    @staticmethod
    def gerarPaletaAleatoria(quantidadeCores):
        paleta = []
        for _ in range(quantidadeCores):
            paleta.append(tuple(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    
    def getPatela(self):
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
