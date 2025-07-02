def ler_csv_simples(nome_arquivo):
    dados = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
        # Assume primeira linha cabeçalho
        for linha in linhas[1:]:
            valores = linha.strip().split(',')
            dados.append(valores)
        return dados
    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
        return []
