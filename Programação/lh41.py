divida = float(input("Valor da dívida: R$ "))
parcelas = [1,3,6,9,12]
juros = [0,10,15,20,25]

print("Valor da Dívida  Valor dos Juros  Quantidade de Parcelas  Valor da Parcela")
for i in range(len(parcelas)):
    valor_juros = divida * (juros[i] / 100)
    total = divida + valor_juros
    parcela_valor = total / parcelas[i]
    print(f"R$ {total:.2f}         R$ {valor_juros:.2f}           {parcelas[i]}     
