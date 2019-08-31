from Application.Adaline.Neuronio import Neuronio
import matplotlib.pyplot as plt

class Rede:

    neuronio = Neuronio

    entradas = [[]]
    saida = 0

    n = 1
    E = 0

    eqm = 0
    epoca = 0

    def __init__(self, qtd_entradas, n, E):

        self.n = n
        self.E = E
        self.neuronio = Neuronio(qtd_entradas, self.n)

    def treinar(self, entradas=[[]], respostas=[]):
        self.entradas = entradas

        while True:

            eqm = 0
            eqm_anterior = self.eqm

            for i in range(len(entradas)):
                self.saida = self.neuronio.get_saida(entradas[i])

                eqm += ((respostas[i] - self.saida) * (respostas[i] - self.saida))
                # if self.sinal(self.saida) != respostas[i]:
                self.neuronio.ajustar_pesos(respostas[i])

            self.eqm = eqm/len(self.entradas)


            self.epoca += 1
            if abs(self.eqm - eqm_anterior) < self.E or self.epoca >= 1000:
                break

    def teste(self, entradas=[[]]):

        for i in range(len(entradas)):
            self.saida = self.neuronio.get_saida(entradas[i])
            print(self.sinal(self.saida))

    def sinal(self, value=0):

        return 1 if (value >= 0) else -1