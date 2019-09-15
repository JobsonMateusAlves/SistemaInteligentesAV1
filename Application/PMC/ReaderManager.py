import math

ENTRADAS = './Files/Xlarge.txt'

RESPOSTAS= './Files/Xsmall.txt'

class ReaderManager:

    @staticmethod
    def get_entradas():
        file = ENTRADAS
        entradas = []
        with open(file) as f:
            conteudo = f.readlines()
        lines = [line.strip() for line in conteudo]

        for i in range(len(lines)):
            entradas.append([])
            vetor = lines[i].split()
            for pos in vetor:
                entradas[i].append(float(pos))

        for entrada in entradas:
            print(entrada)
        return entradas

    @staticmethod
    def get_respostas():
        file = RESPOSTAS
        respostas = []
        with open(file) as f:
            conteudo = f.readlines()
        lines = [line.strip() for line in conteudo]

        for i in range(len(lines)):
            respostas.append([])
            vetor = lines[i].split()
            for pos in vetor:
                respostas[i].append(float(pos))

        for entrada in respostas:
            print(entrada)
        return respostas

    @staticmethod
    def normalizacao(ents):
        soma = 0
        media  = 0
        variancia = 0
        desv = 0

        for v in ents:
            soma += v
        qtd_elementos = len(ents)
        media = soma/float(qtd_elementos)
        for valor in ents:
            soma += math.pow((valor - media), 2)
        variancia = soma/(float(len(ents))-1)

        desv = math.sqrt(variancia)

        return (media, desv)