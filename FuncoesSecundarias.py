from itertools import count

from ConvercaoDecBin import converteDecimal, converteInteiro
from CovercaoBinDec import converteInteiroBin, converteDecimalBin


def leNumero(precisao, lower, upper):
    inteiro = decimal = inteiroBin = decimalBin = sinal = expoente = 0
    num = str(input("Digite um numero: ")).strip()
    if float(num) >= 0:  # guarda o sinal do numero digitado
        sinal = 0
    else:
        sinal = 1
        num = str(num[1::])
    isNumeric = num.isnumeric()  # guarda se o numero é só inteiro ou decimal
    if float(num) == 0:  # se numero for 0
        inteiroBin = decimalBin = 0
        print(f"Número binário: 0")
        print(f"Número normalizado:  0 .", "0" * precisao)
        print(f"Numero decimal: 0")
        return
    if num.isnumeric():  # se o numero não tiver parte decimal
        inteiro = int(num)
        decimal = 0.0
        inteiroBin = converteInteiro(inteiro)
    else:  # se o numero tiver parte decimal
        l = num.split(".")
        inteiro = l[0].strip()
        decimal = "0." + l[1].strip()
        inteiro = int(inteiro)
        decimal = float(decimal)
        inteiroBin = converteInteiro(inteiro)
        decimalBin = converteDecimal(decimal)
    if isNumeric:  # se o numero for apenas inteiro ele converte apenas a parte inteira
        num = str(inteiroBin)
    else:  # se tiver parte decimal ele concatena a inteiro binario e a fração binaria
        num = str(inteiroBin) + str(decimalBin[1::])
    if decimal == 0.0:
        inteiro = converteInteiroBin(inteiroBin)
        numInteiro = inteiro
    else:
        decimal = converteDecimalBin(decimalBin, precisao - len(inteiroBin))
        inteiro = converteInteiroBin(inteiroBin)
        numInteiro = inteiro + decimal

    # Apresentação dos dados:

    if sinal == 1:  # se numero for nagativo
        print(f"Número binário: -{num:.{len(num)}}")
        norma = normaliza(inteiroBin, decimalBin, isNumeric, precisao, lower, upper)
        if norma != 0:
            print(f"Número normalizado:  0 {norma[0]:.{precisao + 2}} 2e{norma[1]}")
        if float(num) < 1:
            expoente = normalizaFracionario(num)
            num = expoente[0]
            expoente = expoente[1]
        sn = sinalAmplitude(num, sinal)
        cp1 = complementoDeUm(num, sinal, precisao)
        cp2 = complementoDe2(num, sinal, precisao)
        if expoente == 0:
            print(f"Sinal e amplitude:   1 .{sn[:precisao + 1]}")
            print(f"Complemento de um:   1 .{cp1[:precisao + 1]}")
            print(f"Complemento de dois: 1 .{cp2[:precisao + 1]}")
        else:
            print(f"Sinal e amplitude:   1 .{sn[:precisao + 1]} 2e-{expoente}")
            print(f"Complemento de um:   1 .{cp1[:precisao + 1]} 2e-{expoente}")
            print(f"Complemento de dois: 1 .{cp2[:precisao + 1]} 2e-{expoente}")
        print(f"Numero decimal: -{numInteiro}")
    else:
        print(f"Número binário: {num:.{len(num)}}")
        norma = normaliza(inteiroBin, decimalBin, isNumeric, precisao, lower, upper)
        if norma != 0:
            print(f"Número normalizado:  {sinal} {norma[0]:.{precisao + 2}} 2e{norma[1]}")
        print(f"Numero decimal: {numInteiro}")


def normaliza(inteiroBin, decimalBin, isNumeric=False, precisao=50, lower=-50, upper=50):
    if inteiroBin != '0':
        if isNumeric:
            decimalBin = "0." + str(inteiroBin)
            decimalBin = float(decimalBin)
            inteiroBin = str(inteiroBin)
            base = len(inteiroBin)
            num = str(decimalBin)
        else:
            decimalBin = "0." + str(inteiroBin) + str(decimalBin[2:len(decimalBin)])
            decimalBin = float(decimalBin)
            inteiroBin = str(inteiroBin)
            base = len(inteiroBin)
            num = str(decimalBin)
        if len(str(decimalBin)) - 2 > precisao:
            print('Truncamento')
    else:
        decimalBin = str(decimalBin)
        i = base = 0
        l = list()
        for i in range(2, len(decimalBin)):
            l.append(decimalBin[i])
        i = 0
        while True:
            if l[i] == '0':
                base += 1
            else:
                break
            i += 1
        while True:
            if l[0] == '0':
                l.pop(0)
            else:
                break
        decimalBin = "0." + "".join(l)
        decimal = float(decimalBin)
        if len(str(decimalBin)) - 2 > precisao:
            print('Truncamento')
        if base != 0:
            num = str(decimalBin)
        else:
            num = str(decimalBin)
        base = base * (-1)
    if base > upper:
        print("Número normalizado: Overflow")
        return 0
    if base < lower:
        print("Número normalizado: Underflow")
        return 0
    norma = []
    norma.append(num)
    norma.append(base)
    return norma


def sinalAmplitude(num, sinal):
    if sinal == 0:
        if num[0] == '0':
            num = num
        else:
            lista = num.split(".")
            num = "".join(lista)
    else:
        if num[0] == '0':
            num = num
        else:
            lista = num.split(".")
            num = "".join(lista)
    return num


def complementoDeUm(num, sinal, precisao):
    l=[]
    num = sinalAmplitude(num, sinal)
    for i in range(0, len(num)):
        l.append(num[i])
        if l[i] == '1':
            l[i] = '0'
        elif l[i]== '0':
            l[i] = '1'
    if len(l) < precisao:
        tan = precisao - len(l)
        for i in range(0, tan):
            l.append('0')
    num = ''.join(l)
    return num


def complementoDe2(num, sinal, precisao):
    l = []
    c = 0
    num = complementoDeUm(num, sinal, precisao)
    if len(num) <= precisao:
        aux = len(num) - 1
    else:
        aux = precisao
    for i in range(0, aux + 1):
        l.append(num[i])
    for i in range(aux, -1, -1):
        if l[i] == '0':
            l[i] = '1'
            c = 0
            break
        elif l[i] == '1':
            l[i] = '0'
            c = 1
    num = ''.join(l)
    if c == 1:
        print('overflow')
    return num


def normalizaFracionario(decimalBin):
        decimalBin = str(decimalBin)
        i = base = 0
        l = list()
        for i in range(2, len(decimalBin)):
            l.append(decimalBin[i])
        i = 0
        while True:
            if l[i] == '0':
                base += 1
            else:
                break
            i += 1
        while True:
            if l[0] == '0':
                l.pop(0)
            else:
                break
        decimalBin = ''.join(l)
        l.clear()
        l.append(decimalBin)
        l.append(base)
        return l
