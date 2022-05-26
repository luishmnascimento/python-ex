distancia = float(input('Qual a distancia da viagem: '))

if distancia <= 200:
    km = 0.50
    valor = distancia * km
else:
    km = 0.45
    valor = distancia * km

print(f'Distância: {distancia} km')
print(f'Valor por km: R$ {km}')
print(f'Valor total: R$ {valor}')