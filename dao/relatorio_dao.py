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
                      f"status_chamado, tipo_chamado, solucao_chamado, date_format(data_abertura_chamado,'%d/%m/%Y')," \
                      f"date_format(data_atualizacao_chamado, '%d/%m/%Y') FROM tb_chamado WHERE " \
                      f"solucao_chamado='{solucao}' ORDER BY numero_chamado"
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
                      f"status_chamado, tipo_chamado, solucao_chamado, date_format(data_abertura_chamado,'%d/%m/%Y')," \
                      f"date_format(data_atualizacao_chamado, '%d/%m/%Y') FROM tb_chamado WHERE" \
                      f"solucao_chamado='{solucao}' ORDER BY contrato_chamado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def relatorio_chamado_data_ordenado_por_numero(self, data_inicial, data_final):
        """Relatório de chamados por data ordenada por número do chamado

        Efetua uma consulta no banco de dados por data e ordenada por número do chamado.
        :param solucao: str
        :return: Lista de chamados por data.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, endereco_chamado," \
                      f"contato_chamado, telefone_chamado, email_chamado, problema_chamado, observacao_chamado," \
                      f"status_chamado, tipo_chamado, solucao_chamado, date_format(data_abertura_chamado,'%d/%m/%Y')," \
                      f"date_format(data_atualizacao_chamado, '%d/%m/%Y') FROM tb_chamado WHERE " \
                      f"data_abertura_chamado BETWEEN ('{data_inicial}') AND ('{data_final}') ORDER BY numero_chamado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def relatorio_chamado_data_ordenado_por_contrato(self, data_inicial, data_final):
        """Relatório de chamados por data ordenada por número do contrato

        Efetua uma consulta no banco de dados por data e ordenada por número do contrato.
        :param solucao: str
        :return: Lista de chamados por data.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, endereco_chamado," \
                      f"contato_chamado, telefone_chamado, email_chamado, problema_chamado, observacao_chamado," \
                      f"status_chamado, tipo_chamado, solucao_chamado, date_format(data_abertura_chamado,'%d/%m/%Y')," \
                      f"date_format(data_atualizacao_chamado, '%d/%m/%Y') FROM tb_chamado WHERE " \
                      f"data_abertura_chamado BETWEEN ('{data_inicial}') AND ('{data_final}') ORDER BY contrato_chamado"
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
                      f"status_chamado, tipo_chamado, solucao_chamado, date_format(data_abertura_chamado,'%d/%m/%Y')," \
                      f"date_format(data_atualizacao_chamado, '%d/%m/%Y') FROM tb_chamado WHERE " \
                      f"tipo_chamado='{tipo_chamado}' ORDER BY numero_chamado"
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
                      f"status_chamado, tipo_chamado, solucao_chamado, date_format(data_abertura_chamado,'%d/%m/%Y')," \
                      f"date_format(data_atualizacao_chamado, '%d/%m/%Y') FROM tb_chamado WHERE " \
                      f"tipo_chamado='{tipo_chamado}' ORDER BY contrato_chamado"
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
                      f"status_chamado, tipo_chamado, solucao_chamado, date_format(data_abertura_chamado,'%d/%m/%Y')," \
                      f"date_format(data_atualizacao_chamado, '%d/%m/%Y') FROM tb_chamado WHERE " \
                      f"status_chamado='{status}' ORDER BY numero_chamado"
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
                      f"status_chamado, tipo_chamado, solucao_chamado, date_format(data_abertura_chamado,'%d/%m/%Y')," \
                      f"date_format(data_atualizacao_chamado, '%d/%m/%Y') FROM tb_chamado WHERE " \
                      f"status_chamado='{status}' ORDER BY contrato_chamado"
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
                      "status_chamado, tipo_chamado, solucao_chamado, date_format(data_abertura_chamado,'%d/%m/%Y')," \
                      "date_format(data_atualizacao_chamado, '%d/%m/%Y') FROM tb_chamado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def gerar_relatorio_chamado_fechado_datas_num_chamado(self, data_inicial, data_final):
        """Gerar relatório de chamados fechados por datas ordenado por número

        Efetua uma consulta no banco de dados retornando os chamados fechados por intervalo de datas
        e ordenados pelo número do chamado
        :param data_inicial: str
        :param data_final: str
        :return: Lista dos chamados da consulta
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado_fechado, contrato_chamado_fechado, nome_cliente_chamado_fechado," \
                      f"contato_chamado_fechado, telefone_chamado_fechado, problema_chamado_fechado," \
                      f"tipo_chamado_fechado, solucao_chamado_fechado, status_chamado_fechado," \
                      f"date_format(data_chamado_fechado, '%d/%m/%Y') FROM tb_chamado_fechado WHERE " \
                      f"data_chamado_fechado BETWEEN ('{data_inicial}') AND ('{data_final}') ORDER BY " \
                      f"numero_chamado_fechado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def gerar_relatorio_chamado_fechado_datas_num_contrato(self, data_inicial, data_final):
        """Gerar relatório de chamados fechados por datas ordenado por contrato

        Efetua uma consulta no banco de dados retornando os chamados fechados por intervalo de datas
        e ordenados pelo número do contrato
        :param data_inicial: str
        :param data_final: str
        :return: Lista dos chamados da consulta
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado_fechado, contrato_chamado_fechado, nome_cliente_chamado_fechado," \
                      f"contato_chamado_fechado, telefone_chamado_fechado, problema_chamado_fechado," \
                      f"tipo_chamado_fechado, solucao_chamado_fechado, status_chamado_fechado," \
                      f"date_format(data_chamado_fechado, '%d/%m/%Y') FROM tb_chamado_fechado WHERE " \
                      f"data_chamado_fechado BETWEEN ('{data_inicial}') AND ('{data_final}') ORDER BY " \
                      f"contrato_chamado_fechado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def gerar_relatorio_chamado_fechado_tipo_num_chamado(self, tipo):
        """Gerar relatório de chamados fechados por tipo ordenado por número.

        Efetua uma consulta no banco de dados retornando os chamados fechados por tipo e ordenados pelo
        número do chamado.
        :param tipo: str
        :return: Lista dos chamados da consulta
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado_fechado, contrato_chamado_fechado, nome_cliente_chamado_fechado," \
                      f"contato_chamado_fechado, telefone_chamado_fechado, problema_chamado_fechado," \
                      f"tipo_chamado_fechado, solucao_chamado_fechado, status_chamado_fechado," \
                      f"date_format(data_chamado_fechado, '%d/%m/%Y') FROM tb_chamado_fechado WHERE " \
                      f"tipo_chamado_fechado='{tipo}' ORDER BY numero_chamado_fechado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def gerar_relatorio_chamado_fechado_tipo_num_contrato(self, tipo):
        """Gerar relatório de chamados fechados por tipo ordenado por contrato

        Efetua uma consulta no banco de dados retornando os chamados fechados por tipo e ordenados pelo
        número do contrato
        :param tipo: str
        :return: Lista dos chamados da consulta
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado_fechado, contrato_chamado_fechado, nome_cliente_chamado_fechado," \
                      f"contato_chamado_fechado, telefone_chamado_fechado, problema_chamado_fechado," \
                      f"tipo_chamado_fechado, solucao_chamado_fechado, status_chamado_fechado," \
                      f"date_format(data_chamado_fechado, '%d/%m/%Y') FROM tb_chamado_fechado WHERE " \
                      f"tipo_chamado_fechado='{tipo}' ORDER BY contrato_chamado_fechado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def gerar_relatorio_chamado_fechado_status_num_chamado(self, status):
        """Gerar relatório de chamados fechados por status ordenado por número.

        Efetua uma consulta no banco de dados retornando os chamados fechados por número e ordenados pelo
        número do chamado
        :param status: str
        :return: Lista dos chamados da consulta
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado_fechado, contrato_chamado_fechado, nome_cliente_chamado_fechado," \
                      f"contato_chamado_fechado, telefone_chamado_fechado, problema_chamado_fechado," \
                      f"tipo_chamado_fechado, solucao_chamado_fechado, status_chamado_fechado," \
                      f"date_format(data_chamado_fechado, '%d/%m/%Y') FROM tb_chamado_fechado WHERE " \
                      f"status_chamado_fechado='{status}' ORDER BY numero_chamado_fechado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def gerar_relatorio_chamado_fechado_status_num_contrato(self, status):
        """Gerar relatório de chamados fechados por status ordenado por contrato.

        Efetua uma consulta no banco de dados retornando os chamados fechados por número e ordenados pelo
        número do contrato
        :param status: str
        :return: Lista dos chamados da consulta
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado_fechado, contrato_chamado_fechado, nome_cliente_chamado_fechado," \
                      f"contato_chamado_fechado, telefone_chamado_fechado, problema_chamado_fechado," \
                      f"tipo_chamado_fechado, solucao_chamado_fechado, status_chamado_fechado," \
                      f"date_format(data_chamado_fechado, '%d/%m/%Y') FROM tb_chamado_fechado WHERE " \
                      f"status_chamado_fechado='{status}' ORDER BY contrato_chamado_fechado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def gerar_relatorio_chamado_fechado(self):
        """Gerar relatório de chamados fechados.

        Efetua uma consulta no banco de dados retornando todos os chamados fechados.
        :return: Lista dos chamados da consulta
        """
        conexao = ConexaoDatabase()
        comando_sql = "SELECT numero_chamado_fechado, contrato_chamado_fechado, nome_cliente_chamado_fechado," \
                      "contato_chamado_fechado, telefone_chamado_fechado, problema_chamado_fechado," \
                      "tipo_chamado_fechado, solucao_chamado_fechado, status_chamado_fechado," \
                      "date_format(data_chamado_fechado, '%d/%m/%Y') FROM tb_chamado_fechado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado
