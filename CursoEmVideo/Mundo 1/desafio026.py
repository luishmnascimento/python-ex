# FRASE QUANTAS VEZES APARECE A LETRA 'A, EM QUE POSIÇÃO APARECE NA PRIMEIRA E NA ULTIMA VEZ

frase = str(input('Digite uma frase: ')).strip().lower()

#contador = frase.count('a')

print(f'Quantas letras A possui na frase? {frase.count("a")}')
print(f'Posição da primeira letra A? {frase.find("a") + 1}')
print(f'Posição da última letra A? {frase.rfind("a") + 1}')