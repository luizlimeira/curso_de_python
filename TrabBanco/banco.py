from funçõesbanco import *

while True:
    print("Selecione uma opção: ")
    print("1-Criar conta")
    print("2-Verificar saldo")
    print("3-Depositar dinheiro")
    print("4-Sacar dinheiro")
    print("5-Encerrar")
        
    opcoes = str(input("Opção: "))

    if opcoes == "1":
        conta()
    elif opcoes == "2":
        saldo()
    elif opcoes == "3":
        deposito()
    elif opcoes == "4":
        saque()
    elif opcoes == "5":
        encerrar()
        break
    else:
        print("Opção Inválida, tente novamente")