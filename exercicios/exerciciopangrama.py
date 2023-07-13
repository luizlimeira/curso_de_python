def pangrama (palavra):
    alfabeto = "abcdefghijlmnopqrstuvxz"
    for i in alfabeto:
        if i not in palavra:
            return False
    return True

frase = input("Frase: ")
if (pangrama(frase) == True):
    print("é pangrama")
else:
    print("Não é pangrama") 