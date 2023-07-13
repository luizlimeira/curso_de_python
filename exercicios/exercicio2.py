numeros = []

for i in range(3):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

numeros_ordenados = sorted(numeros) 
if numeros_ordenados[0] == numeros_ordenados[1] == numeros_ordenados[2]:
    print("Todos os numeros são iguais.")
    
elif numeros_ordenados[0] == numeros_ordenados[1]:
    print("Dois numeros são iguais:", numeros_ordenados[0], ",", numeros_ordenados[1])
    print("O outro numero é:", numeros_ordenados[2])

elif numeros_ordenados[1] == numeros_ordenados[2]:
    print("Dois numeros são iguais:", numeros_ordenados[1], ",", numeros_ordenados[2])
    print("O outro número é:", numeros_ordenados[0])

else:
    print("Numeros em ordem crescente:", numeros_ordenados)