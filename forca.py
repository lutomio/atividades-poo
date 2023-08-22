class Forca:

    def __init__(self, palavra, vidas=6):
        self.palavra = palavra
        self.vidas = vidas
        self.acertos = []
        self.erros = []

    def jogo(self):
        while self.vidas > 0:
            self.exibir_letras()
            letra = input('digite uma letra: ')
            if letra in self.palavra:
                self.acertos.append(letra)
                print(f'letras erradas ja digitadas {self.erros}')
                if self.vitoria():
                    print("Voce ganhou!!")
                    print(f'A palavra era {self.palavra}')
                    break

            else:
                self.vidas -= 1
                self.erros.append(letra)
                print(f'Errou, voce ainda tem {self.vidas} vidas')
                print(f'letras erradas ja digitadas {self.erros}')
                if self.vidas == 0:
                    print('Voce perdeu!!')
                    print(f'A palavra era {self.palavra}')

    def vitoria(self):
        for letra in self.palavra:
            if letra not in self.acertos:
                return False
        return True

    def exibir_letras(self):
        palavra_formatada = ""
        for letra in self.palavra:
            if letra in self.acertos:
                palavra_formatada += letra + " "
            else:
                palavra_formatada += "_ "
        print(palavra_formatada)


game = Forca('python')
game.jogo()
