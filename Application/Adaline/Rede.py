from Application.Adaline.Neuronio import Neuronio
import matplotlib.pyplot as plt
import numpy as np

class Rede:
    normalizado = False

    taxaDeAprendizado = 1
    precisao = 0

    neuronio = Neuronio

    x = [[]]
    entradas = [[]]
    respostas = []
    saida = 0

    epoca = 0
    eqm = 0
    eqm_anterior = 1000

    types = []
    acertos = 0

    def __init__(self, qtd_entradas, taxaDeAprendizado, precisao, types):
        self.types = types
        self.taxaDeAprendizado = taxaDeAprendizado
        self.precisao = precisao
        self.neuronio = Neuronio(qtd_entradas, self.taxaDeAprendizado, self.types)

    def filter(self):

        toRemove = []
        for i in range(len(self.respostas)):
            if self.respostas[i] != self.types[0] and self.respostas[i] != self.types[1]:
                toRemove.append(i)

        for i in reversed(toRemove):
            self.entradas.pop(i)
            self.respostas.pop(i)
            self.x.pop(i)

    def treinar(self, entradas=[], respostas=[]):

        self.entradas = entradas
        self.respostas = respostas
        self.filter()

        while abs(self.eqm - self.eqm_anterior) > self.precisao and self.epoca < 1000:

            self.eqm_anterior = self.eqm

            for i in range(len(self.entradas)):
                self.saida = self.neuronio.get_saida(self.entradas[i])

                if self.get_classe(self.neuronio.sinal(self.saida)) != self.respostas[i]:
                    self.neuronio.ajustar_pesos(self.respostas[i])

            self.epoca += 1
            self.eqm = self.get_Eqm()
        print("Epocas = {}".format(self.epoca))
        print("wo = {}\tw1 = {}\t w2 = {}".format(self.neuronio.pesos[0], self.neuronio.pesos[1], self.neuronio.pesos[2]))
        self.plotar()

    def get_Eqm(self):

        eqmAux = 0

        for i in range(len(self.entradas)):
            u = self.neuronio.get_saida(self.entradas[i])
            eqmAux += ((self.respostas[i] - u)*(self.respostas[i] - u))

        return eqmAux/len(self.entradas)

    def testar(self, entradas=[[]], respostas=[], plotar=True):

        self.acertos = 0

        self.entradas = entradas
        self.respostas = respostas

        self.filter()
        if plotar:
            print("x1\tx2\ty\t\td")
        for i in range(len(self.entradas)):
            self.neuronio.entradas = self.entradas[i]
            u = self.get_classe(self.neuronio.sinal(self.neuronio.get_saida(self.entradas[i])))
            if plotar:
                print("{} \t{} \t{} \t\t{}".format(round(self.entradas[i][1], 3), round(self.entradas[i][2], 3), u, self.respostas[i]))
            if u == self.respostas[i]:
                self.acertos += 1

        if plotar:
            self.plotar()

    def get_classe(self, value=0):

        return self.types[0] if value == 1 else self.types[1]

    def get_taxa_de_acerto(self, entradas=[[]], respostas=[]):
        self.testar(entradas, respostas, False)
        return self.acertos/len(self.entradas)*100

    #Plotando gráficos
    def plotar(self):
        # Gráfico
        plt.figure()
        for i in range(len(self.x)):
            m = '#FF0000' if self.respostas[i] == self.types[0] else '#0000FF'
            plt.scatter(self.x[i][0], self.x[i][1], color=m, marker='x')

        plt.scatter(None, None, color='#FF0000', label=self.types[0])
        plt.scatter(None, None, color='#0000FF', label=self.types[1])

        plt.legend()

        if self.normalizado:
            plt.axis([-2, 2, -2, 2])
        else:
            plt.axis([0, 10, 0, 10])

        plt.tight_layout()

        wo = self.neuronio.pesos[0]
        w1 = self.neuronio.pesos[1]
        w2 = self.neuronio.pesos[2]

        x1 = np.linspace(0, 10, 100)
        if self.normalizado:
            x1 = np.linspace(-10, 10, 100)

        x2 = (-w1*x1 + wo)/w2

        plt.plot(x1, x2, '-g')
        plt.draw()


    def show(self):
        plt.show()
