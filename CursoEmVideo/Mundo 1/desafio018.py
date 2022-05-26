import math

angulo = float(input('Digite o angulo que deseja calcular: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'SENO: {seno:.2f}\nCOSSENO: {cosseno:.2f}\nTANGENTE: {tangente:.2f}')
