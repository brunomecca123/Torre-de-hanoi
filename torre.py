from disco import Disco
import sys

disco = Disco()

class torre():
    pass
numdiscos = 0
comecar = False
mover = 0
torre1 = []
torre2 = []
torre3 = []


def quantDisco():
    global comecar
    global numdiscos
    numdiscos = 0
    while (comecar == False):
        controle = input("\nInforme qual a quantidade de disco: ")
        for i in range(100):
            if controle == i.__str__():
                numdiscos = controle

        if numdiscos != "" and int(numdiscos) >= 3:
            comecar = True
        else:
            print(" A quantidade minima de disco para iniciar o jogo deve ser 3 ou mais discos.")


def init():
    for i in range(0, int(numdiscos)):
        torre1.append(int(numdiscos) - i)
    return True


def printTorre(arrayTorre, torre):
    print('{:>{}}'.format("\nTorre ", (numdiscos)) + torre)
    for n in reversed(arrayTorre):
        desenhartorre = ""
        for i in range(n):
            desenhartorre += "#"
        print('{:>{}}'.format(desenhartorre, numdiscos) + '{:<{}}'.format(desenhartorre, numdiscos))


def verificarMovimento(str):
    strView = ""
    if str == "1":
        strView = "2 ou 3"
    elif (str == "2"):
        strView = "1 ou 3"
    elif (str == "3"):
        strView = "1 ou 2"
    return strView


def movimentar(torre, operacao, valorMove):
    movimento = ""

    if (torre == "1" ) and operacao == 1:
        if validaAlocacao(torre1, operacao, valorMove):
            movimento = torre1.pop()
    elif (torre == "2") and operacao == 1:
        if validaAlocacao(torre2, operacao, valorMove):
            movimento = torre2.pop()
    elif (torre == "3") and operacao == 1:
        if validaAlocacao(torre3, operacao, valorMove):
            movimento = torre3.pop()
    elif (torre == "1") and operacao == 2:
        if validaAlocacao(torre1, operacao, valorMove):
            torre1.append(valorMove)
            movimento = valorMove
    elif (torre == "2") and operacao == 2:
        if validaAlocacao(torre2, operacao, valorMove):
            torre2.append(valorMove)
            movimento = valorMove
    elif (torre == "3") and operacao == 2:
        if validaAlocacao(torre3, operacao, valorMove):
            torre3.append(valorMove)
            movimento = valorMove
    return movimento


def inputValue():
    saida = ""
    movSaida = ""
    entrada = ""
    movEntrada = ""
    controle = False
    reiniciar = False
    novaPartida = False

    while saida == "":

        if movSaida == "" and controle != False:
            print("Torre incorreta, digite novamente.")
            controle = False
        else:
            print("\nPara reiniciar a jogada digite [ reiniciar ] ")
            print("Para iniciar novamente a partida digite [ iniciar ] ")
            print("Para exibir o resultado anterior digite [ exibir ]\n")
            saida = input("Informe a Torre de Saida: ")

            if saida == "reiniciar":
                reiniciar = True
            elif saida == "exibir":
                printResult()
                reiniciar = True
            elif saida == "iniciar":
                novaPartida = True
            else:
                movSaida = verificarMovimento(saida)
                controle = True

        if not reiniciar and not novaPartida:
            saida = movimentar(saida, 1, "")

    controle = False

    while entrada == "" and (not reiniciar and not novaPartida):

        if movEntrada == "" and controle != False:
            print("A Torre informada esta errada, por favor informe uma torre valida.")
            controle = False
        else:
            entrada = input("Informe a Torre de Entrada " + movSaida + ": ")

            if entrada == "reiniciar":
                reiniciar = True
            elif entrada == "exibir":
                printResult()
                reiniciar = True
            elif entrada == "iniciar":
                novaPartida = True
            else:
                movEntrada = verificarMovimento(entrada)

                if movSaida == movEntrada:
                    print("Esse movimento é inválido. Tente outro movimento.")
                    controle = False
                else:
                    controle = True

        if controle:
            entrada = movimentar(entrada, 2, saida)
        else:
            entrada = ""

    if reiniciar:
        inputValue()
    elif novaPartida:
        iniciar()


def validaAlocacao(torre, operacao, valorMove):
    length = torre.__len__()

    if length == 0 and operacao == 1:
        print("Esta torre esta vazia. Mude sua jogada.")
        return False
    elif length > 0 and operacao == 2:
        if valorMove < torre[length - 1]:
            return True
        else:
            print("O ultimo disco que esta na torre è menor que o disco [", valorMove, "]. Mude sua jogada!")
            return False
    else:
        return True


def validaResultado():
    vencedor = False

    if int(torre1.__len__()) == 0 and int(torre2.__len__()) == 0 and int(torre3.__len__()) == int(numdiscos):
        vencedor = True
    elif int(torre1.__len__()) == 0 and int(torre2.__len__()) == int(numdiscos) and int(torre3.__len__()) == 0:
        vencedor = True

    return vencedor


def fimJogo():
    print("Fim de jogo!")

    if input("Para uma nova partida digite [ iniciar ], se quiser digite qualquer tecla!:  ") == "iniciar":
        iniciar()
    else:
        print("Obrigado por jogar!\n")
        sys.exit(0)


def move():
    global mover
    resultado = False

    while not resultado:
        inputValue()
        mover += 1
        printResult()
        resultado = validaResultado()
    else:
        fimJogo()


def printResult():
    print("\n")
    print("Torre 1: ", torre1)
    print("Torre 2: ", torre2)
    print("Torre 3: ", torre3)
    print("mover: ", mover)

    printTorre(torre1, "1")
    printTorre(torre2, "2")
    printTorre(torre3, "3")
    print("\n")


def iniciar():
    global numdiscos
    global comecar
    global mover
    global torre1
    global torre2
    global torre3

    numdiscos = 0
    comecar = False
    mover = 0
    torre1 = []
    torre2 = []
    torre3 = []

    quantDisco()
    init()

    print("\n------JOGO INICIANDO------\n")
    printResult()
    move()


if __name__ == '__main__':
    iniciar()