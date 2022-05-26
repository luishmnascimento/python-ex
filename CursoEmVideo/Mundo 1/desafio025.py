# LER O NOME DE UMA PESSOA E DIZER SE TEM O NOME 'SILVA' NO NOME
nome = str(input('Digite o nome: ')).strip()

print(f'Seu nome tem Silva? {"SILVA" in nome.upper()}')