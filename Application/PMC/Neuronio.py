import numpy as np
import math


class Neuronio:

    taxa_de_aprendizado = 0
    pesos = []
    w0 = 0

    last_saida = 0

    def __init__(self, qtd_entradas, taxa_de_aprendizado):

        self.taxa_de_aprendizado = taxa_de_aprendizado

        self.__set_pesos(qtd_entradas)

    def __set_pesos(self, qtd_entradas):
        value = np.random.uniform(0, 1, 1)
        self.w0 = float(value)

        values = np.random.uniform(0, 1, qtd_entradas)
        for v in values:
            self.pesos.append(float(v))

    def get_saida(self, entradas):

        saida = 0

        for index, entrada in enumerate(entradas):
            saida += entrada * self.pesos[index]
        saida += -1 * self.w0

        self.last_saida = self.__sigmoid(saida)
        return self.last_saida

    def ajustar(self, erro, entradas):

        for index, peso in enumerate(self.pesos):
            peso += self.taxa_de_aprendizado * erro * entradas[index]

        self.w0 += self.taxa_de_aprendizado * erro * -1

    def __sigmoid(self, x):

        return 1/(1 + math.exp(-x))