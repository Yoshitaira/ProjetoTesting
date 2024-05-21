import sqlite3
import getpass
import hashlib

# Obter dados  
def adminlog():

# Conexão com SGDB
    conn = sqlite3.connect("projectdb.db")
    cursor = conn.cursor()
     
    print("NECESSÁRIO ACESSO AUTORIZADO!")

    def adm_login(vcpf, vsenha):

        cursor.execute("SELECT SENHA, AUTORIZAÇÃO FROM user WHERE CPF = ?", (vcpf,))
        rs = cursor.fetchone()

        if rs is None:
            return False
     #cirptografia armazenada no cadastro     
        vs_crip_arm = rs[0]
        vauth = rs[1]

     #criptografia atual
        hasher = hashlib.sha256()
        hasher.update(vsenha.encode('utf-8'))
        vs_crip_forn = hasher.hexdigest()

        return str(vs_crip_arm.decode('utf-8')) == vs_crip_forn and vauth == 1
        
    vcpf = input("CPF: ")
    vsenha = getpass.getpass("Senha: ")

    if adm_login(vcpf, vsenha):
        print("Login bem-sucedido!")

    else:
        print("!VOCÊ NÃO TEM AUTORIZAÇÃO PARA ACESSAR ESTÁ PÁGINA!")
        quit()

        #Fechar conexão
    conn.close()