from utils import limpar_tela, logo
from validacoes import validacao_acesso

def tela_login(usuarios):

    tentativas = 0
    usar_nome = False

    while True:         #Ver se usar nome funciona.
        limpar_tela()
        print(f"{logo()}\nPreencha os dados de login:")

        if usar_nome:
            usuario = input("Nome completo: ").strip().lower()  #Mescla nome completo e email.
        else:
            usuario = input("Email: ").strip().lower()

        senha = input("Senha: ")

        sucesso = validacao_acesso(
            usuarios, usuario, senha, usar_nome #conferir se num_contato vai dar problema.
        )

        if sucesso:
            break

        tentativas += 1

        if tentativas == 1:
            limpar_tela()
            print("""Usuário ou senha incorreto.\nVocê pode usar seu nome completo no lugar do email.""")
            escolha = input("Deseja usar nome? (sim/não): ").lower()

            if escolha == "sim":
                usar_nome = True