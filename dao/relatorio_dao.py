from connection.connection_database import ConexaoDatabase


class RelatorioDao:
    """Classe Relatório dao

    Classe que realiza a conexão com o banco de dados e efetua diversas consultas sql.
    """

    def consulta_nome_solucao(self):
        """Consulta nome solução

        Consulta no banco de dados o nome das soluções cadastradas.
        :return: Lista de soluções.
        """
        conexao = ConexaoDatabase()
        comando_sql = "SELECT solucao FROM tb_solucao"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def relatorio_solucao_ordenado_numero_chamado(self, solucao):
        """Relatório de solução ordenada por número do chamado

        Efetua uma consulta no banco de dados por solução e ordenada por número do chamado.
        :param solucao: str
        :return: Lista de chamados por solução.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, endereco_chamado," \
                      f"contato_chamado, telefone_chamado, email_chamado, problema_chamado, observacao_chamado," \
                      f"status_chamado, tipo_chamado, solucao_chamado, data_abertura_chamado," \
                      f"data_atualizacao_chamado FROM tb_chamado WHERE solucao_chamado='{solucao}' ORDER BY " \
                      f"numero_chamado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def relatorio_solucao_ordenado_contrato_chamado(self, solucao):
        """Relatório de solução ordenada por número do contrato

        Efetua uma consulta no banco de dados por solução e ordenada por número do contrato.
        :param solucao: str
        :return: Lista de chamados por solução.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, endereco_chamado," \
                      f"contato_chamado, telefone_chamado, email_chamado, problema_chamado, observacao_chamado," \
                      f"status_chamado, tipo_chamado, solucao_chamado, data_abertura_chamado," \
                      f"data_atualizacao_chamado FROM tb_chamado WHERE solucao_chamado='{solucao}' ORDER BY " \
                      f"contrato_chamado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def relatorio_chamado_data_ordenado_por_numero(self, data):
        """Relatório de chamados por data ordenada por número do chamado

        Efetua uma consulta no banco de dados por data e ordenada por número do chamado.
        :param solucao: str
        :return: Lista de chamados por data.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, endereco_chamado," \
                      f"contato_chamado, telefone_chamado, email_chamado, problema_chamado, observacao_chamado," \
                      f"status_chamado, tipo_chamado, solucao_chamado, data_abertura_chamado," \
                      f"data_atualizacao_chamado FROM tb_chamado WHERE data_abertura_chamado='{data}' ORDER BY " \
                      f"numero_chamado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def relatorio_chamado_data_ordenado_por_contrato(self, data):
        """Relatório de chamados por data ordenada por número do contrato

        Efetua uma consulta no banco de dados por data e ordenada por número do contrato.
        :param solucao: str
        :return: Lista de chamados por data.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, endereco_chamado," \
                      f"contato_chamado, telefone_chamado, email_chamado, problema_chamado, observacao_chamado," \
                      f"status_chamado, tipo_chamado, solucao_chamado, data_abertura_chamado," \
                      f"data_atualizacao_chamado FROM tb_chamado WHERE data_abertura_chamado='{data}' ORDER BY " \
                      f"contrato_chamado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def relatorio_tipo_chamado_por_numero(self, tipo_chamado):
        """Relatório de chamados por tipo do chamado ordenada por número do chamado

        Efetua uma consulta no banco de dados por tipo do chamado e ordenada por número do chamado.
        :param solucao: str
        :return: Lista de chamados por tipo.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, endereco_chamado," \
                      f"contato_chamado, telefone_chamado, email_chamado, problema_chamado, observacao_chamado," \
                      f"status_chamado, tipo_chamado, solucao_chamado, data_abertura_chamado," \
                      f"data_atualizacao_chamado FROM tb_chamado WHERE tipo_chamado='{tipo_chamado}' ORDER BY " \
                      f"numero_chamado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def relatorio_tipo_chamado_por_contrato(self, tipo_chamado):
        """Relatório de chamados por tipo do chamado ordenada por número do contrato

        Efetua uma consulta no banco de dados por tipo do chamado e ordenada por número do contrato.
        :param solucao: str
        :return: Lista de chamados por tipo.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, endereco_chamado," \
                      f"contato_chamado, telefone_chamado, email_chamado, problema_chamado, observacao_chamado," \
                      f"status_chamado, tipo_chamado, solucao_chamado, data_abertura_chamado," \
                      f"data_atualizacao_chamado FROM tb_chamado WHERE tipo_chamado='{tipo_chamado}' ORDER BY " \
                      f"contrato_chamado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def relatorio_status_chamado_por_numero(self, status):
        """Relatório de chamados por status ordenada por número do chamado

        Efetua uma consulta no banco de dados por status e ordenada por número do chamado.
        :param solucao: str
        :return: Lista de chamados por status.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, endereco_chamado," \
                      f"contato_chamado, telefone_chamado, email_chamado, problema_chamado, observacao_chamado," \
                      f"status_chamado, tipo_chamado, solucao_chamado, data_abertura_chamado," \
                      f"data_atualizacao_chamado FROM tb_chamado WHERE status_chamado='{status}' ORDER BY " \
                      f"numero_chamado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def relatorio_status_chamado_por_contrato(self, status):
        """Relatório de chamados por status ordenada por número do contrato

        Efetua uma consulta no banco de dados por status e ordenada por número do contrato.
        :param solucao: str
        :return: Lista de chamados por status.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, endereco_chamado," \
                      f"contato_chamado, telefone_chamado, email_chamado, problema_chamado, observacao_chamado," \
                      f"status_chamado, tipo_chamado, solucao_chamado, data_abertura_chamado," \
                      f"data_atualizacao_chamado FROM tb_chamado WHERE status_chamado='{status}' ORDER BY " \
                      f"contrato_chamado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def gerar_relatorio_padrao(self):
        """Relatório de chamados sem filtros ou ordenação

        Efetua uma consulta no banco de dados retornando todos os chamados.
        :param solucao: str
        :return: Lista de chamados.
        """
        conexao = ConexaoDatabase()
        comando_sql = "SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, endereco_chamado," \
                      "contato_chamado, telefone_chamado, email_chamado, problema_chamado, observacao_chamado," \
                      "status_chamado, tipo_chamado, solucao_chamado, data_abertura_chamado," \
                      "data_atualizacao_chamado FROM tb_chamado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado
