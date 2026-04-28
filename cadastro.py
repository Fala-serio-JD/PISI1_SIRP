import time
from utils import limpar_tela, logo, parametros_cadastro
from validacoes import nome_valido, email_valido, contato_valido, senha_valida

def tela_cadastro(usuarios):
    limpar_tela()
    print(f"{logo()}\nBem vindo ao cadastro! Por favor, atente-se aos parâmetros de validade de cada campo. {parametros_cadastro()}")

    while True:
        nome = input("\nNome completo: ")
        valido, erro = nome_valido(nome)

        if valido:
            print("Nome válido!")
            time.sleep(2)
            break
        else:
            print(f"Erro: {erro}")
            time.sleep(2)

    while True:
        email = input("\nEmail institucional: ")
        valido, erro = email_valido(email, usuarios)

        if valido:
            print("Email válido!")
            time.sleep(2)
            break
        else:
            print(f"Erro: {erro}")
            time.sleep(2)

    while True:
        num_contato = input("\nNúmero de contato: ")
        valido, erro = contato_valido(num_contato)

        if valido:
            print("Número de contato válido!")
            time.sleep(2)
            break
        else:
            print(f"Erro: {erro}")
            time.sleep(2)

    while True:     #Dá pra usar o getpass no campo senha
        senha = input("\nSenha: ")
        valido, erro = senha_valida(senha)

        if valido:
            print("Senha válida!")
            time.sleep(2)
            break
        else:
            print(f"Erro: {erro}")
            time.sleep(2)

    return nome, email, num_contato, senha

