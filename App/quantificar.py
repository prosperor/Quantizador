import buscas
from problemas import ProblemaLocal, ProblemaQuantificacao
from PIL import Image

def quantificar_subida_encosta(argumento,cores,pixels,largura,altura,**args):
    prob = ProblemaQuantificacao(cores,pixels,altura,largura)
    estado = buscas.subida_encosta(prob,prob.estado)

    for i in range(largura):
        for j in range(altura):
            pixel = pixels[i,j]
            melhor = estado[0]
            for cor in estado:
                if prob.avaliaCor(pixel, cor) < prob.avaliaCor(pixel, melhor):
                    melhor = cor
            
            pixels[i,j] = melhor


def quantificar_feixe_local(**kwargs):
    k = int(argumento)
    prob = ProblemaQuantificacao(cores, pixels, largura, altura)   
    estado = buscas.feixe_local(prob, k)

    for i in range(largura):
        for j in range(altura):
            pixel = pixels[i,j]
            melhor = estado[0]
            for cor in estado:
                if prob.avaliaCor(pixel, cor) < prob.avaliaCor(pixel, melhor):
                    melhor = cor
            
            pixels[i,j] = melhor

def quantificar_geneticamente(**kwargs):
    popInit = [] #população inicial declarada como vazia, a variavel argumento irá definir o tamanho da população

    for i in range(argumento):
        popInit.append(ProblemaLocal(cores, pixels).getPaleta()) #enche a população com paletas aleatorias onde o numero de cores é definido pela variavel cores
    
    res = buscas.busca_genetica(popInit, ProblemaLocal.heuristica) #inicia a busca genetica pela paleta

    #precisa aplicar a paleta a imagem apos obter resposta


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

    if cores < 1:
        print("Quantidade de cores pós-quantizacão deve ser no mínimo 1.")
        exit()

    try:
        original = Image.open(nome_arquivo)
    except IOError as err:
        print("Erro ao acessar arquivo: {0}".format(err))

    reduzida = original.copy()
    pixels = reduzida.load()
    largura, altura = reduzida.size
    
    algoritmo(argumento=argumento, cores=cores, pixels=pixels, largura=largura, altura=altura) 
    
    original.show()
    reduzida.show()
    reduzida.save(nome_arquivo.split(".")[0] + ".png")
    exit()
