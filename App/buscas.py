import random


def subida_encosta(problema, estado):
    cont = 0
    avaliacoes = list()
    stop = 0

    while True:
        atual, filhos = problema.avaliacao(estado), problema.getFilhos(estado)
        melhor = atual
        estado_atual = problema.estado
        avaliacoes.append(atual)
        for filho in filhos:
            avaliacao = problema.avaliacao(filho)
            if avaliacao <= melhor:
                stop += 1 if avaliacao == melhor else 0
                melhor = avaliacao
                estado = filho
        cont += 1
        if melhor == atual and estado_atual == estado or stop == 20:
            break
    return estado, avaliacoes


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

    for cont in range(30):

        fitness = []
        peso = []
        for individuo in populacao:
            fitness.append(fn_fitness(individuo))

        fitnessGeral = sum(fitness)
        for fit in fitness:
            peso.append(fitnessGeral/fit)

        ng = random.choices(populacao, peso, k=len(populacao))

        for i in range(0, len(ng), 2):
            pos = random.randint(1, len(ng[i])-1)
            for j in range(0, pos):
                ng[i, j], ng[i+1, j] = ng[i+1, j], ng[i, j]

        alpha = 0.15
        for i in ng:
            for j in i:
                if(random.random() <= alpha):
                    j = tuple(random.randint(0, 255), random.randint(
                        0, 255), random.randint(0, 255))

        populacao = ng

    populacao.sort(key=lambda x: fn_fitness(individuo))
    return populacao[0]

    raise NotImplementedError
