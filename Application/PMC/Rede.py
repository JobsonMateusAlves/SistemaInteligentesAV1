from Application.PMC.Neuronio import Neuronio
from enum import Enum
import numpy as np
import random
from Application.PMC.ReaderManager import ReaderManager

MAX_EPOCAS = 10000


class Camada(Enum):
    ESCONDIDA = 2
    SAIDA = 3


class TrainMode(Enum):
    ONLINE = 1
    OFFLINE = 2


class Rede:

    camada_escondida = []
    camada_de_saida = []
    Y3 = []
    file = ""

    # Setup
    def __init__(self, entradas, taxa_de_aprendizado, qtd_neuronios_camada_escondida, respostas):

        self.__setup(Camada.ESCONDIDA, len(entradas[0]), qtd_neuronios_camada_escondida, taxa_de_aprendizado)
        self.__setup(Camada.SAIDA, qtd_neuronios_camada_escondida, len(respostas[0]), taxa_de_aprendizado)

    def __setup(self, camada, qtd_entradas, qtd_neuronios, taxa_de_aprendizado):

        for i in range(qtd_neuronios):
            neuronio = Neuronio(qtd_entradas, taxa_de_aprendizado, i)
            if camada == Camada.ESCONDIDA:
                self.camada_escondida.append(neuronio)
            else:
                self.camada_de_saida.append(neuronio)

    # Training cycle
    def treinar(self, tupla, train_mode, precisao):

        if train_mode == TrainMode.ONLINE:
            self.__treinamento_online(tupla, precisao)
        else:
            self.__treinamento_offline(tupla, precisao)


    def __treinamento_online(self, tupla, precisao):
        eqm = 0
        eqm_anterior = 1000
        epocas = 0

        while abs(eqm - eqm_anterior) > precisao and epocas < MAX_EPOCAS:

            self.Y3 = []
            eqm_anterior = eqm
            random.shuffle(tupla)

            for line in tupla:
                entrada = line[0]
                resposta = line[1]
                saidas = self.__forward(entrada, TrainMode.ONLINE)
                self.__backward(entrada, saidas, resposta, TrainMode.ONLINE)

            for line in tupla:
                entrada = line[0]
                self.Y3.append(self.__forward(entrada, TrainMode.ONLINE)[1])
            eqm = self.get_Eqm(tupla)
            epocas += 1
            if epocas == MAX_EPOCAS:
                print("Atingiu o maximo de epocas.")
        # for i in range(len(self.Y3)):
        #     print("-------------------")
        #     print("Y: {}".format(self.Y3[i]))
        #     print("d: {}".format(tupla[i][1]))
        #
        #     self.__write_with("-----------------")
        #     self.__write_with("Y: {}".format(self.Y3[i]))
        #     self.__write_with("d: {}".format(tupla[i][1]))

        print("Epocas: {}".format(epocas))
        self.__write_with("Epoca: {}".format(epocas))

    def __treinamento_offline(self, tupla, precisao):
        eqm = 0
        eqm_anterior = 1000
        epocas = 0

        while abs(eqm - eqm_anterior) > precisao and epocas < MAX_EPOCAS:

            self.Y3 = []
            eqm_anterior = eqm
            saidas_off = []

            for line in tupla:
                entrada = line[0]
                resposta = line[1]
                saidas = self.__forward(entrada, TrainMode.OFFLINE)
                saidas_off.append(saidas)

            self.__backward(tupla, saidas_off, tupla, TrainMode.OFFLINE)

            for line in tupla:
                entrada = line[0]
                self.Y3.append(self.__forward(entrada, TrainMode.OFFLINE)[1])
            eqm = self.get_Eqm(tupla)
            epocas += 1
            if epocas == MAX_EPOCAS:
                print(epocas)
                print("Atingiu o maximo de epocas.")
        print(epocas)

    # Operation phase methods
    def operation_phase(self, entradas, respostas, num):
        self.__write_with("Xnoise{}".format(num))
        for i, entrada in enumerate(entradas):
            s = self.__forward(entrada, TrainMode.ONLINE)
            print("-------------------")
            print("Y: {}".format(s[1]))
            print("d: {}".format(respostas[i]))

            self.__write_with("-----------------")
            self.__write_with("Y: {}".format(s[1]))
            self.__write_with("d: {}".format(respostas[i]))
        self.__separate_secion()

    # Forward methods
    def __forward(self, entrada, trainMode):


        saida_camada0 = self.__run_camada(Camada.ESCONDIDA, entrada)
        saida_camada1 = self.__run_camada(Camada.SAIDA, saida_camada0)

        return (saida_camada0, saida_camada1)

    def __run_camada(self, camada, entrada):

        saida = []

        if camada == Camada.ESCONDIDA:
            neuronios = self.camada_escondida
        else:
            neuronios = self.camada_de_saida

        for neuronio in neuronios:
            saida.append(neuronio.get_saida(entrada))

        return saida

    # Backward methods
    def __backward(self, entrada, saidas, resposta, train_mode):

        if train_mode == TrainMode.ONLINE:
            erro_camada_saida = self.__get_error(Camada.SAIDA, saidas[1], resposta, [])
            self.__adjust(Camada.SAIDA, erro_camada_saida, saidas[0])

            erro_camada_escondida = self.__get_error(Camada.ESCONDIDA, saidas[0], resposta, erro_camada_saida)
            self.__adjust(Camada.ESCONDIDA, erro_camada_escondida, entrada)
        else:
            for index, y in enumerate(saidas):
                erro_camada_saida = self.__get_error(Camada.SAIDA, y[1], resposta[index][1], [])
                self.__adjust(Camada.SAIDA, erro_camada_saida, y[0])

                erro_camada_escondida = self.__get_error(Camada.ESCONDIDA, y[0], resposta[index][1], erro_camada_saida)
                self.__adjust(Camada.ESCONDIDA, erro_camada_escondida, entrada[index][0])


    def __adjust(self, camada, erro, entrada):

        new_pesos = []

        if camada == Camada.ESCONDIDA:
            neuronios = self.camada_escondida
        else:
            neuronios = self.camada_de_saida

        for index, neuronio in enumerate(neuronios):
            new_pesos.append(neuronio.ajustar(erro[index], entrada))

    # General methods
    def __get_error(self, camada, saida, resposta, erro_proxima_camada):

        erro = []

        if camada == Camada.SAIDA:
            neuronios = self.camada_de_saida

            for index, neuronio in enumerate(neuronios):
                erro.append(saida[index] * (1 - saida[index]) * (resposta[index] - saida[index]))

        else:

            neuronios = self.camada_escondida

            for index, neuronio in enumerate(neuronios):
                pesos = self.__get_pesos_of(Camada.SAIDA, index)
                somatorio = 0
                for i, peso in enumerate(pesos):
                    somatorio += peso * erro_proxima_camada[i]

                erro.append(saida[index] * (1 - saida[index]) * somatorio)  # Duvida no somatório

        return erro

    def __get_pesos_of(self, camada, index):

        pesos = []
        if camada == Camada.ESCONDIDA:
            neuronios = self.camada_escondida
        else:
            neuronios = self.camada_de_saida

        for neuronio in neuronios:
            pesos.append(neuronio.pesos[index])

        return pesos

    def get_Eqm(self, tupla):
        eqmAux = 0

        for index in range(len(self.Y3)):
            for i in range(len(self.Y3[index])):
                resposta = tupla[index][1][i]
                eqmAux += (resposta - self.Y3[index][i])*(resposta - self.Y3[index][i])

        return eqmAux/len(tupla)

    def __write_with(self, str):
        self.file.write("{}\n".format(str))

    def __separate_secion(self):
        self.file.write("\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n\n")
