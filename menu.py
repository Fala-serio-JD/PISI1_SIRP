import time
from utils import divisoria_grossa, cabecalho, limpar_stdin

def tela_menu():  #Comportamento estranho: necessário inserir duas vezes o número da tela de preferência do usuário (e se os valores dados forem diferentes?).
    cabecalho()
    print(f"\n{divisoria_grossa()} MENU {divisoria_grossa()}")
    print("\n(1) Ver problemas | (2) Reportar Problema | (3) Perfil | (4) Sair")

    limpar_stdin()
    opcao = input("Digite o número correspondente à tela desejada: ")
    return opcao

