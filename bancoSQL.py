import sqlite3
import os
from menu import tela_menu
from time import sleep
from utils import limpar_tela, divisoria, divisoria_grossa, cabecalho
caminho_atual = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(caminho_atual, "SIRP_BD.db")
banco = sqlite3.connect(caminho_db)
cursor = banco.cursor()
banco.row_factory = sqlite3.Row



#--- PROBLEMAS ------------------------------------------------------------------------------------------

def adicionar_problemaBD(titulo, descricao, autor, contato, areas):
    """
    Cria um novo relato de problema no banco de dados. Status padrão: 'EM ABERTO'.
    Args:
        titulo (str), descricao (str), autor (str), contato (str), areas (str).
    Returns:
        int/None: Retorna o número do ID gerado no banco, ou None se falhar.
    """
    tentativas = 3
    sucesso = False
    status = "EM ABERTO"

    while tentativas > 0 and not sucesso:    
        try:
            # 1. Usamos '?' para segurança (protege contra SQL Injection)
            
            sql = '''INSERT INTO problemas (título, descricao, autor, contato, areas, status) 
                     VALUES (?, ?, ?, ?, ?, ?)'''
            
            valores = titulo, descricao, autor, contato, f"[{areas}]", status
            
            cursor.execute(sql, valores)
            id = cursor.lastrowid
            banco.commit()
            print(f"Problema {id} salvo com sucesso!")
            sleep(3)
            sucesso= True
            banco.commit() # <--- O SEGREDO ESTÁ AQUI
            return id
        
        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                print("⚠️ Banco ocupado (Locked). Tentando novamente em 3s...")
                tentativas -= 1
                sleep(3)
            else:
                print(f"❌ Erro operacional: {e}")
                sleep(3)
                break
        except sqlite3.Error as erro:
            print(f"❌ Erro crítico no SQLite: {erro}")
            sleep(3)
            break

    if not sucesso:
        print("🛑 Não foi possível salvar os dados após várias tentativas.")


def mostrar_problemaBD(id_problema):
    """
    Busca todas as informações de um problema específico.
    Args:
        id_problema (int): ID do relato.
    Returns:
        dict/tupla: Os dados da linha encontrada, ou None se não existir.
    """
    tentativas = 3
    sucesso = False
    
    while tentativas > 0 and not sucesso:    
        try:
            cursor.execute("SELECT * FROM problemas WHERE id = ?", (id_problema,))
            #fetchone() pega a primeira (e única) linha encontrada
            resultado = cursor.fetchone()
            
            if resultado:
                return resultado
            else:
                print(f"⚠️ Problema com ID {id_problema} não encontrado.")
                sleep(3)
                return None

        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                print("⚠️ Banco ocupado (Locked). Tentando novamente em 3s...")
                tentativas -= 1
                sleep(3)
            else:
                print(f"❌ Erro operacional: {e}")
                sleep(3)
                break
        except sqlite3.Error as erro:
            print(f"❌ Erro crítico no SQLite: {erro}")
            sleep(3)
            break

    if not sucesso: 
        print("🛑 Não foi possível recuperar os dados.")

        
def listar_problemasBD():
    """
    Exibe o feed de problemas formatado em caixinhas, 
    puxando os dados diretamente do banco SQLite.
    """

    tentativas = 3
    sucesso = False
    cabecalho()
    while tentativas > 0 and not sucesso:    
        try:
            cursor.execute("SELECT id, título, areas FROM problemas")
            problemas = cursor.fetchall()
            
            limpar_tela()
            print(f"{divisoria_grossa()} FEED DE PROBLEMAS RURALINDA {divisoria_grossa()}")
            
            if problemas:
                for p in problemas:
                    # p[0] = id, p[1] = título, p[2] = areas
                    print(f"\n  {p[0]:02d} 📌 {p[1]}")
                    print(f"          Setor: {p[2]}") 
                    print(f"  {divisoria()}")
                
                sucesso = True
                escolher_problema()
            else:
                print("\n📭 O feed está vazio no momento.")
                print(divisoria())
                sucesso = True

        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                print(f"❌ Erro de operação: {e}")
                print("⚠️ Banco ocupado. Tentando novamente...")
                tentativas -= 1
                sleep(3)
            else:
                print(f"❌ Erro de acesso: {e}")
                sleep(3)
                break
        except sqlite3.Error as erro:
            print(f"❌ Erro no banco de dados: {erro}")
            sleep(3)
            break

    if not sucesso: 
        print("🛑 Falha ao carregar o feed. Verifique a conexão com o banco.")
        sleep(3)




