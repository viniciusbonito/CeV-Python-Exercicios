# Crie um programa que peça ao usuário para indicar um número e retorne a ele o seu dobro, seu triplo e sua raiz quadrada

numero = float(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print(f'Analisando o número {numero}, seu dobro é {dobro}, seu triplo é {triplo} e sua raiz quadrada é {raiz}')