import string
def contar_palavras(lista_de_frases):
    dicionario = {}
    for frase in lista_de_frases:
        palavras = frase.lower().translate(str.maketrans('', '', string.punctuation)).split()
        for palavra in palavras:
            dicionario[palavra] = dicionario.get(palavra, 0) + 1
    return dicionario
