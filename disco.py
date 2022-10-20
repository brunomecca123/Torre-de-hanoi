class Disco():

    def __init__(self):
        self.numdiscos = 0
        self.comecar = False
        self.mover'' = 0
        self.torre1 = []
        self.torre2 = []
        self.torre3 = []

    def quantDisco(self):
        global comecar
        global numdiscos
        numdiscos = 0
        while (comecar == False):
            controle = input("\nDigite o número de discos para o jogo iniciar: ")
            for i in range(100):
                if controle == i.__str__():
                    numdiscos = controle

            if numdiscos != "" and int(numdiscos) >= 3:
                comecar = True
            else:
                print("A quantidade minima de disco para iniciar o jogo deve ser de 3 discos.")


