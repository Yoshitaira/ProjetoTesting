# scripts para usuário
from Ucadusert import *
from Uloginusert import *
from Ucomprat import *
from Ualtusert import *
from Uexcusert import *
# scripts para admin
from Aloginadmt import *
from Acadprodt import *
from Aaltprodt import *
from Aexcprodt import *
from Aconsultprodt import *
from Aaltusert import * 
from Aexcusert import *
from Aconsultusert import *

# Menu inicial do Projeto
def main_menu():# Menu Principal
    while True:
        print("1 - Cadastrar Usuário")
        print("2 - Fazer Login")
        print("3 - Sou administrador!")
        print("0 - Sair")
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1: # Cadastrar Usuário
            cad_user()
            user_log()
            menu_user()

        elif opcao == 2: # Fazer Login
            user_log()
            menu_user()

        elif opcao == 3: # Sou administrador!
            adminlog()
            menu_admin()

        elif opcao == 0: # Finalizar Programa
            print("Obrigado por utilizar nosso sistema!")
            quit()
        break
            

    return True

def menu_user():# Menu do usuário comum
    print("1 - Carrinho")
    print("2 - Alterar meus dados")
    print("3 - Excluir meu perfil")
    print("0 - LOGOFF")
    opcaouser = int(input("Digite a opção desejada: "))

    if opcaouser == 1: # Carrinho
        shopcart()
        menu_user()
    
    elif opcaouser == 2: # Alterar meus dados
        altuser()
        menu_user()

    elif opcaouser == 3: # Excluir meu perfil
        excluir_user()
        main_menu()


    elif opcaouser == 0: #
        print("Obrigado por utilizar nosso sistema!")
        main_menu()
    
# Menu para admin
def menu_admin():# menu exclusivo de administradores
    print("1 - PRODUTOS")
    print("2 - USUÁRIOS")
    print("0 - Sair")
    opcaoadm = int(input("Digite a opção desejada: "))

    if opcaoadm == 1: # Cadastrar Usuário
        products_admin()

    elif opcaoadm == 2: # Fazer Login
        users_admin()

    elif opcaoadm == 0: # Finalizar Programa
        print("Obrigado por utilizar nosso sistema!")
        main_menu()

def products_admin():# produtos para o administrador
    print("1 - Cadastrar produto")
    print("2 - Alterar produto")
    print("3 - Excluir produto")
    print("4 - Consultar produto")
    print("0 - Voltar")
    opcaoprod = int(input("Digite a opção desejada: "))

    if opcaoprod == 1: # Cadastrar produto
        cadprod()
        products_admin()
    
    elif opcaoprod == 2: # Alterar dados do produto
        altprod()
        products_admin()
    
    elif opcaoprod == 3: # Excluir produto
        excprod()
        products_admin()
    
    elif opcaoprod == 4: # Consultar produtos
        consultaprod()
        products_admin()

    else:
        opcaoprod == 0 # retorna ao menu anterior
        menu_admin()

def users_admin(): # usuários para o administrador
    print("1 - Alterar usuário")
    print("2 - Excluir usuário")
    print("3 - Consultar usuário")
    print("0 - Sair")
    opcaoSUuser = int(input("Digite a opção desejada: "))
    
    if opcaoSUuser == 1: # Alterar meus dados
        altuseradm()
        users_admin()
    
    elif opcaoSUuser == 2: # Excluir perfil
        excuseradm()
        users_admin()
    
    elif opcaoSUuser == 3: # Consultar produtos
        consultauseradm()
        users_admin()

    else:
        print("Obrigado por utilizar nosso sistema!")
        menu_admin()

if __name__ == "__main__": # incia a aplicação
    main_menu()
