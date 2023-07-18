import re

class Usuario:
    def __init__(self, nome, idade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email

def criar_usuario():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cpf = input("Digite seu CPF: ")
    email = input("Digite seu Email: ")

    if not verificar_email(email):
        print("Email inválido. Por favor, digite um email valido!")
        return None
    
    usuario = Usuario(nome, idade, cpf, email)
    return usuario

def verificar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if(re.match(padrao,email)):
        return True
    
    else: 
        return False

def mostrar_usuarios(usuario):
    print("Nome: ", usuario.nome)
    print("Idade: ", usuario.idade)
    print("CPF: ", usuario.cpf)
    print("Email: ", usuario.email)

lista_usuarios = []

while True:
    opcao = input("Deseja realizar um cadastro? (S/N): ")

    if opcao.upper() == "S":
        novo_usuario = criar_usuario()

        if novo_usuario is not None:
            lista_usuarios.append(novo_usuario)
            print("Cadastro realizado com sucesso!")
        else: 
            print("Ocorreu um erro. Tente novamente!")

    elif opcao.upper() == "N":
        break
    
    else:
        print("Selecione uma opção válida!")

print("Usuarios cadastrador: ")
for usuarios in lista_usuarios:
    mostrar_usuarios(usuarios)
    print()