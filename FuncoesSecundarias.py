from itertools import count

from ConvercaoDecBin import converteDecimal, converteInteiro
from CovercaoBinDec import converteInteiroBin, converteDecimalBin


def leNumero(precisao, lower, upper):
    inteiro = decimal = inteiroBin = decimalBin = sinal = 0
    num = str(input("Digite um numero: ")).strip()
    if float(num) > 0:
        sinal = 0
    else:
        sinal = 1
        num = str(num[1::])
    isNumeric = num.isnumeric()
    if num.isnumeric():
        inteiro = int(num)
        decimal = 0.0
        inteiroBin = converteInteiro(inteiro)
    else:
        l = num.split(".")
        inteiro = l[0].strip()
        decimal = "0." + l[1].strip()
        inteiro = int(inteiro)
        decimal = float(decimal)
        inteiroBin = converteInteiro(inteiro)
        decimalBin = converteDecimal(decimal)
    if isNumeric:
        num = str(inteiroBin)
    else:
        num = str(inteiroBin) + str(decimalBin[1::])
    if decimal == 0.0:
        inteiro = converteInteiroBin(inteiroBin)
        numInteiro = inteiro
    else:
        decimal = converteDecimalBin(decimalBin, precisao - len(inteiroBin))
        inteiro = converteInteiroBin(inteiroBin)
        numInteiro = inteiro + decimal

    # Apresentação dos dados:

    if sinal == 1:
        print(f"Número binário: -{num:.{len(num)}}")
        norma = normaliza(inteiroBin, decimalBin, isNumeric, precisao, lower, upper)
        if norma != 0:
            print(f"Número normalizado: {sinal} {norma[0]:.{precisao + 2}} 2e{norma[1]}")
        sn = sinalAmplitude(num, sinal)
        cp1 = complementoDeUm(num, sinal)
        cp2 = complementoDe2(num, sinal)
        print(f"Sinal e amplitude: {sn[:precisao + 1]}")
        print(f"Complemento de um: {cp1[:precisao + 1]}")
        print(f"Complemento de dois: {cp2[:precisao + 1]}")
        print(f"Numero decimal: -{numInteiro}")
    else:
        print(f"Número binário: {num:.{len(num)}}")
        norma = normaliza(inteiroBin, decimalBin, isNumeric, precisao, lower, upper)
        if norma != 0:
            print(f"Número normalizado: {sinal} {norma[0]:.{precisao + 2}} 2e{norma[1]}")
        print(f"Numero decimal: {numInteiro}")


def normaliza(inteiroBin, decimalBin, isNumeric, precisao, lower, upper):
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
            num = "0." + str(num[2::])
        else:
            lista = num.split(".")
            num = "".join(lista)
    else:
        if num[0] == '0':
            num = "0." + str(num[2::])
        else:
            lista = num.split(".")
            num = "".join(lista)
    return num


def complementoDeUm(num, sinal):
    l=[]
    num = sinalAmplitude(num, sinal)
    for i in range(0,len(num)):
        l.append(num[i])
        if l[i] == '1':
            l[i] = '0'
        elif l[i]== '0':
            l[i] = '1'
    num = ''.join(l)
    return num


def complementoDe2(num, sinal):
    l = []
    c = 0
    num = complementoDeUm(num, sinal)
    for i in range(0, len(num)):
        l.append(num[i])
    for i in range(len(num)-1, -1, -1):
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
