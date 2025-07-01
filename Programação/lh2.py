while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if usuario == senha:
        print("Erro: a senha não pode ser igual ao nome de usuário.")
    else:
        print("Cadastro realizado com sucesso.")
        break
