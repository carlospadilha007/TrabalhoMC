from ConvercaoDecBin import converteDecimal, converteInteiro
from CovercaoBinDec import converteInteiroBin, converteDecimalBin


def leNumero():
    inteiro = decimal = inteiroBin = decimalBin = 0
    num = str(input("Digite um numero: ")).strip()
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
    num = normaliza(inteiroBin, decimalBin, isNumeric)
    print(num)


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
