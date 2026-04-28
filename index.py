import time

from login import tela_login
from cadastro import tela_cadastro
from utils import limpar_tela, logo, cadastrar_usuario, logoff
from menu import tela_menu
from perfil import tela_perfil
from controle_problemas import reportar_novo_problema, listar_problemas
import banco_dados_problemas

usuarios = []

limpar_tela()
print(f"""{logo()}
Bem vindo(a)!
O SIRP dedica-se como uma rede social integrando os mais diversos saberes na resolução de problemas  de caráter interdiciplinar.

Reporte qualquer problema e encontre alguém que queira dar uma solução…
Assim promovendo a cooperação na comunidade de modo facilitado, entre aqueles que querem gerar projetos e aqueles que precisam de uma solução!

Desse jeito, nunca foi tão fácil fazer networking!
-------------------------------------------------------------------------------
""")

time.sleep(7.5)
print("Já está cadastrado?")
tem_cadastro = input("(S/N)").strip().lower()

while True:
    if tem_cadastro in ["sim", "si", "s"]:
        limpar_tela()
        print("Muito bem! Vamos prosseguir para o login...")
        time.sleep(2)
        tela_login(usuarios)
        break

    elif tem_cadastro in ["não", "nao", "na", "n"]:
        limpar_tela()
        print("Tudo bem. Vamos prosseguir para o cadastramento...")
        time.sleep(2)
        nome, email, num_contato, senha = tela_cadastro(usuarios)
        cadastrar_usuario(nome, email, senha, num_contato, usuarios)
        print("Cadastro concluído com êxito! Por favor, faça login no sistema agora.")
        tela_login(usuarios)
        break

    else:
        limpar_tela()
        time.sleep(2)
        print("Não entendi. Digite 'sim' ou 'não'.")

tela_menu(usuarios, nome)

while True:
    opcao = tela_menu(usuarios, nome)
    if opcao == '1':
        print("Você escolheu 'listar problemas'. Aguarde...")
        time.sleep(2)
        limpar_tela()
        if nome and email: listar_problemas()
        else: tela_perfil(usuarios)  

    elif opcao == '2':
        print("Você escolheu 'Reportar problema'. Aguarde...")
        time.sleep(2)
        limpar_tela()
        if nome and email: reportar_novo_problema(usuarios, nome, email)
        else: tela_perfil(usuarios)

    elif opcao == '3': 
        print("Você escolheu 'Perfil'. Aguarde...")
        time.sleep(2)
        limpar_tela()
        tela_perfil(usuarios, nome, email, num_contato)

    elif opcao == '4': 
        print("Você escolheu 'Sair'. Aguarde...")
        time.sleep(2)
        limpar_tela()
        logoff() #logoff não finaliza o código. o sistema para de rodar pois não tem mais código pra rodar.
        break

    else:print("Selecione uma opção válida!")
