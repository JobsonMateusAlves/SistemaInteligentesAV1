from Application.Adaline.Rede import Rede
# import matplotlib.pyplot as plt

entradas = [[-1, 0.5, 1.5], [-1, -0.5, 0.5], [-1, 0.5, 0.5], [-1, 0.5, -0.3], [-1, 1.5, 1.5]]
respostas = [1, -1, 1, -1, 1]
n = 0.1
E = 0.06

rede = Rede(len(entradas), n, E)
rede.treinar(entradas, respostas)
rede.teste(entradas)


