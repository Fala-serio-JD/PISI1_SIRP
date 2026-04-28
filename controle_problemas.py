import time

from utils import limpar_tela, divisoria, divisoria_grossa, cabecalho, limpar_stdin, submeter_descricao, submeter_titulo
import banco_dados_problemas

def listar_problemas():
    """Interface CLI para exposição em feed dos problemas cadastrados no sistema."""
    cabecalho()
    print("=== FEED DE PROBLEMAS RURALINDA ===")
    for problema in banco_dados_problemas.feed_de_problemas:
        print(f"{problema['id_problema']} - {problema['titulo']} [{problema['area']}]")
    escolher_problema()


def escolher_problema():    #OBS: SAIR DE ESCOLHER PROBLEMA NÃO TÁ FUNCIONANDO!
    """Interface CLI para a escolha e exibição do(s) problema(s) selecionado(s) pelo usuário."""
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
                time.sleep(12)
                listar_problemas()
                
            except ValueError:
                print("Digite um número válido!")

            except IndexError:
                print("Esse problema não existe!")

        else: 
            cabecalho()
            print("Retornando para o Menu...")
            time.sleep(2)
            break

def reportar_novo_problema(usuarios, nome, email):
    """Interface CLI dedicada ao registro de novos problemas
    
    Args:
        usuarios (dicionário)
        nome (str)
        email (str)
    """
    cabecalho()
    print(f"\n{divisoria_grossa()} REPORTADOR DE PROBLEMA {divisoria_grossa()}\n")

    titulo = submeter_titulo()
    descricao = submeter_descricao()

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

