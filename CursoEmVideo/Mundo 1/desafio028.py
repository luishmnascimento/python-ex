import random

num_vencedor = int(input('Digite um numero de 0 a 5: '))

num_sorteado = random.randint(0, 5)

if num_sorteado == num_vencedor:
    print(f'Numero Sorteado: {num_sorteado}. Numero escolhido: {num_vencedor}. Congrats! You Win.')
else:
    print(f'Numero Sorteado: {num_sorteado}. Numero escolhido: {num_vencedor}. Sorry, but you lose!')

