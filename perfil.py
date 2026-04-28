import time
from utils import cabecalho, divisoria

def gerir_usuario(usuarios, nome, email, num_contato):
    """Função dedicada à leitura, atualização e deleção das informações cadastrais de usuário."""
    print(f"Nome: {nome}\nEmail: {email}\nNúmero de contato: {num_contato}") 

def tela_perfil(usuarios, nome, email, num_contato):
    """Interface CLI dedica à exibição e manipulação do CRUD do usuário."""
    cabecalho()
    print("Bem vindo ao perfil! Sinta-se livre para gerir os seus dados pessoais e os seus problemas!")
    time.sleep(3)

    gerir_usuario(usuarios, nome, email, num_contato)
    divisoria()
    time.sleep(6)