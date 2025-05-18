#Tipos primitivos (Primitive types)
'''O valor digitado dentro do input, sempre será considerado uma string'''
'''Exemplo
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma vale', s)'''


'''int(números inteiros) 7, -4, 0, -9875
   float(números reais ou de ponto flutuante) 4.5, 0.076, -15.223, 7.0
   bool(boleanos) True e False
   str(strings) 'Olá' '7.5' '' '''

'''print('A soma vale {}'.format(s))Nova sintaxe utilizando {} como máscara para exibir o valor'''


#Prática
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))


'''Para saber o tipo primitivo, utilize o type
n1 = input('Digite um valor: ')
print(type(n1))
(console) <class 'str'> aparecerá que é string, pois não definido o tipo de dado
n1 = int(input('Digite um valor: ')
print(type(n1))
(console) <class 'int'>'''