import time
from utils import limpar_tela, divisoria, divisoria_grossa, cabecalho
import banco_dados_problemas

def listar_problemas():
    print("=== FEED DE PROBLEMAS RURALINDA ===")
    for problema in banco_dados_problemas.feed_de_problemas:
        print(f"{problema['id_problema']} - {problema['titulo']} [{problema['area']}]")
    escolher_problema()

def escolher_problema():
    while True:
        id_problema = input("\nDigite o número para ler detalhes (ou '0' para voltar): ")
        if id_problema != '0':

            try:
                limpar_tela()
                listar_problemas()
                problema = banco_dados_problemas.feed_de_problemas[(int(id_problema)) - 1]    
                print(f"""\n --- DETALHES DO PROBLEMA #{problema['id_problema']} ---
                    \nTÍTULO: {problema['titulo']}
                    \nDESCRIÇÃO: {problema['descrição']}
                    \nAUTOR: {problema['autor']}
                    \nCONTATO: {problema['contato']} 
                    \n{divisoria()}""")
                
            except IndexError:
                print("Esse problema não existe!")

        elif id_problema == '0': 
            limpar_tela()
            print("Retornando para o Menu...")
            time.sleep(2)
            break

        else:
            print("Insira um valor válido. Tente novamente.")


def reportar_novo_problema(nome, email):
    limpar_tela()

    print(f"\n{divisoria_grossa()} REPORTADOR DE PROBLEMA {divisoria_grossa()}\n")

    titulo = input("Título curto (até 100 caracteres): ")

    while len(titulo) == 0 or len(titulo) > 100:
        if len(titulo) == 0:
            print("Você deve escrever um título.")
        else:
            print(f"Máximo de 100 caracteres. Excedeu {len(titulo) - 100}.")
        titulo = input("Título curto: ")

    descricao = input("Descreva o problema (até 1000 caracteres): ")

    while len(descricao) == 0 or len(descricao) > 1000:
        print("Descrição inválida.")
        descricao = input("Descreva o problema: ")

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

    print(f"\n✅ Problema #{novo_id_problema} publicado com sucesso!")
    time.sleep(4)

