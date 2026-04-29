import time

from utils import limpar_tela, divisoria, divisoria_grossa, cabecalho, limpar_stdin, submeter_descricao, submeter_titulo
import banco_dados_problemas

def listar_problemas():
    """Interface CLI principal do feed."""
    while True:
        cabecalho()
        print("=== FEED DE PROBLEMAS RURALINDA ===")
        for problema in banco_dados_problemas.feed_de_problemas:
            print(f"{problema['id_problema']} - {problema['titulo']} [{problema['area']}]")

        if not escolher_problema():
            break

def escolher_problema():
    """Retorna True para continuar no feed ou False para sair."""
    limpar_stdin()
    id_input = input("Digite o número para ler detalhes ou '0' para voltar: ")

    if id_input == '0':
        print("Retornando para o Menu...")
        time.sleep(2)
        return False

    try:
        indice = int(id_input) - 1
        problema = banco_dados_problemas.feed_de_problemas[indice]
        
        limpar_tela()
        print(f""" --- DETALHES DO PROBLEMA #{problema["id_problema"]} ---
\nTÍTULO: {problema["titulo"]}
\nDESCRIÇÃO: {problema["descrição"]}
\nAUTOR: {problema["autor"]}
\nCONTATO: {problema["contato"]} 
\n{divisoria()}""")
        
        input("\nPressione ENTER para voltar ao feed.")
        return True

    except (ValueError, IndexError):
        print("Selecione um problema existente! Tente novamente.")
        time.sleep(2)
        return True


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

