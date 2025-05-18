'''Desafio 004: Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações
possíveis sobre ele:'''
algo = input('Type something: ')
print(f'Você digitou {algo}, e seu tipo primitivo é: ',type(algo))
print('Só tem espaços: ', algo.isspace())
print('Só tem maíusculas: ', algo.isupper())
print('Só tem minúsculas: ', algo.islower())
print('É numérico: ', algo.isnumeric())
print('É alfabético: ', algo.isalpha())
print('É alfanumérico: ', algo.isalnum())
print('Esta captalizado: ', algo.istitle())


