class DigitoDisplay:
    REPRESENTACOES = {
        0: [[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]],
        1: [[0,1,0],[1,1,0],[0,1,0],[0,1,0],[1,1,1]],
        2: [[1,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,1]],
        3: [[1,1,1],[0,0,1],[1,1,1],[0,0,1],[1,1,1]],
        4: [[1,0,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1]],
        5: [[1,1,1],[1,0,0],[1,1,1],[0,0,1],[1,1,1]],
        6: [[1,1,1],[1,0,0],[1,1,1],[1,0,1],[1,1,1]],
        7: [[1,1,1],[0,0,1],[0,1,0],[1,0,0],[1,0,0]],
        8: [[1,1,1],[1,0,1],[1,1,1],[1,0,1],[1,1,1]],
        9: [[1,1,1],[1,0,1],[1,1,1],[0,0,1],[1,1,1]],
        10: [[1,1,1],[1,0,1],[1,1,1],[1,0,1],[1,0,1]], # A
        11: [[1,0,0],[1,0,0],[1,1,0],[1,0,1],[1,1,0]], # B
        12: [[1,1,1],[1,0,0],[1,0,0],[1,0,0],[1,1,1]], # C
        13: [[1,0,0],[1,0,0],[1,0,1],[1,0,0],[1,1,1]], # D
        14: [[1,1,1],[1,0,0],[1,1,1],[1,0,0],[1,1,1]], # E
        15: [[1,1,1],[1,0,0],[1,1,1],[1,0,0],[1,0,0]], # F
    }

    def __init__(self, valor_decimal):
        self.valor_decimal = valor_decimal
        self.representacao_binaria = self.REPRESENTACOES[valor_decimal]

    def obter_representacao_binaria(self):
        return self.representacao_binaria

class DisplayDigital:
    def __init__(self, num_digitos, largura_digito=3, altura_digito=5):
        self.num_digitos = num_digitos
        self.largura_digito = largura_digito
        self.altura_digito = altura_digito
        self.digitos = [DigitoDisplay(0) for _ in range(num_digitos)]

    def exibir_numero(self, numero_str, base):
        numero_str = converter_base(numero_str, base, 16) if base != 16 else numero_str.upper()
        if len(numero_str) > self.num_digitos:
            print("Número muito grande para o display")
            return
        self.digitos = [DigitoDisplay(DIGITOS.index(c)) for c in numero_str.zfill(self.num_digitos)]

    def renderizar_display(self):
        linhas_display = [[' ' for _ in range(self.num_digitos * (self.largura_digito + 1) - 1)]
                          for _ in range(self.altura_digito)]

        for idx, digito in enumerate(self.digitos):
            binario = digito.obter_representacao_binaria()
            col_offset = idx * (self.largura_digito + 1)
            for i in range(self.altura_digito):
                for j in range(self.largura_digito):
                    if binario[i][j]:
                        linhas_display[i][col_offset + j] = '*'

        for linha in linhas_display:
            print(''.join(linha))
