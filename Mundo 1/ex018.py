#faça um programa que leia um angulo qualquer e mostre na tela o seu seno, coseno e tangente

import math
angulo = int(input('Informe um ângulo para saber seu seno, cosseno e tangente: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O âmgulo de {}º tem como seno {:.2f} , cosseno {:.2f}'.format(angulo, seno, cosseno))
print('e tangente {:.2f}'. format(tangente))
