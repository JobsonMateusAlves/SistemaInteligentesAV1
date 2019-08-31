
class Neuronio:

    entradas = []
    pesos = []
    saida = 0
    n = 0

    def __init__(self, qtd_entradas=0, n = 0):

        self.entradas = []
        self.n = n
        # for i in range(qtd_entradas):
        self.pesos = [-2.0, 1.0, 2.0]

    def get_saida(self, entradas=[]):
        self.entradas = entradas

        self.saida = 0

        for i in range(len(self.entradas)):
            self.saida = self.saida + (self.pesos[i] * self.entradas[i])

        return self.saida

    def ajustar_pesos(self, resposta = 0):
        for i in range(len(self.pesos)):
            # print("w = {} + {} * ({} - {}) * {}".format(self.pesos[i], self.n, resposta, self.saida, self.entradas[i]))
            self.pesos[i] = self.pesos[i] + self.n * (resposta - self.saida) * self.entradas[i]

        y = self.sinal(self.saida)
        u = round(self.saida, 3)
        w0 = round(self.pesos[0], 3)
        w1 = round(self.pesos[1], 3)
        w2 = round(self.pesos[2], 3)
        # print("y = {} \tu = {} \tw0 = {} \tw1 = {} \tw2 = {}".format(y, u, w0, w1, w2))


    def sinal(self, value=0):

        return 1 if (value >= 0) else -1

