import sqlite3   # Biblioteca do sqlite
from tabulate import tabulate

def excuseradm():

    conn = sqlite3.connect("projectdb.db")
    cursor = conn.cursor()
    print("CUIDADO A AÇÃO EXECUTADA É IRREVERSÍVEL")

    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall()

    # colocar as informações em forma de tabela 
    print("Catálogo de produtos")
    headers = ["CPF", "EMAIL", "NOME", "SENHA", "AUTHS"]
    print(tabulate(users, headers = headers))

    print("Digite o CPF do usuário que deseja EXCLUIR")
    vcpf = int(input("CPF: "))

    cursor.execute("SELECT * FROM user WHERE CPF=?", (vcpf,))
    rs = cursor.fetchone()
        
    if rs[0] > 0:
        print ("PRODUTO LOCALIZADO!")
        print ("EMAIL: ", rs[1])
        print ("NOME: ", rs[2])
        print("SENHA: ", rs[3])
        print ("AUTHS: ", rs[4])

        vconfirma = input("Confirma a EXCLUSÃO deste usuário? (S/N): ")

        if vconfirma.upper() == "S":
                    # Enviar instrução SQL para ser executada
            cursor.execute("DELETE FROM user WHERE CPF = ?", (vcpf,))
            conn.commit()
            print("USUÁRIO EXCLUÍDO COM SUCESSO!")
        else:
            print("Exlcusão cancelada.")
    else:
        print("Este usuário não esta cadastrado.")
            
    vcontinuar = input("Deseja excluir mais algum usuário? (S/N): ")

    if vcontinuar.upper() == "N":
    # Fechar conexão
        conn.close
        quit()