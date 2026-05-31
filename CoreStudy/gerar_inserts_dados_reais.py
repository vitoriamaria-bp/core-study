from datetime import date, datetime
from decimal import Decimal

from conexao import conectar


ARQUIVO_SAIDA = "inserts_dados_reais.sql"

TABELAS = [
    "tbl_categoria",
    "tbl_usuarios",
    "tbl_cursos",
    "tbl_modulos",
    "tbl_aulas",
    "tbl_materiais",
]


def formatar_valor(valor):
    if valor is None:
        return "NULL"
    if isinstance(valor, bool):
        return "1" if valor else "0"
    if isinstance(valor, (int, float, Decimal)):
        return str(valor)
    if isinstance(valor, (date, datetime)):
        return f"'{valor.strftime('%Y-%m-%d')}'"

    texto = str(valor)
    texto = texto.replace("\\", "\\\\").replace("'", "''")
    return f"'{texto}'"


def gerar_insert(tabela, colunas, linha):
    nomes_colunas = ", ".join(f"`{coluna}`" for coluna in colunas)
    valores = ", ".join(formatar_valor(valor) for valor in linha)
    return f"INSERT INTO `{tabela}` ({nomes_colunas}) VALUES ({valores});"


def main():
    conexao = conectar()

    if conexao is None:
        print("Nao foi possivel conectar ao MySQL.")
        return

    cursor = conexao.cursor()
    linhas_sql = [
        "-- Inserts gerados a partir dos dados reais do MySQL",
        "-- Banco: db_core_study1",
        "",
        "SET FOREIGN_KEY_CHECKS = 0;",
        "",
    ]

    for tabela in TABELAS:
        cursor.execute(f"SELECT * FROM `{tabela}`")
        dados = cursor.fetchall()
        colunas = [descricao[0] for descricao in cursor.description]

        linhas_sql.append(f"-- Dados da tabela {tabela}")

        if dados:
            for linha in dados:
                linhas_sql.append(gerar_insert(tabela, colunas, linha))
        else:
            linhas_sql.append(f"-- Nenhum registro encontrado em {tabela}.")

        linhas_sql.append("")

    linhas_sql.extend([
        "SET FOREIGN_KEY_CHECKS = 1;",
        "",
    ])

    with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as arquivo:
        arquivo.write("\n".join(linhas_sql))

    cursor.close()
    conexao.close()

    print(f"Arquivo gerado: {ARQUIVO_SAIDA}")


if __name__ == "__main__":
    main()