def deletar_problemaBD(id_problema):
    """
    Remove permanentemente um relato de problema do banco de dados.
    Args:
        id_problema (int): O número de identificação do problema.
    Returns:
        bool: True se o problema foi deletado, False se o ID não foi encontrado.
    """
    tentativas = 3
    sucesso = False
    
    while tentativas > 0 and not sucesso:    
        try:
            cursor.execute("DELETE FROM problemas WHERE id = ?", (id_problema,))
            
            # 2. Verificamos se alguma linha foi REALMENTE afetada
            if cursor.rowcount > 0:
                banco.commit()
                sucesso = True
                print(f"✅ Problema #{id_problema} excluído com sucesso!")
                banco.commit()
                sleep(3)
            else:
                print(f"⚠️ O ID #{id_problema} não existe no banco de dados.")
                sleep(3)
                return None# Sai da função pois não há o que tentar de novo

        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                print("⚠️ Banco ocupado. Tentando novamente...")
                tentativas -= 1
                sleep(3)
            else:
                print(f"❌ Erro operacional: {e}")
                sleep(3)
                break
        except sqlite3.Error as erro:
            print(f"❌ Erro crítico: {erro}")
            sleep(3)
            break

    if not sucesso and tentativas == 0:
        print("🛑 Falha técnica: não conseguimos acessar o banco para deletar.")
        sleep(3)


