import sqlite3
import hashlib
import getpass


def cpf_save():
     cpf_salvo = vcpf
     return cpf_salvo

def user_log():# função principal
     global vcpf

     def user_login(vcpf, vsenha):
          conn = sqlite3.connect("projectdb.db")
          cursor = conn.cursor()
               
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

     t = 3 # number of tries to login 
     while t > 0: 
          vcpf = input("CPF: ")
          vsenha = getpass.getpass("Senha: ")
          
          if user_login(vcpf, vsenha):
               print(f"Login bem-sucedido!")
               break
          else:
               t -= 1 
               print(f"CPF ou senha incorretos. Tente novamente. Restam {t} tentativas")
          
          if t == 0:
               print("Você excedeu o número de tentativas permitidas. Tente novamente mais tarde.")
               quit()
     #Fechar conexão



