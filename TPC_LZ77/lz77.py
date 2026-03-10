def lz77_encode(inputString: str)->list:
    """
    lz77_encode()
    O processo de codificação dos dados segue o seguinte procedimento:
    -A variável match irá representar o maior padrão possível que for encontrado na janela de pesquisa.
    -O valor desta é composto de todas as letras correspondentes até o padrão não corresponder, com o 
    caractér que quebra este padrão (o ultimo elemento dos tuplos) sendo guardado na sua própria variável.
    -De seguida, o offset (o primeiro elemento dos tuplos e o valor que "temos de voltar") vai ser calculado, 
    utilizando o tamanho da janela deslizante (NOTA: em contextos reais, a janela tem um tamanho máximo definido pelo 
    programador em kb, mas não foi definido um atributo para tal neste tpc) e a ultima aparência do nosso padrão dentro desta.
    -O ultimo atributo dos tuplos, o tamanho do que está a ser copiado, simplesmente utiliza o tamanho do padrão (len(match))

    Args:
    inputString (str): A string que está a ser processada pelo algorítmo.

    Returns:
    output (list): Uma lista de todos os tuplos representantes da inputString
    """    
    window = ""
    output = []
    
    while inputString != "":
        match = ""
        for char in range(len(inputString)):
            if inputString[:char+1] in window:
                match = inputString[:char+1]
            else:
                break
        match_len = len(match)
        if match_len < len(inputString):
            next_char = inputString[match_len]
        else:
            next_char = ""
        if match == "":
            offset = 0
            length = 0
        else:
            offset = len(window) - window.rfind(match)
            length = match_len
        output.append((offset, length, next_char))

        window += inputString[:match_len + 1]
        inputString = inputString[match_len + 1:]
        
    return output


def lz77_decode(inputTuples: list):
    """    
    lz77_encode()
    O processo de descodificação é relativamente simples, seguindo sempre a mesma estrutura:
    -Se o offset for 0 (primeira aparência de um caractér), este é escrito.
    -Caso contrário, segue o protocolo esperado do algorítmo, "volta" x caractéres "a trás" e 
    copia o numero de caracteres correspeondentes ao tamanho

    Args:
        inputTuples (list): uma lista de tuplos, seguindo o formato que a função lz77_decode tem como output

    Returns:
        originalString (str): A string descodificada. 
    """    
    originalString = ""
    for offset, length, next_char in inputTuples:
        if offset == 0:
            originalString += next_char
        else:
            copy_index_start = len(originalString) - offset
            for char_index in range(length):
                originalString += originalString[copy_index_start + char_index]
            originalString += next_char
    return originalString
