from connection.connection_database import ConexaoDatabase


class FecharChamadoDao:
    """Classe FecharChamadoDao

    Está classe é responsável pela conexão com o banco de dados e execução de consultas e querys sql.
    """

    def listar_chamado_fechado_tabela_banco(self):
        """Listar Chamado fechado

        Este método efetua uma consulta no banco de dados retornando todos os chamados fchados cadastrados.
        :return: Lista de chamados fechados.
        """
        conexao = ConexaoDatabase()
        comando_sql = "SELECT numero_chamado_fechado, contrato_chamado_fechado, nome_cliente_chamado_fechado," \
                      "contato_chamado_fechado, telefone_chamado_fechado, problema_chamado_fechado," \
                      "tipo_chamado_fechado, solucao_chamado_fechado, status_chamado_fechado," \
                      "date_format(data_chamado_fechado, '%d/%m/%Y') FROM tb_chamado_fechado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def consultar_numero_chamado_formulario(self, numero):
        """Consulta por número do chamado.

        Efetua uma consulta de chamados fechados no banco de dados passando como parametro de busca o número
        do chamado.
        :param numero: int
        :return: Retorna o número de chamado passado como parâmetro.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, contato_chamado," \
                      f"telefone_chamado, problema_chamado, tipo_chamado FROM tb_chamado WHERE numero_chamado={numero}"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def fechar_chamado(self, numero, contrato, nome_cliente, contato, telefone, problema, tipo, fechamento, status,
                       data_fechamento):
        """Fechar Chamado

        Salva o status do chamado fechado no banco de dados.
        :param numero: int
        :param contrato: int
        :param nome_cliente: str
        :param contato: str
        :param telefone: str
        :param problema: str
        :param tipo: str
        :param fechamento: str
        :param status: str
        :param data_fechamento: str
        """
        conexao = ConexaoDatabase()
        comando_sql = f"INSERT INTO tb_chamado_fechado (numero_chamado_fechado, contrato_chamado_fechado," \
                      f"nome_cliente_chamado_fechado, contato_chamado_fechado, telefone_chamado_fechado, " \
                      f"problema_chamado_fechado, tipo_chamado_fechado, solucao_chamado_fechado," \
                      f"status_chamado_fechado, data_chamado_fechado) VALUES ({numero}, {contrato}, '{nome_cliente}'," \
                      f"'{contato}', '{telefone}', '{problema}', '{tipo}', '{fechamento}', '{status}'," \
                      f"'{data_fechamento}')"
        conexao.executar_query(comando_sql)

    def listar_chamado_por_numero_banco(self, numero_chamado):
        """Listar chamado por número do chamado

        Lista todos os chamados conforme número passado como parâmetro.
        :param numero_chamado: int
        :return: Lista de chanmado conforme parâmetro passado.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado_fechado, contrato_chamado_fechado, nome_cliente_chamado_fechado," \
                      f"contato_chamado_fechado, telefone_chamado_fechado, problema_chamado_fechado," \
                      f"tipo_chamado_fechado, solucao_chamado_fechado, status_chamado_fechado," \
                      f"date_format(data_chamado_fechado, '%d/%m/%Y') FROM tb_chamado_fechado WHERE " \
                      f"numero_chamado_fechado={numero_chamado}"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def consultar_chamado_fechado_por_numero_tabela(self, numero_chamado):
        """Consulta de chamado por número

        Efetua uma consulta no banco de dados tendo como parâmetro o número do chamado.
        :param numero_chamado: int
        :return: Listagem de chamado na tabela dechamados fechados.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado_fechado, contrato_chamado_fechado, nome_cliente_chamado_fechado," \
                      f"contato_chamado_fechado, telefone_chamado_fechado, problema_chamado_fechado," \
                      f"tipo_chamado_fechado, solucao_chamado_fechado, status_chamado_fechado," \
                      f"date_format(data_chamado_fechado, '%d/%m/%Y') FROM tb_chamado_fechado WHERE " \
                      f"numero_chamado_fechado LIKE '%{numero_chamado}%'"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def consultar_chamado_fechado_por_contrato_tabela(self, numero_contrato):
        """Consultar chamado por Contrato.

        Efetua uma consulta no banco de dados tendo como parâmetro o contrato do chamado.
        :param numero_contrato: int
        :return: Listagem de chamado na tabela dechamados fechados.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado_fechado, contrato_chamado_fechado, nome_cliente_chamado_fechado," \
                      f"contato_chamado_fechado, telefone_chamado_fechado, problema_chamado_fechado," \
                      f"tipo_chamado_fechado, solucao_chamado_fechado, status_chamado_fechado," \
                      f"date_format(data_chamado_fechado, '%d/%m/%Y') FROM tb_chamado_fechado WHERE " \
                      f"contrato_chamado_fechado LIKE '%{numero_contrato}%'"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def consultar_chamado_fechado_por_nome_cliente_tabela(self, nome_cliente):
        """Consulta chamado por Nome do CLiente

        Efetua uma consulta no banco de dados tendo como parâmetro o nome do cliente do chamado.
        :param nome_cliente:
        :return: Listagem de chamado na tabela dechamados fechados.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado_fechado, contrato_chamado_fechado, nome_cliente_chamado_fechado," \
                      f"contato_chamado_fechado, telefone_chamado_fechado, problema_chamado_fechado," \
                      f"tipo_chamado_fechado, solucao_chamado_fechado, status_chamado_fechado," \
                      f"date_format(data_chamado_fechado, '%d/%m/%Y') FROM tb_chamado_fechado WHERE " \
                      f"nome_cliente_chamado_fechado LIKE '%{nome_cliente}%'"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado
