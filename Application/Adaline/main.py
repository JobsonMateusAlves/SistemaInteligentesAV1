from Application.Adaline.Rede import Rede
from Application.Adaline.ReaderManager import ReaderManager

taxaDeAprendizado = 1
precisao = 0.0001

normalizar = True #Booleando que informa se será Normalizado ou não

def normalizar_x1():
    ents = []
    for entTrain in entradasTrain:
        ents.append(entTrain[0])
    for entTest in entradasTest:
        ents.append(entTest[0])
    norm = ReaderManager.normalizacao(ents)
    media = norm[0]
    desv = norm[1]
    for i in range(len(entradasTrain)):
        entradasTrain[i][0] = (entradasTrain[i][0] - media) / desv
        xTrain[i][0] = (xTrain[i][0] - media) / desv
    for i in range(len(entradasTest)):
        entradasTest[i][0] = (entradasTest[i][0] - media) / desv
        xTest[i][0] = (xTest[i][0] - media) / desv

def normalizar_x2():
    ents = []
    for entTrain in entradasTrain:
        ents.append(entTrain[1])
    for entTest in entradasTest:
        ents.append(entTest[1])
    norm = ReaderManager.normalizacao(ents)
    media = norm[0]
    desv = norm[1]
    for i in range(len(entradasTrain)):
        entradasTrain[i][1] = (entradasTrain[i][1] - media) / desv
        xTrain[i][1] = (xTrain[i][1] - media) / desv
    for i in range(len(entradasTest)):
        entradasTest[i][1] = (entradasTest[i][1] - media) / desv
        xTest[i][1] = (xTest[i][1] - media) / desv

def normalizar_x3():
    ents = []
    for entTrain in entradasTrain:
        ents.append(entTrain[2])
    for entTest in entradasTest:
        ents.append(entTest[2])
    norm = ReaderManager.normalizacao(ents)
    media = norm[0]
    desv = norm[1]
    for i in range(len(entradasTrain)):
        entradasTrain[i][2] = (entradasTrain[i][2] - media) / desv
        xTrain[i][2] = (xTrain[i][2] - media) / desv
    for i in range(len(entradasTest)):
        entradasTest[i][2] = (entradasTest[i][2] - media) / desv
        xTest[i][2] = (xTest[i][2] - media) / desv

def normalizar_x4():
    ents = []
    for entTrain in entradasTrain:
        ents.append(entTrain[3])
    for entTest in entradasTest:
        ents.append(entTest[3])
    norm = ReaderManager.normalizacao(ents)
    media = norm[0]
    desv = norm[1]
    for i in range(len(entradasTrain)):
        entradasTrain[i][3] = (entradasTrain[i][3] - media) / desv
        xTrain[i][3] = (xTrain[i][3] - media) / desv
    for i in range(len(entradasTest)):
        entradasTest[i][3] = (entradasTest[i][3] - media) / desv
        xTest[i][3] = (xTest[i][3] - media) / desv

# ----------------------------------- Leituras ------------------------------------------
xTrain = ReaderManager.new_get_entradas(True)
entradasTrain = ReaderManager.new_get_entradas(True)
respostasTrain = ReaderManager.get_respostas(True)

xTest = ReaderManager.new_get_entradas(False)
entradasTest = ReaderManager.new_get_entradas(False)
respostasTest = ReaderManager.get_respostas(False)

# entradasTrain = [[1000,0], [3000,0], [1500,0], [3000,0], [4000,0]]
# entradasTest = []
#
# x = [[1, 1], [0, 0], [0, 1], [1, 0]]
# entradas = [[1, 1], [0, 0], [0, 1], [1, 0]]
# respostas = [1, -1, -1, -1]
# print(entradasTrain)
if normalizar:
    normalizar_x1()
    normalizar_x2()
    if len(entradasTrain[0]) > 2:
        normalizar_x3()
        normalizar_x4()


# print(entradasTrain)

for entrada in entradasTrain:
    entrada.insert(0, -1)
for entrada in entradasTest:
    entrada.insert(0, -1)

# # ----------------------------------- Treinamento ------------------------------------------
rede = Rede(len(entradasTrain[0]), taxaDeAprendizado, precisao, [1, 2], True)
rede.x = xTrain
rede.normalizado = normalizar
rede.treinar(entradasTrain, respostasTrain)
print("Taxa de acertos Treino: {}".format(rede.get_taxa_de_acerto(entradasTrain, respostasTrain)))

# # ----------------------------------- Teste ------------------------------------------
rede.x = xTest
rede.testar(entradasTest, respostasTest)
print("Taxa de acertos Teste: {}".format(rede.get_taxa_de_acerto(entradasTest, respostasTest)))
rede.show()
