

class Neuronio:

    entradas = []
    pesos = []
    saida = 0
    n = 0

    def __init__(self, qtd_entradas=0, n = 0):

        self.entradas = []
        self.n = n
        # for i in range(qtd_entradas):
        self.pesos.append(2)
        self.pesos.append(1)
        self.pesos.append(2)

    def get_saida(self):

        value = 0

        for i in range(len(self.entradas)):
            value = value + self.pesos[i]*self.entradas[i]

        self.saida = 1 if (value >= 0) else -1

        return self.saida

    def ajustar_pesos(self, resposta = 0):

        for i in range(len(self.pesos)):
            self.pesos[i] = self.pesos[i] + self.n * (resposta - self.saida) * self.entradas[i]
        print(self.pesos)



