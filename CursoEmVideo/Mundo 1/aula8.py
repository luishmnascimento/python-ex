#import math

from  math import sqrt, floor

num = int(input('Digite um número: '))

#raiz = math.sqrt(num)
raiz = sqrt(num)


#print(f'A raiz de {num} é: {raiz}')

print(f'A raiz de {num} é: {floor(raiz)}')