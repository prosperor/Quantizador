from math import sqrt
import random
from copy import deepcopy
from scipy.spatial import distance


class ProblemaLocal():
    """Classe abstrata com interfaces para implementacao de busca local"""

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
        paleta = list()
        for i in range(quantidadeCores):
            paleta.append(tuple(random.randint(0, 255),
                          random.randint(0, 255), random.randint(0, 255)))

    def getPaleta(self):
        return self.paleta

    def getHeuristica(self):
        return self.h

    def acoes(self, s):
        raise NotImplementedError()

    def resultado(self, s, a):
        raise NotImplementedError()


class ProblemaQuantificacao(ProblemaLocal):

    def __init__(self, cores, pixels, largura, altura):
        self.largura = largura
        self.altura = altura
        self.cores = cores
        self.pixels = pixels
        self.estado = self.est()

    def gerar_iniciais(self, i):
        estados = list()
        for _ in range(i):
            paleta = list()
            for _ in range(self.cores):
                paleta.append(tuple(random.randint(0, 255),
                              random.randint(0, 255), random.randint(0, 255)))
            estados.append(paleta)
        return estados

    def est(self):
        cores_p = list()
        for _ in range(self.cores):
            cores_p.append(tuple(random.randint(0, 255),
                           random.randint(0, 255), random.randint(0, 255)))
        return cores_p

    def getFilhos(self, estado):
        filhos = list()
        for i in range(len(estado)):
            tupla = estado[i]
            novoFilho = estado.copy()
            for j in range(len(tupla)):
                lista_tupla = list(tupla)
                lista_tupla[j] += 1
                nova_tupla = tuple(lista_tupla)
                novoFilho[i] = nova_tupla
                filhos.append(novoFilho)
                novoFilho = deepcopy(estado)

            for j in range(len(tupla)):
                lista_tupla = list(tupla)
                lista_tupla[j] -= 1
                nova_tupla = tuple(lista_tupla)
                novoFilho[i] = nova_tupla
                filhos.append(novoFilho)
                novoFilho = deepcopy(estado)
        return filhos

    def avaliaCor(self, pixel, cor):
        return sqrt(
            (pixel[0] - cor[0]) ** 2 + (pixel[1] - cor[1]) ** 2 + (pixel[2] - cor[2]) ** 2
            )

    def avaliacao(self, estado):
        dist = 0
        for cor in estado:
            for i in range(self.largura):
                for h in range(self.altura):
                    pixel = self.pixels[i, h]
                    distB = sqrt(
                        (pixel[0] - cor[0]) ** 2 + (pixel[1] - cor[1]) ** 2 + (pixel[2] - cor[2]) ** 2
                    )
                    dist += distB
        return dist
