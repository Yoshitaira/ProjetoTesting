import sqlite3
from tabulate import tabulate

def consultauseradm():

    conn = sqlite3.connect("projectdb.db")
    cursor = conn.cursor()

    print("CONSULTA DE USUÁRIOS")

    cursor.execute("SELECT * FROM user")
    rs = cursor.fetchall()
    headers = ["CPF", "EMAIL", "NOME", "SENHA", "AUTHS"]
    print(tabulate(rs, headers = headers, tablefmt="psql"))

    def filtrar_cpf():

        vcpf = input("CPF: ")
        cursor.execute("SELECT * FROM user WHERE CPF =?", (vcpf,))
        rs = cursor.fetchall()
        headers = ["CPF", "EMAIL", "NOME", "SENHA", "AUTHS"]
        print(tabulate(rs, headers = headers, tablefmt="psql"))
        

    def filtrar_email():

        vemail = input("EMAIL: ")
        cursor.execute("SELECT * FROM user WHERE EMAIL =?", (vemail,))
        rs = cursor.fetchall()
        headers = ["CPF", "EMAIL", "NOME", "SENHA", "AUTHS"]
        print(tabulate(rs, headers = headers, tablefmt="psql"))
    
    def filtrar_nome():

        vnome = input("NOME: ")
        cursor.execute("SELECT * FROM user WHERE NOME =?", (vnome,))
        rs = cursor.fetchall()
        headers = ["CPF", "EMAIL", "NOME", "SENHA", "AUTHS"]
        print(tabulate(rs, headers = headers, tablefmt="psql"))
    
    def filtrar_auth():

        vauth = input("AUTHS: ")
        cursor.execute("SELECT * FROM user WHERE AUTORIZAÇÃO =?", (vauth,))
        rs = cursor.fetchall()
        headers = ["CPF", "EMAIL", "NOME", "SENHA", "AUTHS"]
        print(tabulate(rs, headers = headers, tablefmt="psql"))

    print("ESCOLHA UM FILTRO PARA CONSULTAR")
    print("1 - CPF")
    print("2 - EMAIL")
    print("3 - NOME")
    print("4 - AUTH")
    print("0- Voltar")
    opcaofilter = int(input("Digite a opção desejada: "))

    if opcaofilter == 1:
        filtrar_cpf()

    elif opcaofilter == 2:
        filtrar_email()
    
    elif opcaofilter == 3:
        filtrar_nome()
    
    elif opcaofilter == 4:
        filtrar_auth()
    
    else:
        quit()
    

    conn.close()