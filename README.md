# 📝 SIRP - System Integration Ruralinda Problems (Release 1.0)

![Status do Projeto](https://img.shields.io/badge/Status-Versão%20Estável-green)
![Versão](https://img.shields.io/badge/Release-1.0--Volatile-orange)
![Python Version](https://img.shields.io/badge/Python-3.x-blue)

O **SIRP** é uma plataforma de integração interdisciplinar desenvolvida para a comunidade acadêmica da **UFRPE**. O sistema visa conectar estudantes que possuem problemas técnicos com colaboradores de diversas áreas dispostos a resolvê-los, fomentando a cooperação mútua e o networking dentro da universidade.

---

## 👥 Integrantes do Projeto
* **Jezreel David Ferreira Figueiredo**
* **Daniel Eric Pimenta**

---

## 🚀 Funcionalidades e Objetivos

* **Autenticação de Usuário:** Sistema de login e cadastro com validação rigorosa de e-mail institucional (`@ufrpe.br`) e segurança de credenciais.
* **Feed de Problemas (In-Memory):** Exibição dinâmica de problemas reportados, permitindo que qualquer usuário logado visualize as demandas da comunidade.
* **Reporte de Problemas:** Interface para descrição detalhada de incidentes, categorização por área técnica e fornecimento de contato.
* **Gerenciamento de Perfil:** Visualização dos dados cadastrais do usuário logado.
* **Interface CLI Profissional:** Navegação baseada em menus, uso de artes ASCII e tratamento de fluxo de tela para uma melhor experiência do usuário (UX).

## 🛠️ Tecnologias e Bibliotecas Utilizadas

Para esta versão, o projeto utiliza exclusivamente recursos nativos do Python, priorizando a lógica algorítmica e a manipulação de dados em memória:

* **Linguagem:** Python 3.x
* **Biblioteca `time`**: Utilizada para gerenciar o fluxo de tempo, delays de resposta e transições de tela.
* **Bibliotecas `os` & `sys`**: Essenciais para a limpeza do terminal (`cls`/`clear`) e manipulação do buffer de entrada (`stdin`).
* **Lógica de Strings (Built-in)**: Validações customizadas de formato sem bibliotecas externas, utilizando métodos como `.isalpha()`, `.isdigit()`, `.isspace()` e `.endswith()`.

## 💾 Estrutura de Dados e Persistência (Lógica da Ementa)

Seguindo os requisitos acadêmicos, a Release 1.0 utiliza **Persistência Volátil**, o que significa que os dados são armazenados enquanto o programa está em execução:

1.  **Dicionários (`dict`)**: Cada usuário e cada problema é um objeto mapeado com chaves e valores.
2.  **Listas (`list`)**: Funcionam como o banco de dados principal, armazenando as coleções de usuários e o feed de problemas.
3.  **Modularização**: O código é dividido em arquivos `.py` distintos para separar a lógica de interface, validação e armazenamento.

## ⚙️ Instalação e Detalhes de Execução

### Pré-requisitos
* Possuir o Python 3.10 ou superior instalado.

### Passo a Passo
1.  **Clonar o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/SIRP.git](https://github.com/seu-usuario/SIRP.git)
    cd SIRP
    ```
2.  **Executar o sistema:**
    ```bash
    python index.py
    ```

> **Aviso:** Esta versão não utiliza SQL. Ao encerrar o processo no terminal, os novos dados cadastrados durante a sessão serão resetados para o estado inicial definido em `banco_dados_problemas.py`.

## 🎓 Critérios Acadêmicos Atendidos

Este projeto demonstra a aplicação prática de:
* **Estruturas de Controle**: Loops (`while`, `for`) e Condicionais (`if/elif/else`).
* **Coleções Avançadas**: Manipulação profunda de listas e dicionários.
* **Modularização**: Criação de um sistema multi-arquivos com importações organizadas.
* **Funções com Retorno**: Uso de tuplas para validação de erros e booleanos para controle de acesso.

---
**Projeto desenvolvido para a disciplina de PISI1 - BSI / UFRPE.**