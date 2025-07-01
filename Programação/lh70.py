import random
import string
def gerar_senha(comprimento, incluir_numeros=True, incluir_simbolos=False):
    caracteres = string.ascii_letters
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += "!@#$%^&*"
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha
