from flask import Flask, render_template, request, redirect, session, flash
from mysql.connector import IntegrityError
from conexao import conectar

app = Flask(__name__)
app.secret_key = "corestudy_secret_key"

@app.route("/")
def home():
    return render_template("index.html")

def verificar_admin():
    if "tipo_usuario" not in session: return False
    if session["tipo_usuario"] != "ADMIN": return False
    return True

def erro_validacao(mensagem, voltar):
    flash(mensagem, "danger")
    return redirect(voltar)

def campo_vazio(valor): return valor is None or valor.strip() == ""

def carga_hora_valida(carga_hora):
    try: return int(carga_hora) > 0
    except ValueError: return False

def registro_existe(cursor, tabela, coluna, valor):
    cursor.execute(f"SELECT COUNT(*) FROM {tabela} WHERE {coluna} = %s", (valor,))
    return cursor.fetchone()[0] > 0

def email_em_uso(cursor, email, id_usuario=None):
    if id_usuario is None:
        cursor.execute("SELECT COUNT(*) FROM tbl_usuarios WHERE email_usuario = %s", (email,))
    else:
        cursor.execute("SELECT COUNT(*) FROM tbl_usuarios WHERE email_usuario = %s AND id_usuario <> %s", (email, id_usuario))
    return cursor.fetchone()[0] > 0

