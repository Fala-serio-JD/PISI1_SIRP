import os
import time

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def logo():
    return"""
███████╗██╗██████╗ ██████╗ 
██╔════╝██║██╔══██╗██╔══██╗
███████╗██║██████╔╝██████╔╝
╚════██║██║██╔══██╗██╔═══╝ 
███████║██║██║  ██║██║    
╚══════╝╚═╝╚═╝  ╚═╝╚═╝     
        
System Integration Ruralinda Problems      
------------------------------------------------------------------------------------------------------------------
"""

def parametros_cadastro():
    return"""\n[Nome completo]
- Não pode estar vazio
- Deve ter pelo menos 5 caracteres
- Não deve conter números
- Não deve conter caracteres especiais

[Email institucional]
- Não pode estar vazio
- Deve conter domínio válido
- Apenas emails com domínio "@ufrpe.br" são permitidos

[Número de contato]
- Não pode estar vazio
- Deve conter apenas números
- Não deve conter caracteres especiais
- Deve ter entre 10 e 13 dígitos

[Senha]
- Não pode estar vazio
- Deve ter no mínimo 8 caracteres
- Deve conter pelo menos um número
- Deve conter pelo menos um caractere especial
- Deve conter pelo menos uma letra"""

id_usuario = 1

def cadastrar_usuario(nome, email, senha, num_contato, usuarios):
    global id_usuario

    usuario = {
        "id": id_usuario,
        "nome": nome,
        "email": email,
        "senha": senha,
        "num_contato": num_contato
        }

    usuarios.append(usuario)
    id_usuario += 1

def divisoria():  
    return "-" * 90

def divisoria_grossa():
    return "=" * 35

def status(usuarios, nome):
    condicao = f"[Logado como: {nome}]" if nome else "[Deslogado]" 
    return condicao

def logoff():
    limpar_tela()
    print("Saindo do sistema...")
    time.sleep(2)

def cabecalho():
    limpar_tela()
    logo()