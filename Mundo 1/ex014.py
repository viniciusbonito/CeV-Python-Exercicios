# crie um programa que solicite uma temperatura em graus celsius e retorne em fahrenheit

print('-' * 40)
print('{:^40}'.format('Conversor ºC para ºF'))
print('-' * 40)

celsius = float(input('Informe a temperatura em ºC: '))
fahrenheit = (celsius * 1.8) + 32

print('\nVocê informou {:.1f}ºC, isto equivale a {:.1f}ºF'.format(celsius, fahrenheit))
