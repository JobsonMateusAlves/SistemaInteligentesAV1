from Application.PMC.ReaderManager import ReaderManager
from Application.PMC.Rede import Rede
from Application.PMC.Rede import TrainMode

TAXA_DE_APRENDIZADO = 0.01
QTD_NEURONIOS_CAMADA_ESCONDIDA = 2
PRECISAO = 0.00001

# entradas = ReaderManager.get_entradas()
# respostas = ReaderManager.get_respostas()

entradas = ReaderManager.get_entradas_xor()
respostas = ReaderManager.get_respostas_xor()

tupla = []
for i in range(len(entradas)):
    tupla.append((entradas[i], respostas[i]))

# ---------------------------------------- Treinamento ------------------------------------------
file = open("./Files/result{}.txt".format(1), "a")
file.write("PMC{}\n".format(1))

rede = Rede(entradas, TAXA_DE_APRENDIZADO, QTD_NEURONIOS_CAMADA_ESCONDIDA, respostas)
rede.file = file
rede.treinar(tupla, TrainMode.ONLINE, PRECISAO)

# ------------------------------------------- Testes ---------------------------------------------
entradas_de_teste = ReaderManager.get_entradas_xor()
rede.operation_phase(entradas_de_teste, respostas, 2)


# entradas_de_teste = ReaderManager.get_entradas_teste(2)
# rede.operation_phase(entradas_de_teste, respostas, 2)
#
# entradas_de_teste = ReaderManager.get_entradas_teste(5)
# rede.operation_phase(entradas_de_teste, respostas, 5)
#
# entradas_de_teste = ReaderManager.get_entradas_teste(10)
# rede.operation_phase(entradas_de_teste, respostas, 10)
file.close()
