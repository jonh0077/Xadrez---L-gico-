from pecas.peao import Peao
from pecas.torre import Torre
from pecas.rei import Rei

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [[None for _ in range(8)] for _ in range(8)]
        self.inicializar_pecas()

    def inicializar_pecas(self):
        self.tabuleiro[1][0] = Peao("branco")
        self.tabuleiro[6][0] = Peao("preto")
        self.tabuleiro[0][0] = Torre("branco")
        self.tabuleiro[7][0] = Torre("preto")
        self.tabuleiro[0][4] = Rei("branco")
        self.tabuleiro[7][4] = Rei("preto")

    def exibir_tabuleiro(self):
        for linha in self.tabuleiro:
            for casa in linha:
                if casa:
                    print(casa.simbolo, end=" ")
                else:
                    print(".", end=" ")
            print()
