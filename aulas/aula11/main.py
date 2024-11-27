from Pessoa import *
import os
def limpar(): os.system('clear')

limpar()
def pergunta():
    res = int(input("deseja cadastrar uma nova pessoa? 1 - SIM ou 0 - NÂO: \n"))
    return res

cadastro = []

def cadastrar():
    res = pergunta()
    while(res == 1):
        nome = str(input("Digite o nome da pessoa: \n"))
        idade = int(input("Digite a idade da pessoa: \n"))
        cargo = str(input("Digite o cargo da pessoa: \n"))
        salario = float(input("Digite o salario da pessoa: \n"))

        cadastro.append(Pessoa(nome,idade,cargo,salario))
        res = pergunta()



def mostrar():
    print("{:<4}{:<10}{:<7}{:<10}{:<7}"
          .format("N°", "Nome", "Idade", "Cargo", "Salário"))
    y = 1
    for x in cadastro:
        print("{:<4}{:<10}{:<7}{:<10}{:<7}"
              .format (y,
                       x.get_nome(),
                       x.get_idade(),
                       x.get_cargo(),
                       x.get_salario()))
        y+=1


def alterar():
    mostrar()
    linha = int(input("Digite a linha que deseja alterar: \n"))
    linha -=1
    opcao = int(input("Escolha as opções: \n1 - nome\n2- idade\n3 - cargo\n4 - Salário\n"))
    if (opcao == 1):
        nome = str(input("Digite o novo nome: \n"))
        cadastro[linha].set_nome(nome)
    elif (opcao == 2):
        idade = int(input("Digite a nova idade: \n"))
        cadastro[linha].set_idade(idade)
    elif (opcao == 3):
        cargo = str(input("Digite o novo cargo: \n"))
        cadastro[linha].set_cargo(cargo)
    elif (opcao == 4):
        salario = float(input("Digite o novo salario: \n"))
        cadastro[linha].set_salario(salario)
    else:
        print("Valor Incorreto!")
        alterar()
    mostrar()

def remover():
    linha = int(input("Digite a linha que deseja deletar: \n"))
    linha -=1
    res = int(input("Certeza que deseja remover a linha {linha}?\n1 - SIM\n2 - NÃO\n"))
    if (res == 1):
        cadastro.pop(linha)

    mostrar()

def menu():
    men = int(input("\n1 - Cadastro\n2 - Alterar\n3 - Remover\n4 - Mostrar\n"))
    if (men == 1):
        cadastrar()
        mostrar()
        menu()
    elif(men == 2):
        alterar()
        menu()
    elif(men == 3):
        mostrar()
        remover()
        mostrar()
        menu()
    elif(men == 4):
        mostrar()
        menu()
    else:
        print("Opção invalida!")

menu()








