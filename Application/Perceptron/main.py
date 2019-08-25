from Application.Perceptron.Rede import Rede
# import matplotlib.pyplot as plt

entradas = [[-1, 0.5, 1.5], [-1, -0.5, 0.5], [-1, 0.5, 0.5], [-1, 0.5, -0.3], [-1, 1.5, 1.5]]
respostas = [1, -1, 1, -1, 1]
n = 1

rede = Rede(len(entradas[0]), n)

rede.treinar(entradas, respostas)
rede.testar(entradas)
rede.show()

