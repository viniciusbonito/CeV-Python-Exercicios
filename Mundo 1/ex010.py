# criar um programa que pergunte a cotação do dólar e quantos reais a pessoa tem na carteira
# em seguida o programa deve retornar a quantidade de dólares que a pessoa pode comprar

print('-' * 40)
print('{:^40}'.format('Assistente de Câmbio'))
print('-' * 40)

dolar = float(input('Favor informar a cotação atual do dólar em reais: '))
reais = float(input('Agora me informe quantos tem disponíveis para a compra de dólares. R$: '))

print('\nCom R$ {:.2f} você consegue adquirir USD {:.2f}'.format(reais, reais/dolar))