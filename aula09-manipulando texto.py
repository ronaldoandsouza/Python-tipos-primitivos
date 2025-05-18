# Manipulando texto (manipulating text)
'''Fatiamento:
Exemplo 1
frase = 'Python'
         012345
frase[2]
console vai imprimir o índice 't'

exemplo 2
frase = 'Python'
         012345
frase[1:4]
console vai imprimir os índices 'yth' (inclui o primeiro e exclui o ultimo)

exemplo 3
frase = 'Python'
         012345
frase[0:6:2]
console vai imprimir os índices 'Pto' (pegando o inicio até o final saltando 2)

exemplo 4
frase = 'Python'
         012345
frase[:6]
console vai imprimir 'Python' (considerando ":" como índice zero)

exempo 5
frase = 'Python'
         012345
frase[1:]
console vai imprimir 'ython' (iniciando no índice 1 até e considerando ":" como o índice final)

exemplo 6
frase = 'Python'
         012345
frase[0::2]
console vai imprimir 'Pto' (adicionando o primeiro índice até o final e vai saltar 2)
'''

#Análise
'''
exemplo 1 
frase = 'Python'
         012345
len(frase)
console vai mostrar a quantidade de caracter(6), a função "len" significa COMPRIMENTO.

exemplo 2
frase = 'Python'
         012345
frase.count('o')
console mostrará (1) ou seja, vai utilizar o contador informando quantas vezes o parametro indicado foi utilizado.

exemplo 3
frase = 'Python'
         012345  
frase.find('thon')
console mostrará (2), pois .find significa encontrar e vai indicar onde começou ou seja, onde está o índice 't'

        '''