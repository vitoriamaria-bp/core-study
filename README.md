<p align="center">
  <h1 align="center">🐧 Core Study</h1>
  <p align="center">Sistema de gestão educacional robusto, focado em organização, segurança e performance.</p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" />
  <img src="https://img.shields.io/badge/MySQL_Workbench-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
</p>

---

## 📖 Sobre o Projeto
O **Core Study** é uma plataforma desenvolvida para gerir o ciclo de vida acadêmico. Com uma arquitetura modular, o sistema separa responsabilidades entre administrador e aluno, garantindo que a integridade dos dados seja mantida e a experiência do utilizador final seja fluida.

---

## 🛠 Como Configurar no Seu Computador (Local)

Para rodar este projeto no seu ambiente local (VS Code + Workbench), siga estes passos:

### 1. Preparação do Banco de Dados
1. Abra o **MySQL Workbench**.
2. Crie uma nova conexão e execute o script `Banco de dados Core Study.sql` contido na raiz do projeto.
3. Certifique-se de que o banco `db_core_study1` foi criado com sucesso.

### 2. Preparação do Ambiente Python
1. Certifique-se de ter o Python instalado.
2. Abra a pasta do projeto no **VS Code**.
3. No terminal do VS Code, instale a dependência necessária:
   ```bash
   pip install mysql-connector-python
