import sqlite3
import hashlib
import getpass
import binascii
from email_validator import validate_email, EmailNotValidError
from tabulate import tabulate

def altuseradm():
    conn = sqlite3.connect("projectdb.db")
    cursor = conn.cursor()
    
    # lista dos usuários cadastrados no sistema
    cursor.execute("SELECT * FROM user")
    rs = cursor.fetchall()
    headers = ["CPF", "EMAIL", "NOME", "SENHA", "AUTHS"]
    print(tabulate(rs, headers = headers, tablefmt="psql"))
    

    # encripta a nova senha
    def criptar_novasenha(altersenha):
        #verifica se a senha contém pelo menos 1 caracter de cada
        letter = any(c.isalpha() for c in altersenha)
        number = any(c.isdigit() for c in altersenha)
        spchar = any(c in "!@#$%&*?" for c in altersenha)
        lenght = len(altersenha) <= 18
        
        return letter and number and spchar and lenght

    def cript_pass(altersenha):

        if criptar_novasenha(altersenha):
            hasher1 = hashlib.sha256()
            hasher1.update(altersenha.encode('utf-8'))
            senha_hash = hasher1.digest()
            vsenhacrip = binascii.hexlify(senha_hash)
            return vsenhacrip

    def verificar_email(alteremail):
        try:
            # Valida o email usando a função validate_email
            valid = validate_email(alteremail)
            return True
        except EmailNotValidError as e:
            # Captura a exceção EmailNotValidError caso o email não seja válido
            print(str(e))
            return False

    def verificar_nome(alternome):
        if all((c.isalpha() or c.isspace()) for c in alternome) and  len(alternome) > 0:
            return True
        else:
            return False
        
    vcpf = input("CPF: ")

    cursor.execute("SELECT count(*), CPF, EMAIL, NOME, AUTORIZAÇÃO FROM user WHERE CPF = ?", (vcpf,))
    rs = cursor.fetchone()

    if rs[0] > 0:
        print ("Usuário localizado!")
        print ("CPF: ", rs[0])
        print ("EMAIL: ", rs[1])
        print ("NOME: ", rs[2])
        
        vconfirma = input("Quer alterar este usuário? (S/N)")

        if vconfirma.upper() == "S":

            while True:
                print("O que deseja alterar? (EMAIL(E), NOME(N), SENHA(S), SAIR(X))")
                campo = input("Campo: ")

                if campo.upper() == "X": # Seleção de alteração para sair
                    break
                

                elif campo.upper() == "E": # Seleção de alteração para email
                    altermail = input("Novo email: ")
                    cursor.execute("UPDATE user SET EMAIL = ? WHERE CPF = ?", (altermail, vcpf))
                
                elif campo.upper() == "N": # Seleção de alteração para nome
                    alternome = input("Novo nome: ")
                    cursor.execute("UPDATE user SET NOME =? WHERE CPF =?", (alternome, vcpf))

                elif campo.upper() == "S": # Seleção de alteração para senha
                    print("LEMBRE-SE! A senha deve conter ao menos um caracter especial, um número e letras!")
                    altersenha = getpass.getpass("Nova senha: ")
                    vsenhacrip = cript_pass(altersenha)
                        
                    cursor.execute("UPDATE user SET SENHA =? WHERE CPF =?", (vsenhacrip, vcpf))

            # Enviar instrução SQL para ser executada
                conn.commit()
                print("DADOS ALTERADOS COM SUCESSO!")

    #Fechar conexão
    conn.close()