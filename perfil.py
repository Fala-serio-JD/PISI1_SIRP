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
    time.sleep(5) #Provisório. colocar a função tela_perfil em uma estrutura while e definir um botão padrão para sair da tela

    #chamar a função feed de problemas com apenas os problemas associados ao nome do usuário. Necessário ainda criar uma estrutura para manipulação dos dados dos problemas, bem como a sua exclusão.