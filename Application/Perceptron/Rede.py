from Application.Perceptron.Neuronio import Neuronio
import matplotlib.pyplot as plt

class Rede:

    neuronio = Neuronio
    entradas = [[]]
    saida = 0
    n = 1
    epoca = 0
    existe_erro = True


    def __init__(self, qtd_entradas, n=0):

        self.n = n
        self.neuronio = Neuronio(qtd_entradas, self.n)

    def treinar(self, entradas=[[]], respostas=[]):
        self.entradas = entradas

        while self.existe_erro and self.epoca < 1000:

            erros = 0

            for i in range(len(entradas)):

                self.neuronio.entradas = entradas[i]
                self.saida = self.neuronio.get_saida()

                if self.saida != respostas[i]:

                    self.neuronio.ajustar_pesos(respostas[i])
                    self.plotar()
                    erros += 1

                self.epoca += 1

            self.existe_erro = erros > 0


    def testar(self, entradas=[[]]):
        self.entradas = entradas

        for i in range(len(entradas)):
            self.neuronio.entradas = entradas[i]
            self.saida = self.neuronio.get_saida()
            print(self.saida)

    def plotar(self):
        # Gráfico
        a = [[0.5, 1.5], [-0.5, 0.5], [0.5, 0.5], [0.5, -0.3], [1.5, 1.5]]
        plt.figure()
        for i in range(len(a)):
            m = 'o' if i % 2 == 0 else 'x'
            plt.scatter(a[i][0], a[i][1], marker=m)
        # plt.axis([])

        plt.tight_layout()

        wo = self.neuronio.pesos[0]
        w1 = self.neuronio.pesos[1]
        w2 = self.neuronio.pesos[2]

        # p1 = [(wo - w2 * 0) / w1, 0]
        # p2 = [0, (wo - w1 * 0) / w2]
        p1 = [0, (wo - w1 * 0) / w2]
        p2 = [2, (wo - w1 * 2) / w2]
        # print("p1: {} p2: {}".format(p1, p2))

        plt.plot(p1, p2)
        plt.draw()


    def show(self):
        plt.show()






