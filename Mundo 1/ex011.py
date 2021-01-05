# criar um programa que pergunte as dimensões de uma parede, calcule sua área e informe quantos litros de tinta
# seriam necessários para a pintura, após perguntar o rendimento da tinta informado na lata

print('=' * 40)
print('{:^40}'.format('Assistente de pintura'))
print('=' * 40)

altura = float(input('Informe a altura da parede em metros: '))
largura = float(input('Informe a largura da parede em metros: '))
area = altura * largura

print('\nA área total da parede é de {:.2f}m²'.format(area))

litros = float(input('\nQuantos litros contém a lata de tinta escolhida? '))
rendlata = float(input('Qual o rendimento em metros informado na lata? '))
rendlitro = rendlata / litros

print('\nSe a lata possui {:.2f}L e rende {:.2f}m²'.format(litros, rendlata))
print('então o rendimento por litro é de {:.2f}m²'.format(rendlitro))
print('\nSerão necessário {:.2f}L para pintar toda a parede'.format(area / rendlitro))