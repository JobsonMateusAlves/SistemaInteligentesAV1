import numpy as np

class Neuronio:
    taxaDeAprendizado = 0

    entradas = []
    pesos = []
    saida = 0

    types = []

    def __init__(self, qtd_entradas, taxaDeAprendizado, types):

        self.entradas = []
        self.taxaDeAprendizado = taxaDeAprendizado

        self.types = types

        intValues = np.random.uniform(0, 1, qtd_entradas)

        for v in intValues:
            self.pesos.append(float(v))

        print(self.pesos)

    def get_saida(self):

        self.saida = 0

        for i in range(len(self.entradas)):
            self.saida = self.saida + self.pesos[i] * self.entradas[i] # Calculo do u (u = -1 * w0 + x1 * w1 + x2 *w2...)

        return self.saida

    def ajustar_pesos(self, resposta):

        # Calculando novos pesos (w = w + n * (d - y) * x)
        for i in range(len(self.pesos)):
            d = 1 if resposta == self.types[0] else -1
            y = self.sinal(self.saida)
            self.pesos[i] = self.pesos[i] + self.taxaDeAprendizado * (d - y) * self.entradas[i]

    def sinal(self, value):
        return 1 if (value >= 0) else -1 # Sinal
