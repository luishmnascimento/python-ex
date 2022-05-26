capital = float(input('Qual valor deseja simular? '))
juros = float(input('Taxa de Juros: '))


for i in range(1, 25):
    montante = capital * (1 + (juros/100)) ** i
    parcela = montante / i
    print(f'R$: {i}x {parcela:.2f} = {montante:.2f}')