from connection.connection_database import ConexaoDatabase


class SolucaoDao:

    def listar_solucoes(self):
        conexao = ConexaoDatabase()
        comando_sql = "SELECT * FROM tb_solucao"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def carregar_campos_formulario_id(self, id):
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT * FROM tb_solucao WHERE id_solucao={id}"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def cadastrar_solucao_banco(self, solucao, descricao):
        conexao = ConexaoDatabase()
        comando_sql = f"INSERT INTO tb_solucao (solucao, descricao) VALUES ('{solucao}', '{descricao}')"
        conexao.executar_query(comando_sql)

    def alterar_usuario_banco(self, id, solucao, descricao):
        conexao = ConexaoDatabase()
        comando_sql = f"UPDATE tb_solucao SET solucao_solucao='{solucao}', solucao_descricao='{descricao}'" \
                      f"WHERE id_solucao='{id}'"
        conexao.executar_query(comando_sql)

    def excluir_solucao_banco(self, id):
        conexao = ConexaoDatabase()
        comando_sql = f"DELETE FROM tb_solucao WHERE id_solucao={id}"
        conexao.executar_query(comando_sql)
