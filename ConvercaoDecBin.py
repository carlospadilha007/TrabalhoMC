# inverte o numero na lista e retorna o numero inteiro
def inverteNum(l):
    '''
    :param l: lista com numeros binarios
    :return: num invertido e inteiro
    '''
    l.reverse()
    for i, c in enumerate(l):
        l[i] = str(l[i])
    num = "".join(l)
    return num


# transforma o "vetor" (lista) em um numero unico
def joinNum(l):
    '''
    :param l: lista com numeros binarios
    :return: num invertido e inteiro
    '''
    for i, c in enumerate(l):
        l[i] = str(l[i])
    num = "0." + "".join(l)
    float(num)
    return num


# converte a parte inteira de um numero para binario
def converteInteiro (num):
    l = []
    if num == 0:
        l.append(0)
    else:
        while num >= 1:
            l.append(num % 2)
            num = int(num / 2)
    return inverteNum(l)


# converte a parte decimal de um numero para decimal binario
def converteDecimal(num):
    i = 0
    l = list()
    while (i < 50) and (num > 0.0):
        aux = int(num * 2)
        l.append(aux)
        num = num * 2
        num = num - l[len(l) - 1]
        i += 1
    # print(l)
    return joinNum(l)
