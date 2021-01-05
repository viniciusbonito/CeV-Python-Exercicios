# Crie um programa que pergunte o nome de um funcionário, seu salário atual e uma alíquota de aumento
# em seguida este programa deve retornar o novo salário com o reajuste solicitado

print('=' * 40)
print('{:^40}'.format('Reajuste salarial'))
print('=' * 40)

nome = str(input('Informe o nome do funcionário: '))
salario = float(input('Informe o salário atual do funcionário: '))
aumento = float(input('Informe o percentual de aumento pretendido: '))
salfinal = (salario / 100) * (100 + aumento)

print('\n{} recebe atualmente R$ {:.2f}, com o aumento de {:.2f}%'.format(nome, salario, aumento))
print('passará a receber R$ {:.2f}'.format(salfinal))