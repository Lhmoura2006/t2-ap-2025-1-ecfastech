ef exercicio_62(frase):
    limpa = ''.join(c.lower() for c in frase if c.isalnum())
    print(limpa == limpa[::-1])
