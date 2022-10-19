class Disco():

    def __init__(self):
        self.ndiscos = 0
        self.iniciarjogo = False
        self.movimentos = 0
        self.torreA = []
        self.torreB = []
        self.torreC = []

    def quantDisco(self):
        global iniciarjogo
        global ndiscos
        ndiscos = 0
        while (iniciarjogo == False):
            ctrl = input("\nInforme qual a quantidade de disco: ")
            for i in range(100):
                if ctrl == i.__str__():
                    ndiscos = ctrl

            if ndiscos != "" and int(ndiscos) >= 3:
                iniciarjogo = True
            else:
                print("|------>   A quantidade minima de disco para iniciar o jogo deve ser >= 3 discos.")


