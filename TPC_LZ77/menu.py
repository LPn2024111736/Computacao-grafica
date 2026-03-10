import lz77 
import gerarDados

while True:
    print("""
Opções: 
1. Gerar dados
2. Codificar dados 
3. Decodificar dados [DADOS TÊM DE TER SIDO CODIFICADOS]
4. Relação entre lz77 e restantes algorítmos da familia LZ 
5. Saír
    """)
    option=input("Escolha uma opção: ")
    match option:
        case "1":
            gerarDados.criarDados(100,100)
            print("Dados (binário e hex) foram guardados nos seus ficheiros! Verifique estes para ver o que está escrito.")
        case "2":
            with open("dadosindexplaintext.txt","r") as f:
                dadosPaleta=f.read()
            with open("dadostruecolorplaintext.txt","r") as f:
                dadosTrue=f.read()
            dadosConvertidosI=lz77.lz77_encode(dadosPaleta)
            dadosConvertidosT=lz77.lz77_encode(dadosTrue)
            print("Número de tuplos (Imagem com paleta reduzida): ", len(dadosConvertidosI))
            print("Número de tuplos (Imagem true color): ", len(dadosConvertidosT))
            with open("tuplosindex.txt","w") as f:
                 f.write(str(dadosConvertidosI))
            with open("tuplostruecolor.txt","w") as f:
                 f.write(str(dadosConvertidosT))
            print("Dados (lista de tuplos) foram guardados nos seus ficheiros! Verifique estes para ver o que está escrito. NOTA: Por questões de tempo, estes dados são apenas para leitura. Valores codificados para traduzir são apenas salvos durante runtime.")
        case "3":
            dadosTraduzidosI=lz77.lz77_decode(dadosConvertidosI)
            dadosTraduzidosT=lz77.lz77_decode(dadosConvertidosT)
            with open("traducaoindex.txt","w") as f:
                 f.write(str(dadosTraduzidosI))
            with open("traducaotruecolor.txt","w") as f:
                 f.write(str(dadosTraduzidosT))
            print("Dados (texto) foram guardados nos seus ficheiros! Verifique estes para ver o que está escrito.")
        case "4":
            print("A família de algorítmos LZ são uma família de algorítmos de compressão sem perdas publicados por Abraham Lempel e Jacob Ziv, daí o nome. O algorítmo em estudo neste exercício, o algorítmo LZ77 (publicado em 1977), serve como a base para algorítmos utilizando janela deslizante, com algorítmos que utilizam dicionários de padrões explícitos usando o algorítmo LZ78 como base. A variante mais notável do algorítmo LZ77 é o algorítmo DEFLATE, o qual é utilizado em formatos populares como PNG, ZIP e GIF. Este algorítmo trata-se de uma combinação do LZ77 com codificação de Huffman, um sistema que atribui códigos a caractéres dependendo da sua frequência.")
        case "5":
            break
            

            


