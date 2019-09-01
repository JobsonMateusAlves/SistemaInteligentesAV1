from Application.Adaline.Rede import Rede
# import matplotlib.pyplot as plt


entradas = [[-1, 0.5, 1.5], [-1, -0.5, 0.5], [-1, 0.5, 0.5], [-1, 0.5, -0.3], [-1, 1.5, 1.5]]
respostasEsperadas = [1, -1, 1, -1, 1]
taxaDeAprendizado = 0.1
precisao = 0.06

rede = Rede(len(entradas[0]), taxaDeAprendizado, precisao)
rede.treinar(entradas, respostasEsperadas)
rede.teste(entradas)


