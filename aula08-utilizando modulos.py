#Utilizando modulos (using modules)
#import **** usa toda o modulo importado (generalista)
#from **** import **** usa apenas as funcionalidades que escolher (especifico) economizando na  memória.

#exemplo
'''import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))'''

#exemplo
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))