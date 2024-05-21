import sqlite3
from tabulate import tabulate

def consultaprod():

    conn = sqlite3.connect("projectdb.db")
    cursor = conn.cursor()

    print("CONSULTA DE PRODUTOS")

    cursor.execute("SELECT * FROM products")
    rs = cursor.fetchall()
    headers = ["ID","CATEGORIA", "SABOR", "PRECO", "QUANTIDADE"]
    print(tabulate(rs, headers = headers, tablefmt="psql"))

    def filtrar_id():

        vId = input("ID: ")
        cursor.execute("SELECT * FROM products WHERE ID =?", (vId,))
        rs = cursor.fetchall()
        headers = ["ID","CATEGORIA", "SABOR", "PRECO", "QUANTIDADE"]
        print(tabulate(rs, headers = headers, tablefmt="psql"))
        

    def filtrar_categoria():

        vcat = input("CATEGORIA: ")
        cursor.execute("SELECT * FROM products WHERE PRODUTO =?", (vcat,))
        rs = cursor.fetchall()
        headers = ["ID","CATEGORIA", "SABOR", "PRECO", "QUANTIDADE"]
        print(tabulate(rs, headers = headers, tablefmt="psql"))
    
    def filtrar_sabor():

        vsab = input("SABOR: ")
        cursor.execute("SELECT * FROM products WHERE SABOR =?", (vsab,))
        rs = cursor.fetchall()
        headers = ["ID","CATEGORIA", "SABOR", "PRECO", "QUANTIDADE"]
        print(tabulate(rs, headers = headers, tablefmt="psql"))
    
    def filtrar_preco():

        vpreco = input("PRECO: ")
        cursor.execute("SELECT * FROM products WHERE PRECO =?", (vpreco,))
        rs = cursor.fetchall()
        headers = ["ID","CATEGORIA", "SABOR", "PRECO", "QUANTIDADE"]
        print(tabulate(rs, headers = headers, tablefmt="psql"))
    
    def filtrar_quantidade():

        vquantidade = input("QUANTIDADE: ")
        cursor.execute("SELECT * FROM products WHERE QUANTIDADE =?", (vquantidade,))
        rs = cursor.fetchall()
        headers = ["ID","CATEGORIA", "SABOR", "PRECO", "QUANTIDADE"]
        print(tabulate(rs, headers = headers, tablefmt="psql"))

    print("ESCOLHA UM FILTRO PARA CONSULTAR")
    print("1 - ID")
    print("2 - CATEGORIA")
    print("3 - SABOR")
    print("4 - PRECO")
    print("5 - QUANTIDADE")
    print("0- Voltar")
    opcaofilter = int(input("Digite a opção desejada: "))

    if opcaofilter == 1:
        filtrar_id()

    elif opcaofilter == 2:
        filtrar_categoria()
    
    elif opcaofilter == 3:
        filtrar_sabor()
    
    elif opcaofilter == 4:
        filtrar_preco()

    elif opcaofilter == 5:
        filtrar_quantidade()
    
    else:
        quit()
    

    conn.close()

