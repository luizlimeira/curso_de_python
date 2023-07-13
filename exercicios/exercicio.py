#variaveis
salario = 1200
emprestimo = int(input("Emprestimo: "))

#processo
if emprestimo <= salario * 0.50:
    print("Emprestimo aprovado!")

elif emprestimo <= salario * 0.75:
    print("Emprestimo em análise...")

else:
    print("Emprestimo negado.")