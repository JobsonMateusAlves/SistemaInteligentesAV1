from Application.Adaline.Neuronio import Neuronio
import matplotlib as plt
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
        print(self.epoca)

    def get_Eqm(self):

        eqmAux = 0

        for i in range(len(self.entradas)):
            u = self.neuronio.get_saida(self.entradas[i])
            eqmAux += ((self.respostas[i] - u)*(self.respostas[i] - u))

        return eqmAux/len(self.entradas)

    def testar(self, entradas=[[]], respostas=[]):

        self.entradas = entradas
        self.respostas = respostas

        self.filter()
        print("x1\tx2\ty\t\td")
        for i in range(len(self.entradas)):
            self.neuronio.entradas = self.entradas[i]
            self.saida = self.get_classe(self.neuronio.sinal(self.neuronio.get_saida()))

            print("{} \t{} \t{} \t\t{}".format(round(self.entradas[i][1], 3), round(self.entradas[i][2], 3), self.saida, self.respostas[i]))

        # self.plotar()

    def get_classe(self, value=0):

        return self.types[0] if value == 1 else self.types[1]