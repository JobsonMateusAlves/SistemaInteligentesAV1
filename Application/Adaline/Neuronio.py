import numpy as np

class Neuronio:

    taxaDeAprendizado = 0

    entradas = []
    pesos = []
    saida = 0

    types = []

    def __init__(self, qtd_entradas, taxaDeAprendizado, types):

        self.taxaDeAprendizado = taxaDeAprendizado
        self.types = types

        values = np.random.uniform(0, 1, qtd_entradas)

        # self.pesos = [-2, 1, 2]
        for v in values:
            self.pesos.append(float(v))
        print("wo = {}\tw1 = {}\t w2 = {}".format(self.pesos[0], self.pesos[1], self.pesos[2]))

    def get_saida(self, entradas=[]):
        self.entradas = entradas

        self.saida = 0

        for i in range(len(self.entradas)):
            self.saida = self.saida + (self.pesos[i] * self.entradas[i])

        return self.saida

    def ajustar_pesos(self, resposta=0):

        for i in range(len(self.pesos)):
            d = 1 if resposta == self.types[0] else -1
            u = self.saida
            self.pesos[i] = self.pesos[i] + (self.taxaDeAprendizado * (d - u) * self.entradas[i])

    def sinal(self, value=0):
        return 1 if (value >= 0) else -1

