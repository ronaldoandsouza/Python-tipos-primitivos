# Operadores aritméticos (arithmetic operators)

'''
+ adição    ex: 5+2 == 7
- subtração ex: 5-2 == 3
* multiplicação ex: 5*2 == 10
/ divisão   ex: 5/2 == 2.5
** potência ex: 5**2 == 25
// divisão inteira  ex: 5//2 == 2
% resto da divisão  ex: 5%2 == 1
'''

# Ordem de precedência (Order of Precedence)

'''
1-> () 
2-> **
3-> *, /, //, %
4-> +, - 
'''
'''
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))
'''

n1 = int(input('Um valor: '))
n2 = int(input('outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, \no produto é {} e a divisão é {:.3f}'.format(s, m, d), end='')
print('Divisão inteira é {} e potência é {}'.format(di, e))
