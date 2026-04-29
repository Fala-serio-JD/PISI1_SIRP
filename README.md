# 📝 SIRP - System Integration Ruralinda Problems

![Status do Projeto](https://img.shields.io/badge/Status-Em%20Desenvolvimento-blue)
![Python Version](https://img.shields.io/badge/Python-3.x-green)
![Database](https://img.shields.io/badge/Database-SQLite3-lightgrey)

O **SIRP** é uma plataforma de integração voltada para a comunidade acadêmica da **UFRPE**. O sistema funciona como uma rede social técnica, onde usuários podem reportar problemas de caráter interdisciplinar e encontrar colaboradores para desenvolver soluções conjuntas, promovendo o networking e a cooperação mútua.

## 🚀 Funcionalidades Principais

* **Sistema de Cadastro e Login:** Autenticação robusta com validação obrigatória de e-mail institucional (`@ufrpe.br`) e requisitos de segurança para senhas.
* **Gestão de Sessão:** Controle de estado do usuário (logado/deslogado) para garantir a segurança dos dados.
* **Feed de Problemas:** Listagem dinâmica de incidentes reportados, permitindo a visualização de detalhes como título, descrição, área técnica e contato do autor.
* **Reporte de Problemas:** Interface para submissão de novos relatos com categorização por área e sistema de status (Em Aberto, Resolvido, etc.).
* **Persistência de Dados:** Integração completa com banco de dados relacional para armazenamento permanente de usuários e relatos.
* **Perfil do Usuário:** Área dedicada para visualização e gerenciamento das informações cadastrais.

## 🛠️ Tecnologias e Bibliotecas Utilizadas

O projeto foi desenvolvido puramente em **Python**, utilizando recursos nativos para garantir a eficiência e o foco na lógica de programação:

* `sqlite3`: Camada de persistência e manipulação de banco de dados relacional.
* `os` & `sys`: Manipulação do terminal e limpeza de buffers.
* `time`: Controle de fluxo e melhoria da experiência do usuário (delays de interface).
* **Lógica de Strings (Built-in):** Validações robustas de dados utilizando métodos nativos como `.isalpha()`, `.isdigit()` e `.endswith()`.
  
## 🏛️ Estrutura do Projeto (Modularização)

Seguindo as boas práticas da ementa de BSI, o código foi dividido em módulos:

| Arquivo | Descrição |
| :--- | :--- |
| `index.py` | Ponto de entrada da aplicação e controle do fluxo principal. |
| `bancoSQL.py` | Toda a lógica de comunicação CRUD com o SQLite. |
| `validacoes.py` | Motor de regras de negócio para entradas de dados (Nomes, E-mails, Senhas). |
| `utils.py` | Funções utilitárias, artes ASCII e tratamentos de interface CLI. |
| `cadastro.py` / `login.py` | Interfaces dedicadas ao gerenciamento de acesso. |
| `controle_problemas.py`| Lógica de submissão e visualização do feed de problemas. |

## ⚙️ Detalhes de Instalação e Execução

### Pré-requisitos
* Python 3.10 ou superior instalado.

### Passo a Passo
1.  **Clonar o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/SIRP.git
    cd SIRP
    ```
2.  **Executar a aplicação:**
    ```bash
    python index.py
    ```


## 🎓 Aspectos Acadêmicos (Ementa)

Este projeto aplica diversos conceitos fundamentais de programação:
* **Estruturas de Repetição e Decisão:** Controle de menus e validações.
* **Listas e Dicionários:** Manipulação temporária de dados e objetos.
* **Tratamento de Exceções:** Gestão de erros operacionais e concorrência de banco de dados.
* **Modularização:** Divisão de responsabilidades em múltiplos arquivos.

---
**Desenvolvido por:** Jezreel David Ferreira Figueiredo e Daniel Eric Pimenta (Projeto Acadêmico UFRPE - 2026).

