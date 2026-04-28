import time

from utils import cabecalho, parametros_cadastro, limpar_stdin
from validacoes import nome_valido, email_valido, contato_valido, senha_valida

def tela_cadastro(usuarios):
    cabecalho()
    print(f"\nBem vindo ao cadastro! Por favor, atente-se aos parâmetros de validade de cada campo. {parametros_cadastro()}")

    while True:
        limpar_stdin()
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
        limpar_stdin()
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
        limpar_stdin()
        num_contato = input("\nNúmero de contato: ")
        valido, erro = contato_valido(num_contato)

        if valido:
            print("Número de contato válido!")
            time.sleep(2)
            break
        else:
            print(f"Erro: {erro}")
            time.sleep(2)

    while True:
        limpar_stdin()
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

id_usuario = 1
def cadastrar_usuario(nome, email, senha, num_contato, usuarios):
    global id_usuario   #Usar global é má prática.

    usuario = {
        "id": id_usuario,
        "nome": nome,
        "email": email,
        "senha": senha,
        "num_contato": num_contato
        }

    usuarios.append(usuario)
    id_usuario += 1