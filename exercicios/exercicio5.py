palavra = input("Palavra:")

if palavra == palavra[::-1]:
    print("é um palindromo")
else:
    print("não é um palindromo")