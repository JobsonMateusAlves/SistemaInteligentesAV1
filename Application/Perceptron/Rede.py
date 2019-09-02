from Application.Perceptron.Neuronio import Neuronio
import matplotlib.pyplot as plt
import numpy as np

class Rede:

    normalizado = False
    neuronio = Neuronio
    x = [[]]
    a = [[]]
    entradas = [[]]
    respostas = []

    saida = 0

    taxaDeAprendizado = 1
    epoca = 0

    existe_erro = True
    types = []


    def __init__(self, qtd_entradas, taxaDeAprendizado, types):

        self.taxaDeAprendizado = taxaDeAprendizado
        self.neuronio = Neuronio(qtd_entradas, self.taxaDeAprendizado, types)
        self.types = types

    def treinar(self, entradas=[[]], respostas=[]):

        self.entradas = entradas
        self.respostas = respostas
        self.filter()

        while self.existe_erro and self.epoca < 1000:

            erros = 0

            for i in range(len(entradas)):

                self.neuronio.entradas = entradas[i]

                self.saida = self.sinal(self.neuronio.get_saida())

                if self.saida != respostas[i]:

                    self.neuronio.ajustar_pesos(respostas[i])
                    erros += 1

            self.epoca += 1

            self.existe_erro = erros > 0
        print("wo = {} \tw1 = {} \t w2 = {}".format(self.neuronio.pesos[0], self.neuronio.pesos[1], self.neuronio.pesos[2]))
        print("Epoca: {}".format(self.epoca))
        self.plotar()

    def filter(self):

        toRemove = []
        for i in range(len(self.respostas)):
            if self.respostas[i] != self.types[0] and self.respostas[i] != self.types[1]:
                toRemove.append(i)
        for i in reversed(toRemove):
            self.entradas.pop(i)
            self.respostas.pop(i)
            self.x.pop(i)
            if len(self.a) > i:
                self.a.pop(i)

    def sinal(self, value):
        return self.types[0] if (value >= 0) else self.types[1]


    def testar(self, entradas=[[]], respostas=[], a=[]):
        self.entradas = entradas
        self.respostas = respostas
        self.a = a
        self.filter()

        print("x1\tx2\tx1N\tx2N\ty\t\td")
        for i in range(len(self.entradas)):
            self.neuronio.entradas = self.entradas[i]
            self.saida = self.sinal(self.neuronio.get_saida())
            print("{} \t{} \t{} \t{} \t{} \t\t{}".format(round(a[i][0], 3), round(a[i][1], 3), round(self.entradas[i][1], 3), round(self.entradas[i][2], 3), self.saida, self.respostas[i]))
        self.plotar()

















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
            plt.axis([-1, 1, -1, 1])
        else:
            plt.axis([0, 10, 0, 10])

        plt.tight_layout()

        wo = self.neuronio.pesos[0]
        w1 = self.neuronio.pesos[1]
        w2 = self.neuronio.pesos[2]

        x1 = np.linspace(0, 10, 100)
        if self.normalizado:
            x1 = np.linspace(-1, 1, 100)
        x2 = (-w1*x1 + wo)/w2

        plt.plot(x1, x2, '-g')
        plt.draw()


    def show(self):
        plt.show()






