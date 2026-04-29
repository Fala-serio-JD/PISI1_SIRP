import time
from utils import cabecalho, divisoria, limpar_tela, limpar_stdin
from validacoes import nome_valido, contato_valido, senha_valida, email_valido

def gerir_usuario(usuarios, email):
    id_usuario = None
    for id_busca, dados in usuarios.items():
        if dados['email'] == email:
            id_usuario = id_busca
            break

    while True:
        limpar_tela()
        cabecalho()
        
        print(f"--- DADOS ATUAIS ---")
        print(f"Nome:    {usuarios[id_usuario]['nome']}")
        print(f"Contato: {usuarios[id_usuario]['num_contato']}")
        print(f"Senha:   {usuarios[id_usuario]['senha']}")
        print(f"Email:   {usuarios[id_usuario]['email']}")
        divisoria()

        print(f"\n--- O QUE DESEJA ALTERAR? ---")
        print("1 | Nome")
        print("2 | Contato")
        print("3 | Senha")
        print("4 | Email")
        print("5 | Sair")
        opcao = input("\nSelecione uma opção: ").strip()

        if opcao == '1':
            novo = input("Novo nome: ")
            valido, erro = nome_valido(novo)
            if valido:
                usuarios[id_usuario]['nome'] = novo
                print("Nome atualizado!")
            else:
                print(f"Erro: {erro}")
            time.sleep(1.5)

        elif opcao == '2':
            novo = input("Novo contato: ")
            valido, erro = contato_valido(novo)
            if valido:
                usuarios[id_usuario]['num_contato'] = novo
                print("Contato atualizado!")
            else:
                print(f"Erro: {erro}")
            time.sleep(1.5)

        elif opcao == '3':
            nova = input("Nova senha: ")
            valido, erro = senha_valida(nova)
            if valido:
                usuarios[id_usuario]['senha'] = nova
                print("Senha atualizada!")
            else:
                print(f"Erro: {erro}")
            time.sleep(1.5)

        elif opcao == '4':
            novo_email = input("Novo email institucional: ").strip().lower()
            
            
            valido, erro = email_valido(novo_email, usuarios)
            
            if valido:
                usuarios[id_usuario]['email'] = novo_email
                email = novo_email 
                print("Email atualizado com sucesso!")
            else:
                print(f"Erro: {erro}")
            time.sleep(2)

        elif opcao == '5':
            print("Saindo da gestão de perfil...")
            return usuarios[id_usuario]

def tela_perfil(usuarios, nome, email, num_contato):
    cabecalho()
    print("Acessando área de edição de dados do usuário...")
    time.sleep(1)
    return gerir_usuario(usuarios, email)
