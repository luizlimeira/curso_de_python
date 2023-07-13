palavra = input("Digite algo:")
palavra_minuscula = palavra.lower()
vogais = "aeiou"
numeros_vogais = 0

for letra in palavra:
    if letra in vogais:
        numeros_vogais += 1

print(numeros_vogais)