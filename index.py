import time

from login import tela_login
from cadastro import tela_cadastro, cadastrar_usuario
from utils import limpar_tela, logoff, cabecalho , limpar_stdin, main_cabecalho
from menu import tela_menu
from perfil import tela_perfil
from controle_problemas import reportar_novo_problema, listar_problemas

usuarios = []
usuario_conectado = False

main_cabecalho()

time.sleep(7.5)
print("Já está cadastrado?")

while True:
    limpar_stdin()
    tem_cadastro = input("(S/N)").strip().lower()

    if tem_cadastro in ["sim", "si", "s"]:
        cabecalho()
        print("Muito bem! Vamos prosseguir para o login...")
        time.sleep(2)
        break

    elif tem_cadastro in ["não", "nao", "na", "n"]:
        cabecalho()
        print("Tudo bem. Vamos prosseguir para o cadastramento...")
        time.sleep(2)
        nome, email, num_contato, senha = tela_cadastro(usuarios)
        cadastrar_usuario(nome, email, senha, num_contato, usuarios)
        cabecalho()
        print("Cadastro concluído com êxito! Por favor, faça login no sistema agora.")
        time.sleep(2)
        usuario_conectado = tela_login(usuarios)
        time.sleep(2)
        break

    else:
        limpar_tela()
        time.sleep(2)
        print("Não entendi. Digite 'sim' ou 'não'.")

while True:
    opcao = tela_menu()
    if opcao == '1':
        print("Você escolheu 'listar problemas'. Aguarde...")
        time.sleep(2)
        limpar_tela()
        if nome and email: listar_problemas()
        else: tela_perfil(usuarios, nome, email, num_contato)  

    elif opcao == '2':
        print("Você escolheu 'Reportar problema'. Aguarde...")
        time.sleep(2)
        limpar_tela()
        if nome and email: reportar_novo_problema(usuarios, nome, email)
        else: tela_perfil(usuarios, nome, email, num_contato)

    elif opcao == '3': 
        print("Você escolheu 'Perfil'. Aguarde...")
        time.sleep(2)
        limpar_tela()
        tela_perfil(usuarios, nome, email, num_contato)

    elif opcao == '4': 
        usuario_conectado = logoff()    #ver se tá funcionando
        break

    else:print("Selecione uma opção válida!")