def buscar_problemas_userlogBD(autor_nome):
    """Retorna todos os problemas escritos por um usuário específico."""
    try:
        # Filtramos pelo nome do autor que está logado na sessão
        cursor.execute("SELECT id, título, areas FROM problemas WHERE autor = ?", (autor_nome,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erro ao buscar seus relatos: {e}")
        return []

def atualizar_coluna_problemaBD(id_p, coluna, novo_valor):
    """Atualiza uma informação específica de um problema no banco."""
    try:
        # Usamos f-string na coluna apenas porque nomes de colunas não aceitam '?' 
        # mas como o valor vem de um menu fixo, é seguro.
        sql = f"UPDATE problemas SET {coluna} = ? WHERE id = ?"
        cursor.execute(sql, (novo_valor, id_p))
        banco.commit()
        return True
    except sqlite3.Error as e:
        print(f"Erro ao atualizar: {e}")
        return False


def escolher_problema():
    while True:
        id_problema = input("\nDigite o número para ler detalhes (ou '0' para voltar): ")
        if id_problema != '0':
            try:
                # 1. Busca o problema no banco usando o ID digitado
                p = mostrar_problemaBD(int(id_problema))
                
                if p:
                    limpar_tela()
                    # 2. Exibe os detalhes usando os índices da tupla 'p'
                    print(f"""
                            \n{divisoria_grossa()}
                            \n--- DETALHES DO PROBLEMA #{p[0]:02d} ---
                            \n{divisoria_grossa()}

                            \nTÍTULO:    {p[1]}
                            \nSETOR:     {p[5]}
                            \nSTATUS:    {p[6]}

                            \nDESCRIÇÃO: {p[2]}

                            \nAUTOR:     {p[3]}
                            \nCONTATO:   {p[4]} 

                            \n{divisoria()}""")
                    
                    input("\nPressione ENTER para voltar ao feed...")
                    limpar_tela()
                    listar_problemasBD() # Recarrega o feed para o usuário ver as opções de novo
                
            except ValueError:
                print("❌ Erro: Digite apenas números para selecionar o problema.")
                sleep(2)

        elif id_problema == '0': 
            limpar_tela()
            print("Retornando para o Menu...")
            sleep(2)
            tela_menu()
            break

        else:
            print("Insira um valor válido. Tente novamente.")


def reportar_novo_problema(nome, email):
    limpar_tela()

    print(f"\n{divisoria_grossa()} REPORTADOR DE PROBLEMA {divisoria_grossa()}\n")

    titulo = input("Título curto (até 70 caracteres): ")

    while len(titulo) == 0 or len(titulo) > 70:
        if len(titulo) == 0:
            print("Você deve escrever um título.")
        else:
            print(f"Máximo de 70 caracteres. Excedeu {len(titulo) - 70}.")
        titulo = input("Título curto: ")

    descricao = input("Descreva o problema: ")

    while len(descricao) == 0:
        print("Descrição inválida.")
        descricao = input("Descreva o problema: ")

    print(f"\n[ TECNOLOGIA, AGRÁRIA, SAÚDE, SOCIAIS, EXATAS ]")
    areas = input("Quais dessas áreas ou outra seu problema está inserido? ").upper()
    adicionar_problemaBD(titulo, descricao, nome, email, areas)
    


def mudar_status_problemaBD(id_problema, novo_status):
    """
    Altera exclusivamente a fase/status de um relato de problema.
    Status permitidos: 'EM ABERTO', 'EM DESENVOLVIMENTO', 'RESOLVIDO', 'NÃO RESOLVIDO'.
    
    Args: 
        id_problema (int): O número de identificação do problema.
        novo_status (str): O novo status em texto maiúsculo.
    Returns: 
        bool: True se atualizou, False se o ID não existir ou status for inválido.
    """
    status_permitidos = ["EM ABERTO", "EM DESENVOLVIMENTO", "RESOLVIDO", "NÃO RESOLVIDO"]
    
    if novo_status.upper() not in status_permitidos:
        print(f"🛑 Erro: '{novo_status}' não é um status válido.")
        return False

    tentativas = 3
    while tentativas > 0:
        try:
            sql = "UPDATE problemas SET status = ? WHERE id = ?"
            cursor.execute(sql, (novo_status.upper(), id_problema))
            banco.commit()
            
            if cursor.rowcount > 0:
                print(f"✅ Status do problema #{id_problema} mudou para {novo_status.upper()}!")
                return True
            return False

        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                sleep(2)
                tentativas -= 1
            else: break
    return False


def atualizar_campo_problemaBD(id_problema, atributo, novo_valor):
    """
    Altera um campo específico de um problema (ex: título, status, areas).
    Args:
        id_problema (int): ID do relato.
        atributo (str): Nome da coluna no banco.
        novo_valor (qualquer): O novo dado.
    Returns: bool: True se atualizado, False se atributo inválido ou ID não achado.
    """
    tentativas = 3
    sucesso = False
    
    colunas_permitidas = ['título', 'descricao', 'autor', 'contato', 'areas', 'status']
    if atributo not in colunas_permitidas:
        print(f"🛑 Erro: O atributo '{atributo}' não existe na tabela de problemas.")
        return False

    while tentativas > 0 and not sucesso:
        try:
            sql = f"UPDATE problemas SET {atributo} = ? WHERE id = ?"
            cursor.execute(sql, (novo_valor, id_problema))
            banco.commit()
            
            if cursor.rowcount > 0:
                print(f"✅ O campo '{atributo}' do problema #{id_problema} foi atualizado!")
                sleep(2)
                sucesso = True
                return True
            else:
                print(f"⚠️ Problema #{id_problema} não localizado.")
                sleep(2)
                return False

        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                tentativas -= 1
                sleep(3)
            else:
                break
        except sqlite3.Error as erro:
            print(f"❌ Erro crítico ao alterar problema: {erro}")
            sleep(3)
            break
            
    return False

#--USUÁRIOS-----------------------------------------------------------------------------------------



def adicionar_usuarioBD(nome, email, telefone, senha):
    """
    Cadastra um novo usuário no sistema. Por padrão, ele nasce deslogado (0).
    Args:
        nome (str), email (str - Chave Primária), telefone (str), senha (str).
    Returns:
        bool: True se o cadastro foi um sucesso, False em caso de falha (ex: email já existe).
    """
    tentativas = 3
    sucesso = False
    # Definimos que o usuário começa deslogado (0)
    status_logado = 0 

    while tentativas > 0 and not sucesso:    
        try:
            sql = '''INSERT INTO usuarios (nome, email, telefone, senha, logado) 
                     VALUES (?, ?, ?, ?, ?)'''
            
            valores = (nome, email, telefone, senha, status_logado)
            
            cursor.execute(sql, valores)
            banco.commit()
            
            print(f"👤 Usuário {nome} cadastrado com sucesso!")
            sleep(3)
            sucesso = True
            return True # Retorna True para seu código saber que o cadastro foi feito
        
        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                print("⚠️ Banco ocupado. Tentando novamente em 3s...")
                tentativas -= 1
                sleep(3)
            else:
                print(f"❌ Erro operacional: {e}")
                break
        except sqlite3.Error as erro:
            # Se o email já existir e for uma chave única, o erro cai aqui
            print(f"❌ Erro ao cadastrar usuário: {erro}")
            sleep(3)
            break

    if not sucesso:
        print("🛑 Falha ao registrar novo usuário.")
        sleep(3)
        return False
    


def mostrar_usuario_logadoBD(email_sessao):
    """
    Recupera os dados do perfil do usuário logado.
    Args: email_sessao (str): E-mail da conta ativa.
    Returns: Row/None: Objeto com (nome, email, telefone, senha, logado).
    """
    # O email_sessao virá automaticamente do login
    tentativas = 3
    sucesso = False
    
    while tentativas > 0 and not sucesso:    
        try:
            # CORREÇÃO: Tabela 'usuarios' e coluna 'email'
            cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email_sessao,))
            resultado = cursor.fetchone()
            
            if resultado:
                sucesso = True
                return resultado # Retorna: (nome, email, telefone, senha, logado)
            else:
                print(f"⚠️ Usuário [{email_sessao}] não encontrado no sistema.")
                sleep(3)
                return False

        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                print("⚠️ Banco ocupado. Tentando novamente...")
                tentativas -= 1
                sleep(3)
            else:
                print(f"❌ Erro de conexão: {e}")
                sleep(3)
                break
        except sqlite3.Error as erro:
            print(f"❌ Erro no Banco: {erro}")
            sleep(3)
            break

    if not sucesso: 
        print("🛑 Falha ao recuperar perfil do usuário.")



