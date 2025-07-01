ano_contratacao = 1995
salario_inicial = float(input("Salário inicial: R$ "))
ano_atual = 2025  # Exemplo, pode pedir input do usuário
salario = salario_inicial
percentual = 1.5 / 100
for ano in range(ano_contratacao + 1, ano_atual + 1):
    salario += salario * percentual
    percentual *= 2
print(f"Salário atual em {ano_atual}: R$ {salario:.2f}")
