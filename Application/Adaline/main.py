from Application.Adaline.Rede import Rede
from Application.Adaline.ReaderManager import ReaderManager

taxaDeAprendizado = 1
precisao = 0.0001

normalizar = False #Booleando que informa se será Normalizado ou não

x = [] #Entradas sem o -1 do limiar (utilizado para plotar o gráfico
entradas = [] #Entradas com o -1 do limiar
respostas = [] #Saídas esperadas (d)


# ----------------------------------- Treinamento ------------------------------------------
x = ReaderManager.get_entradas(True)
entradas = ReaderManager.get_entradas(True)
respostas = ReaderManager.get_respostas(True)

x = [[0.5, 1.5], [-0.5, 0.5], [0.5, 0.5], [0.5, -0.3], [1.5, 1.5]]
entradas = [[0.5, 1.5], [-0.5, 0.5], [0.5, 0.5], [0.5, -0.3], [1.5, 1.5]]
respostas = [1, -1, 1, -1, 1]

if normalizar: #Normalizando entradas para o treinamento
    #TODO: NORMAlIZACAO
    print("TODO")

for entrada in entradas: #Inserindo o -1 do limiar
    entrada.insert(0, -1)

rede = Rede(len(entradas[0]), taxaDeAprendizado, precisao, [1, -1])  # Criando a rede
rede.x = x  # Setando o x (Utilizado para plotar os gráficos)
rede.normalizado = normalizar  # Informando para a rede se os dados são normalizados ou não(Utilizado para alterar os limites dos gráficos)
rede.treinar(entradas, respostas)
rede.testar(entradas, respostas)