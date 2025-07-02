def substituir_em_arquivo(nome_arquivo, texto_antigo, texto_novo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        conteudo = conteudo.replace(texto_antigo, texto_novo)
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write(conteudo)
    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
