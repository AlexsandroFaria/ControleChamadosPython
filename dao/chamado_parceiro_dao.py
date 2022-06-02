from connection.connection_database import ConexaoDatabase


class ChamadoParceiroDao:

    def consultar_numero_chamado_para_combo(self):
        conexao = ConexaoDatabase()
        comando_sql = "SELECT numero_chamado FROM tb_chamado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def consultar_nome_parceiro_para_combo(self):
        conexao = ConexaoDatabase()
        comando_sql = "SELECT nome_parceiro FROM tb_parceiro"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def consultar_nome_cliente_para_combo(self):
        conexao = ConexaoDatabase()
        comando_sql = "SELECT nome_cliente FROM tb_cliente"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def listar_chamado_parceiro_banco(self):
        conexao = ConexaoDatabase()
        comando_sql = "SELECT numero_chamado_parceiro, chamado_simpress, empresa_parceira, responsavel_parceiro," \
                      "nome_cliente, problema_chamado_parceiro, observacao_chamado_parceiro, " \
                      "data_abertura_chamado_parceiro FROM tb_chamado_parceiro"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def cadastrar_chamado_parceiro_banco(self, numero_chamado, chamado_simpress, empresa, responsavel, nome_cliente,
                                         problema, observacao, data_abertura):
        conexao = ConexaoDatabase()
        comando_sql = f"INSERT INTO tb_chamado_parceiro (numero_chamado_parceiro, chamado_simpress, empresa_parceira," \
                      f"responsavel_parceiro, nome_cliente, problema_chamado_parceiro, observacao_chamado_parceiro," \
                      f"data_abertura_chamado_parceiro) VALUES ({numero_chamado}, {chamado_simpress}, '{empresa}'," \
                      f"'{responsavel}', '{nome_cliente}', '{problema}', '{observacao}', '{data_abertura}')"
        conexao.executar_query(comando_sql)
