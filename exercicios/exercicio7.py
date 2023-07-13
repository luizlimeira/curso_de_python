lista = input("Numeros: ")

numeros = lista.split(",")

numeros_inteiros = []
for numero in numeros:
    numeros_inteiros.append(int(numero))

numeros_pares = []
for numero in numeros_inteiros:
    if numero % 2 == 0:
        numeros_pares.append(numero)

numeros_impares = []
for numero in numeros_inteiros:
    if numero % 2 == 1:
        numeros_impares.append(numero)

print("Lista completa:", numeros_inteiros)
print("Numeros pares:", numeros_pares)
print("Numeros impares:", numeros_impares)