dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))

total_dias = dias * 60
total_km = km * 0.15
pagar = total_dias + total_km

print(f'Saldo devedor: {pagar}')