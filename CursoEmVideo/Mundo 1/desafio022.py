nome = 'Luis Henrique Maia Nascimento'

print('Nome com letra maiúscula: ')
print(nome.upper())

print('\nNome com letra minúscula: ')
print(nome.lower())

print('\nTotal de letras sem espaço: ')
print(len(nome.replace(' ', '')))
print(len(nome) - nome.count(' '))

primeironome = nome.split()
print(f'Seu nome é {nome} e seu primeiro nome tem {len(primeironome[0])} letras!')
# ou
print(nome.find(' '))