contas = {}

def conta():
    nome = input("Digite seu nome: ")
    saldo = float(input("Digite seu saldo: "))

    #definindo o numero das contas e criando um dicionario para cada
    numero_contas = len(contas) + 1
    contas[numero_contas] = {"Nome": nome, "Saldo": saldo}
    print(f"Conta criada com sucesso! Numero da conta: {numero_contas}")
    print("Saldo:", contas[numero_contas]["Saldo"])

def saldo():
    numero_contas = int(input("Digite o número da conta: "))

    if numero_contas in contas:
        saldo = contas[numero_contas]["Saldo"]
        print("Saldo da conta:", saldo)

    else:
        print("Conta não encontrada")

def deposito():
    numero_contas = int(input("Digite o número da conta: "))

    if numero_contas in contas:
        deposito = float(input("Quanto deseja depositar: "))
        contas[numero_contas]["Saldo"] += deposito
        print("Deposito feito com sucesso!")
        print("Saldo atual:", contas[numero_contas]["Saldo"])

    else:
        print("Conta não encontrada")

def saque():
    numero_contas = int(input("Digite o número da conta: "))

    if numero_contas in contas:
        saque = float(input("Quanto deseja sacar: "))
        if contas[numero_contas]["Saldo"] >= saque:
            contas[numero_contas]["Saldo"] -= saque
            print("Saque realizado com sucesso!")
            print("Saldo restante:", contas[numero_contas]["Saldo"])

        else:
            print("Saldo insuficiente")

    else:
        print("Conta não encontrada")

def encerrar():
        print("Programa encerrado, obrigado!")