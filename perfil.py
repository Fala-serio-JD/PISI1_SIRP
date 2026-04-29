import time
from utils import cabecalho, divisoria, limpar_tela, divisoria_grossa
from validacoes import nome_valido, contato_valido, senha_valida, email_valido
from menu import tela_menu
from index import nome
from bancoSQL import mostrar_problemaBD, buscar_problemas_userlogBD, atualizar_coluna_problemaBD

def tela_perfil():
    cabecalho()  
    print("Bem vindo ao perfil! Sinta-se livre para gerir os seus dados pessoais e os seus problemas!")
    time.sleep(3)
    aba_perfil(nome)
    tela_menu()

def aba_perfil(usuario_logado):
    while True:
        limpar_tela()
        print(divisoria_grossa())
        print(f"           👤 PERFIL: {usuario_logado}")
        print(divisoria_grossa())
        
        print("\n--- MEUS RELATOS NO SISTEMA ---")
        meus_p = buscar_problemas_userlogBD(usuario_logado)
        
        if not meus_p:
            print("\nVocê ainda não enviou nenhum relato.")
        else:
            for p in meus_p:
                print(f"  [{p[0]:02d}] 📌 {p[1]} {p[2]}")
        
        print(f"\n{divisoria()}")
        opcao = input("\nDigite o ID para EDITAR ou '0' para VOLTAR: ")
        
        if opcao == '0':
            break
            
        try:
            id_sel = int(opcao)
            # Verifica se o problema pertence mesmo ao usuário (segurança)
            p_detalhe = mostrar_problemaBD(id_sel)
            
            if p_detalhe and p_detalhe[3] == usuario_logado: # p[3] é o autor
                limpar_tela()
                print(f"📝 EDITANDO RELATO #{id_sel:02d}")
                print(divisoria())
                print("O que você deseja alterar?")
                print("1 - Título\n2 - Descrição\n3 - Área/Setor")
                
                escolha = input("\nEscolha uma opção: ")
                
                # Mapeia a escolha para o nome real da coluna no seu banco
                mapa_colunas = {'1': 'título', '2': 'descricao', '3': 'areas'}
                
                if escolha in mapa_colunas:
                    coluna_nome = mapa_colunas[escolha]
                    novo_texto = input(f"Digite o novo conteúdo para {coluna_nome}: ")
                    
                    if atualizar_coluna_problemaBD(id_sel, coluna_nome, novo_texto):
                        print("\n✅ Atualizado com sucesso!")
                        # Mostra como ficou
                        p_atualizado = mostrar_problemaBD(id_sel)
                        print(f"\nNOVO {coluna_nome.upper()}: {p_atualizado[mapa_colunas.index(escolha)+1] if escolha == '1' else p_atualizado[2]}")
                        time.sleep(2)
                else:
                    print("Opção inválida.")
                    time.sleep(1)
            else:
                print("⚠️ ID inválido ou você não tem permissão para editar este relato.")
                time.sleep(2)
                
        except ValueError:
            print("Digite um número válido.")
            time.sleep(1)
