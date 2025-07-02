def filtrar_linhas(nome_arquivo_origem, nome_arquivo_destino, palavra_chave):
    try:
        with open(nome_arquivo_origem, 'r', encoding='utf-8') as f_origem, \
             open(nome_arquivo_destino, 'w', encoding='utf-8') as f_destino:
            for linha in f_origem:
                if palavra_chave.lower() in linha.lower():
                    f_destino.write(linha)
    except FileNotFoundError:
        print("Erro: arquivo de origem não encontrado.")
