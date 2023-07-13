#lista vazia
contas = {}


while True:
    print("Selecione uma opção: ")
    print("1-Criar conta")
    print("2-Verificar saldo")
    print("3-Depositar dinheiro")
    print("4-Sacar dinheiro")
    print("5-Encerrar")
    
    opcoes = str(input("Opção: "))

    #base
    if opcoes == "1":
        nome = input("Digite seu nome: ")
        saldo = float(input("Digite seu saldo: "))

        #definindo o numero das contas e criando um dicionario para cada
        numero_contas = len(contas) + 1
        contas[numero_contas] = {"Nome": nome, "Saldo": saldo}
        print("Conta criada com sucesso! Numero da conta:", numero_contas)
        
    #ver saldo na conta
    elif opcoes == "2":
        numero_contas = int(input("Digite o número da conta: "))

        if numero_contas in contas:
            saldo = contas[numero_contas]["Saldo"]
            print("Saldo da conta:", saldo)

        else:
            print("Conta não encontrada")

    #somar o saldo com o deposito feito          
    elif opcoes == "3":
        numero_contas = int(input("Digite o número da conta: "))

        if numero_contas in contas:
            deposito = float(input("Quanto deseja depositar: "))
            contas[numero_contas]["Saldo"] += deposito
            print("Deposito feito com sucesso!")

        else:
            print("Conta não encontrada")

    #subtrair do saldo o valor do saque    
    elif opcoes == "4":
        numero_contas = int(input("Digite o número da conta: "))

        if numero_contas in contas:
            saque = float(input("Quanto deseja sacar: "))
            if contas[numero_contas]["Saldo"] >= saque:
                contas[numero_contas]["Saldo"] -= saque
                print("Saque realizado com sucesso!")

            else:
                print("Saldo insuficiente")

        else:
            print("Conta não encontrada")

    #fechar o programa    
    elif opcoes == "5":
        print("Programa encerrado, obrigado!")
        break

    else:
        print("Selecione uma opção valida")