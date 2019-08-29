from itertools import count

from ConvercaoDecBin import converteDecimal, converteInteiro
from CovercaoBinDec import converteInteiroBin, converteDecimalBin


def leNumero(precisao, lower, upper):
    inteiro = decimal = inteiroBin = decimalBin = sinalExp = sinal = expoente = 0
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
        if norma != -1:
            print(f"Número normalizado:  0 {norma[0]:.{precisao + 2}} 2e{norma[1]}")
        else:
            return
        if float(num) < 1:  # caso o numero esteja entre 0 e 1, o sinal e amplitude, complemento usão o num nromalizado
            expoente = normalizaFracionario(num)
            num = expoente[0]
            expoente = expoente[1]
            sinalExp = 1
        sn = sinalAmplitude(num, sinal)
        cp1 = complementoDeUm(num, sinal, precisao)
        cp2 = complementoDe2(num, sinal, precisao)
        if expoente == 0:  # se exponte 0 (numero sem parte decimal)
            print(f"Sinal e amplitude:   1 .{sn[:precisao + 1]} 2e{norma[1]}")
            print(f"Complemento de um:   1 .{cp1[:precisao + 1]} 2e{norma[1]}")
            print(f"Complemento de dois: 1 .{cp2[:precisao + 1]} 2e{norma[1]}")
        else:  # se o exponte for negativo
            print(f"Sinal e amplitude:   1 .{sn[:precisao + 1]} 2e{norma[1]}")
            print(f"Complemento de um:   1 .{cp1[:precisao + 1]} 2e{norma[1]}")
            print(f"Complemento de dois: 1 .{cp2[:precisao + 1]} 2e{norma[1]}")
    else:  # se o numero digitado for positivo
        print(f"Número binário: {num:.{len(num)}}")
        norma = normaliza(inteiroBin, decimalBin, isNumeric, precisao, lower, upper)
        if norma != -1:
            print(f"Número normalizado:  {sinal} {norma[0]:.{precisao + 2}} 2e{norma[1]}")
    if float(numInteiro) < 1:
        if sinal == 1:
            print(f"Numero decimal: -{numInteiro}")
        else:
            print(f"Numero decimal: {numInteiro}")
    else:
        expoente = norma
        if expoente == -1:
            return
        if sinal == 0:
            print(f"Numero decimal: {chamaConvercao(norma, sinalExp, precisao)}")
        else:
            print(f"Numero decimal: -{chamaConvercao(norma, sinalExp, precisao)}")


def normaliza(inteiroBin, decimalBin, isNumeric=False, precisao=50, lower=-50, upper=50):
    # base guarda o expoente
    numTruncado = 0
    truncado = False
    if inteiroBin != '0':  # se o numero tiver a parte inteira diferente de 0
        if isNumeric:  # se possui apenas a parte inteira
            decimalBin = "0." + str(inteiroBin)
            decimalBin = float(decimalBin)
            inteiroBin = str(inteiroBin)
            base = len(inteiroBin)
            num = str(decimalBin)
        else:  # se possui apenas a parte real
            decimalBin = "0." + str(inteiroBin) + str(decimalBin[2:len(decimalBin)])
            decimalBin = float(decimalBin)
            inteiroBin = str(inteiroBin)
            base = len(inteiroBin)
            num = str(decimalBin)
        if len(str(decimalBin)) - 2 > precisao:
            print('Truncamento')
            decimalBin = str(decimalBin)
            aux = [str(inteiroBin), str(decimalBin[1::])]
            numTruncado = ''.join(aux)
            if '.' in str(numTruncado[0:precisao]):
                numTruncado = str(numTruncado[0:precisao])
            else:
                numTruncado = str(numTruncado[0:precisao])
            while True:
                if len(numTruncado) <= precisao:
                    numTruncado = numTruncado + '0'
                else:
                    break

            truncado = True

    else:  # se o numero tiver a apenas parte real
        decimalBin = str(decimalBin)
        i = base = 0
        l = list()
        for i in range(2, len(decimalBin)):
            l.append(decimalBin[i])
        i = 0
        # conta o numero de 0 antes do primeiro 1 (calculo o expoente nagativo)
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
            numTruncado = str(decimalBin[0: precisao + 1])
            truncado = True
        if base != 0:
            num = str(decimalBin)
        else:
            num = str(decimalBin)
        base = base * (-1)
    if base > upper:
        print("Número normalizado: Overflow")
        if truncado:
            if numTruncado.isnumeric():
                int_dec = converteInteiroBin(numTruncado)
                print(int_dec)
            elif float(numTruncado) >= 1:
                aux2 = numTruncado.split('.')
                int_dec = converteInteiroBin(aux2[0])
                fra_dec = converteDecimalBin("0." + aux2[1], precisao)
                numTruncado = int_dec + fra_dec
                print(numTruncado)
            else:
                fra_dec = converteDecimalBin(numTruncado, precisao)
                print(fra_dec)
        return -1
    elif base < lower:
        print("Número normalizado: Underflow")
        if truncado:
            if numTruncado.isnumeric():
                int_dec = converteInteiroBin(numTruncado)
                # print(int_dec)
            elif float(numTruncado) >= 1:
                aux2 = numTruncado.split('.')
                int_dec = converteInteiroBin(aux2[0])
                fra_dec = converteDecimalBin("0." + aux2[1], precisao)
                numTruncado = int_dec + fra_dec
                # print(numTruncado)
            else:
                fra_dec = converteDecimalBin(numTruncado, precisao)
                # print(fra_dec)
        return -1
    norma = []
    norma.append(num)
    norma.append(base)
    return norma


