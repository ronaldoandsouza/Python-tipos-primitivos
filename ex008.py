'''Desafio 008: Escreva um programa que leia um valor em metros e o exiba convertido em
contímetros e milímetros'''
medida = float(input('Digite um valor em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m correspoonde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))