# LER O NOME DA CIDADE E DIZER SE COMEÇA OU NÃO COM O NOME 'SANTO'
cidade = str(input('Digite o nome da cidade: ')).strip()

print(cidade[:5].upper() == 'SANTO')