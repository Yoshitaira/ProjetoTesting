import sqlite3
from tabulate import tabulate

def altprod():
    # conexão com banco de dados
    conn = sqlite3.connect("projectdb.db")
    cursor = conn.cursor()

    # trazer inforações do banco de dados
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    # colocar as informações em forma de tabela 
    print("Catálogo de produtos")
    headers = ["ID","CATEGORIA", "SABOR", "PRECO", "QUANTIDADE"]
    print(tabulate(products, headers = headers))

    print("Digite o ID do produto que deseja alterar")
    product_id = input("ID: ")

    cursor.execute("SELECT * FROM products WHERE ID=?", (product_id,))
    rs = cursor.fetchone()

    if rs[0] > 0:
        print ("Produto localizado")
        print ("CATEGORIA: ", rs[1])
        print ("SABOR: ", rs[2])
        vconfirma = input("Quer alterar este produto? (S/N)")

        if vconfirma.upper() == "S":

            while True:
                print("O que deseja alterar? (CATEGOGRIA(C), SABOR(S), PREÇO(P), QUANTIDADE(Q), SAIR(X))")
                campo = input("Campo: ")

                if campo.upper() == "X": # Seleção de alteração para sair
                    break
                
                elif campo.upper() == "C": # Seleção de alteração para email
                    altercat = input("Nova categoria: ")
                    cursor.execute("UPDATE products SET PRODUTO = ? WHERE ID = ?", (altercat, product_id))
                
                elif campo.upper() == "S": # Seleção de alteração para nome
                    altersab = input("Novo sabor: ")
                    cursor.execute("UPDATE products SET SABOR =? WHERE ID =?", (altersab, product_id))

                elif campo.upper() == "P": # Seleção de alteração para senha
                    alterpre = input("Novo preço: ")
                    cursor.execute("UPDATE products SET PRECO =? WHERE ID =?", (alterpre, product_id))

                elif campo.upper() == "Q": # Seleção de alteração para senha
                    alterqtd = input("Nova quantidade: ")
                    cursor.execute("UPDATE products SET QUANTIDADE =? WHERE ID =?", (alterqtd, product_id))

            # Enviar instrução SQL para ser executada
                conn.commit()
                print("DADOS ALTERADOS COM SUCESSO!")

    #Fechar conexão
    conn.close()