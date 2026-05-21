import hashlib
import mysql.connector
from conexao import conectar, fechar_conexao

def criptografar_senha(senha):
    """
    Função de Segurança: Aplica um algoritmo de dispersão (Hash SHA-256) na senha.
    Isso garante conformidade de segurança, impedindo o armazenamento em texto claro.
    """
    return hashlib.sha256(senha.encode('utf-8')).hexdigest()

def cadastrar_usuario():
    print('\n------ CADASTRO DE NOVO ALUNO ------')
    
    # 1. Fluxo de Conformidade LGPD (Segurança Jurídica)
    print("\nAVISO DE PRIVACIDADE (LGPD):")
    print("Para criar sua conta, precisamos coletar e armazenar seus dados cadastrais")
    print("estritamente para fins de autenticação e prestação do serviço educacional.")
    aceite_lgpd = input("Você aceita o tratamento dos seus dados de acordo com a LGPD? (S/N): ").strip().upper()
    
    if aceite_lgpd != 'S':
        print("\n[CADASTRO CANCELADO]: O consentimento de dados é obrigatório para o uso do sistema.")
        return

    # 2. Coleta de Dados cadastrais (Alinhados com as restrições do banco)
    nome = input('Digite seu nome completo: ').strip()
    email = input('Digite seu email: ').strip()
    telefone = input('Digite seu telefone: ').strip()
    dt_nasc = input('Digite sua data de nascimento (AAAA-MM-DD): ').strip()
    senha = input('Digite sua senha: ')
    confirmacao_senha = input('Digite sua senha novamente: ')
    
    # 3. Validação de Integridade Elementar
    if senha != confirmacao_senha:
        print('\n[ERRO DE VALIDAÇÃO]: As senhas digitadas não são iguais! Tente novamente.')
        return
        
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            
            # Criptografia da senha antes do envio à camada de persistência
            senha_segura = criptografar_senha(senha)
            
            # Query Parametrizada (Proteção Nativa contra SQL Injection)
            sql = """
                INSERT INTO tbl_usuarios 
                (nome_usuario, email_usuario, telefone_usuario, dt_nasc_usuario, senha_usuario) 
                VALUES (%s, %s, %s, %s, %s)
            """
            valores = (nome, email, telefone, dt_nasc, senha_segura)
            
            cursor.execute(sql, valores)
            conexao.commit()
            
            print(f'\n[SUCESSO]: Aluno {nome} cadastrado e protegido com sucesso!')
            
        except mysql.connector.Error as erro:
            print(f"\n[ERRO BANCO DE DADOS]: Falha na inserção do registro: {erro}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            fechar_conexao(conexao)

def logar_usuario():
    print('\n------ LOGIN DE ACESSO ------')
    email = input('Digite seu email: ').strip()
    senha = input('Digite sua senha: ')
    
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            
            # Transforma a senha digitada no mesmo padrão hash salvo no banco para comparação
            senha_hash = criptografar_senha(senha)
            
            # Busca pelo e-mail e pela senha criptografada simultaneamente
            sql = """
                SELECT id_usuario, nome_usuario 
                FROM tbl_usuarios 
                WHERE email_usuario = %s AND senha_usuario = %s
            """
            cursor.execute(sql, (email, senha_hash))
            resultado = cursor.fetchone()
            
            if resultado:
                id_usuario = resultado[0]
                nome_usuario = resultado[1]
                print(f'\n[SUCESSO]: Autenticação realizada. Bem-vindo(a), {nome_usuario}!')
                return id_usuario # Retorna o ID da sessão ativa para o arquivo principal
            else:
                print('\n[ERRO DE AUTENTICAÇÃO]: E-mail ou senha incorretos.')
                return None
                
        except mysql.connector.Error as erro:
            print(f"\n[ERRO BANCO DE DADOS]: Falha ao validar credenciais: {erro}")
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
            fechar_conexao(conexao)
    return None