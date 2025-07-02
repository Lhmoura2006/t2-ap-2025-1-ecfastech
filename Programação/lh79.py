def ler_e_imprimir(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
