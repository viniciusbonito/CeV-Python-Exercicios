#Crie um programa que leia o nome de quatro alunos e sorteie um deles para apagar a lousa

import random
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]

print('\nO escolhido para apagar a lousa foi {}'.format(random.choice(lista)))
