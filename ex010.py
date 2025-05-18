'''Desafio 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
quantos dólares ela pode comprar'''
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = 5.86
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, real/dolar))
