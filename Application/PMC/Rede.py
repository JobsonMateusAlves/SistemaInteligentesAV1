from Application.PMC.Neuronio import Neuronio
from enum import Enum
import numpy as np

MAX_EPOCAS = 10000


class Camada(Enum):
    ENTRADA = 1
    ESCONDIDA = 2
    SAIDA = 3


class TrainMode(Enum):
    ONLINE = 1
    OFFLINE = 2


class Rede:

    camada_de_entrada = []
    camada_escondida = []
    camada_de_saida = []

    # Setup
    def __init__(self, entradas, taxa_de_aprendizado, qtd_neuronios_camada_escondida, respostas):

        self.__setup_camada(Camada.ENTRADA, len(entradas[0]), len(entradas[0]), taxa_de_aprendizado)
        self.__setup_camada(Camada.ESCONDIDA, len(entradas[0]), qtd_neuronios_camada_escondida, taxa_de_aprendizado)
        self.__setup_camada(Camada.SAIDA, qtd_neuronios_camada_escondida, len(respostas[0]), taxa_de_aprendizado)

    def __setup_camada(self, camada, qtd_entradas, qtd_neuronios, taxa_de_aprendizado):

        for _ in range(qtd_neuronios):

            if camada == Camada.ENTRADA:
                self.camada_de_entrada.append(Neuronio(qtd_entradas, taxa_de_aprendizado))
            elif camada == Camada.ESCONDIDA:
                self.camada_escondida.append(Neuronio(qtd_entradas, taxa_de_aprendizado))
            else:
                self.camada_de_saida.append(Neuronio(qtd_entradas, taxa_de_aprendizado))

    # Training cycle
    def treinar(self, entradas, train_mode, precisao):

        if train_mode == TrainMode.ONLINE:
            self.__treinamento_online(entradas, precisao)

    def __treinamento_online(self, entradas, respostas, precisao):
        eqm = 0
        eqm_anterior = 1000
        epocas = 0

        while abs(eqm - eqm_anterior) > precisao and epocas < MAX_EPOCAS:

            eqm_anterior = eqm

            for index, entrada in enumerate(entradas):

                saidas = self.__forward(entrada)
                self.__backward(entrada, saidas, respostas[index])
            #?
            #new EQM
            epocas += 1
            if epocas == MAX_EPOCAS:
                print("Atingiu o maximo de epocas.")



    # Forward methods
    def __forward(self, entrada):

        saida_camada0 = self.__run_camada(Camada.ENTRADA, entrada)
        saida_camada1 = self.__run_camada(Camada.ESCONDIDA, saida_camada0)
        saida_camada2 = self.__run_camada(Camada.SAIDA, saida_camada1)

        return (saida_camada0, saida_camada1, saida_camada2)

    def __run_camada(self, camada, entrada):

        saida = []
        neuronios = []

        if camada == Camada.ENTRADA:
            neuronios = self.camada_de_entrada
        elif camada == Camada.ESCONDIDA:
            neuronios = self.camada_escondida
        else:
            neuronios = self.camada_de_saida

        for neuronio in neuronios:
            saida.append(neuronio.get_saida(entrada))

        return saida

    # Backward methods
    def __backward(self, entrada, saidas, resposta):
        print("TODO")
        erro_camada_saida = self.__get_error(saidas[2], resposta, [])
        self.__adjust_camada(Camada.SAIDA, erro_camada_saida, saidas[1])

        erro_camada_escondida = self.__get_error(saidas[1], resposta, erro_camada_saida)
        self.__adjust_camada(Camada.ESCONDIDA, erro_camada_escondida, saidas[0])

        erro_camada_entrada = self.__get_error(saidas[0], resposta, erro_camada_escondida)
        self.__adjust_camada(Camada.ESCONDIDA, erro_camada_entrada, entrada)

    def __adjust_camada(self, camada, erro, entrada):

        neuronios = []
        new_pesos = []
        if camada == Camada.ENTRADA:
            neuronios = self.camada_de_entrada
        elif camada == Camada.ESCONDIDA:
            neuronios = self.camada_escondida
        else:
            neuronios = self.camada_de_saida

        for index, neuronio in enumerate(neuronios):
            new_pesos.append(neuronio.ajustar(erro[index]))


    # General methods

    def __get_error(self, camada, saida, resposta, erro_proxima_camada):

        erro = []

        if camada == Camada.SAIDA:
            neuronios = self.camada_de_saida

            for index, neuronio in enumerate(neuronios):
                 erro.append(saida[index] * (1 - saida[index]) * (resposta[index] - saida[index]))

        elif camada == Camada.ESCONDIDA:

            neuronios = self.camada_escondida

            for index, neuronio in enumerate(neuronios):
                pesos = self.__get_pesos_of(Camada.SAIDA, index)
                somatorio = 0
                for i, peso in enumerate(pesos):
                    somatorio += peso * erro_proxima_camada[i]

                erro.append(saida[index] * (1 - saida[index]) * somatorio) # Duvida no somatório

        else:

            neuronios = self.camada_de_entrada

            for index, neuronio in enumerate(neuronios):
                pesos = self.__get_pesos_of(Camada.SAIDA, index)
                somatorio = 0
                for i, peso in enumerate(pesos):
                    somatorio += peso * erro_proxima_camada[i]

                erro.append(saida[index] * (1 - saida[index]) * somatorio)


        return erro

    def __get_pesos_of(self, camada, index):

        neuronios = []
        pesos = []
        if camada == Camada.ENTRADA:
            neuronios = self.camada_de_entrada
        elif camada == Camada.ESCONDIDA:
            neuronios = self.camada_escondida
        else:
            neuronios = self.camada_de_saida

        for neuronio in neuronios:
            pesos.append(neuronio.pesos[index])

        return pesos

    # def get_Eqm(self, eqm):
    #
    #
    #
    #     for i in range(len(self.u_array)):
    #         u = self.u_array[i]
    #         eqmAux += ((self.respostas[i] - u)*(self.respostas[i] - u))
    #
    #     return eqmAux/len(self.entradas)