import sqlite3   # Biblioteca do sqlite
from tabulate import tabulate

def excprod():

    conn = sqlite3.connect("projectdb.db")
    cursor = conn.cursor()
    print("CUIDADO A AÇÃO EXECUTADA É IRREVERSÍVEL")

    cursor.execute("SELECT * FROM products")
    productos = cursor.fetchall()

    # colocar as informações em forma de tabela 
    print("Catálogo de produtos")
    headers = ["ID","CATEGORIA", "SABOR", "PRECO", "QUANTIDADE"]
    print(tabulate(productos, headers = headers))

    print("Digite o ID do produto que deseja EXCLUIR")
    product_id = input("ID: ")

    cursor.execute("SELECT * FROM products WHERE ID=?", (product_id,))
    rs = cursor.fetchone()
        
    if rs[0] > 0:
        print ("PRODUTO LOCALIZADO!")
        print ("ID: ", rs[0])
        print ("CATEGORIA: ", rs[1])
        print ("SABOR: ", rs[2])
        print("PREÇO: ", rs[3])
        print ("QUANTIDADE: ", rs[4])

        vconfirma = input("Confirma a EXCLUSÃO deste produto? (S/N): ")

        if vconfirma.upper() == "S":
                    # Enviar instrução SQL para ser executada
            cursor.execute("DELETE FROM products WHERE ID = ?", (product_id,))
            conn.commit()
            print("PRODUTO EXCLUÍDO COM SUCESSO!")
        else:
            print("Exlcusão cancelada.")
    else:
        print("Este produto não existe no catálogo.")
            
    vcontinuar = input("Deseja excluir mais algum produto? (S/N): ")

    if vcontinuar.upper() == "N":
    # Fechar conexão
        conn.close
        quit()