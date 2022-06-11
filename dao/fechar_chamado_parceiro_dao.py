from connection.connection_database import ConexaoDatabase


class FecharChamadoParceiroDao:
    """Classe de fechar chamado Dao.

    Está classe é responsável pela conexão com o banco de dados e execução de consultas e querys sql.
    """

    def consultar_chamado_para_fechamento(self, numero_chamado):
        """Consultar Chamado para fechamento.

        Método efetua a consulta do chamado passando como parâmetro o número do chamado.
        :param numero_chamado: int
        :return: Dados do chamado pesquisado por número.
        """
        conexao = ConexaoDatabase()
        comando_sql = f'SELECT empresa_parceira, numero_chamado_parceiro, chamado_simpress, responsavel_parceiro,' \
                      f'nome_cliente FROM tb_chamado_parceiro WHERE numero_chamado_parceiro={numero_chamado}'
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def listar_chamado_fechado_parceiro_banco(self):
        """Listar chamados fechados do Parceiro.

        Método que lista todos os chamados fechados.
        :return: Lista de chamados fechados.
        """
        conexao = ConexaoDatabase()
        comando_sql = "SELECT empresa_parceira, numero_chamado_parceiro, chamado_simpress, responsavel_parceiro," \
                      "nome_cliente, solucao_chamado_parceiro," \
                      "data_fechamento_chamado_parceiro FROM tb_fechar_chamado_parceiro"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def cadastrar_chamado_parceiro_fechado_banco(self, empresa_parceira, numero_chamado, chamado_simpress, responsavel,
                                                 cliente, solucao, data_fechamento):
        """Cadastrar chamado fechado do Parceiro.

        Método que insere no banco de dados o chamado encerrado.
        :param empresa_parceira: str
        :param numero_chamado: int
        :param chamado_simpress: int
        :param responsavel: str
        :param cliente: str
        :param solucao: str
        :param data_fechamento: str
        """
        conexao = ConexaoDatabase()
        comando_sql = f"INSERT INTO tb_fechar_chamado_parceiro (empresa_parceira, numero_chamado_parceiro," \
                      f"chamado_simpress, responsavel_parceiro, nome_cliente, solucao_chamado_parceiro," \
                      f"data_fechamento_chamado_parceiro) VALUES ('{empresa_parceira}', {numero_chamado}," \
                      f"{chamado_simpress}, '{responsavel}', '{cliente}', '{solucao}', '{data_fechamento}')"
        conexao.executar_query(comando_sql)

    def consultar_chamado_parceiro_numero_banco(self, numero_chamado):
        """Consultar chamado por Número.

        Efetua uma consulta no banco retornando uma lista com o parâmetro passado.
        :param numero_chamado: int
        :return: Lista de chamado por Número
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT empresa_parceira, numero_chamado_parceiro, chamado_simpress, responsavel_parceiro," \
                      f"nome_cliente, solucao_chamado_parceiro," \
                      f"data_fechamento_chamado_parceiro FROM tb_fechar_chamado_parceiro WHERE " \
                      f"numero_chamado_parceiro LIKE '%{numero_chamado}%'"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def consultar_chamado_nome_cliente_banco(self, nome_cliente):
        """Consultar chamado por Nome do cliente.

        Efetua uma consulta no banco retornando uma lista com o parâmetro passado.
        :param nome_cliente: str
        :return: Lista de chamado por Nome do cliente.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT empresa_parceira, numero_chamado_parceiro, chamado_simpress, responsavel_parceiro," \
                      f"nome_cliente, solucao_chamado_parceiro," \
                      f"data_fechamento_chamado_parceiro FROM tb_fechar_chamado_parceiro WHERE " \
                      f"nome_cliente LIKE '%{nome_cliente}%'"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def consulta_chamado_data_banco(self, data):
        """Consultar chamado por Data.

        Efetua uma consulta no banco retornando uma lista com o parâmetro passado.
        :param data: str
        :return: Lista de chamado por Data.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT empresa_parceira, numero_chamado_parceiro, chamado_simpress, responsavel_parceiro," \
                      f"nome_cliente, solucao_chamado_parceiro," \
                      f"data_fechamento_chamado_parceiro FROM tb_fechar_chamado_parceiro WHERE " \
                      f"data_fechamento_chamado_parceiro LIKE '%{data}%'"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado
