from itertools import count

from ConvercaoDecBin import converteDecimal, converteInteiro
from CovercaoBinDec import converteInteiroBin, converteDecimalBin


def leNumero():
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
    print(complementoDe2(num, sinal))


def normaliza(inteiroBin, decimalBin, isNumeric):
    if inteiroBin != 0:
        if isNumeric:
            decimalBin = "0." + str(inteiroBin)
            decimalBin = float(decimalBin)
            inteiroBin = str(inteiroBin)
            base = len(inteiroBin)
            num = str(decimalBin) + " 2e" + str(base)
        else:
            decimalBin = "0." + str(inteiroBin) + str(decimalBin[2:len(decimalBin)])
            decimalBin = float(decimalBin)
            inteiroBin = str(inteiroBin)
            base = len(inteiroBin)
            num = str(decimalBin) + " 2e" + str(base)
    else:
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
        if base != 0:
            num = str(decimalBin) + " 2e-" + str(base)
        else:
            num = str(decimalBin) + " 2e0"
    return num


def sinalAmplitude(num, sinal):
    if sinal == 0:
        if num[0] == '0':
            num = "0.0" + str(num[2::])
        else:
            num = "0" + str(num)
    else:
        if num[0] == '0':
            num = "0.1" + str(num[2::])
        else:
            num = "1" + str(num)
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
            c = 1
    num = ''.join(l)
    if c == 1:
        print('overflow')
    return num
