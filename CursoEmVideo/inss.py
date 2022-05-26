salario = float(input('Qual seu salário: '))

if salario <= 1212:
    inss = salario * 0.075
    liquido = salario - inss
    print(f'Desconto de 7,5%. INSS: {inss}\nSeu salário líquido é: {liquido}')
elif salario > 1212.01 and salario < 2427.35:
    inss = salario * 0.09
    liquido = salario - inss
    print(f'Desconto de 9%. INSS: {inss}\nSeu salário líquido é: {liquido}')
elif salario > 2427.36 and salario < 3641.03:
    inss = salario * 0.12
    liquido = salario - inss
    print(f'Desconto de 12%. INSS: {inss}\nSeu salário líquido é: {liquido}')
else:
    inss = salario * 0.14
    liquido = salario - inss
    print(f'Desconto de 14%. INSS: {inss}\nSeu salário líquido é: {liquido}')

