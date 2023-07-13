#Questão 1
def som():
    x = 10
    y = 5
    return x + y

soma = som()
print(soma)
print("-----------------------------------------------------------------------")

#Questão 2
def graus(f):
    c = int(input("Digite uma temperatura: "))
    f = c * 1.8 + 32
    return f

temp = graus(1)
print(temp)
print("-----------------------------------------------------------------------")

#Questão 3
def par():
    x = int(input("Digite um numero: "))
    if x % 2 == 0:
        return "é par"
    else:
        return "não é par"

resultado = par()
print(resultado)
print("-----------------------------------------------------------------------")

#Questão 4
def lista():
    x = input("Digite numeros: ")
    y = x.split(",")

    numeros_inteiros = []
    for numero in y:
            numeros_inteiros.append(int(numero))
    return max(numeros_inteiros)

lista_final = lista()
print(lista_final)
print("-----------------------------------------------------------------------")

#Questão 5
def fatorial():
    x = int(input("Digite um numero: "))
    y = 1
    for i in range(1, x + 1):
        y *= i
    return y

resultado_fatorial = fatorial()
print("O resultado do fatorial é: ", resultado_fatorial)
print("-----------------------------------------------------------------------")

#Questão 6
def palavra():
    x = input("Digite uma palavra: ")
    return x[::-1]

palav_final = palavra()
print(palav_final)
print("-----------------------------------------------------------------------")

#Questão 7
def lista1():
    x = input("Digite numeros: ")
    y = x.split(",")

    lista1_ = []
    for numero in y:
        lista1_.append(int(numero))
    return sum(lista1_) / len(lista1_)

lista1_final = lista1()
print(lista1_final)
print("-----------------------------------------------------------------------")

#Questão 8
def lista2():
    x = input("Digite palavras: ")
    z = x.split(" ")

    y = []
    for i in z:
        if len(i) >= 5:
            y.append(i)
    print(y)
    return len(y)

palav1 = lista2()
print(palav1)
print("-----------------------------------------------------------------------")

#Questão 9
def lista3():
    x = input("Digite numeros: ")
    z = x.split(",")

    y = []
    numeros_inteiros2 = []
    for numero in z:
            numeros_inteiros2.append(int(numero))
    for i in numeros_inteiros2:
        if i % 2 == 0:
            y.append(i)
    return y

listafinal = lista3()
print(listafinal)