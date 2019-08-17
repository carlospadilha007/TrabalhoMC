def converteInteiroBin(num):
    num = str(num)
    soma = j = 0
    l = []
    for i in range(0, len(num)):
        l.append(num[i])
    for i, o in enumerate(l):
        l[i] = int(l[i])

    # converção
    for i in range(len(l) - 1, -1, -1):
        soma += l[i] * 2 ** j
        j += 1
    return soma


def converteDecimalBin(num, n):
    num = str(num)
    soma = 0.0
    j = 1
    l = []
    for i in range(0, len(num)):
        l.append(num[i])
    l.pop(0), l.pop(0)
    for i, o in enumerate(l):
        l[i] = int(l[i])
    # falta passa como parametro a precisão para limitar, o tamanho do for
    for i in range(0, n):
        soma += l[i] * 2**(-j)
        j += 1
    return soma
