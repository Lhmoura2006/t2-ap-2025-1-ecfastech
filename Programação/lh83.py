def somar_numeros_arquivo(nome_arquivo):
    soma = 0
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                try:
                    soma += int(linha.strip())
                except ValueError:
                    pass
        return soma
    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
        return 0
