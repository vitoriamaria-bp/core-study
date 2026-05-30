import mysql.connector
from conexao import conectar

def popular_banco():
    conexao = None
    cursor = None
    try:
        # Usa o seu próprio arquivo conexao.py
        conexao = conectar()
        cursor = conexao.cursor()

        print("Iniciando inserção da trilha de teste...")

        # 1. Cria a Categoria
        cursor.execute("INSERT INTO tbl_categoria (nome_categoria) VALUES (%s)", ('Tecnologia e Desenvolvimento',))
        id_cat = cursor.lastrowid

        # 2. Cria o Curso
        query_curso = """
            INSERT INTO tbl_cursos (titulo_curso, descricao_curso, carga_hora_curso, fk_tbl_categoria_id_categoria) 
            VALUES (%s, %s, %s, %s)
        """
        valores_curso = ('Desenvolvimento Python Profissional', 'Aprenda a criar estruturas robustas para a web, com foco em bancos de dados e boas práticas.', 40, id_cat)
        cursor.execute(query_curso, valores_curso)
        id_curso = cursor.lastrowid

        # 3. Cria os Módulos vinculados ao Curso
        cursor.execute("INSERT INTO tbl_modulos (titulo_modulo, fk_tbl_cursos_id_curso) VALUES (%s, %s)", ('Módulo 1: Lógica e Estrutura', id_curso))
        id_mod1 = cursor.lastrowid

        cursor.execute("INSERT INTO tbl_modulos (titulo_modulo, fk_tbl_cursos_id_curso) VALUES (%s, %s)", ('Módulo 2: Integração com Banco de Dados', id_curso))
        id_mod2 = cursor.lastrowid

        # 4. Cria as Aulas (Com links reais do YouTube)
        query_aula = "INSERT INTO tbl_aulas (titulo_aula, url_arqui_aula, fk_tbl_modulos_id_modulo) VALUES (%s, %s, %s)"
        
        # Aulas Módulo 1
        cursor.execute(query_aula, ('Aula 1: Introdução ao Ambiente', 'https://www.youtube.com/watch?v=kYJzXFexDjc', id_mod1))
        id_aula1 = cursor.lastrowid
        
        cursor.execute(query_aula, ('Aula 2: Estruturas de Repetição', 'https://www.youtube.com/watch?v=1IsL6g2ixak', id_mod1))
        
        # Aula Módulo 2
        cursor.execute(query_aula, ('Aula 3: Modelagem Relacional e SQL', 'https://www.youtube.com/watch?v=Ofkqj1uibkw', id_mod2))
        id_aula3 = cursor.lastrowid

        # 5. Anexa os Materiais nas Aulas
        query_material = "INSERT INTO tbl_materiais (nome_material, tipo_material, tam_arqu_material, fk_tbl_aulas_id_aula) VALUES (%s, %s, %s, %s)"
        materiais = [
            ('Guia de Instalação do Ambiente', 'PDF', '2.5 MB', id_aula1),
            ('Script SQL - Criação de Tabelas', 'SQL', '12 KB', id_aula3),
            ('Dicionário de Dados', 'XLSX', '45 KB', id_aula3)
        ]
        cursor.executemany(query_material, materiais)

        # Salva as alterações
        conexao.commit()
        print("Sucesso! Trilha cadastrada perfeitamente. Pode abrir a vitrine do aluno e testar.")

    except mysql.connector.Error as err:
        if conexao:
            conexao.rollback() # Desfaz se der erro
        print(f"Erro no banco de dados ao tentar popular: {err}")
    except Exception as e:
        if conexao:
            conexao.rollback()
        print(f"Erro interno: {e}")
    finally:
        if cursor: cursor.close()
        if conexao: conexao.close()

if __name__ == "__main__":
    popular_banco()