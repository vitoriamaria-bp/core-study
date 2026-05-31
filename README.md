# 🎓 Core Study

<p align="center">
  <h3 align="center">Plataforma Educacional EAD</h3>
  <p align="center">
    Sistema desenvolvido para gerenciamento, organização e distribuição de conteúdos educacionais digitais.
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Scrum-6DB33F?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Kanban-0052CC?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Trello-0052CC?style=for-the-badge&logo=trello&logoColor=white" />
  <img src="https://img.shields.io/badge/Miro-050038?style=for-the-badge&logo=miro&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
</p>

<p align="center">
  🔗 Repositório Oficial
  <br>
  https://github.com/vitoriamaria-bp/core-study
</p>

---

## 📖 Sobre o Projeto

O **Core Study** é um **Produto Mínimo Viável (MVP)** desenvolvido como Projeto Semestral da **UNIFECAF**.

A plataforma foi criada para centralizar conteúdos educacionais em um único ambiente, permitindo que administradores organizem cursos, módulos, aulas e materiais de apoio, enquanto os alunos acessam os conteúdos por meio de uma interface simples, organizada e intuitiva.

Durante o desenvolvimento foram aplicados conceitos de programação backend com Python, modelagem e implementação de banco de dados MySQL, além da utilização de metodologias ágeis para planejamento, acompanhamento e organização das atividades da equipe.

---

## 👨‍💻 Equipe de Desenvolvimento

| Integrante       | GitHub                                     |
| ---------------- | ------------------------------------------ |
| Vitória Maria    | https://github.com/vitoriamaria-bp         |
| Fabiano Matheus  | https://github.com/0Matheus-Silva          |
| Adrian           | https://github.com/Adrian-2003             |
| Guilherme        | https://github.com/Guilhermepereiramarques |
| Luiz             | https://github.com/shiidw                  |

---

## 🚀 Tecnologias Utilizadas

### Desenvolvimento

* Python
* Flask
* MySQL
* HTML5
* CSS3
* JavaScript

### Metodologias Ágeis

* Scrum
* Kanban

### Gestão e Planejamento

* Trello
* Miro

---

## 🏗️ Arquitetura do Sistema

O sistema utiliza autenticação baseada em sessões e está dividido em dois módulos principais.

### 🛡️ Painel Administrativo

Área restrita destinada ao gerenciamento completo da plataforma.

#### Funcionalidades

* Gestão de usuários
* Controle de níveis de acesso
* Cadastro de categorias
* Cadastro de cursos
* Organização de módulos
* Cadastro de aulas
* Gerenciamento de materiais de apoio
* Estruturação hierárquica dos conteúdos
* Edição de Perfil

---

### 📚 Painel do Aluno

Ambiente desenvolvido para o consumo dos conteúdos educacionais.

#### Funcionalidades

* Catálogo de cursos
* Visualização de conteúdos
* Trilha de aprendizagem
* Navegação em Accordion (Sanfona)
* Gerenciamento de perfil
* Acesso a materiais complementares

---

## 📂 Estrutura dos Conteúdos

```text
Curso
 ├── Módulo
 │    ├── Aula
 │    │    ├── Vídeo
 │    │    ├── PDF
 │    │    └── Material Complementar
```

---

## ⚙️ Preparação do Ambiente

Antes de executar o projeto, certifique-se de possuir os seguintes requisitos instalados:

### Requisitos

* Python 3.10 ou superior
* MySQL Server 8.0 ou superior
* Git

Verifique as versões instaladas:

```bash
python --version
mysql --version
git --version
```

---

## 🚀 Instalação e Execução

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/vitoriamaria-bp/core-study.git

Para versão com Front End
cd CoreStudy

ou

Para Back End no Terminal
cd CoreStudy_BackEnd
```

---

### 2️⃣ Instalar Dependências

```bash
pip install flask flask-session mysql-connector-python
```

---

### 3️⃣ Instalar e Iniciar o MySQL

Linux / GitHub Codespaces:

```bash
sudo apt-get update

sudo apt-get install mysql-server -y

sudo service mysql start
```

---

### 4️⃣ Importar o Banco de Dados

Execute o comando abaixo para criar toda a estrutura do banco:

```bash
mysql -u root -p < "Banco de dados Core Study.sql"
```

---

### 5️⃣ Configurar a Conexão

Verifique se as credenciais definidas no arquivo:

```text
conexao.py
```

correspondem às credenciais configuradas em seu servidor MySQL.

---

### 6️⃣ Popular o Banco de Dados

Após configurar a conexão, execute:

```bash
python gerar_inserts.py

sudo mysql -u root -p db_core_study1 < inserts_dados.sql
```

Esse script será responsável por inserir os dados iniciais utilizados pela plataforma.

---

### 7️⃣ Executar a Aplicação

```bash
python app.py
```

A aplicação estará disponível em:

```text
http://127.0.0.1:5000
```

---

## 🎯 Objetivos Acadêmicos

Este projeto foi desenvolvido com o propósito de aplicar conhecimentos relacionados a:

* Programação Backend com Python
* Desenvolvimento de aplicações utilizando Flask
* Modelagem de Banco de Dados Relacional
* Implementação de Banco de Dados MySQL
* Operações CRUD
* Controle de Sessões e Autenticação
* Levantamento e organização de requisitos
* Metodologias Ágeis
* Planejamento e acompanhamento de atividades
* Trabalho em equipe
* Desenvolvimento colaborativo de software

---

## 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos e educacionais.

---

## 🎓 Projeto Acadêmico

O **Core Study** foi desenvolvido como Projeto Semestral da **UNIFECAF**, permitindo a aplicação prática dos conhecimentos adquiridos durante a graduação, desde a modelagem do banco de dados até a implementação completa da aplicação.

Além do desenvolvimento técnico, o projeto envolveu planejamento, organização de tarefas e acompanhamento da equipe utilizando metodologias ágeis e ferramentas amplamente utilizadas no mercado de tecnologia.

A equipe recomenda conhecer a instituição responsável pela formação e incentivo ao desenvolvimento deste projeto:

🔗 https://www.unifecaf.com.br

---

<p align="center">
  Desenvolvido com dedicação pela equipe Core Study ❤️
</p>
