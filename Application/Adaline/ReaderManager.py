import math

ENTRADAS_TRAIN_FILE = './Files/xtrain.txt'
RESPOSTAS_TRAIN_FILE = './Files/dTrain.txt'

ENTRADAS_TEST_FILE = './Files/xTest.txt'
RESPOSTAS_TEST_FILE = './Files/dTest.txt'

# ENTRADAS_TRAIN_FILE = './Files/xtrain2.txt'
# RESPOSTAS_TRAIN_FILE = './Files/dTrain2.txt'
#
# ENTRADAS_TEST_FILE = './Files/xTest2.txt'
# RESPOSTAS_TEST_FILE = './Files/dTest2.txt'

class ReaderManager:

    @staticmethod
    def get_entradas(train): #Lendo as entradas do txt do treino ou dos teste
        file = ENTRADAS_TRAIN_FILE if train else ENTRADAS_TEST_FILE
        ent = []
        with open(file) as f:
            conteudo = f.readlines()
        lines = [line.strip() for line in conteudo]

        for i in range(len(lines)):
            ent.append([])
            count = 0

            for l in lines[i]:
                if l == '\t':
                    break
                count += 1
            ent[i].append(float(lines[i][:count]))



            count = 0
            for l in reversed(lines[i]):
                if l == '\t':
                    break
                count += 1
            ent[i].append(float(lines[i][-count:]))
        return ent

    @staticmethod
    def new_get_entradas(train):
        file = ENTRADAS_TRAIN_FILE if train else ENTRADAS_TEST_FILE
        ent = []
        with open(file) as f:
            conteudo = f.readlines()
        lines = [line.strip() for line in conteudo]

        for i in range(len(lines)):
            ent.append([])
            vetor = lines[i].split()
            for pos in vetor:
                ent[i].append(float(pos))

        return ent

    @staticmethod
    def get_respostas(train): #Lendo as repostas esperadas do txt do treino ou do teste
        file = RESPOSTAS_TRAIN_FILE if train else RESPOSTAS_TEST_FILE
        r = []
        with open(file) as f:
            conteudo = f.readlines()
        lines = [line.strip() for line in conteudo]

        for line in lines:
            try:
                r.append(int(line))
            except ValueError:
                print("Erro")
        return r

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