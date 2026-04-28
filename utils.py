import os
import time
import sys

def limpar_tela():
    """Função dedicada à limpeza do terminal"""
    os.system("cls" if os.name == "nt" else "clear")

def logo():
    """Arte ASCII do SIRP"""
    print("""
███████╗██╗██████╗ ██████╗ 
██╔════╝██║██╔══██╗██╔══██╗
███████╗██║██████╔╝██████╔╝
╚════██║██║██╔══██╗██╔═══╝ 
███████║██║██║  ██║██║    
╚══════╝╚═╝╚═╝  ╚═╝╚═╝     

System Integration Ruralinda Problems      
-------------------------------------------------------------------------------""")

def cabecalho():
    """Função dedicada à exibição da  logo do SIRP de forma geral."""
    limpar_tela()
    logo()

def main_cabecalho():
    """Função dedicada à apresentação principal da logo do SIRP."""
    cabecalho()
    print("""
Bem vindo(a)!
O SIRP dedica-se como uma rede social integrando os mais diversos saberes na resolução de problemas  de caráter interdiciplinar.

Reporte qualquer problema e encontre alguém que queira dar uma solução…
Assim promovendo a cooperação na comunidade de modo facilitado, entre aqueles que querem gerar projetos e aqueles que precisam de uma solução!

Desse jeito, nunca foi tão fácil fazer networking!
-------------------------------------------------------------------------------
""")

def parametros_cadastro():
    """Função dedicada à exibição dos parâmetros de aceitação dos campos do cadastro."""
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

def divisoria():
    """Exibe uma linha divisória constituída de 90 traços (-) sequenciados"""
    return "-" * 90

def divisoria_grossa():
    """Exibe uma linha divisória grossa constituída de 20 iguais (=) sequenciados"""
    return "=" * 20

def logoff():
    """Função dedicada ao logoff do usuário no SIRP
    
    Returns:
        bool: False
    """
    limpar_tela()
    print("Saindo do sistema...")
    time.sleep(2)
    return False

def limpar_stdin():
    """Função dedicada a limpar buffer do terminal para evitar comportamento indesejado."""
    if os.name == "posix":
        # Linux / macOS
        import termios
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

    elif os.name == "nt":
        # Windows
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()

def submeter_titulo():
    """Função dedicada à submissão do título do problema
    
    Returns:
        str: titulo.
    """
    while True:
        limpar_stdin()
        titulo = input("Título (até 100 caracteres): ")

        if len(titulo) > 0 and len(titulo)<= 100:
            print("Título válido!")
            break
        elif len(titulo) == 0:
            print("O título é obrigatório.")
        else:
            print("O seu título excedeu o limite de 100 caracteres.")
    return titulo

def submeter_descricao():
    """Função dedicada à submissão da descrição do problema
    
    Returns:
        str: descricao.
    """
    while True:
        limpar_stdin()
        descricao = input("Descreva o problema (até 1000 caracteres): ")

        if len(descricao) > 0 and len(descricao) <= 1000:
            print("Descrição válida.")
            break
        elif len(descricao) == 0:
            print("A descrição é obrigatória.")
        else:
            print("A sua descrição excedeu o limite máximo de 1000 caracteres.")
    return descricao