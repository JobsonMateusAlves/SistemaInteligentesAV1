from Application.Perceptron.Rede import Rede
from sklearn import preprocessing
import numpy as np

ENTRADAS_TRAIN_FILE = './xtrain.txt'
RESPOSTAS_TRAIN_FILE = './dTrain.txt'

ENTRADAS_TEST_FILE = './XTest.txt'
RESPOSTAS_TEST_FILE = './dTest.txt'


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

def normalizar_entradas(ents): #Normalizando as entradas
    scale = preprocessing.MinMaxScaler(feature_range=(-1, 1)).fit(ents)
    entradasAux = list(scale.transform(entradas))
    for i in range(len(entradasAux)):
        ents[i] = list(entradasAux[i])

    return ents



normalizar = True #Booleando que informa se será Normalizado ou não

x = [] #Entradas sem o -1 do limiar (utilizado para plotar o gráfico
entradas = [] #Entradas com o -1 do limiar
respostas = [] #Saídas esperadas (d)


# ----------------------------------- Treinamento ------------------------------------------
x = get_entradas(True)
entradas = get_entradas(True)
respostas = get_respostas(True)
taxaDeAprendizado = 0.01

if normalizar: #Normalizando entradas para o treinamento
    x = normalizar_entradas(x)
    entradas = normalizar_entradas(entradas)

for entrada in entradas: #Inserindo o -1 do limiar
    entrada.insert(0, -1)

rede = Rede(len(entradas[0]), taxaDeAprendizado, [1, 2]) #Criando a rede
rede.x = x #Setando o x (Utilizado para plotar os gráficos)
rede.normalizado = normalizar #Informando para a rede se os dados são normalizados ou não(Utilizado para alterar os limites dos gráficos)
rede.treinar(entradas, respostas)


# -------------------------------------- Teste ---------------------------------------------
x = get_entradas(False)
entradas = get_entradas(False)
respostas = get_respostas(False)


if normalizar: #Normalizando entradas para o teste
    x = normalizar_entradas(x)
    entradas = normalizar_entradas(entradas)

for entrada in entradas: #Inserindo o -1 do limiar
    entrada.insert(0, -1)


rede.x = x
rede.testar(entradas, respostas)
rede.show()
