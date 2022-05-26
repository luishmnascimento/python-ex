import colors_lh
salario = float(input('Digite seu salário: R$'))

if salario < 1250:
    aumento = 15
    nsalario = salario + (salario * (aumento / 100))
else:
    aumento = 10
    nsalario = salario + (salario * (aumento / 100))

print(f'Salario atual: {colors_lh.cores["vermelho em negrito"]}R${salario}\033[m\nAumento: {colors_lh.cores["azul em negrito"]}{aumento}%\033[m\nNovo salário: {colors_lh.cores["verde em negrito"]}R${nsalario:.2f}\033[m')
