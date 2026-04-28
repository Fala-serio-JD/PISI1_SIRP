import time
from utils import cabecalho, divisoria

def gerir_usuario(usuarios, nome, email, num_contato):
    print(f"Nome: {nome}\nEmail: {email}\nNúmero de contato: {num_contato}") 

def tela_perfil(usuarios, nome, email, num_contato):
    cabecalho()
    print("Bem vindo ao perfil! Sinta-se livre para gerir os seus dados pessoais e os seus problemas!")
    time.sleep(3)

    gerir_usuario(usuarios, nome, email, num_contato)
    divisoria()
    time.sleep(6)