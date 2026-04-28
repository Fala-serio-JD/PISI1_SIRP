import sqlite3
from time import sleep
banco = sqlite3.connect('SIRP_BD.db')
cursor = banco.cursor()


#cursor.execute("""
#CREATE TABLE problemas (
    #id INTEGER PRIMARY KEY AUTOINCREMENT,
    #título TEXT,
    #descricao TEXT,
    #autor TEXT,
    #contato INTEGER,
    #areas TEXT,
    #status TEXT
#)
#""")
def adicionar_problemaBD(titulo, descricao, autor, contato, areas):
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
            id= cursor.lastrowid
            banco.commit()
            print(f"Problema {id} salvo com sucesso!")
            sucesso= True
            return id
        
        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                print("⚠️ Banco ocupado (Locked). Tentando novamente em 2s...")
                tentativas -= 1
                sleep(2)
            else:
                print(f"❌ Erro operacional: {e}")
                break
        except sqlite3.Error as erro:
            print(f"❌ Erro crítico no SQLite: {erro}")
            break

    if not sucesso:
        print("🛑 Não foi possível salvar os dados após várias tentativas.")

#TESTE: adicionar_problemaBD('Pacientes entediados', 'seilá','Jezreel', 'jdferreira@ufrpe.br', 'Saúde, Ciências')

def mostrar_problema(id_problema):
    tentativas = 3
    sucesso = False
    
    while tentativas > 0 and not sucesso:    
        try:
            problema = cursor.execute(f"SELECT {id_problema} FROM problemas")
            banco.commit()
            return problema
            sucesso= True
        
        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                print("⚠️ Banco ocupado (Locked). Tentando novamente em 2s...")
                tentativas -= 1
                sleep(2)
            else:
                print(f"❌ Erro operacional: {e}")
                break
        except sqlite3.Error as erro:
            print(f"❌ Erro crítico no SQLite: {erro}")
            break

    if not sucesso: print("🛑 Não foi possível mostrar os dados após várias tentativas.")

#Reolhar código abaixo:
def deletar_problema(id_problema):
    tentativas = 3
    sucesso = False
    
    while tentativas > 0 and not sucesso:    
        try:
            cursor.execute(f"DELETE {id_problema} FROM problemas")
            banco.commit()
            sucesso= True
        
        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                print("⚠️ Banco ocupado (Locked). Tentando novamente em 2s...")
                tentativas -= 1
                sleep(2)
            else:
                print(f"❌ Erro operacional: {e}")
                break
        except sqlite3.Error as erro:
            print(f"❌ Erro crítico no SQLite: {erro}")
            break

    if not sucesso: print("🛑 Não foi possível deletar os dados após várias tentativas.")
    else: print(f"problema #{id_problema} excluído com sucesso!")


def mostrar_usuarios(id_usuario):
    tentativas = 3
    sucesso = False
    
    while tentativas > 0 and not sucesso:    
        try:
            pessoa = cursor.execute(f"SELECT {id_usuario} FROM usuarios")
            banco.commit()
            sucesso= True
            return pessoa
        
        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                print("⚠️ Banco ocupado (Locked). Tentando novamente em 2s...")
                tentativas -= 1
                sleep(2)
            else:
                print(f"❌ Erro operacional: {e}")
                break
        except sqlite3.Error as erro:
            print(f"❌ Erro crítico no SQLite: {erro}")
            break

    if not sucesso:
        print("🛑 Não foi possível mostrar os dados após várias tentativas.")






# Gerar funções:
    # Função de inserir dado em cada atributo de problema e usuário
        #E seu tratamento de erro
    # Função de editar dados específicos de problema e usuário
        #E seu tratamento de erro
    # Função de deletar dados epecíficos de problema e usuário
        #E seu tratamento de erro

#banco.commit()
#banco.close()



""" try:
    #cursor.execute("CREATE TABLE usuarios (nome text, email text, telefone integer, senha text)")

    #cursor.execute("INSERT INTO usuarios VALUES('Aline Cruel Dantas', 'aline.cruel@ufrpe.br', 81983608888, 'Ol@5xis2')")

    cursor.execute("DELETE from usuarios WHERE nome='NULL'") """

    

""" except sqlite3.Error as erro:
    print("Error ao excluir: ", erro)


 cursor.execute("SELECT * FROM usuarios")
print(cursor.fetchall()) """