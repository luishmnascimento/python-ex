alcool = float(input('Preço do Alcool: '))
gasolina = float(input('Preço do Gasolina: '))

t = alcool * 100 / gasolina


if t >= 70:
    print(f'Porcentagem está em: {t:.2f}% \nCompensa abastercer com Alcool!')
else:
    print(f'Porcentagem está em: {t:.2f}% \nCompensa abastercer com Gasolina!')