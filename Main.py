from FuncoesSecundarias import leNumero
import os

while True:
    '''precisao = int(input('Número de algarismos da mantissa: '))
    lower = int(input('Menor valor do expoente: '))
    upper = int(input('Maior valor do expoente: '))'''
    precisao = 3
    lower = -1
    upper = 3
    leNumero(precisao, lower, upper)
    op = str(input('(S)-Continue ou (N)-Parar: ')).strip().upper()[0]
    if 'N' in op:
        break
    os.system('cls')
