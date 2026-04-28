import time
from utils import limpar_tela, divisoria, divisoria_grossa, cabecalho, limpar_stdin
import banco_dados_problemas

def listar_problemas():
    cabecalho()
    print("=== FEED DE PROBLEMAS RURALINDA ===")
    for problema in banco_dados_problemas.feed_de_problemas:
        print(f"{problema['id_problema']} - {problema['titulo']} [{problema['area']}]")
    escolher_problema()


def escolher_problema():
    while True:
        limpar_stdin()
        id_problema = input("Digite o número para ler detalhes ou '0' para voltar: ")
        if id_problema != '0':

            try:
                limpar_tela()
                problema = banco_dados_problemas.feed_de_problemas[(int(id_problema)) - 1]    
                print(f""" --- DETALHES DO PROBLEMA #{problema["id_problema"]} ---
                      \nTÍTULO: {problema["titulo"]}
                      \nDESCRIÇÃO: {problema["descrição"]}
                      \nAUTOR: {problema["autor"]}
                      \nCONTATO: {problema["contato"]} 
                      \n{divisoria()}""")
                time.sleep(12)  # Remover o limite de tempo e,quando o usuário quiser voltar, pressionar 0. 
                listar_problemas()
                
            except IndexError:
                print("Esse problema não existe!")

        elif id_problema == '0': 
            cabecalho()
            print("Retornando para o Menu...")
            time.sleep(2)
            break

        else:
            print("Insira um valor válido.")


def reportar_novo_problema(usuarios, nome, email):
    cabecalho()

    print(f"\n{divisoria_grossa()} REPORTADOR DE PROBLEMA {divisoria_grossa()}\n")

    limpar_stdin()
    while len(titulo) == 0 or len(titulo) > 100:    # Recomenda-se tranferir essa validação para validacoes --> ver se vai ficar recursivo demais
        titulo = input("Título curto (até 100 caracteres): ")

        if len(titulo) > 0 and len(titulo)<= 100:
            print("Título válido")

        elif len(titulo) == 0: 
            print("Você deve escrever um título.")

        else: print(f"Máximo de 100 caracteres. Excedeu {len(titulo) - 100}.")
        limpar_stdin()

    limpar_stdin()
    descricao = input("Descreva o problema (até 1000 caracteres): ")

    while len(descricao) == 0 or len(descricao) > 1000:
        print("Descrição inválida.")
        limpar_stdin()
        descricao = input("Descreva o problema: ")

    limpar_stdin()
    area = input("Área do problema: ")

    novo_id_problema = len(banco_dados_problemas.feed_de_problemas) + 1
    novo_problema = {
        "id_problema": novo_id_problema,
        "titulo": titulo,
        "descrição": descricao,
        "autor": nome,
        "area": area,
        "contato": email
    }

    banco_dados_problemas.feed_de_problemas.append(novo_problema)
    print(f"\nProblema #{novo_id_problema} publicado com sucesso!")
    time.sleep(4)

