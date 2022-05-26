preco_normal = float(input('Digite o preço do produto: '))

for parcelas in range(1, 11):
    parcelado = preco_normal / parcelas
    print(f'{parcelas}x{parcelado:.2f}')
    #
    juros = (preco_normal / parcelas) * 0.0199
    print(f'{parcelas}x{parcelado:.2f}')