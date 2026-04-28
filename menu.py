from utils import divisoria_grossa, cabecalho, limpar_stdin

def tela_menu():
    """Interface CLI dedicada à exibição do menu de ação do usuário para 
    
    Returns:
        str: opcao.
    """
    cabecalho()
    print(f"\n{divisoria_grossa()} MENU {divisoria_grossa()}")
    print("\n(1) Ver problemas | (2) Reportar Problema | (3) Perfil | (4) Sair")

    limpar_stdin()
    opcao = input("Digite o número correspondente à tela desejada: ")
    return opcao

