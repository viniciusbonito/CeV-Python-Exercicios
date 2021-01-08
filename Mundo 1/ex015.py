# crie um programa que calcule o preço de aluguel de um carro perguntando  a quantidade de dias que passou alugado
# e a km rodada

print('=' * 40)
print('{:^40}'.format('Cálculo de aluguél'))
print('=' * 40)

dias = int(input('\nQuantos dias o carro permaneceu alugado? '))
km = int(input('Quantos Km o carro rodou? '))
diaria = float(input('Informe o valor da diária de aluguel em R$: '))
kmrodados = float(input('Informe o valor do KM rodado em R$: '))

print('\nO carro foi alugado por {} dias, a R$ {:.2f} a diária'.format(dias, diaria))
print('e foram rodados {}Km ao custo de R$ {:.2f} por Km rodado'. format(km, kmrodados))
print('\nO Valor total a ser pago é de R$ {:.2f}'. format((diaria * dias) + (km * kmrodados)))