def sinalAmplitude(num, sinal):
    if sinal == 0:  # se numero positivo
        lista = num.split(".")
        num = "".join(lista)
    else:  # se numero negativo
        lista = num.split(".")
        num = "".join(lista)
    return num


def complementoDeUm(num, sinal, precisao):
    l=[]
    num = sinalAmplitude(num, sinal)
    # complemento de 1 do numero (invercao dos valores)
    for i in range(0, len(num)):
        l.append(num[i])
        if l[i] == '1':  # 0 vira 1
            l[i] = '0'
        elif l[i] == '0':  # 1 vira 0
            l[i] = '1'
    if len(l) < precisao:  # verifica se falta valores na mantissa para preencher de 0s
        tan = precisao - len(l)
        for i in range(0, tan):
            l.append('0')
    num = ''.join(l)
    return num


def complementoDe2(num, sinal, precisao):
    l = []
    c = 0
    num = complementoDeUm(num, sinal, precisao)
    if len(num) <= precisao:  # se numero for menor que a precição (para não extouro da posição da lista)
        aux = len(num) - 1
    else:
        aux = precisao
    for i in range(0, aux + 1):
        l.append(num[i])
    for i in range(aux, -1, -1):  # faz o complemento de 2
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


# calcula o expoente e normaliza os numeros entre 0 e 1
def normalizaFracionario(decimalBin):
        decimalBin = str(decimalBin)
        i = base = 0
        l = list()
        for i in range(2, len(decimalBin)):
            l.append(decimalBin[i])
        i = 0
        while True:  # vide normaliza numeros menores 1 e maiores que 0
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


def desnormaliza(numBin, expoente, sinalExp):
        l = list()
        l = list(numBin)
        if sinalExp == 0:  # se expoente positivo
            if len(numBin) < expoente:  # numero mantissa menor que expoente
                for i in range(len(numBin), expoente):
                    l.append('0')
        if len(numBin) > expoente:
            l.insert(expoente, '.')
        numBin = "".join(l)
        return numBin


# guarda numero desnormalizado, verifica se ele tem plonto flutuante ou inteiro, e depois converte para um num na ()10'
def chamaConvercao(norma, sinalExp, precisao):
    num = desnormaliza(str(norma[0][2:precisao + 2]), norma[1], sinalExp)
    if '.' in num:  # se tiver ponto flutuante ocorre convercao de parte decimal e parte ibteira
        l = num.split('.')
        decimal = converteDecimalBin(str("0." + l[1]), precisao - len(l[0]))
        inteiro = converteInteiroBin(l[0])
        numInteiro = inteiro + decimal
    else:  # convercao so da parte inteira do binario
        inteiro = converteInteiroBin(num)
        numInteiro = inteiro
    return numInteiro  # retorna numero na base 10
