from connection.connection_database import ConexaoDatabase


class ParceiroDao:

    def listar_prceiro(self):
        conexao = ConexaoDatabase()
        comando_sql = "SELECT * FROM tb_parceiro"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def cadastrar_parceiro_banco(self, nome, contato, telefone):
        conexao = ConexaoDatabase()
        comando_sql = f"INSERT INTO tb_parceiro (nome_parceiro, contato_parceiro, telefone_parceiro) VALUES " \
                      f"('{nome}', '{contato}', '{telefone}')"
        conexao.executar_query(comando_sql)