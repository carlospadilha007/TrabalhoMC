from FuncoesSecundarias import leNumero
import os


precisao = int(input('Número de algarismos da mantissa: '))
lower = int(input('Menor valor do expoente: '))
upper = int(input('Maior valor do expoente: '))
"""precisao = 20
lower = -10
upper = 10"""
while True:
    leNumero(precisao, lower, upper)
    op = str(input('(S)-Continue ou (N)-Parar: ')).strip().upper()[0]
    if 'N' in op:
        precisao = int(input('Número de algarismos da mantissa: '))
        lower = int(input('Menor valor do expoente: '))
        upper = int(input('Maior valor do expoente: '))
    os.system('cls')
