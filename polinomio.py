class Polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes

    def grau(self):
        return len(self.coeficientes) - 1

    def avaliar(self, x):
        resultado = 0
        for i in range(len(self.coeficientes)):
            resultado += self.coeficientes[i] * (x ** i)
        return resultado

    def soma(self, outro):
        novo_poli = []
        max_grau = max(self.grau(), outro.grau())
        for i in range(max_grau + 1):
            if i <= self.grau():
                c1 = self.coeficientes[i]
            else:
                c1 = 0
            if i <= outro.grau():
                c2 = outro.coeficientes[i]
            else:
                c2 = 0
            novo_poli.append(c1 + c2)
        return novo_poli

    def multiplicacao(self, outro):
        novo_poli = [0] * (self.grau() + outro.grau() + 1)
        for i in range(self.grau() + 1):
            for j in range(outro.grau() + 1):
                novo_poli[i + j] += self.coeficientes[i] * outro.coeficientes[j]
        return novo_poli


p1 = Polinomio([1, 2, 3])
p2 = Polinomio([4, 5, 6])

print(p1.grau())
print(p1.soma(p2))
print(p1.avaliar(2))
print(p1.multiplicacao(p2))

