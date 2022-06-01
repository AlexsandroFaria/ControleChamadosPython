from connection.connection_database import ConexaoDatabase


class FecharChamadoDao:

    def listar_chamado_fechado_tabela_banco(self):
        conexao = ConexaoDatabase()
        comando_sql = "SELECT numero_chamado_fechado, contrato_chamado_fechado, nome_cliente_chamado_fechado," \
                      "contato_chamado_fechado, telefone_chamado_fechado, problema_chamado_fechado," \
                      "tipo_chamado_fechado, solucao_chamado_fechado, status_chamado_fechado," \
                      "data_chamado_fechado FROM tb_chamado_fechado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def consultar_numero_chamado_formulario(self, numero):
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, contato_chamado," \
                      f"telefone_chamado, problema_chamado, tipo_chamado FROM tb_chamado WHERE numero_chamado={numero}"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def fechar_chamado(self, numero, contrato, nome_cliente, contato, telefone, problema, tipo, fechamento, status,
                       data_fechamento):
        conexao = ConexaoDatabase()
        comando_sql = f"INSERT INTO tb_chamado_fechado (numero_chamado_fechado, contrato_chamado_fechado," \
                      f"nome_cliente_chamado_fechado, contato_chamado_fechado, telefone_chamado_fechado, " \
                      f"problema_chamado_fechado, tipo_chamado_fechado, solucao_chamado_fechado," \
                      f"status_chamado_fechado, data_chamado_fechado) VALUES ({numero}, {contrato}, '{nome_cliente}'," \
                      f"'{contato}', '{telefone}', '{problema}', '{tipo}', '{fechamento}', '{status}'," \
                      f"'{data_fechamento}')"
        conexao.executar_query(comando_sql)

    def listar_chamado_por_numero_banco(self, numero_chamado):
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado_fechado, contrato_chamado_fechado, nome_cliente_chamado_fechado," \
                      f"contato_chamado_fechado, telefone_chamado_fechado, problema_chamado_fechado," \
                      f"tipo_chamado_fechado, solucao_chamado_fechado, status_chamado_fechado," \
                      f"data_chamado_fechado FROM tb_chamado_fechado WHERE numero_chamado_fechado={numero_chamado}"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def consultar_chamado_fechado_por_numero_tabela(self, numero_chamado):
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado_fechado, contrato_chamado_fechado, nome_cliente_chamado_fechado," \
                      f"contato_chamado_fechado, telefone_chamado_fechado, problema_chamado_fechado," \
                      f"tipo_chamado_fechado, solucao_chamado_fechado, status_chamado_fechado," \
                      f"data_chamado_fechado FROM tb_chamado_fechado WHERE numero_chamado_fechado LIKE '%{numero_chamado}%'"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def consultar_chamado_fechado_por_contrato_tabela(self, numero_contrato):
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado_fechado, contrato_chamado_fechado, nome_cliente_chamado_fechado," \
                      f"contato_chamado_fechado, telefone_chamado_fechado, problema_chamado_fechado," \
                      f"tipo_chamado_fechado, solucao_chamado_fechado, status_chamado_fechado," \
                      f"data_chamado_fechado FROM tb_chamado_fechado WHERE contrato_chamado_fechado LIKE '%{numero_contrato}%'"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def consultar_chamado_fechado_por_nome_cliente_tabela(self, nome_cliente):
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado_fechado, contrato_chamado_fechado, nome_cliente_chamado_fechado," \
                      f"contato_chamado_fechado, telefone_chamado_fechado, problema_chamado_fechado," \
                      f"tipo_chamado_fechado, solucao_chamado_fechado, status_chamado_fechado," \
                      f"data_chamado_fechado FROM tb_chamado_fechado WHERE nome_cliente_chamado_fechado LIKE '%{nome_cliente}%'"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado
