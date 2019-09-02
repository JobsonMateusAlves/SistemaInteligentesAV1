from Application.Perceptron.Rede import Rede
from sklearn import preprocessing
import numpy as np



ENTRADAS_TRAIN_FILE = './xtrain.txt'
RESPOSTAS_TRAIN_FILE = './dTrain.txt'

ENTRADAS_TEST_FILE = './XTest.txt'
RESPOSTAS_TEST_FILE = './dTest.txt'


def get_entradas(train):
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


def get_respostas(train):
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

def normalizar_entradas(entradas):
    scale = preprocessing.MinMaxScaler(feature_range=(-1, 1)).fit(entradas)
    entradasAux = list(scale.transform(entradas))
    for i in range(len(entradasAux)):
        entradas[i] = list(entradasAux[i])

    return entradas

def normalizar_x(x):
    scale = preprocessing.MinMaxScaler(feature_range=(-1, 1)).fit(x)
    xAux = list(scale.transform(x))
    for i in range(len(xAux)):
        x[i] = list(xAux[i])
    return x



normalizar = True
entradas = []
respostas = []

# Treinamento
x = get_entradas(True)
entradas = get_entradas(True)
respostas = get_respostas(True)
taxaDeAprendizado = 0.01

if normalizar:
    x = normalizar_x(x)
    entradas = normalizar_entradas(entradas)

for entrada in entradas:
    entrada.insert(0, -1)

rede = Rede(len(entradas[0]), taxaDeAprendizado, [1, 2])
rede.x = x
rede.normalizado = normalizar
rede.treinar(entradas, respostas)

# Teste
a = get_entradas(False)
x = get_entradas(False)
entradas = get_entradas(False)
respostas = get_respostas(False)


if normalizar:
    x = normalizar_x(x)
    entradas = normalizar_entradas(entradas)

for entrada in entradas:
    entrada.insert(0, -1)


rede.x = x
rede.testar(entradas, respostas, a)
rede.show()






# entradas = [[-1, 0.5, 1.5], [-1, -0.5, 0.5], [-1, 0.5, 0.5], [-1, 0.5, -0.3], [-1, 1.5, 1.5]]
# respostas = [1, -1, 1, -1, 1] #2. Associando a saída desejada para cada amostra obtida