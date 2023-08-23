import random

class Card:
    def __init__(self, valor, nipe):
        self.valor = valor
        self.nipe = nipe

    def __str__(self):
        return f"{self.valor} de {self.nipe}"


class Deck:
    def __init__(self):
        self.cards = []

    def criar_deck(self):
        valores = ["as", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valete", "rainha", "rei"]
        nipes = ["copas", "ouros", "espadas", "paus"]
        for nipe in nipes:
            for valor in valores:
                card = Card(nipe, valor)
                self.cards.append(card)

    def embaralhar(self):
        random.shuffle(self.cards)

    def mostra_deck(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None


# Exemplo de uso:
# Cria um baralho, embaralha e faz uma mão de 5 cartas
deck = Deck()
deck.criar_deck()
deck.embaralhar()
mao = [deck.mostra_deck() for _ in range(10)]

for card in mao:
    print(card)