def deletar_conta_usuarioBD(email_sessao):
    """
    Exclui a conta do usuário logado. Ação irreversível.
    Args:
        email_sessao (str): E-mail do usuário que deseja deletar a própria conta.
    Returns:
        bool: True se a conta foi excluída, False caso contrário.
    """
    tentativas = 3
    sucesso = False
    
    while tentativas > 0 and not sucesso:    
        try:
            cursor.execute("DELETE FROM usuarios WHERE email = ?", (email_sessao,))
            
            if cursor.rowcount > 0:
                banco.commit()
                sucesso = True
                print(f"✅ Conta [{email_sessao}] removida com sucesso.")
                sleep(2)
                return True
            else:
                print("⚠️ Usuário não localizado para exclusão.")
                sleep(2)
                return False

        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                tentativas -= 1
                sleep(2)
            else:
                break
        except sqlite3.Error as erro:
            print(f"❌ Erro crítico: {erro}")
            sleep(2)
            break



def atualizar_campo_usuarioBD(email_sessao, atributo, novo_valor):
    """
    Edita o valor de uma única coluna do perfil do usuário.
    Args:
        email_sessao (str): E-mail de quem está logado.
        atributo (str): Nome da coluna (ex: 'nome', 'telefone', 'senha').
        novo_valor (str): O novo dado a ser gravado.
    Returns:
        bool: True se a alteração foi feita, False se deu erro.
    """
    tentativas = 3
    sucesso = False
    
    colunas_permitidas = ['nome', 'telefone', 'senha', 'logado']
    if atributo not in colunas_permitidas:
        print(f"🛑 Erro: O atributo '{atributo}' não existe ou não pode ser alterado.")
        return False

    while tentativas > 0 and not sucesso:
        try:
            sql = f"UPDATE usuarios SET {atributo} = ? WHERE email = ?"
            cursor.execute(sql, (novo_valor, email_sessao))
            banco.commit()
            
            if cursor.rowcount > 0:
                print(f"✅ O campo '{atributo}' da conta [{email_sessao}] foi atualizado!")
                sleep(2)
                sucesso = True
                return True
            else:
                print(f"⚠️ Usuário [{email_sessao}] não localizado.")
                sleep(2)
                return False

        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                tentativas -= 1
                sleep(3)
            else:
                break
        except sqlite3.Error as erro:
            print(f"❌ Erro crítico ao alterar usuário: {erro}")
            sleep(3)
            break
    
    return False


def verificar_sessao_ativaBD(email_sessao):
    """
    Verifica se a conta do usuário já está em uso em outro lugar.
    Args: email_sessao (str): O e-mail (ID) do usuário.
    Returns: bool: True se a conta já estiver LOGADA (1). False se estiver DESLOGADA (0) ou não existir.
    """
    tentativas = 3
    while tentativas > 0:    
        try:
            cursor.execute("SELECT logado FROM usuarios WHERE email = ?", (email_sessao,))
            resultado = cursor.fetchone()
            
            if resultado and resultado[0] == 1:
                return True  
            return False     

        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                sleep(2)
                tentativas -= 1
            else: break
        except sqlite3.Error as erro:
            print(f"❌ Erro: {erro}")
            break
    return False


def fazer_loginBD(email_sessao):
    """
    Registra a entrada do usuário no sistema, bloqueando a conta para outros (logado = 1).
    Args: email_sessao (str): E-mail do usuário.
    Returns: bool: True se o login foi registrado no banco, False se deu erro.
    """
    tentativas = 3
    while tentativas > 0:    
        try:
            cursor.execute("UPDATE usuarios SET logado = 1 WHERE email = ?", (email_sessao,))
            banco.commit()
            if cursor.rowcount > 0:
                return True
            return False

        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                sleep(2)
                tentativas -= 1
            else: break
    return False


def fazer_logoffBD(email_sessao):
    """
    Libera a conta do usuário, permitindo novo login futuro (logado = 0).
    Args: email_sessao (str): E-mail do usuário logado.
    Returns: bool: True se liberou com sucesso, False se deu erro.
    """
    tentativas = 3
    while tentativas > 0:    
        try:
            cursor.execute("UPDATE usuarios SET logado = 0 WHERE email = ?", (email_sessao,))
            banco.commit()
            banco.close()
            return True
        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                sleep(2)
                tentativas -= 1
            else: break
    return False

