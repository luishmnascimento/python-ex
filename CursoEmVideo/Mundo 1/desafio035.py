from colors_lh import cores

print(f'{cores["verde em negrito"]}=================')
a = int(input('Medida 1: '))
b = int(input('Medida 2: '))
c = int(input('Medida 3: '))

if a + b > c and a + c > b and b + c > a:
    print('Triângulo formado')
else:
    print('Impossível formar um triangulo')