altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))

area = altura * largura
tinta = 2

cobertura = area / 2

print(f'A parede tem {area} metros!\nSerá necessário {cobertura} litros de tinta!')
