def validacao_acesso(usuarios, usuario_input, senha_input):
    for u in usuarios:

        usuario_valido = usuario_input == u["email"].lower()

        if not usuario_valido:
            usuario_valido = usuario_input == u["nome"].lower() 

        if usuario_valido and senha_input == u["senha"]:
            print("Credenciais aceitas! Pode prosseguir.")
            return True

    print("Usuário ou senha incorretos.")
    return False

def nome_valido(nome):
    tem_letra = any(c.isalpha() for c in nome)
    tem_numero = any(c.isdigit() for c in nome)
    tem_especial = any(not (c.isalnum() or c.isspace()) for c in nome)
    tamanho = len(nome) >= 5

    if not nome.strip():
        return False, "O nome não pode estar vazio."
    if not tamanho:
        return False, "O nome deve ter pelo menos 5 caracteres."
    if tem_numero:
        return False, "O nome não deve conter números."
    if tem_especial:
        return False, "O nome não deve conter caracteres especiais."
    if not tem_letra:
        return False, "O nome deve conter letras."

    return True, None

def email_valido(email, usuarios):
    tem_numero = any(c.isdigit() for c in email)
    tem_espaco = any(c.isspace() for c in email)
    tem_dominio = email.count("@") == 1
    tem_dominio_valido = email.endswith("@ufrpe.br")
    tamanho = len(email) > 9

    if not email.strip():
        return False, "O email não pode estar vazio."
    if tem_espaco:
        return False, "O email não deve conter espaços."
    if not tem_dominio:
        return False, "O email deve conter um '@'."
    if not tem_dominio_valido:
        return False, "Apenas emails '@ufrpe.br' são permitidos."
    if not tamanho:
        return False, "O email é muito curto."
    if tem_numero:
        return False, "O email não deve conter números."
    
    for u in usuarios:
        if u["email"] == email:
            return False, "O email já existe."

    return True, None

def contato_valido(num_contato):
    tem_letra = any(c.isalpha() for c in num_contato)
    tem_numero = any(c.isdigit() for c in num_contato)
    tem_espaco = any(c.isspace() for c in num_contato)
    tem_especial = any(not (c.isalnum() or c.isspace()) for c in num_contato)
    tamanho = 10 < len(num_contato) <= 13

    if not num_contato.strip():
        return False, "O número é obrigatório."
    if tem_letra:
        return False, "O número não deve conter letras."
    if tem_espaco:
        return False, "O número não deve conter espaços."
    if tem_especial:
        return False, "O número não deve conter caracteres especiais."
    if not tem_numero:
        return False, "O número deve conter dígitos."
    if not tamanho:
        return False, "O número deve ter entre 11 e 13 dígitos."

    return True, None

def senha_valida(senha):
    tem_letra = any(c.isalpha() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_especial = any(not (c.isalnum() or c.isspace()) for c in senha)
    tamanho = len(senha) >= 8
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(not (c.isupper()) for c in senha)

    if not tem_letra:
        return False, "A senha deve conter pelo menos uma letra."
    if not tem_numero:
        return False, "A senha deve conter pelo menos um número."
    if not tem_especial:
        return False, "A senha deve conter pelo menos um caractere especial."
    if not tamanho:
        return False, "A senha deve ter pelo menos 8 caracteres."
    if not tem_maiuscula:
        return False, "A senha deve conter pelo menos um caractere em maiúscula."
    if not tem_minuscula:
        return False, "A senha deve conter pelo menos um caractere em minúscula." #TESTAR

    return True, None