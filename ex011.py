'''Desafio 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule
a sua área e a quantidade de tinta necessária para pinta-la, sabemos que a cada litro de tinta, pinta
uma área de 2 metros quadrados.'''
alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))
area = alt * larg
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(alt, larg, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(tinta))