#Crie um programa que peça para o professor informar 4 alunos e sorteie a ordem de apresentação
#dos trabalhos

import random

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
Lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(Lista)

print('A ordem de apresentação dos trabalhos é:\n{}'. format(Lista))
