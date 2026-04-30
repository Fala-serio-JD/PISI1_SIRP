# 📝 SIRP - System Integration Ruralinda Problems (Release 1.0)

![Status do Projeto](https://img.shields.io/badge/Status-Versão%20Estável-green)
![Versão](https://img.shields.io/badge/Release-1.0--Volatile-orange)
![Python Version](https://img.shields.io/badge/Python-3.x-blue)

O **SIRP** é uma plataforma de integração interdisciplinar desenvolvida para a comunidade acadêmica da **UFRPE**. O sistema visa conectar estudantes com problemas técnicos a colaboradores dispostos a resolvê-los, fomentando a cooperação mútua.

---

## 👥 Integrantes do Projeto
* **Jezreel David Ferreira Figueiredo**
* **Daniel Eric Pimenta**

---

## 🚀 Funcionalidades e Objetivos

* **Autenticação de Usuário:** Sistema de login e cadastro com validação de e-mail institucional (`@ufrpe.br`).
* **Feed de Problemas (In-Memory):** Exibição de problemas reportados armazenados temporariamente na sessão.
* **Reporte de Problemas:** Interface para descrição de incidentes, categorização e contato.
* **Gerenciamento de Perfil:** Visualização dos dados cadastrais do usuário.
* **Interface CLI:** Navegação intuitiva via terminal com artes ASCII e menus organizados.

## 🛠️ Tecnologias e Bibliotecas Utilizadas

O projeto utiliza apenas recursos nativos do Python, focando na lógica algorítmica:

* **Linguagem:** Python 3.x.
* **Biblioteca `time`**: Gerenciamento de fluxo e transições de tela.
* **Bibliotecas `os` & `sys`**: Limpeza de terminal e manipulação de buffer.
* **Lógica de Strings**: Validações customizadas com métodos como `.isalpha()` e `.endswith()`.

## 💾 Estrutura de Dados e Persistência

Esta release utiliza **Persistência Volátil**, aplicando conceitos fundamentais da ementa:

1.  **Dicionários (`dict`)**: Representação de usuários e problemas.
2.  **Listas (`list`)**: Armazenamento das coleções de dados durante a execução.
3.  **Modularização**: Divisão em arquivos `.py` para separação de responsabilidades.

## ⚙️ Instalação e Execução

### Passo a Passo
1.  **Clonar o repositório:**
    ```bash
    git clone [https://github.com/Fala-serio-JD/PISI1_SIRP.git](https://github.com/Fala-serio-JD/PISI1_SIRP.git)
    cd PISI1_SIRP
    ```
2.  **Executar o sistema:**
    ```bash
    python index.py
    ```

> **Aviso:** Esta versão não utiliza SQL. Ao encerrar o programa, os dados novos serão redefinidos para o estado inicial de `banco_dados_problemas.py`.

## 🎓 Critérios Acadêmicos Atendidos

* **Estruturas de Controle**: Uso de loops (`while`, `for`) e condicionais.
* **Coleções**: Manipulação de listas e dicionários.
* **Modularização**: Organização em multi-arquivos.
* **Funções com Retorno**: Uso de tuplas para validação de erros.

## 📊 Documentação e Fluxo
O mapeamento da lógica de navegação e as decisões do sistema podem ser conferidos no fluxograma oficial do projeto:

* [📥 Baixar Fluxograma_SIRP_1VA.drawio](Fluxograma_SIRP_1VA.drawio)

> **Nota:** Para visualizar ou editar o fluxo, basta carregar o arquivo acima no [diagrams.net](https://app.diagrams.net/).

* [📥 Baixar Tabela de Acompanhamento_de_Projetos-JezreeleDaniel.pdf](Acompanhamento_de_Projetos-JezreeleDaniel.pdf)

---
**Projeto acadêmico para PISI1 - BSI - UFRPE.**
