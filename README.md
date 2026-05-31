# 🎓 Core Study

O **Core Study** é um Produto Mínimo Viável (MVP) de uma plataforma educacional desenvolvida como projeto acadêmico. O sistema centraliza conteúdos didáticos, facilitando a organização, distribuição e o consumo de materiais educacionais.

## 👥 Equipe de Desenvolvimento

| Integrante | Perfil GitHub |
| :--- | :--- |
| **Vitória Pinheiro** | [@vitoriamaria-bp](https://github.com/vitoriamaria-bp) |
| **Fabiano Matheus** | [@0Matheus-Silva](https://github.com/0Matheus-Silva) |
| **Adrian** | [@Adrian-2003](https://github.com/Adrian-2003) |
| **Guilherme** | [@Guilherme](https://github.com/Guilhermepereiramarques) |
| **Luiz (shiidw)** | [@shiidw](https://github.com/shiidw) |

---

## 🚀 Tecnologias Utilizadas

O projeto foi construído sob uma arquitetura Fullstack Monolítica, utilizando:

* **Linguagem Principal:** Python 3.x
* **Framework Web:** Flask (com Jinja2 e Flask-Session)
* **Banco de Dados:** MySQL (Relacional)
* **Front-end:** HTML5, CSS3, JavaScript (Vanilla)
* **Gestão e Versionamento:** Git, GitHub, Trello e Miro (Metodologias Ágeis)

---

## ⚙️ Funcionalidades e Arquitetura

O sistema é segmentado em dois painéis distintos com rotas protegidas por verificação de sessão.

### 🛡️ Módulo Administrativo (Admin)
Painel restrito com operações de **CRUD** (Create, Read, Update, Delete) completas para:
* **Usuários:** Gestão de níveis de acesso.
* **Categorias e Cursos:** Estruturação temática.
* **Conteúdo:** Cadastro hierárquico (Módulos > Aulas > Materiais).

### 📚 Módulo do Aluno (View)
Ambiente de consumo focado na experiência do usuário:
* **Catálogo:** Listagem dinâmica de cursos.
* **Trilha de Aprendizagem:** Visualização em "Sanfona" (Accordion) via JavaScript.
* **Perfil:** Gestão de dados pessoais.

---

## 🔧 Como Executar o Projeto

1. **Configuração do Banco:** Importe o script `Banco de dados Core Study.sql` no seu servidor MySQL local ou via Codespace.
2. **Dependências:** No diretório raiz, instale os pacotes:
```bash
   pip install flask flask-session mysql-connector-python
