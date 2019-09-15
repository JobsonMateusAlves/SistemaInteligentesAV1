from Application.PMC.ReaderManager import ReaderManager
from Application.PMC.Rede import Rede

TAXA_DE_APRENDIZADO = 1
QTD_NEURONIOS_CAMADA_ESCONDIDA = 2

entradas = ReaderManager.get_entradas()
respostas = ReaderManager.get_respostas()

rede = Rede(entradas, TAXA_DE_APRENDIZADO, QTD_NEURONIOS_CAMADA_ESCONDIDA, respostas)
