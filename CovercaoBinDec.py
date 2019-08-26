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
    # pega da string e coloca no lista
    for i in range(0, len(num)):
        l.append(num[i])
    l.pop(0), l.pop(0)  # esclui o 0 e . da lista
    # converte os valores armazenados na lista em inteiro
    for i, o in enumerate(l):
        l[i] = int(l[i])
    # soma das valores (converção)
    # se o numero for dizima ele usa toda a mantissa
    if len(num) - 2 > n:
        for i in range(0, n + 1):
            soma += l[i] * 2**(-j)
            j += 1
    # se for menor que a que o tamanho da mantissa ele é multiplo de dois e não usa toda a mantissa
    else:
        for i in range(0, len(num) - 2):
            soma += l[i] * 2**(-j)
            j += 1
    return soma
