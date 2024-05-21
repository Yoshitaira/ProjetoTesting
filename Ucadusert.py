import sqlite3
from email_validator import validate_email, EmailNotValidError
import hashlib
import binascii
from Principalt import *


def cad_user():#função principal
    conn = sqlite3.connect("projectdb.db")

    print("Cadastre seu usuário")
#verifica se o CPF tem apenas números
    def  verificar_cpf(vcpf):
        if vcpf.isdigit() and len(vcpf) == 11:
            return True
        else:
            return False
        
    #verifica se o email é válido
    def verificar_email(vemail):
        try:
            #Valida o email usando a função validate_email
            valid = validate_email(vemail)
            return True
        except EmailNotValidError as e:
            #Captura a exceção EmailNotValidError caso o email não seja válido
            print(str(e))
            return False

    #verificar se o nome contém apenas letras
    def verificar_nome(vnome):
        if all((c.isalpha() or c.isspace()) for c in vnome) and  len(vnome) > 0:
            return True
        else:
            return False

    #verificar senha e criptografa
    def verificar_senha(vsenha):
        #verifica se a senha contém pelo menos 1 caracter de cada
        letter = any(c.isalpha() for c in vsenha)
        number = any(c.isdigit() for c in vsenha)
        spchar = any(c in "!@#$%&*?" for c in vsenha)
        lenght = len(vsenha) <= 18
        
        return letter and number and spchar and lenght

    def cript_pass(vsenha):

        if verificar_senha(vsenha):
            hasher = hashlib.sha256()
            hasher.update(vsenha.encode('utf-8'))
            senha_hash = hasher.digest()
            vsenhacrip = binascii.hexlify(senha_hash)
            return vsenhacrip
            
    ##########################################################################################################

    #input do CPF 
    while True:
        vcpf = cad_cpf.get()

        if verificar_cpf(vcpf):
            print("CPF válido.")
            break
        else:
            print("CPF inválido. Certifique-se de digitar apenas números e que o CPF tenha 11 dígitos.")

    #input email
    while True:
        vemail = input("Digite o email: ")
        if verificar_email(vemail):
            print("Email válido.")
            break
        else:
            print("Email inválido. Tente novamente.")

    #input nome
    while True:
        vnome = input("NOME: ")
        if verificar_nome(vnome):
            print("Nome válido.")
            break
        else:
            print("Nome inválido. Certifique-se de digitar apenas letras e não deixe vazio.")

    #input senha
    while True:
        print("LEMBRE-SE! A senha deve conter ao menos um caracter especial, um número e letras!")
        vsenha = input("SENHA: ")
        sec = input("REPITA A SENHA: ")
        
        if vsenha == sec and verificar_senha(vsenha):
            vsenhacrip = cript_pass(vsenha)
            print("Cadastrado com sucesso!")
            break
        else:
            print("Senha inválida. Tente novamente!")

    aunthenticate = 2 
    # enviar instrução sql para ser executada pelo banco
    conn.execute("insert into user values (?, ?, ?, ?, ?)", (vcpf, vemail, vnome, vsenhacrip, aunthenticate))
    conn.commit()  
    ## fechar conexão

    conn.close()
    












