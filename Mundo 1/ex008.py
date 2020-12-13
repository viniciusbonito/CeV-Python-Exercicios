# Crie um programa que peça um valor em metros e o exiba em centímetros e milímetros

print('='*20)
print('Conversor de medidas')
print('='*20)

medida = float(input('Informe um valor em metros: '))
centimetros = medida * 100
milimetros = medida * 1000

print(f'Você informou {medida}m \n{medida}m corresponde a {centimetros}cm')
print(f'{medida}m corresponde a {milimetros}mm')