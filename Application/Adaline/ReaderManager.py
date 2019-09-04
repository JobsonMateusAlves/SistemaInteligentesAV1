
ENTRADAS_TRAIN_FILE = './Files/xtrain.txt'
RESPOSTAS_TRAIN_FILE = './Files/dTrain.txt'

ENTRADAS_TEST_FILE = './Files/xTest.txt'
RESPOSTAS_TEST_FILE = './Files/dTest.txt'

class ReaderManager:

    @staticmethod
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

    @staticmethod
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
