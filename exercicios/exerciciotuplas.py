numeros = [2,5,10,100,5,12,17]

valor = int(input("Digite um valor: "))
if valor in numeros:
    print("Esse valor se encontra")

else:
    numeros.append(valor)
    print("Nova lista: ", numeros)
