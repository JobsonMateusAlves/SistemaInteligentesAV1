import numpy as np

class Neuronio:

    entradas = []
    pesos = []
    saida = 0
    taxaDeAprendizado = 0
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
            self.saida = self.saida + self.pesos[i] * self.entradas[i]

        return self.saida

    def ajustar_pesos(self, resposta):

        for i in range(len(self.pesos)):
            r = 1 if resposta == self.types[0] else -1
            self.pesos[i] = self.pesos[i] + self.taxaDeAprendizado * (r - self.sinal(self.saida)) * self.entradas[i]

    def sinal(self, value):
        return 1 if (value >= 0) else -1
