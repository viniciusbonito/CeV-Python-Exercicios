# crie um programa que peça ao usuário que digite algo, armazene o dado em uma variável e analise essa variável

analise = input('Digite algo: ')

print('O tipo primitivo da variável é: ', type(analise))
print('O valor é numérico?', analise.isnumeric())
print('O valor é alfanumérico? ', analise.isalnum())
print('O valor é alfabético? ', analise.isalpha())
print('O valor é imprimível? ',analise.isprintable())
print('Contém apenas letras minúsculas? ', analise.islower())
print('Contém apenas letras maiúsculas? ', analise.isupper())
