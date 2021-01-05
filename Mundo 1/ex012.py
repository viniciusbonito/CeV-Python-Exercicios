# crie um programa que pergunte o nome e valor de um produto, em seguida ele deve perguntar um percentual de desconto
# de liquidação e retornar o novo valor do produto com o desconto solicitado

print('=' * 40)
print('{:^40}'.format('Auxiliar de descontos'))
print('=' * 40)

produto = str(input('\nInforme o nome do produto: '))
preco = float(input('Informe o preço normal do produto: '))
desconto = float(input('Informe o percentual de desconto da liquidação: '))
final = (preco / 100) * (100 - desconto)

print('\nO produto {} custa habitualmente R$ {:.2f}, com o desconto de {:.2f}%'.format(produto, preco, desconto))
print('seu preço passa a ser de R$ {:.2f}'.format(final))