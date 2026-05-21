import mysql.connector
from mysql.connector import Error


def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="db_core_study1"
        )
        return conexao

    except Error as error:
        print(f"Erro ao conectar no MySQL: {error}")
        return None


def criar_tabelas():
    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbl_usuarios (
        id_usuario INT AUTO_INCREMENT PRIMARY KEY,
        nome_usuario VARCHAR(100) NOT NULL,
        email_usuario VARCHAR(200) NOT NULL,
        telefone_usuario VARCHAR(50) NOT NULL,
        dt_nasc_usuario DATE NOT NULL,
        senha_usuario VARCHAR(100) NOT NULL,
        dt_cad_usuario DATE DEFAULT (CURRENT_DATE)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbl_categoria (
        id_categoria INT AUTO_INCREMENT PRIMARY KEY,
        nome_categoria VARCHAR(100) NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbl_cursos (
        id_curso INT AUTO_INCREMENT PRIMARY KEY,
        titulo_curso VARCHAR(100) NOT NULL,
        descricao_curso VARCHAR(500) NOT NULL,
        carga_hora_curso INT NOT NULL,
        fk_tbl_categoria_id_categoria INT NOT NULL,

        CONSTRAINT FK_tbl_cursos_categoria
            FOREIGN KEY (fk_tbl_categoria_id_categoria)
            REFERENCES tbl_categoria(id_categoria)
            ON DELETE RESTRICT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbl_modulos (
        id_modulo INT AUTO_INCREMENT PRIMARY KEY,
        titulo_modulo VARCHAR(100) NOT NULL,
        fk_tbl_cursos_id_curso INT NOT NULL,

        CONSTRAINT FK_tbl_modulos_cursos
            FOREIGN KEY (fk_tbl_cursos_id_curso)
            REFERENCES tbl_cursos(id_curso)
            ON DELETE RESTRICT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbl_aulas (
        id_aula INT AUTO_INCREMENT PRIMARY KEY,
        titulo_aula VARCHAR(200) NOT NULL,
        url_arqui_aula VARCHAR(2000) NOT NULL,
        fk_tbl_modulos_id_modulo INT NOT NULL,

        CONSTRAINT FK_tbl_aulas_modulos
            FOREIGN KEY (fk_tbl_modulos_id_modulo)
            REFERENCES tbl_modulos(id_modulo)
            ON DELETE RESTRICT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbl_materiais (
        id_material INT AUTO_INCREMENT PRIMARY KEY,
        nome_material VARCHAR(200) NOT NULL,
        tipo_material VARCHAR(100),
        tam_arqu_material VARCHAR(200),
        fk_tbl_aulas_id_aula INT NOT NULL,

        CONSTRAINT FK_tbl_materiais_aulas
            FOREIGN KEY (fk_tbl_aulas_id_aula)
            REFERENCES tbl_aulas(id_aula)
            ON DELETE CASCADE
    )
    """)

    conexao.commit()
    print("Tabelas criadas com sucesso!")

    cursor.close()
    conexao.close()


def adicionar_usuario():
    nome = input("Nome do usuário: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    dt_nasc = input("Data de nascimento (AAAA-MM-DD): ")
    senha = input("Senha: ")

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO tbl_usuarios
    (nome_usuario, email_usuario, telefone_usuario, dt_nasc_usuario, senha_usuario)
    VALUES (%s, %s, %s, %s, %s)
    """

    valores = (nome, email, telefone, dt_nasc, senha)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Usuário cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tbl_usuarios")
    usuarios = cursor.fetchall()

    print("\n===== USUÁRIOS =====")

    for usuario in usuarios:
        print(f"ID: {usuario[0]}")
        print(f"Nome: {usuario[1]}")
        print(f"Email: {usuario[2]}")
        print(f"Telefone: {usuario[3]}")
        print(f"Nascimento: {usuario[4]}")
        print(f"Data cadastro: {usuario[6]}")
        print("-" * 40)

    cursor.close()


def adicionar_categoria():
    nome = input("Nome da categoria: ")

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO tbl_categoria (nome_categoria)
    VALUES (%s)
    """

    cursor.execute(sql, (nome,))
    conexao.commit()

    print("Categoria cadastrada com sucesso!")

    cursor.close()
    conexao.close()


def listar_categorias():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tbl_categoria")
    categorias = cursor.fetchall()

    print("\n===== CATEGORIAS =====")
    for categoria in categorias:
        print(f"ID: {categoria[0]}")
        print(f"Nome: {categoria[1]}")
        print("-" * 30)

    cursor.close()
    conexao.close()


def adicionar_curso():
    titulo = input("Título do curso: ")
    descricao = input("Descrição do curso: ")
    carga_hora = int(input("Carga horária do curso: "))

    listar_categorias()
    categoria_id = int(input("Digite o ID da categoria: "))

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO tbl_cursos
    (titulo_curso, descricao_curso, carga_hora_curso, fk_tbl_categoria_id_categoria)
    VALUES (%s, %s, %s, %s)
    """

    valores = (titulo, descricao, carga_hora, categoria_id)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Curso cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def listar_cursos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT tbl_cursos.id_curso,
           tbl_cursos.titulo_curso,
           tbl_cursos.descricao_curso,
           tbl_cursos.carga_hora_curso,
           tbl_categoria.nome_categoria
    FROM tbl_cursos
    INNER JOIN tbl_categoria
    ON tbl_cursos.fk_tbl_categoria_id_categoria = tbl_categoria.id_categoria
    """

    cursor.execute(sql)
    cursos = cursor.fetchall()

    print("\n===== CURSOS =====")
    for curso in cursos:
        print(f"ID: {curso[0]}")
        print(f"Título: {curso[1]}")
        print(f"Descrição: {curso[2]}")
        print(f"Carga horária: {curso[3]} horas")
        print(f"Categoria: {curso[4]}")
        print("-" * 40)

    cursor.close()
    conexao.close()


def adicionar_modulo():
    titulo = input("Título do módulo: ")

    listar_cursos()
    curso_id = int(input("Digite o ID do curso: "))

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO tbl_modulos
    (titulo_modulo, fk_tbl_cursos_id_curso)
    VALUES (%s, %s)
    """

    cursor.execute(sql, (titulo, curso_id))
    conexao.commit()

    print("Módulo cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def listar_modulos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT tbl_modulos.id_modulo,
           tbl_modulos.titulo_modulo,
           tbl_cursos.titulo_curso
    FROM tbl_modulos
    INNER JOIN tbl_cursos
    ON tbl_modulos.fk_tbl_cursos_id_curso = tbl_cursos.id_curso
    """

    cursor.execute(sql)
    modulos = cursor.fetchall()

    print("\n===== MÓDULOS =====")
    for modulo in modulos:
        print(f"ID: {modulo[0]}")
        print(f"Módulo: {modulo[1]}")
        print(f"Curso: {modulo[2]}")
        print("-" * 40)

    cursor.close()
    conexao.close()


def adicionar_aula():
    titulo = input("Título da aula: ")
    url = input("URL/arquivo da aula: ")

    listar_modulos()
    modulo_id = int(input("Digite o ID do módulo: "))

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO tbl_aulas
    (titulo_aula, url_arqui_aula, fk_tbl_modulos_id_modulo)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (titulo, url, modulo_id))
    conexao.commit()

    print("Aula cadastrada com sucesso!")

    cursor.close()
    conexao.close()


def listar_aulas():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT tbl_aulas.id_aula,
           tbl_aulas.titulo_aula,
           tbl_aulas.url_arqui_aula,
           tbl_modulos.titulo_modulo
    FROM tbl_aulas
    INNER JOIN tbl_modulos
    ON tbl_aulas.fk_tbl_modulos_id_modulo = tbl_modulos.id_modulo
    """

    cursor.execute(sql)
    aulas = cursor.fetchall()

    print("\n===== AULAS =====")
    for aula in aulas:
        print(f"ID: {aula[0]}")
        print(f"Aula: {aula[1]}")
        print(f"Arquivo/URL: {aula[2]}")
        print(f"Módulo: {aula[3]}")
        print("-" * 40)

    cursor.close()
    conexao.close()


def adicionar_material():
    nome = input("Nome do material: ")
    tipo = input("Tipo do material: ")
    tamanho = input("Tamanho do arquivo: ")

    listar_aulas()
    aula_id = int(input("Digite o ID da aula: "))

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO tbl_materiais
    (nome_material, tipo_material, tam_arqu_material, fk_tbl_aulas_id_aula)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (nome, tipo, tamanho, aula_id))
    conexao.commit()

    print("Material cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def listar_materiais():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT tbl_materiais.id_material,
           tbl_materiais.nome_material,
           tbl_materiais.tipo_material,
           tbl_materiais.tam_arqu_material,
           tbl_aulas.titulo_aula
    FROM tbl_materiais
    INNER JOIN tbl_aulas
    ON tbl_materiais.fk_tbl_aulas_id_aula = tbl_aulas.id_aula
    """

    cursor.execute(sql)
    materiais = cursor.fetchall()

    print("\n===== MATERIAIS =====")
    for material in materiais:
        print(f"ID: {material[0]}")
        print(f"Material: {material[1]}")
        print(f"Tipo: {material[2]}")
        print(f"Tamanho: {material[3]}")
        print(f"Aula: {material[4]}")
        print("-" * 40)

    cursor.close()
    conexao.close()


def menu():
    criar_tabelas()

    while True:

        print("\n==============================")
        print("      SISTEMA CORE STUDY")
        print("==============================")
        
        print("1 - Adicionar usuário")
        print("2 - Listar usuários")
        print("3 - Adicionar categoria")
        print("4 - Listar categorias")
        print("5 - Adicionar curso")
        print("6 - Listar cursos")
        print("7 - Adicionar módulo")
        print("8 - Listar módulos")
        print("9 - Adicionar aula")
        print("10 - Listar aulas")
        print("11 - Adicionar material")
        print("12 - Listar materiais")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            adicionar_categoria()
        elif opcao == "4":
            listar_categorias()
        elif opcao == "5":
            adicionar_curso()
        elif opcao == "6":
            listar_cursos()
        elif opcao == "7":
            adicionar_modulo()
        elif opcao == "8":
            listar_modulos()
        elif opcao == "9":
            adicionar_aula()
        elif opcao == "10":
            listar_aulas()
        elif opcao == "11":
            adicionar_material()
        elif opcao == "12":
            listar_materiais()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


menu()