def categoria_em_uso(cursor, nome_categoria, id_categoria=None):
    if id_categoria is None:
        cursor.execute("SELECT COUNT(*) FROM tbl_categoria WHERE nome_categoria = %s", (nome_categoria,))
    else:
        cursor.execute("SELECT COUNT(*) FROM tbl_categoria WHERE nome_categoria = %s AND id_categoria <> %s", (nome_categoria, id_categoria))
    return cursor.fetchone()[0] > 0

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        if email == "admin" and senha == "admin":
            session["tipo_usuario"] = "ADMIN"
            session["nome_usuario"] = "Administrador"
            session["id_usuario"] = 0
            return redirect("/admin")

        conexao = conectar()
        cursor = conexao.cursor(buffered=True)
        cursor.execute("SELECT id_usuario, nome_usuario FROM tbl_usuarios WHERE email_usuario = %s AND senha_usuario = %s", (email, senha))
        usuario = cursor.fetchone()
        cursor.close()
        conexao.close()

        if usuario:
            session["tipo_usuario"] = "ALUNO"
            session["nome_usuario"] = usuario[1]
            session["id_usuario"] = usuario[0]
            return redirect("/aluno")
        else:
            flash("E-mail ou senha inválidos.", "danger")
            return redirect("/login")

    return render_template("login.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form.get("telefone") # O JS do outro dev envia este campo oculto
        data_nasc = request.form["data_nasc"]
        senha = request.form["senha"]

        conexao = conectar()
        cursor = conexao.cursor()

        if campo_vazio(nome) or campo_vazio(email) or campo_vazio(telefone) or campo_vazio(data_nasc) or campo_vazio(senha):
            cursor.close()
            conexao.close()
            return erro_validacao("Preencha todos os campos.", "/cadastro")

        if len(senha) < 8:
            cursor.close()
            conexao.close()
            return erro_validacao("A senha deve ter no mínimo 8 caracteres.", "/cadastro")

        if email_em_uso(cursor, email):
            cursor.close()
            conexao.close()
            return erro_validacao("Este e-mail já está cadastrado.", "/cadastro")

        cursor.execute("INSERT INTO tbl_usuarios (nome_usuario, email_usuario, telefone_usuario, dt_nasc_usuario, senha_usuario) VALUES (%s, %s, %s, %s, %s)", (nome, email, telefone, data_nasc, senha))
        conexao.commit()
        cursor.close()
        conexao.close()

        flash("Cadastro realizado com sucesso! Faça login.", "success")
        return redirect("/login")

    return render_template("cadastro.html")

@app.route("/admin")
def admin():
    if not verificar_admin(): return redirect("/login")
    return render_template("admin.html", nome_usuario=session["nome_usuario"])

@app.route("/aluno")
def aluno():
    if "tipo_usuario" not in session or session["tipo_usuario"] != "ALUNO": return redirect("/login")
    return render_template("aluno.html", nome_usuario=session["nome_usuario"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# --- MANTIVE AS SUAS ROTAS DO ADMIN EXATAMENTE COMO ESTAVAM, APENAS TROCANDO O RENDER DE ERRO PELO FLASH ---
@app.route("/admin/usuarios")
def usuarios():
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id_usuario, nome_usuario, email_usuario, telefone_usuario, dt_nasc_usuario, dt_cad_usuario FROM tbl_usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template("usuarios.html", usuarios=usuarios)

@app.route("/admin/adicionar-usuario", methods=["GET", "POST"])
def adicionar_usuario_admin():
    if not verificar_admin(): return redirect("/login")
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        data_nasc = request.form["data_nasc"]
        senha = request.form["senha"]
        conexao = conectar()
        cursor = conexao.cursor()
        if campo_vazio(nome) or campo_vazio(email) or campo_vazio(telefone) or campo_vazio(data_nasc) or campo_vazio(senha):
            cursor.close(); conexao.close()
            return erro_validacao("Preencha todos os campos.", "/admin/adicionar-usuario")
        if len(senha) < 8:
            cursor.close(); conexao.close()
            return erro_validacao("A senha deve ter no mínimo 8 caracteres.", "/admin/adicionar-usuario")
        if email_em_uso(cursor, email):
            cursor.close(); conexao.close()
            return erro_validacao("E-mail já cadastrado.", "/admin/adicionar-usuario")
        cursor.execute("INSERT INTO tbl_usuarios (nome_usuario, email_usuario, telefone_usuario, dt_nasc_usuario, senha_usuario) VALUES (%s, %s, %s, %s, %s)", (nome, email, telefone, data_nasc, senha))
        conexao.commit()
        cursor.close(); conexao.close()
        flash("Usuário cadastrado!", "success")
        return redirect("/admin/usuarios")
    return render_template("adicionar_usuario.html")

@app.route("/admin/editar-usuario/<int:id_usuario>", methods=["GET", "POST"])
def editar_usuario_admin(id_usuario):
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        data_nasc = request.form["data_nasc"]
        senha = request.form["senha"]
        if campo_vazio(nome) or campo_vazio(email) or campo_vazio(telefone) or campo_vazio(data_nasc) or campo_vazio(senha):
            cursor.close(); conexao.close()
            return erro_validacao("Preencha todos os campos.", f"/admin/editar-usuario/{id_usuario}")
        if len(senha) < 8:
            cursor.close(); conexao.close()
            return erro_validacao("A senha deve ter no mínimo 8 caracteres.", f"/admin/editar-usuario/{id_usuario}")
        if email_em_uso(cursor, email, id_usuario):
            cursor.close(); conexao.close()
            return erro_validacao("E-mail já cadastrado para outro.", f"/admin/editar-usuario/{id_usuario}")
        cursor.execute("UPDATE tbl_usuarios SET nome_usuario=%s, email_usuario=%s, telefone_usuario=%s, dt_nasc_usuario=%s, senha_usuario=%s WHERE id_usuario=%s", (nome, email, telefone, data_nasc, senha, id_usuario))
        conexao.commit()
        cursor.close(); conexao.close()
        flash("Usuário atualizado!", "success")
        return redirect("/admin/usuarios")
    cursor.execute("SELECT id_usuario, nome_usuario, email_usuario, telefone_usuario, dt_nasc_usuario, senha_usuario FROM tbl_usuarios WHERE id_usuario = %s", (id_usuario,))
    usuario = cursor.fetchone()
    cursor.close()
    conexao.close()
    return render_template("editar_usuario.html", usuario=usuario)

@app.route("/admin/excluir-usuario/<int:id_usuario>", methods=["POST"])
def excluir_usuario_admin(id_usuario):
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tbl_usuarios WHERE id_usuario = %s", (id_usuario,))
    conexao.commit()
    cursor.close()
    conexao.close()
    flash("Usuário excluído!", "danger")
    return redirect("/admin/usuarios")

@app.route("/cursos")
def cursos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tbl_cursos")
    cursos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template("cursos.html", cursos=cursos, admin=False)

@app.route("/admin/cursos")
def cursos_admin():
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT tbl_cursos.id_curso, tbl_cursos.titulo_curso, tbl_cursos.descricao_curso, tbl_cursos.carga_hora_curso, tbl_categoria.nome_categoria FROM tbl_cursos LEFT JOIN tbl_categoria ON tbl_cursos.fk_tbl_categoria_id_categoria = tbl_categoria.id_categoria")
    cursos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template("cursos.html", cursos=cursos, admin=True)

@app.route("/admin/adicionar-curso", methods=["GET", "POST"])
def adicionar_curso():
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    if request.method == "POST":
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        carga_hora = request.form["carga_hora"]
        categoria_id = request.form["categoria_id"]
        if campo_vazio(titulo) or campo_vazio(descricao):
            cursor.close(); conexao.close()
            return erro_validacao("Preencha título e descrição.", "/admin/adicionar-curso")
        cursor.execute("INSERT INTO tbl_cursos (titulo_curso, descricao_curso, carga_hora_curso, fk_tbl_categoria_id_categoria) VALUES (%s, %s, %s, %s)", (titulo, descricao, carga_hora, categoria_id))
        conexao.commit()
        cursor.close(); conexao.close()
        flash("Curso cadastrado!", "success")
        return redirect("/admin/cursos")
    cursor.execute("SELECT id_categoria, nome_categoria FROM tbl_categoria")
    categorias = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template("adicionar_curso.html", categorias=categorias)

@app.route("/admin/editar-curso/<int:id_curso>", methods=["GET", "POST"])
def editar_curso(id_curso):
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    if request.method == "POST":
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        carga_hora = request.form["carga_hora"]
        categoria_id = request.form["categoria_id"]
        cursor.execute("UPDATE tbl_cursos SET titulo_curso=%s, descricao_curso=%s, carga_hora_curso=%s, fk_tbl_categoria_id_categoria=%s WHERE id_curso=%s", (titulo, descricao, carga_hora, categoria_id, id_curso))
        conexao.commit()
        cursor.close(); conexao.close()
        flash("Curso atualizado!", "success")
        return redirect("/admin/cursos")
    cursor.execute("SELECT id_curso, titulo_curso, descricao_curso, carga_hora_curso, fk_tbl_categoria_id_categoria FROM tbl_cursos WHERE id_curso = %s", (id_curso,))
    curso = cursor.fetchone()
    cursor.execute("SELECT id_categoria, nome_categoria FROM tbl_categoria")
    categorias = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template("editar_curso.html", curso=curso, categorias=categorias)

@app.route("/admin/excluir-curso/<int:id_curso>", methods=["POST"])
def excluir_curso(id_curso):
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM tbl_cursos WHERE id_curso = %s", (id_curso,))
        conexao.commit()
        flash("Curso excluído!", "danger")
    except IntegrityError:
        flash("Exclua os módulos vinculados primeiro.", "danger")
    finally:
        cursor.close()
        conexao.close()
    return redirect("/admin/cursos")

@app.route("/admin/categorias")
def categorias():
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id_categoria, nome_categoria FROM tbl_categoria")
    categorias = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template("categorias.html", categorias=categorias)

@app.route("/admin/adicionar-categoria", methods=["GET", "POST"])
def adicionar_categoria():
    if not verificar_admin(): return redirect("/login")
    if request.method == "POST":
        nome_categoria = request.form["nome_categoria"]
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO tbl_categoria (nome_categoria) VALUES (%s)", (nome_categoria,))
        conexao.commit()
        cursor.close(); conexao.close()
        flash("Categoria cadastrada!", "success")
        return redirect("/admin/categorias")
    return render_template("adicionar_categoria.html")

@app.route("/admin/editar-categoria/<int:id_categoria>", methods=["GET", "POST"])
def editar_categoria(id_categoria):
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    if request.method == "POST":
        nome_categoria = request.form["nome_categoria"]
        cursor.execute("UPDATE tbl_categoria SET nome_categoria=%s WHERE id_categoria=%s", (nome_categoria, id_categoria))
        conexao.commit()
        cursor.close(); conexao.close()
        flash("Categoria atualizada!", "success")
        return redirect("/admin/categorias")
    cursor.execute("SELECT id_categoria, nome_categoria FROM tbl_categoria WHERE id_categoria = %s", (id_categoria,))
    categoria = cursor.fetchone()
    cursor.close()
    conexao.close()
    return render_template("editar_categoria.html", categoria=categoria)

@app.route("/admin/excluir-categoria/<int:id_categoria>", methods=["POST"])
def excluir_categoria(id_categoria):
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM tbl_categoria WHERE id_categoria = %s", (id_categoria,))
        conexao.commit()
        flash("Categoria excluída!", "danger")
    except IntegrityError:
        flash("Exclua os cursos vinculados primeiro.", "danger")
    finally:
        cursor.close()
        conexao.close()
    return redirect("/admin/categorias")

@app.route("/admin/modulos")
def modulos():
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT m.id_modulo, m.titulo_modulo, c.titulo_curso FROM tbl_modulos m INNER JOIN tbl_cursos c ON m.fk_tbl_cursos_id_curso = c.id_curso")
    modulos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template("modulos.html", modulos=modulos)

@app.route("/admin/adicionar-modulo", methods=["GET", "POST"])
def adicionar_modulo():
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    if request.method == "POST":
        titulo = request.form["titulo"]
        curso_id = request.form["curso_id"]
        cursor.execute("INSERT INTO tbl_modulos (titulo_modulo, fk_tbl_cursos_id_curso) VALUES (%s, %s)", (titulo, curso_id))
        conexao.commit()
        cursor.close(); conexao.close()
        flash("Módulo cadastrado!", "success")
        return redirect("/admin/modulos")
    cursor.execute("SELECT id_curso, titulo_curso FROM tbl_cursos")
    cursos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template("adicionar_modulo.html", cursos=cursos)

@app.route("/admin/editar-modulo/<int:id_modulo>", methods=["GET", "POST"])
def editar_modulo(id_modulo):
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    if request.method == "POST":
        titulo = request.form["titulo"]
        curso_id = request.form["curso_id"]
        cursor.execute("UPDATE tbl_modulos SET titulo_modulo=%s, fk_tbl_cursos_id_curso=%s WHERE id_modulo=%s", (titulo, curso_id, id_modulo))
        conexao.commit()
        cursor.close(); conexao.close()
        flash("Módulo atualizado!", "success")
        return redirect("/admin/modulos")
    cursor.execute("SELECT id_modulo, titulo_modulo, fk_tbl_cursos_id_curso FROM tbl_modulos WHERE id_modulo = %s", (id_modulo,))
    modulo = cursor.fetchone()
    cursor.execute("SELECT id_curso, titulo_curso FROM tbl_cursos")
    cursos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template("editar_modulo.html", modulo=modulo, cursos=cursos)

@app.route("/admin/excluir-modulo/<int:id_modulo>", methods=["POST"])
def excluir_modulo(id_modulo):
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM tbl_modulos WHERE id_modulo = %s", (id_modulo,))
        conexao.commit()
        flash("Módulo excluído!", "danger")
    except IntegrityError:
        flash("Exclua as aulas vinculadas primeiro.", "danger")
    finally:
        cursor.close()
        conexao.close()
    return redirect("/admin/modulos")

@app.route("/admin/aulas")
def aulas():
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT a.id_aula, a.titulo_aula, a.url_arqui_aula, m.titulo_modulo, c.titulo_curso FROM tbl_aulas a INNER JOIN tbl_modulos m ON a.fk_tbl_modulos_id_modulo = m.id_modulo INNER JOIN tbl_cursos c ON m.fk_tbl_cursos_id_curso = c.id_curso")
    aulas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template("aulas.html", aulas=aulas)

@app.route("/admin/adicionar-aula", methods=["GET", "POST"])
def adicionar_aula():
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    if request.method == "POST":
        titulo = request.form["titulo"]
        url = request.form["url"]
        modulo_id = request.form["modulo_id"]
        cursor.execute("INSERT INTO tbl_aulas (titulo_aula, url_arqui_aula, fk_tbl_modulos_id_modulo) VALUES (%s, %s, %s)", (titulo, url, modulo_id))
        conexao.commit()
        cursor.close(); conexao.close()
        flash("Aula cadastrada!", "success")
        return redirect("/admin/aulas")
    cursor.execute("SELECT m.id_modulo, m.titulo_modulo, c.titulo_curso FROM tbl_modulos m INNER JOIN tbl_cursos c ON m.fk_tbl_cursos_id_curso = c.id_curso")
    modulos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template("adicionar_aula.html", modulos=modulos)

@app.route("/admin/editar-aula/<int:id_aula>", methods=["GET", "POST"])
def editar_aula(id_aula):
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    if request.method == "POST":
        titulo = request.form["titulo"]
        url = request.form["url"]
        modulo_id = request.form["modulo_id"]
        cursor.execute("UPDATE tbl_aulas SET titulo_aula=%s, url_arqui_aula=%s, fk_tbl_modulos_id_modulo=%s WHERE id_aula=%s", (titulo, url, modulo_id, id_aula))
        conexao.commit()
        cursor.close(); conexao.close()
        flash("Aula atualizada!", "success")
        return redirect("/admin/aulas")
    cursor.execute("SELECT id_aula, titulo_aula, url_arqui_aula, fk_tbl_modulos_id_modulo FROM tbl_aulas WHERE id_aula = %s", (id_aula,))
    aula = cursor.fetchone()
    cursor.execute("SELECT m.id_modulo, m.titulo_modulo, c.titulo_curso FROM tbl_modulos m INNER JOIN tbl_cursos c ON m.fk_tbl_cursos_id_curso = c.id_curso")
    modulos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template("editar_aula.html", aula=aula, modulos=modulos)

@app.route("/admin/excluir-aula/<int:id_aula>", methods=["POST"])
def excluir_aula(id_aula):
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM tbl_aulas WHERE id_aula = %s", (id_aula,))
        conexao.commit()
        flash("Aula excluída!", "danger")
    except IntegrityError:
        flash("Exclua os materiais vinculados primeiro.", "danger")
    finally:
        cursor.close()
        conexao.close()
    return redirect("/admin/aulas")

@app.route("/admin/materiais")
def materiais():
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT m.id_material, m.nome_material, m.tipo_material, m.tam_arqu_material, a.titulo_aula FROM tbl_materiais m INNER JOIN tbl_aulas a ON m.fk_tbl_aulas_id_aula = a.id_aula")
    materiais = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template("materiais.html", materiais=materiais)

@app.route("/admin/adicionar-material", methods=["GET", "POST"])
def adicionar_material():
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    if request.method == "POST":
        nome = request.form["nome"]
        tipo = request.form["tipo"]
        tamanho = request.form["tamanho"]
        aula_id = request.form["aula_id"]
        cursor.execute("INSERT INTO tbl_materiais (nome_material, tipo_material, tam_arqu_material, fk_tbl_aulas_id_aula) VALUES (%s, %s, %s, %s)", (nome, tipo, tamanho, aula_id))
        conexao.commit()
        cursor.close(); conexao.close()
        flash("Material cadastrado!", "success")
        return redirect("/admin/materiais")
    cursor.execute("SELECT id_aula, titulo_aula FROM tbl_aulas")
    aulas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template("adicionar_material.html", aulas=aulas)

@app.route("/admin/editar-material/<int:id_material>", methods=["GET", "POST"])
def editar_material(id_material):
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    if request.method == "POST":
        nome = request.form["nome"]
        tipo = request.form["tipo"]
        tamanho = request.form["tamanho"]
        aula_id = request.form["aula_id"]
        cursor.execute("UPDATE tbl_materiais SET nome_material=%s, tipo_material=%s, tam_arqu_material=%s, fk_tbl_aulas_id_aula=%s WHERE id_material=%s", (nome, tipo, tamanho, aula_id, id_material))
        conexao.commit()
        cursor.close(); conexao.close()
        flash("Material atualizado!", "success")
        return redirect("/admin/materiais")
    cursor.execute("SELECT id_material, nome_material, tipo_material, tam_arqu_material, fk_tbl_aulas_id_aula FROM tbl_materiais WHERE id_material = %s", (id_material,))
    material = cursor.fetchone()
    cursor.execute("SELECT id_aula, titulo_aula FROM tbl_aulas")
    aulas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template("editar_material.html", material=material, aulas=aulas)

@app.route("/admin/excluir-material/<int:id_material>", methods=["POST"])
def excluir_material(id_material):
    if not verificar_admin(): return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tbl_materiais WHERE id_material = %s", (id_material,))
    conexao.commit()
    cursor.close()
    conexao.close()
    flash("Material excluído!", "danger")
    return redirect("/admin/materiais")

@app.route("/trilha/curso/<int:id_curso>")
def visualizar_curso(id_curso):
    if "tipo_usuario" not in session: return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT titulo_curso, descricao_curso FROM tbl_cursos WHERE id_curso = %s", (id_curso,))
    curso = cursor.fetchone()
    cursor.execute("SELECT id_modulo, titulo_modulo FROM tbl_modulos WHERE fk_tbl_cursos_id_curso = %s", (id_curso,))
    modulos = cursor.fetchall()
    cursor.close(); conexao.close()
    return render_template("curso_aluno.html", curso=curso, modulos=modulos, nome_usuario=session["nome_usuario"])

@app.route("/trilha/modulo/<int:id_modulo>")
def visualizar_modulo(id_modulo):
    if "tipo_usuario" not in session: return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT titulo_modulo FROM tbl_modulos WHERE id_modulo = %s", (id_modulo,))
    modulo = cursor.fetchone()
    cursor.execute("SELECT id_aula, titulo_aula, url_arqui_aula FROM tbl_aulas WHERE fk_tbl_modulos_id_modulo = %s", (id_modulo,))
    aulas = cursor.fetchall()
    cursor.close(); conexao.close()
    return render_template("modulo_aluno.html", modulo=modulo, aulas=aulas, nome_usuario=session["nome_usuario"])

@app.route("/trilha/aula/<int:id_aula>")
def visualizar_aula(id_aula):
    if "tipo_usuario" not in session: return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT titulo_aula, url_arqui_aula FROM tbl_aulas WHERE id_aula = %s", (id_aula,))
    aula = cursor.fetchone()
    cursor.execute("SELECT nome_material, tipo_material, tam_arqu_material FROM tbl_materiais WHERE fk_tbl_aulas_id_aula = %s", (id_aula,))
    materiais = cursor.fetchall()
    cursor.close(); conexao.close()
    return render_template("aula_aluno.html", aula=aula, materiais=materiais, nome_usuario=session["nome_usuario"])

@app.route("/trilha")
def trilha():
    if "tipo_usuario" not in session: return redirect("/login")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT tbl_cursos.id_curso, tbl_cursos.titulo_curso, tbl_cursos.descricao_curso, tbl_cursos.carga_hora_curso, tbl_categoria.nome_categoria FROM tbl_cursos LEFT JOIN tbl_categoria ON tbl_cursos.fk_tbl_categoria_id_categoria = tbl_categoria.id_categoria ORDER BY tbl_categoria.nome_categoria ASC, tbl_cursos.titulo_curso ASC")
    cursos = cursor.fetchall()
    cursos_por_categoria = []
    for curso in cursos:
        nome_categoria = curso[4] or "Sem categoria"
        if not cursos_por_categoria or cursos_por_categoria[-1]["nome_categoria"] != nome_categoria:
            cursos_por_categoria.append({"nome_categoria": nome_categoria, "cursos": []})
        cursos_por_categoria[-1]["cursos"].append(curso)
    cursor.close(); conexao.close()
    return render_template("trilha.html", cursos_por_categoria=cursos_por_categoria, nome_usuario=session["nome_usuario"])

if __name__ == "__main__":
    app.run(debug=True)