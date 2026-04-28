import time
from utils import divisoria_grossa, cabecalho

def tela_menu(usuarios, nome):  #Comportamento estranho: necessário inserir duas vezes o número da tela de preferência do usuário (e se os valores dados forem diferentes?).
    cabecalho(usuarios, nome)

    print(f"\n{divisoria_grossa()} MENU {divisoria_grossa()}")
    print("\n(1) Ver problemas | (2) Reportar Problema | (3) Perfil | (4) Sair")

    opcao = input("Digite o número correspondente à tela desejada: ")
    return opcao

