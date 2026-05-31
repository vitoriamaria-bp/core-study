from datetime import date, datetime
from decimal import Decimal

from conexao import conectar


ARQUIVO_SAIDA = "inserts_dados.sql"

TABELAS = [
    "tbl_categoria",
    "tbl_usuarios",
    "tbl_cursos",
    "tbl_modulos",
    "tbl_aulas",
    "tbl_materiais",
]

CHAVES_PRIMARIAS = {
    "tbl_categoria": "id_categoria",
    "tbl_usuarios": "id_usuario",
    "tbl_cursos": "id_curso",
    "tbl_modulos": "id_modulo",
    "tbl_aulas": "id_aula",
    "tbl_materiais": "id_material",
}

CHAVES_ESTRANGEIRAS = {
    "tbl_cursos": {
        "fk_tbl_categoria_id_categoria": "tbl_categoria",
    },
    "tbl_modulos": {
        "fk_tbl_cursos_id_curso": "tbl_cursos",
    },
    "tbl_aulas": {
        "fk_tbl_modulos_id_modulo": "tbl_modulos",
    },
    "tbl_materiais": {
        "fk_tbl_aulas_id_aula": "tbl_aulas",
    },
}


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


def buscar_dados(cursor, tabela):
    chave_primaria = CHAVES_PRIMARIAS[tabela]
    cursor.execute(f"SELECT * FROM `{tabela}` ORDER BY `{chave_primaria}`")
    dados = cursor.fetchall()
    colunas = [descricao[0] for descricao in cursor.description]
    return colunas, dados


def remapear_linha(tabela, colunas, linha, mapas_ids, proximo_id):
    linha_remapeada = list(linha)
    chave_primaria = CHAVES_PRIMARIAS[tabela]
    indice_pk = colunas.index(chave_primaria)
    id_original = linha_remapeada[indice_pk]

    mapas_ids[tabela][id_original] = proximo_id
    linha_remapeada[indice_pk] = proximo_id

    for coluna_fk, tabela_referencia in CHAVES_ESTRANGEIRAS.get(tabela, {}).items():
        indice_fk = colunas.index(coluna_fk)
        id_referencia_original = linha_remapeada[indice_fk]
        linha_remapeada[indice_fk] = mapas_ids[tabela_referencia][id_referencia_original]

    return linha_remapeada


def main():
    conexao = conectar()

    if conexao is None:
        print("Nao foi possivel conectar ao MySQL.")
        return

    cursor = conexao.cursor()
    mapas_ids = {tabela: {} for tabela in TABELAS}

    linhas_sql = [
        "-- Inserts gerados a partir dos dados reais do MySQL",
        "-- IDs remapeados para iniciar em 1 de forma sequencial por tabela",
        "-- Banco original: db_core_study1",
        "",
        "SET FOREIGN_KEY_CHECKS = 0;",
        "",
    ]

    for tabela in TABELAS:
        colunas, dados = buscar_dados(cursor, tabela)
        linhas_sql.append(f"-- Dados da tabela {tabela}")

        if dados:
            for proximo_id, linha in enumerate(dados, start=1):
                linha_remapeada = remapear_linha(tabela, colunas, linha, mapas_ids, proximo_id)
                linhas_sql.append(gerar_insert(tabela, colunas, linha_remapeada))
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
