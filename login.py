from utils import limpar_tela, limpar_stdin, cabecalho
from validacoes import validacao_acesso

def tela_login(usuarios):
    while True:
        cabecalho()
        print("Preencha os dados de login:")

        limpar_stdin()
        usuario = input("Email ou nome completo: ").strip().lower()

        limpar_stdin()
        senha = input("Senha: ")

        sucesso = validacao_acesso(usuarios, usuario, senha)

        if sucesso:
            break
        else:
            limpar_tela()
            print("Usuário ou senha incorreto. Preencha os campos novamente.")