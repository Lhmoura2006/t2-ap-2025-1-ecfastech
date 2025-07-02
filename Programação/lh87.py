def adicionar_numero_linha(nome_arquivo_origem, nome_arquivo_destino):
    try:
        with open(nome_arquivo_origem, 'r', encoding='utf-8') as f_origem, \
             open(nome_arquivo_destino, 'w', encoding='utf-8') as f_destino:
            for idx, linha in enumerate(f_origem, 1):
                f_destino.write(f"{idx} {linha}")
    except FileNotFoundError:
        print("Erro: arquivo de origem não encontrado.")
