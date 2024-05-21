import sqlite3

# Obter dados  
def cadprod():
     # Conexão com SGDB
     conn = sqlite3.connect("projectdb.db")
     cursor = conn.cursor()

     #Gerar ID
     def generate_unique_id():

          counter = 1
          generated_ids = set()
          
          formatted_ID = f"{counter:04d}"
          counter += 1

          while formatted_ID in generated_ids:
               formatted_ID = f"{counter:04d}"
               counter += 1

               generated_ids.add(formatted_ID)
               return int(formatted_ID)
                    
     #verifica se o email é válido
     def verificar_produto(vprod):
          if all((c.isalpha() or c.isspace()) for c in vprod) and  len(vprod) > 0:
               return vprod
          else:
               return False

     #verificar se o nome contém apenas letras
     def verificar_sabor(vsabor):
          if all((c.isalpha() or c.isspace()) for c in vsabor) and  len(vsabor) > 0:
               return vsabor
          else:
               return None

     #verificar senha e criptografa
     def verificar_preco(vpreco):
     #verifica se a senha contém pelo menos 1 caracter de cada
          try:
               preco = float(vpreco)
               return preco
          except ValueError:
               return None
     #########################################################################################

     while True:
          print("CADASTRAR PRODUTO!")
          vID = generate_unique_id()
     #input produto
          while True:
               vprod = input("Categoria: ")
               if verificar_produto(vprod):
                    break
               else:
                    print("Certifique-se de digitar apenas letras e não deixe vazio.")

     #input sabor
          while True:
               vsabor = input("Sabor: ")
               if verificar_sabor(vsabor):
                    break
               else:
                    print("Certifique-se de digitar apenas letras e não deixe vazio.")

     #input preço
          while True:
               vpreco = float(input("Preço: "))
               preco = verificar_preco(vpreco)
               if preco is not None:
                    break
               else:
                    print("Certifique-se de digitar apenas números e não deixe vazio.")

          while True:
               vqtd = input("Quantidade: ")
               try:
                    qtd = int(vqtd)
                    if qtd > 0:
                         break
                    else:
                         print("Quantidade deve ser maior que zero.")
               except ValueError:
                    print("Certifique-se de digitar apenas números.")

          print("Produto cadstrado com sucesso!")

          conn.execute("INSERT INTO products VALUES (?, ?, ?, ?, ?)", (vID, vprod, vsabor, vpreco, vqtd))
          conn.commit()

          vcontinuar = input(" X FINALIZA o processo OU TECLA ENTER para CONTINUAR: ")
          if vcontinuar.upper() != '':
               break
     
     ## fechar conexão
     conn.close()
     quit()
