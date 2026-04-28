import os
import time
import sys

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def logo():
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
    limpar_tela()
    logo()

def main_cabecalho():
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

def divisoria():  #Dá pra mesclar com a linha divisoria grossa
    return "-" * 90

def divisoria_grossa():
    return "=" * 20

def logoff():
    limpar_tela()
    print("Saindo do sistema...")
    time.sleep(2)

#Limpar buffer do terminal para evitar comportamento indesejado.
def limpar_stdin():
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