n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
n3 = int(input('Digite um número:'))

maior = n1
menor = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f'Maior: {maior}')
print(f'Menor: {menor}')