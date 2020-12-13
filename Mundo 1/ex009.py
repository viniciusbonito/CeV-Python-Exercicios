# Crie um programa que leia um número inteiro qualquer e exiba sua tabuada na tela

print('='*20)
print('{:^20}'.format('Tabuada'))
print('='*20)

numero = int(input('Digite um número qualquer para saber sua tabuada: '))

print('=' * 37)
print('|{:>5} x 1 = {:^5}|{:>5} x 6 = {:^5}|'.format(numero, numero*1, numero, numero*6))
print('|{:>5} x 2 = {:^5}|{:>5} x 7 = {:^5}|'.format(numero, numero*2, numero, numero*7))
print('|{:>5} x 3 = {:^5}|{:>5} x 8 = {:^5}|'.format(numero, numero*3, numero, numero*8))
print('|{:>5} x 4 = {:^5}|{:>5} x 9 = {:^5}|'.format(numero, numero*4, numero, numero*9))
print('|{:>5} x 5 = {:^5}|{:>5} x 10 ={:^5}|'.format(numero, numero*5, numero, numero*10))
print('=' * 37)