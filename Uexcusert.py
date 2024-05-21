import sqlite3   # Biblioteca do sqlite
import getpass
import hashlib
from Uloginusert import *

def excluir_user():

    conn = sqlite3.connect("projectdb.db")
    cursor = conn.cursor()

    def user_login(vcpf, vsenha):

        cursor.execute("SELECT SENHA FROM user WHERE CPF = ?", (vcpf,))
        rs = cursor.fetchone()

        if rs is None:
            return False
        #cirptografia armazenada no cadastro     
        vs_crip_arm = rs[0]

        #criptografia atual
        hasher = hashlib.sha256()
        hasher.update(vsenha.encode('utf-8'))
        vs_crip_forn = hasher.hexdigest()
        
        if str(vs_crip_arm.decode('utf-8')) == vs_crip_forn:
            return True
        else: 
            return False
        
    vcpf = cpf_save()
    cursor.execute("SELECT count(*), EMAIL, NOME, AUTORIZAÇÃO FROM user WHERE CPF = ?", (vcpf,))
    rs = cursor.fetchone()

    if rs[0] > 0:
        print ("Usuário localizado")
        print ("Email: ", rs[1])
        print ("Nome: ", rs[2])
        vconfirma = input("Confirma a exclusão deste usuário? (S/N)")

        if vconfirma.upper() == "S":
            print("QUAL A SENHA DO USUÁRIO QUE DESEJA EXCLUIR?")

            vsenha = getpass.getpass("Senha: ")

            if user_login(vcpf, vsenha):
            # Enviar instrução SQL para ser executada
                conn.execute("DELETE FROM user WHERE CPF = " + vcpf)
                conn.commit()
                print("USUÁRIO EXCLUÍDO COM SUCESSO!")
            

        else:
            print("VOCÊ NÃO PODE EXCLUIR ESTE USUÀRIO!")


    # Fechar conexão
    conn.close