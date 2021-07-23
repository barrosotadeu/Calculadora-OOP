from calculadoraoop import Calculadora
from sys import exit
from math import sqrt, pow


calculadora = Calculadora()

print('*********Calculadora*********\n\n\n\n')


while True:

    escolha = int(input('''Qual operação você deseja fazer: 


                           1: Soma
                           2: Subtração
                           3: Multiplicação
                           4: Divisão
                           5: Potenciação
                           6: Raiz
                           7: Sai
                           '''))

    
    calculadora.resultado(escolha)