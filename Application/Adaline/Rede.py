from Application.Adaline.Neuronio import Neuronio
import matplotlib.pyplot as plt

class Rede:

    neuronio = Neuronio

    entradas = [[]]
    saida = 0

    taxaDeAprendizado = 1
    precisao = 0

    epoca = 0
    eqm = 0
    eqm_anterior = 0

    def __init__(self, qtd_entradas, taxaDeAprendizado, precisao):

        self.taxaDeAprendizado = taxaDeAprendizado
        self.precisao = precisao
        self.neuronio = Neuronio(qtd_entradas, self.taxaDeAprendizado)

    def treinar(self, entradas, respostas):

        self.entradas = entradas

        while True:

            self.eqm_anterior = self.eqm

            eqm = 0

            for i in range(len(entradas)):

                self.saida = self.neuronio.get_saida(entradas[i])

                eqm += ((respostas[i] - self.saida) * (respostas[i] - self.saida))

                self.neuronio.ajustar_pesos(respostas[i])

            self.eqm = eqm/len(self.entradas)

            self.epoca += 1

            if abs(self.eqm - self.eqm_anterior) < self.precisao or self.epoca >= 10000:
                break
        print("epoca: {}".format(self.epoca))



    def sinal(self, value=0):

        return 1 if (value >= 0) else -1

    def teste(self, entradas=[[]]):

        for i in range(len(entradas)):
            self.saida = self.neuronio.get_saida(entradas[i])
            print(self.sinal(self.saida))