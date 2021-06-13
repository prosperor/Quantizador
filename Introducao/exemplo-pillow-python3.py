#!/usr/bin/env python3

"""Exemplo de utilizacao de imagens em python3 com Pillow"""

from PIL import Image

__author__ = "Nome do aluno"
__copyright__ = "Copyleft"
__credits__ = ["python3 wikibooks"]
__license__ = "GPLv3"
__version__ = "1.0"
__maintainer__ = "Ricardo Inácio Álvares e Silva"
__email__ = "ricardo.silva@unifil.br"
__status__ = "Entregue"

if __name__ == "__main__":
    # cria uma nova imagem RGB, toda preta
    img = Image.new( 'RGB', (255,255), "white")

    img.show()

    # cria a matriz de pixels
    pixels = img.load()

    # para cada pixel:
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            # define uma cor (R, G, B)
            if i < 50 or i > 200 or j < 50 or j > 200:
                pixels[i,j] = (40, 100, 0)
            elif i < 65 or i > 185 or j < 65 or j > 185:
                pixels[i,j] = (100,0,0)
            else:
                pixels[i,j] = (0,0,100)

    img.show()
    img.save("exemplo.png")
