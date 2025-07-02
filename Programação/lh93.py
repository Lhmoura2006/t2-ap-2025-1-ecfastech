class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Livro: {self.titulo} por {self.autor}"

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f"Conta de {self.titular}, Saldo: R${self.saldo:.2f}"
