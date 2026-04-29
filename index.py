import time

from login import tela_login
from cadastro import tela_cadastro, cadastrar_usuario
from utils import limpar_tela, logoff, cabecalho , limpar_stdin, main_cabecalho
from menu import tela_menu
from perfil import tela_perfil
from controle_problemas import reportar_novo_problema, listar_problemas

usuarios = {}
usuario_logado = None

main_cabecalho()
time.sleep(1.5)
print("Já está cadastrado?")

while True:
    limpar_stdin()
    tem_cadastro = input("(S/N): ").strip().lower()

    if tem_cadastro in ["sim", "si", "s"]:
        cabecalho()
        usuario_logado = tela_login(usuarios) 
        break

    elif tem_cadastro in ["não", "nao", "na", "n"]:
        cabecalho()
        nome, email, num_contato, senha = tela_cadastro(usuarios)
        cadastrar_usuario(nome, email, senha, num_contato, usuarios)
        
        cabecalho()
        print("Cadastro concluído! Faça login agora.")
        time.sleep(2)
        usuario_logado = tela_login(usuarios) # Login após cadastro
        break
    else:
        print("Digite 'sim' ou 'não'.")

while usuario_logado:
    u_nome = usuario_logado['nome']
    u_email = usuario_logado['email']
    u_contato = usuario_logado['num_contato']

    opcao = tela_menu()
    
    if opcao == '1':
        limpar_tela()
        listar_problemas() # Se a lista for global

    elif opcao == '2':
        limpar_tela()
        reportar_novo_problema(usuarios, u_nome, u_email)

    elif opcao == '3': 
        limpar_tela()
        tela_perfil(usuarios, u_nome, u_email, u_contato)

    elif opcao == '4': 
        logoff()
        break
    else:
        print("Selecione uma opção válida!")
