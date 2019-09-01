from Application.Perceptron.Rede import Rede
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap #Lista de cores para plotagens

def get_entradas():
    ent =[]
    with open('./xtrain.txt') as f:
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

    # print(entradas)
    return ent

def get_respostas():
    with open('./dTrain.txt') as f:
        conteudo = f.readlines()
    lines = [line.strip() for line in conteudo]

    for line in lines:
        try:
            respostas.append(int(line))
        except ValueError:
            print("Erro")

    # print(respostas)
    return respostas

entradas = []
respostas = []

x = get_entradas()
entradas = get_entradas() #1. Obtendo conjunto de amostras de treinamento
respostas = get_respostas() #2. Associando a saída desejada para cada amostra obtida
taxaDeAprendizado = 1 #4. Especificando tava de aprendizagem



for entrada in entradas:
    entrada.insert(0, -1)


rede = Rede(len(entradas[0]), taxaDeAprendizado, [1, 3])
rede.x = x
rede.treinar(entradas, respostas)
rede.testar(entradas)
rede.show()






# entradas = [[-1, 0.5, 1.5], [-1, -0.5, 0.5], [-1, 0.5, 0.5], [-1, 0.5, -0.3], [-1, 1.5, 1.5]]
# respostas = [1, -1, 1, -1, 1] #2. Associando a saída desejada para cada amostra obtida