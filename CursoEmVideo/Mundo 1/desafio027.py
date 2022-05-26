# LER O NOME COMPLETO DE UMA PESSOA, E MOSTRAR SOMENTE O PRIMEIRO E ULTIMO NOME

n = str(input('Qual seu nome: ')).title().strip()

nome = n.split()

print(f'First Name: {nome[0]}')
print(f'Last Name: {nome[len(nome) -1]}')