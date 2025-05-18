'''Manipulando strings (manipulating strings)
Manipular strings em Python é essencial para lidar com textos e dados.
No Pycharm, você pode usar diversas funções e métodos para modificar,
formatar e analisar strings.
O Python fornece muitas funções integradas para manipular strings
Python string é imutáve, então todas essas funções retornam uma nova
string e a string original permanece inalterada.'''

#Concatenação: Junta strings com + ou join().
#Fatiamento: Acessar partes da string com string[início:fim].

#Métodos úteis:
'''upper() e lower() para alterar maiúsculas/minúsculas.'''
'''strip() para remover espaços extras'''
'''replace() para substituir partes da string.'''
'''split() para dividir uma string em uma lista.'''
'''find() usado para encontrar o índice de uma substring em uma string.'''
'''capitalize() usado para colocar a primeira letra em maiúscula.'''
'''title() coloca todas as iniciais das palavras em maiúsculas.'''

#Interpolação e formatação:
'''f"{variável}"(f-strings) para formatar dinamicamente.'''
'''format() e % para formatação mais tradicional.'''

#testes
frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android'))
lista = 'Curso em Vídeo Python'
print(lista.split())