#crie um programa que peça os cumprimentos dos catetos adjacente e oposto de um triângulo retângulo e calcule
#a hipotenusa

import math
oposto = float(input('Informe o comprimento do cateto oposto: '))
adjacente = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)

print('A hipotenusa é {:.2f}'.format(hipotenusa))

