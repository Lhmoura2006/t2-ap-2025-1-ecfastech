def exercicio_59(texto):
    texto = texto.lower()
    vogais = 'aeiou'
    count_vogais = sum(1 for c in texto if c in vogais)
    count_consoantes = sum(1 for c in texto if c.isalpha() and c not in vogais)
    print(f"Vogais: {count_vogais}")
    print(f"Consoantes: {count_consoantes}")
