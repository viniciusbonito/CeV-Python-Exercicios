## crie um programa que utilize módulos para mostrar a porção inteira de um número real

import math

numero = float(input('Digite um número real para ver apenas a sua parte inteira: '))
numint = math.trunc(numero)
print('A parte inteira de {} é {}'.format(numero, numint))
