from ConvercaoDecBin import converteDecimal, converteInteiro


def leNumero():
    inteiro = decimal = inteiroBin = decimalBin = 0
    num = str(input("Digite um numero: ")).strip()
    l = num.split(".")
    inteiro = l[0].strip()
    decimal = "0." + l[1].strip()
    inteiro = int(inteiro)
    decimal = float(decimal)
    inteiroBin = converteInteiro(inteiro)
    decimalBin = converteDecimal(decimal)
    print(inteiroBin + decimalBin)
