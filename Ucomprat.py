import sqlite3
from indext import menu_user
from tabulate import tabulate

def shopcart():# função carrinho de compras
    cart = []

    conn = sqlite3.connect("projectdb.db")
    cursor = conn.cursor()

    while True:# menu do carrinho
        print("CARRINHO")
        print("1 - Ver catálogo de produtos")
        print("2 - Adionar itens ao carrinho")
        print("3 - Finalizar compra")
        print("0 - Voltar ao menu anterior")

        vescolha = int(input("O que deseja fazer? "))

        if vescolha == 1: # Adicionar produto
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()# mostra o catálogo de produtos para o cliente

            print("Catálogo de produtos")
            headers = ["ID","CATEGORIA", "PRODUTO", "PRECO", "QUANTIDADE"]
            print(tabulate(products, headers = headers))
            
            
        elif vescolha == 2: # Remover produto
            product_id = int(input("Digite o ID do produto:"))
            quantity = int(input("Digite a quantidade: "))

            cursor.execute("SELECT * FROM products WHERE ID=?", (product_id,))
            product = cursor.fetchone()

            if product and product[4] >= quantity:
                cart.append((product_id, quantity))
                print(f"Adicionado {quantity} {product[1]} no carrinho.")

                new_quantity = product[4] - quantity
                cursor.execute("UPDATE products SET QUANTIDADE=? WHERE ID=?", (new_quantity, product_id))
            else:
                print("Produto não encontrado ou quantidade insuficiente.")
        
        elif vescolha == 3: # Finalizar compra
            total_cost = 0

            for item in cart:
                cursor.execute("SELECT PRECO FROM products WHERE ID=?", (item[0],))
                price = cursor.fetchone()

                total_cost += price[0] * item[1]

            print(f"Custo da compra: R${total_cost}")
            break
        
        elif vescolha == 0: # Sair
            print("Obrigado por comprar, volte sempre!")
            menu_user()
        else:
            print("Opção inválida")
    cart.clear()
    
    conn.commit()
    conn.close()

        
