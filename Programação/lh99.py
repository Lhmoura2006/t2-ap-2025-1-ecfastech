def realizar_operacao_base(num1_str, num2_str, base_origem, operacao, base_destino):
    n1 = para_decimal(num1_str, base_origem)
    n2 = para_decimal(num2_str, base_origem)

    if operacao == '+':
        resultado = n1 + n2
    elif operacao == '-':
        resultado = n1 - n2
    elif operacao == '*':
        resultado = n1 * n2
    elif operacao == '/':
        if n2 == 0:
            return "Erro: divisão por zero"
        resultado = round(n1 / n2)
    else:
        return "Operação inválida"

    return de_decimal(resultado, base_destino)
