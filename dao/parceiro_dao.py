from connection.connection_database import ConexaoDatabase


class ParceiroDao:

    def listar_prceiro(self):
        conexao = ConexaoDatabase()
        comando_sql = "SELECT * FROM t_parceiro"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado