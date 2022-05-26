# CALCULAR VALOR DE SOBREAVISO, COM BASE EM 1/3 DA HORA
salario = float(input('Qual seu salário: '))
horas = int(input('Quantas horas de banco você quer calcular: '))

valor_hora = salario /220
terco_hora = valor_hora * 0.33
valor_hora_mes = terco_hora * horas
total = salario + valor_hora_mes

print(f'Salario Bruto: {salario}\nTotal de Horas: {horas}\nValor por Hora: {terco_hora}\nValor das Horas/Mês: {valor_hora_mes}\nSalario + Horas: {total}')