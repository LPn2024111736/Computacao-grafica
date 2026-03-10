import numpy as np
from PIL import Image
from random import randint
import binascii


def criarDados(height:int,width:int):
    """
    criarDados()
    Esta função utiliza arrays criados com a biblioteca numpy para criar imagens raster com cores aleatórias,
    através da biblioteca PIL. O array é composto por height* linhas (arrays), cada um com arrays de 3 valores, 
    representando pixeis. Estes dados são guardados em binário e em hexadecimal (plaintext) para testar o programa.

    Args:
    height (int): Número de arrays de pixeis presente no array principal
    width (int): Número de pixeis nos arrays de pixeis. 

    """    
    truecolor = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    paletaDeCores=[(255,255,0),(0,0,255),(0,255,255),(255,0,0),(255,0,255),(0,255,0),]
    index = np.zeros((height, width, 3), dtype=np.uint8)
    for line in range(len(index)):
        for pixel in range(len(index[line])):
            index[line,pixel]=paletaDeCores[randint(0,5)]
    with open("dadosindex.bin", "wb") as f:
        f.write(index.tobytes())
    with open("dadosindex.bin", "rb") as f:
        hexdataIndex = binascii.hexlify(f.read())
    hexdataIndex=str(hexdataIndex)[2:-1]
    with open("dadosindexplaintext.txt", "w") as f:
        f.write(hexdataIndex)
    with open("dadostruecolor.bin", "wb") as f:
        f.write(truecolor.tobytes())
    with open("dadostruecolor.bin", "rb") as f:
        hexdataTrue = binascii.hexlify(f.read())
    hexdataTrue=str(hexdataTrue)[2:-1]
    with open("dadostruecolorplaintext.txt", "w") as f:
        f.write(hexdataTrue)
    imgb = Image.fromarray(index)
    imga = Image.fromarray(truecolor)
    imga.show()
    imgb.show()
