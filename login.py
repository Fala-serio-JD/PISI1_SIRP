import time
from utils import limpar_tela, limpar_stdin, cabecalho
from validacoes import validacao_acesso

def tela_login(usuarios):
    """Interface CLI dedicada ao login do usuário
    
    Returns:
        dict: O dicionário do usuário logado (u)
    """
    while True:
        cabecalho()
        print("Preencha os dados de login:")

        limpar_stdin()
        usuario_input = input("Email ou nome completo: ").strip().lower()

        limpar_stdin()
        senha_input = input("Senha: ")

        # validacao_acesso agora retorna o dicionário do usuário ou False
        sucesso = validacao_acesso(usuarios, usuario_input, senha_input)

        if sucesso:
            # Retorna o dicionário para que o index possa usar nome, email, etc.
            return sucesso 
        else:
            limpar_tela()
            print("Usuário ou senha incorreto. Preencha os campos novamente.")
            time.sleep(3)
