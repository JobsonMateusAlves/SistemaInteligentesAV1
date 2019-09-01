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
        # for i in range(qtd_entradas):
        intValues = np.random.randint(low=0, high=10, size=qtd_entradas) #3. Iniciando o vetor de pesos com valores aleatorios
        for v in intValues:
            self.pesos.append(float(v))

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
