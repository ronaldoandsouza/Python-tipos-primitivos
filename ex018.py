'''Desafio 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo'''
from math import radians,sin, cos, tan
a = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(a))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(a, seno))
cosseno = cos(radians(a))
print('O ângulo de {} tem p COSSENO de {:.2f}.'.format(a, cosseno))
tangente = tan(radians(a))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(a, tangente))

