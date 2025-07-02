def contar_linhas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
        return len(linhas)
    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
        return 0
