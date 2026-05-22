import getpass
from conexao import conectar

# --- USUÁRIOS E PERFIL ---
def adicionar_usuario():
    print("\n========================================")
    print("             NOVO CADASTRO              ")
    print("========================================")
    nome = input("Nome Completo: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    nascimento = input("Data de Nascimento (AAAA-MM-DD): ")
    senha = getpass.getpass("Senha: ")
    
    aceite = input("Aceita os termos de uso do Core Study? (S/N): ").upper()
    if aceite != 'S': 
        print("Cadastro cancelado: É necessário aceitar os termos.")
        return

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO tbl_usuarios (nome_usuario, email_usuario, telefone_usuario, dt_nasc_usuario, senha_usuario) VALUES (%s, %s, %s, %s, %s)", (nome, email, telefone, nascimento, senha))
    conexao.commit()
    print("\nUsuário cadastrado com sucesso!")
    cursor.close()
    conexao.close()

def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tbl_usuarios")
    for u in cursor.fetchall(): print(f"ID: {u[0]} | Nome: {u[1]} | E-mail: {u[2]}")
    cursor.close()
    conexao.close()

def visualizar_perfil(id_usuario):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tbl_usuarios WHERE id_usuario = %s", (id_usuario,))
    u = cursor.fetchone()
    print("\n========================================")
    print("             SEUS DADOS                 ")
    print("========================================")
    print(f"Nome: {u['nome_usuario']}")
    print(f"E-mail: {u['email_usuario']}")
    print(f"Telefone: {u['telefone_usuario']}")
    print(f"Nascimento: {u['dt_nasc_usuario']}")
    print("========================================")
    cursor.close()
    conexao.close()

def editar_perfil(id_usuario):
    print("\n========================================")
    print("1 - Editar Nome Completo")
    print("2 - Editar Telefone")
    print("3 - Editar Senha")
    print("----------------------------------------")
    print("0 - Voltar")
    print("========================================")
    op = input("Escolha o que deseja editar: ")
    
    if op == "0":
        return
        
    campo = {"1": "nome_usuario", "2": "telefone_usuario", "3": "senha_usuario"}.get(op)
    
    if not campo:
        print("Opção inválida.")
        return
        
    val = getpass.getpass("Novo valor: ") if op == "3" else input("Novo valor: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(f"UPDATE tbl_usuarios SET {campo} = %s WHERE id_usuario = %s", (val, id_usuario))
    conexao.commit()
    print("\nPerfil atualizado com sucesso!")
    cursor.close()
    conexao.close()

def excluir_conta(id_usuario):
    print("\nAtenção: Esta ação é irreversível.")
    if input("Tem certeza que deseja excluir sua conta? (S/N): ").upper() == 'S':
        senha = getpass.getpass("Confirme sua senha para excluir: ")
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM tbl_usuarios WHERE id_usuario = %s AND senha_usuario = %s", (id_usuario, senha))
        
        if cursor.rowcount > 0:
            conexao.commit()
            print("\nConta excluída com sucesso.")
            sucesso = True
        else:
            print("\nSenha incorreta. Exclusão cancelada.")
            sucesso = False
            
        cursor.close()
        conexao.close()
        return sucesso
    return False

# --- CATEGORIAS ---
def adicionar_categoria():
    nome = input("Nome da Categoria: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO tbl_categoria (nome_categoria) VALUES (%s)", (nome,))
    conexao.commit()
    cursor.close()
    conexao.close()

def listar_categorias():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tbl_categoria")
    for c in cursor.fetchall(): print(f"ID: {c[0]} | Nome: {c[1]}")
    cursor.close()
    conexao.close()

def editar_categoria():
    listar_categorias()
    id_c = input("ID da Categoria: ")
    nome = input("Novo Nome da Categoria: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE tbl_categoria SET nome_categoria = %s WHERE id_categoria = %s", (nome, id_c))
    conexao.commit()
    cursor.close()
    conexao.close()

def excluir_categoria():
    listar_categorias()
    id_c = input("ID da Categoria: ")
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM tbl_categoria WHERE id_categoria = %s", (id_c,))
        conexao.commit()
        print("\nCategoria excluída com sucesso!")
    except:
        print("\n[ERRO] Não é possível excluir uma categoria que possui cursos vinculados.")
    finally:
        cursor.close()
        conexao.close()

# --- CURSOS ---
def adicionar_curso():
    titulo = input("Título do Curso: ")
    desc = input("Descrição do Curso: ")
    carga = input("Carga Horária: ")
    cat = input("ID da Categoria: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO tbl_cursos (titulo_curso, descricao_curso, carga_hora_curso, fk_tbl_categoria_id_categoria) VALUES (%s, %s, %s, %s)", (titulo, desc, carga, cat))
    conexao.commit()
    cursor.close()
    conexao.close()

def listar_cursos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id_curso, titulo_curso, descricao_curso, carga_hora_curso FROM tbl_cursos")
    cursos = cursor.fetchall()
    
    if not cursos:
        print("\nNenhum curso cadastrado.")
        cursor.close()
        conexao.close()
        return

    print("\n========================================")
    print("       VISÃO GERAL DO ADMINISTRADOR     ")
    print("========================================")
    for c in cursos:
        print(f"\n[ID CURSO: {c[0]}] {c[1]} ({c[3]}h)")
        print(f"Descrição: {c[2]}")
        
        cursor.execute("SELECT id_modulo, titulo_modulo FROM tbl_modulos WHERE fk_tbl_cursos_id_curso = %s", (c[0],))
        modulos = cursor.fetchall()
        if not modulos:
            print("  └-- [Nenhum módulo cadastrado]")
            
        for m in modulos:
            print(f"  └-- [ID MÓDULO: {m[0]}] {m[1]}")
            cursor.execute("SELECT id_aula, titulo_aula, url_arqui_aula FROM tbl_aulas WHERE fk_tbl_modulos_id_modulo = %s", (m[0],))
            aulas = cursor.fetchall()
            if not aulas:
                print("        └-- [Nenhuma aula cadastrada]")
                
            for a in aulas:
                print(f"        ▶ [ID AULA: {a[0]}] {a[1]} | {a[2]}")
                cursor.execute("SELECT id_material, nome_material, tipo_material FROM tbl_materiais WHERE fk_tbl_aulas_id_aula = %s", (a[0],))
                materiais = cursor.fetchall()
                for mat in materiais:
                    print(f"            └-- [ID MATERIAL: {mat[0]}] {mat[1]} ({mat[2]})")
        print("----------------------------------------")
        
    cursor.close()
    conexao.close()

def editar_curso():
    listar_cursos()
    id_c = input("ID do Curso que deseja editar: ")
    titulo = input("Novo Título: ")
    desc = input("Nova Descrição: ")
    carga = input("Nova Carga Horária: ")
    cat = input("Novo ID da Categoria: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE tbl_cursos SET titulo_curso=%s, descricao_curso=%s, carga_hora_curso=%s, fk_tbl_categoria_id_categoria=%s WHERE id_curso=%s", (titulo, desc, carga, cat, id_c))
    conexao.commit()
    cursor.close()
    conexao.close()

def excluir_curso():
    listar_cursos()
    id_c = input("ID do Curso: ")
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM tbl_cursos WHERE id_curso = %s", (id_c,))
        conexao.commit()
        print("\nCurso excluído com sucesso!")
    except:
        print("\n[ERRO] Não é possível excluir um curso que possui módulos vinculados.")
    finally:
        cursor.close()
        conexao.close()

# --- MÓDULOS ---
def adicionar_modulo():
    titulo = input("Título do Módulo: ")
    curso = input("ID do Curso: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO tbl_modulos (titulo_modulo, fk_tbl_cursos_id_curso) VALUES (%s, %s)", (titulo, curso))
    conexao.commit()
    cursor.close()
    conexao.close()

def listar_modulos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tbl_modulos")
    for m in cursor.fetchall(): print(f"ID: {m[0]} | Título: {m[1]}")
    cursor.close()
    conexao.close()

def editar_modulo():
    listar_modulos()
    id_m = input("ID do Módulo: ")
    titulo = input("Novo Título: ")
    curso = input("Novo ID do Curso: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE tbl_modulos SET titulo_modulo=%s, fk_tbl_cursos_id_curso=%s WHERE id_modulo=%s", (titulo, curso, id_m))
    conexao.commit()
    cursor.close()
    conexao.close()

def excluir_modulo():
    listar_modulos()
    id_m = input("ID do Módulo: ")
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM tbl_modulos WHERE id_modulo = %s", (id_m,))
        conexao.commit()
        print("\nMódulo excluído com sucesso!")
    except:
        print("\n[ERRO] Não é possível excluir um módulo que possui aulas vinculadas.")
    finally:
        cursor.close()
        conexao.close()

# --- AULAS ---
def adicionar_aula():
    titulo = input("Título da Aula: ")
    url = input("URL da Aula: ")
    mod = input("ID do Módulo: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO tbl_aulas (titulo_aula, url_arqui_aula, fk_tbl_modulos_id_modulo) VALUES (%s, %s, %s)", (titulo, url, mod))
    conexao.commit()
    cursor.close()
    conexao.close()

def listar_aulas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tbl_aulas")
    for a in cursor.fetchall(): print(f"ID: {a[0]} | Título: {a[1]}")
    cursor.close()
    conexao.close()

def editar_aula():
    listar_aulas()
    id_a = input("ID da Aula: ")
    titulo = input("Novo Título: ")
    url = input("Nova URL: ")
    mod = input("Novo ID do Módulo: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE tbl_aulas SET titulo_aula=%s, url_arqui_aula=%s, fk_tbl_modulos_id_modulo=%s WHERE id_aula=%s", (titulo, url, mod, id_a))
    conexao.commit()
    cursor.close()
    conexao.close()

def excluir_aula():
    listar_aulas()
    id_a = input("ID da Aula: ")
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM tbl_aulas WHERE id_aula = %s", (id_a,))
        conexao.commit()
        print("\nAula excluída com sucesso!")
    except:
        print("\n[ERRO] Não é possível excluir uma aula que possui materiais vinculados.")
    finally:
        cursor.close()
        conexao.close()

# --- MATERIAIS ---
def adicionar_material():
    nome = input("Nome do Material: ")
    tipo = input("Tipo do Material: ")
    tam = input("Tamanho: ")
    aula = input("ID da Aula: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO tbl_materiais (nome_material, tipo_material, tam_arqu_material, fk_tbl_aulas_id_aula) VALUES (%s, %s, %s, %s)", (nome, tipo, tam, aula))
    conexao.commit()
    cursor.close()
    conexao.close()

def listar_materiais():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tbl_materiais")
    for m in cursor.fetchall(): print(f"ID: {m[0]} | Nome: {m[1]}")
    cursor.close()
    conexao.close()

def editar_material():
    listar_materiais()
    id_m = input("ID do Material: ")
    nome = input("Novo Nome: ")
    tipo = input("Novo Tipo: ")
    tam = input("Novo Tamanho: ")
    aula = input("Novo ID da Aula: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE tbl_materiais SET nome_material=%s, tipo_material=%s, tam_arqu_material=%s, fk_tbl_aulas_id_aula=%s WHERE id_material=%s", (nome, tipo, tam, aula, id_m))
    conexao.commit()
    cursor.close()
    conexao.close()

def excluir_material():
    listar_materiais()
    id_m = input("ID do Material: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tbl_materiais WHERE id_material = %s", (id_m,))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("\nMaterial excluído com sucesso!")

# --- FLUXO DO ALUNO ---
def trilha_do_aluno():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id_curso, titulo_curso FROM tbl_cursos")
    print("\n========================================")
    print("          CATÁLOGO DE CURSOS            ")
    print("========================================")
    for c in cursor.fetchall(): print(f"ID: [{c[0]}] - {c[1]}")
    id_c = input("\nDigite o ID do Curso para ver o conteúdo: ")
    
    cursor.execute("SELECT titulo_curso, descricao_curso FROM tbl_cursos WHERE id_curso = %s", (id_c,))
    curso = cursor.fetchone()
    if not curso: 
        print("Curso não encontrado.")
        return
        
    print("\n========================================")
    print(f"CURSO: {curso[0]}")
    print(f"DESCRIÇÃO: {curso[1]}")
    print("========================================")
    
    cursor.execute("SELECT id_modulo, titulo_modulo FROM tbl_modulos WHERE fk_tbl_cursos_id_curso = %s", (id_c,))
    for m in cursor.fetchall():
        print(f"\n[ MÓDULO: {m[1]} ]")
        cursor.execute("SELECT id_aula, titulo_aula, url_arqui_aula FROM tbl_aulas WHERE fk_tbl_modulos_id_modulo = %s", (m[0],))
        for a in cursor.fetchall():
            print(f"  ▶ Aula: {a[1]} | Link: {a[2]}")
            cursor.execute("SELECT nome_material, tipo_material FROM tbl_materiais WHERE fk_tbl_aulas_id_aula = %s", (a[0],))
            for mat in cursor.fetchall(): 
                print(f"    └-- Material Anexo: {mat[0]} ({mat[1]})")
    
    print("\n========================================")
    cursor.close()
    conexao.close()