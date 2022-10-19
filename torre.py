from disco import Disco
import sys

disco = Disco()

class torre():
    pass
ndiscos = 0
iniciarjogo = False
movimentos = 0
torreA = []
torreB = []
torreC = []


def quantDisco():
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
            print("|------>   A quantidade minima de disco para iniciar o jogo deve ser >= 7 disco.")


def init():
    for i in range(0, int(ndiscos)):
        torreA.append(int(ndiscos) - i)
    return True


def printTorre(arrayTorre, torre):
    print('{:>{}}'.format("\nTorre ", (ndiscos)) + torre)
    for n in reversed(arrayTorre):
        pino = ""
        for i in range(n):
            pino += "#"
        print('{:>{}}'.format(pino, ndiscos) + '{:<{}}'.format(pino, ndiscos))


def verificarMovimento(str):
    strView = ""
    if str == "a" or str == "A":
        strView = "B ou C"
    elif (str == "b" or str == "B"):
        strView = "A ou C"
    elif (str == "c" or str == "C"):
        strView = "A ou B"
    return strView


def movimentar(torre, operacao, valorMove):
    movimento = ""

    if (torre == "a" or torre == "A") and operacao == 1:
        if validaAlocacao(torreA, operacao, valorMove):
            movimento = torreA.pop()
    elif (torre == "b" or torre == "B") and operacao == 1:
        if validaAlocacao(torreB, operacao, valorMove):
            movimento = torreB.pop()
    elif (torre == "c" or torre == "C") and operacao == 1:
        if validaAlocacao(torreC, operacao, valorMove):
            movimento = torreC.pop()
    elif (torre == "a" or torre == "A") and operacao == 2:
        if validaAlocacao(torreA, operacao, valorMove):
            torreA.append(valorMove)
            movimento = valorMove
    elif (torre == "b" or torre == "B") and operacao == 2:
        if validaAlocacao(torreB, operacao, valorMove):
            torreB.append(valorMove)
            movimento = valorMove
    elif (torre == "c" or "torre" == "C") and operacao == 2:
        if validaAlocacao(torreC, operacao, valorMove):
            torreC.append(valorMove)
            movimento = valorMove
    return movimento


def inputValue():
    saida = ""
    movSaida = ""
    entrada = ""
    movEntrada = ""
    ctrl = False
    reset = False
    novaPartida = False

    while saida == "":

        if movSaida == "" and ctrl != False:
            print("A Torre informada esta errada, por favor informe uma torre valida.")
            ctrl = False
        else:
            print("\nPara resetar a jogada digite [ reset ] ")
            print("Para iniciar novamente a partida digite [ iniciar ] ")
            print("Para imprimir o resultado anterior digite [ print ]\n")
            saida = input("Informe a Torre de Saida: ")

            if saida == "reset":
                reset = True
            elif saida == "print":
                printResult()
                reset = True
            elif saida == "iniciar":
                novaPartida = True
            else:
                movSaida = verificarMovimento(saida)
                ctrl = True

        if not reset and not novaPartida:
            saida = movimentar(saida, 1, "")

    ctrl = False

    while entrada == "" and (not reset and not novaPartida):

        if movEntrada == "" and ctrl != False:
            print("A Torre informada esta errada, por favor informe uma torre valida.")
            ctrl = False
        else:
            entrada = input("Informe a Torre de Entrada " + movSaida + ": ")

            if entrada == "reset":
                reset = True
            elif entrada == "print":
                printResult()
                reset = True
            elif entrada == "iniciar":
                novaPartida = True
            else:
                movEntrada = verificarMovimento(entrada)

                if movSaida == movEntrada:
                    print("Essa joganda não é valida. Você deve muda sua jogada.")
                    ctrl = False
                else:
                    ctrl = True

        if ctrl:
            entrada = movimentar(entrada, 2, saida)
        else:
            entrada = ""

    if reset:
        inputValue()
    elif novaPartida:
        iniciar()


def validaAlocacao(torre, operacao, valorMove):
    length = torre.__len__()

    if length == 0 and operacao == 1:
        print("Esta torre esta vazia. Você deve muda sua jogada.")
        return False
    elif length > 0 and operacao == 2:
        if valorMove < torre[length - 1]:
            return True
        else:
            print("Os ultimo disco que esta na torre è menor que o disco [", valorMove, "]. Você deve muda sua jogada.")
            return False
    else:
        return True


def validaResultado():
    vencedor = False

    if int(torreA.__len__()) == 0 and int(torreB.__len__()) == 0 and int(torreC.__len__()) == int(ndiscos):
        vencedor = True
    elif int(torreA.__len__()) == 0 and int(torreB.__len__()) == int(ndiscos) and int(torreC.__len__()) == 0:
        vencedor = True

    return vencedor


def fimJogo():
    print("PARABÉNS, VOCÊ GANHOU...\nAgora o que voce acha de aumentar o desafio.\n")

    if input("Para uma nova partida digite [ iniciar ]: ") == "iniciar":
        iniciar()
    else:
        print("Que pena, entao ate a proxima... bye bye\n")
        sys.exit(0)


def move():
    global movimentos
    resultado = False

    while not resultado:
        inputValue()
        movimentos += 1
        printResult()
        resultado = validaResultado()
    else:
        fimJogo()


def printResult():
    print("\n")
    print("Torre A: ", torreA)
    print("Torre B: ", torreB)
    print("Torre C: ", torreC)
    print("Movimentos: ", movimentos)

    printTorre(torreA, "A")
    printTorre(torreB, "B")
    printTorre(torreC, "C")
    print("\n")


def iniciar():
    global ndiscos
    global iniciarjogo
    global movimentos
    global torreA
    global torreB
    global torreC

    ndiscos = 0
    iniciarjogo = False
    movimentos = 0
    torreA = []
    torreB = []
    torreC = []

    quantDisco()
    init()

    print("\n     PRONTO VAMOS INCIAR O JOGO \n")
    printResult()
    move()


if __name__ == '__main__':
    iniciar()