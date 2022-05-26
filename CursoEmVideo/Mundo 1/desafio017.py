from math import hypot

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))

#hi = (co ** 2 + ca ** 2) ** 1/2
hi = hypot(co, ca)

print(f'Hipotenusa é: {hi:.2f}')

