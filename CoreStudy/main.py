from conexao import criar_tabelas
from login import logar_sistema
from operacoes import *

def menu_admin():
    while True:
        print("\n========================================")
        print("         PAINEL ADMINISTRATIVO          ")
        print("========================================")
        print("1 - Gerenciar Usuários")
        print("2 - Gerenciar Categorias")
        print("3 - Gerenciar Cursos")
        print("4 - Gerenciar Módulos")
        print("5 - Gerenciar Aulas")
        print("6 - Gerenciar Materiais")
        print("0 - Fazer Logout")
        print("========================================")
        op = input("Escolha uma opção: ")
        if op == "1": submenu_usuarios()
        elif op == "2": submenu_categorias()
        elif op == "3": submenu_cursos()
        elif op == "4": submenu_modulos()
        elif op == "5": submenu_aulas()
        elif op == "6": submenu_materiais()
        elif op == "0": break

def submenu_usuarios():
    while True:
        print("\n=== GERENCIAR USUÁRIOS ===")
        print("1 - Listar Usuários")
        print("0 - Voltar")
        op = input("Escolha: ")
        if op == "1": listar_usuarios()
        elif op == "0": break

def submenu_categorias():
    while True:
        print("\n=== GERENCIAR CATEGORIAS ===")
        print("1 - Adicionar Categoria")
        print("2 - Listar Categorias")
        print("3 - Editar Categoria")
        print("4 - Excluir Categoria")
        print("0 - Voltar")
        op = input("Escolha: ")
        if op == "1": adicionar_categoria()
        elif op == "2": listar_categorias()
        elif op == "3": editar_categoria()
        elif op == "4": excluir_categoria()
        elif op == "0": break

def submenu_cursos():
    while True:
        print("\n=== GERENCIAR CURSOS ===")
        print("1 - Adicionar Curso")
        print("2 - Listar Cursos")
        print("3 - Editar Curso")
        print("4 - Excluir Curso")
        print("0 - Voltar")
        op = input("Escolha: ")
        if op == "1": adicionar_curso()
        elif op == "2": listar_cursos()
        elif op == "3": editar_curso()
        elif op == "4": excluir_curso()
        elif op == "0": break

def submenu_modulos():
    while True:
        print("\n=== GERENCIAR MÓDULOS ===")
        print("1 - Adicionar Módulo")
        print("2 - Listar Módulos")
        print("3 - Editar Módulo")
        print("4 - Excluir Módulo")
        print("0 - Voltar")
        op = input("Escolha: ")
        if op == "1": adicionar_modulo()
        elif op == "2": listar_modulos()
        elif op == "3": editar_modulo()
        elif op == "4": excluir_modulo()
        elif op == "0": break

def submenu_aulas():
    while True:
        print("\n=== GERENCIAR AULAS ===")
        print("1 - Adicionar Aula")
        print("2 - Listar Aulas")
        print("3 - Editar Aula")
        print("4 - Excluir Aula")
        print("0 - Voltar")
        op = input("Escolha: ")
        if op == "1": adicionar_aula()
        elif op == "2": listar_aulas()
        elif op == "3": editar_aula()
        elif op == "4": excluir_aula()
        elif op == "0": break

def submenu_materiais():
    while True:
        print("\n=== GERENCIAR MATERIAIS ===")
        print("1 - Adicionar Material")
        print("2 - Listar Materiais")
        print("3 - Editar Material")
        print("4 - Excluir Material")
        print("0 - Voltar")
        op = input("Escolha: ")
        if op == "1": adicionar_material()
        elif op == "2": listar_materiais()
        elif op == "3": editar_material()
        elif op == "4": excluir_material()
        elif op == "0": break

def menu_aluno(id_u, nome):
    while True:
        print(f"\n=== ÁREA DO ALUNO: {nome} ===")
        print("1 - Catálogo de Cursos")
        print("2 - Gerenciar Perfil")
        print("0 - Fazer Logout")
        op = input("Escolha: ")
        if op == "1":
            listar_cursos()
            cid = input("ID do curso: ")
            ver_curso_completo(cid)
        elif op == "2":
            while True:
                print("\n=== PERFIL ===")
                print("1 - Visualizar | 2 - Editar | 3 - Excluir | 0 - Voltar")
                sub = input("Escolha: ")
                if sub == "1": visualizar_perfil(id_u)
                elif sub == "2": editar_perfil(id_u)
                elif sub == "3": 
                    if excluir_conta(id_u): return
                elif sub == "0": break
        elif op == "0": break

def menu_principal():
    criar_tabelas()
    while True:
        print("\n=== CORE STUDY ===")
        print("1 - Cadastrar Aluno | 2 - Logar | 0 - Sair")
        op = input("Opção: ")
        if op == "1": adicionar_usuario()
        elif op == "2":
            p, n, id_u = logar_sistema()
            if p == "ADMIN": menu_admin()
            elif p == "ALUNO": menu_aluno(id_u, n)
        elif op == "0": break

if __name__ == "__main__":
    menu_principal()