while True:
    try:
        pop_a = int(input("População do país A: "))
        pop_b = int(input("População do país B: "))
        taxa_a = float(input("Taxa de crescimento A (%): "))
        taxa_b = float(input("Taxa de crescimento B (%): "))

        if pop_a > 0 and pop_b > 0 and taxa_a > 0 and taxa_b > 0:
            anos = 0
            while pop_a < pop_b:
                pop_a *= (1 + taxa_a / 100)
                pop_b *= (1 + taxa_b / 100)
                anos += 1
            print(f"População de A ultrapassará B em {anos} anos.")
        else:
            print("Todos os valores devem ser maiores que zero.")

    except ValueError:
        print("Digite apenas números válidos.")

    repetir = input("Deseja repetir? (s/n): ").lower()
    if repetir != 's':
        break
