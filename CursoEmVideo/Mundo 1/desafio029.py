velocidade = float(input('Qual a velocidade apurada no radar? '))

limite = 80

if velocidade > limite:
    excedido = velocidade - limite
    multa = excedido * 7
    print(f'Velocidade permitida: {limite}km')
    print(f'Velocidade apurada: {velocidade}km')
    print(f'Você excedeu: {excedido}km')
    print(f'Multa aplicada de: {multa} reais')
print('Tenha um bom dia. Dirija com segurança.')