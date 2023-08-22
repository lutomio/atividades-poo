class Series:

    def __init__(self, numero):
        self.numero = numero

    def fatorial(self):
        fat = 1
        for i in range(1, self.numero + 1):
            fat *= i

        return fat

    def primo(self):
        if self.numero <= 1:
            return False
        for i in range(2,self.numero):
            if self.numero % i == 0:
                return False
        return True

    def fibonacci(self):
        ultimo = 1
        penultimo = 1
        if (self.numero == 1) or (self.numero == 2):
            print("1")
        else:
            for count in range(2, self.numero, 1):
                termo = ultimo + penultimo
                penultimo = ultimo
                ultimo = termo
            return termo


se = Series(4)
o_fatorial = se.fatorial()
print(f'O fatorial é {o_fatorial}')
verifica = se.primo()
print(f'O numero é primo? {verifica}')
print(se.fibonacci())

