# C u r s o   e m   V í  d  e  o     P  y  t  h  o  n
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

frase = 'Curso em Vídeo Python '

print(frase.split())

# frase[3] - mostra somente a string na posição 3
# frase[1:15] - mostra as string da posição 1 até a 15
# frase[1:15:2] - mostra as string da posição 1 até a 15 pulando de 2 em 2
# frase[1::5] - mostra as string da posição 1 até o final pulando de 5 em 5
# len(frase) - comprimento da frase
# frase.count('o') - quantas vezes aparece a palavra
# frase.find('deo') - encontrar (retorna a posição da string)
# 'Curso' in frase - semelhante ao find mas retorna true ou false
# frase.replace('Python','Java') - Substitui a palavra pela outra
# frase.upper() - COLOCA TUDO EM MAIUSCULO
# frase.lower() - tudo em minusculo
# frase.capitalize - Só a primeira letra da frase em maiusculo
# frase.title() - Todas As Primeiras Letras De Cada Palavra Fica Maiuscula
# frase.strip() - remove espaços no começo e no final da frase antes das palavras
# frase.rstrip() - remove espaços no final (lado direito) da frase
# frase.lstrip() - remove espaços no começo (lado esquerdo) da frase
# frase.split() - divide uma string e gera uma lista por palavras
# '-'.frase.join() - junta as strings e insere o que vc quiser no local do espaço

# frase.upper().count('O') - combinar... converte tudo pra maiúscula depois conta quantos "O" tem na frase...
# dividido = frase.split() | print (dividido[2]) - divide por lista e exibe a palavra na posição

# Imprimir um texto grande = usa aspas 3x = """ TEXT """
'''print('\n')
print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book.""")'''
