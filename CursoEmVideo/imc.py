# Peso / Altura²

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = (peso / (altura * altura))

print(f'Seu IMC é {imc:.2f}')

