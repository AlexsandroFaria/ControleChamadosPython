from connection.connection_database import ConexaoDatabase


class ChamadoParceiroDao:
    """Classe Chamado Parceiro Dao

    Classe que realiza a conexão com o banco de dados, além de consultas sql, inserção,
    alteração e exclusão de chamados no banco de dados conforme solicitação da tela de Chamados de Parceiro.
    """

    def consultar_numero_chamado_para_combo(self):
        """Consulta Chamado para Combo

        Lista somente o número de chamado para popular a combo de numero de chamado Simpress.
        :return: Listagem de numero de chamados Simpress cadastrados.
        """
        conexao = ConexaoDatabase()
        comando_sql = "SELECT numero_chamado FROM tb_chamado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def consultar_nome_parceiro_para_combo(self):
        """Consultar Nome Parceiro para Combo

        Consulta somente os nomes de parceiro para popular a Combo de Parceiro.
        :return: Lista de Parceiro.
        """
        conexao = ConexaoDatabase()
        comando_sql = "SELECT nome_parceiro FROM tb_parceiro"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def consultar_nome_cliente_para_combo(self):
        """Consulta Por nome do Cliente

        Consulta somente o nome dos cliente para popular a combo Nome Cliente.
        :return: lista de nome de clientes.
        """
        conexao = ConexaoDatabase()
        comando_sql = "SELECT nome_cliente FROM tb_cliente"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def listar_chamado_parceiro_banco(self):
        """Listar Chamados Parceiro.

        Lista todos os chamado de Parceiro cadastrados.
        :return: Lista de Chamados dos Parceiros.
        """
        conexao = ConexaoDatabase()
        comando_sql = "SELECT numero_chamado_parceiro, chamado_simpress, empresa_parceira, responsavel_parceiro," \
                      "nome_cliente, problema_chamado_parceiro, observacao_chamado_parceiro, " \
                      "data_abertura_chamado_parceiro FROM tb_chamado_parceiro"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def cadastrar_chamado_parceiro_banco(self, numero_chamado, chamado_simpress, empresa, responsavel, nome_cliente,
                                         problema, observacao, data_abertura):
        """Cadastrar Chamado de Parceiro.

        Cadastra o chamado de parceiro no banco de dados.
        :param numero_chamado: int
        :param chamado_simpress: int
        :param empresa: str
        :param responsavel: str
        :param nome_cliente: str
        :param problema: str
        :param observacao: str
        :param data_abertura: str
        :return: Cadastro de chamado.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"INSERT INTO tb_chamado_parceiro (numero_chamado_parceiro, chamado_simpress, empresa_parceira," \
                      f"responsavel_parceiro, nome_cliente, problema_chamado_parceiro, observacao_chamado_parceiro," \
                      f"data_abertura_chamado_parceiro) VALUES ({numero_chamado}, {chamado_simpress}, '{empresa}'," \
                      f"'{responsavel}', '{nome_cliente}', '{problema}', '{observacao}', '{data_abertura}')"
        conexao.executar_query(comando_sql)

    def alterar_chamado_parceiro_banco(self, numero_chamado, chamado_simpress, empresa, responsavel, nome_cliente,
                                         problema, observacao, data_abertura):
        """Alterar chamado de Parceiro.

        Altera um chamado de Parceiro já cadastrado no banco de Dados.
        :param numero_chamado: int
        :param chamado_simpress: int
        :param empresa: str
        :param responsavel: str
        :param nome_cliente: str
        :param problema: str
        :param observacao: str
        :param data_abertura: str
        :return: Alteração do chamado selecionado.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"UPDATE tb_chamado_parceiro SET numero_chamado_parceiro={numero_chamado}," \
                      f"chamado_simpress={chamado_simpress}, empresa_parceira='{empresa}', responsavel_parceiro=" \
                      f"'{responsavel}', nome_cliente='{nome_cliente}', problema_chamado_parceiro='{problema}'," \
                      f"observacao_chamado_parceiro='{observacao}', data_abertura_chamado_parceiro=" \
                      f"'{data_abertura}' WHERE numero_chamado_parceiro={numero_chamado}"
        conexao.executar_query(comando_sql)

    def consultar_numero_chamado_por_numero(self, numero_chamado):
        """Consultar Chamado por número

        Consulta um chamado tendo como parâmetro o número do mesmo.
        :param numero_chamado: int
        :return: Lista de chamados conforme parâmetro de pesquisa.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado_parceiro, chamado_simpress, empresa_parceira, responsavel_parceiro," \
                      f"nome_cliente, problema_chamado_parceiro, observacao_chamado_parceiro, " \
                      f"data_abertura_chamado_parceiro FROM tb_chamado_parceiro WHERE numero_chamado_parceiro=" \
                      f"{numero_chamado}"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def excluir_chamado_parceiro_banco(self, numero_chamado):
        """Excluir chamado Parceiro.

        Exclui um chamado de parceiro conforme o número do mesmo passado como parâmetro.
        :param numero_chamado: int
        """
        conexao = ConexaoDatabase()
        comando_sql = f"DELETE FROM tb_chamado_parceiro WHERE numero_chamado_parceiro={numero_chamado}"
        conexao.executar_query(comando_sql)

    def listar_chamado_parceiro_por_numero_chamado_banco(self, numero_chamado):
        """Listar chamado parceiro por número.

        Lista os chamados de parceiro conforme parâmetro passado.
        :param numero_chamado: int
        :return: Lista de chamado de parceiro conforme numero passado por parâmetro.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado_parceiro, chamado_simpress, empresa_parceira, responsavel_parceiro," \
                      f"nome_cliente, problema_chamado_parceiro, observacao_chamado_parceiro, " \
                      f"data_abertura_chamado_parceiro FROM tb_chamado_parceiro WHERE numero_chamado_parceiro LIKE '%{numero_chamado}%'"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def listar_chamado_parceiro_por_numero_chamado_simpress_banco(self, chamado_simpress):
        """Listar chamado Parceiro por número de Contrato.

        Lista chamados por número de contrato passado como Parâmetro.
        :param chamado_simpress: int
        :return: Lista de chamados de Parceiro conforme contrato passado como parâmetro.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado_parceiro, chamado_simpress, empresa_parceira, responsavel_parceiro," \
                      f"nome_cliente, problema_chamado_parceiro, observacao_chamado_parceiro, " \
                      f"data_abertura_chamado_parceiro FROM tb_chamado_parceiro WHERE chamado_simpress LIKE '%{chamado_simpress}%'"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado
