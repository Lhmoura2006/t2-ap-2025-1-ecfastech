while True:
    nome = input("Nome (mais de 3 letras): ")
    if len(nome) <= 3:
        print("Nome deve ter mais de 3 caracteres.")
        continue

    idade = int(input("Idade (0 a 150): "))
    if idade < 0 or idade > 150:
        print("Idade inválida.")
        continue

    salario = float(input("Salário (maior que 0): "))
    if salario <= 0:
        print("Salário inválido.")
        continue

    sexo = input("Sexo (f/m): ").lower()
    if sexo not in ['f', 'm']:
        print("Sexo inválido.")
        continue

    estado_civil = input("Estado civil (s/c/v/d): ").lower()
    if estado_civil not in ['s', 'c', 'v', 'd']:
        print("Estado civil inválido.")
        continue

    print("Informações válidas.")
    break
