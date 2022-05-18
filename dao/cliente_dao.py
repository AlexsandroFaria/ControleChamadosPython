from connection.connection_database import ConexaoDatabase


class ClienteDao:
    """Classe Cliente dao

    Classe que realiza a conexão com o banco de dados, além de consultas sql, inserção,
    alteração e exclusão de Clientes no banco de dados conforme solicitação da tela de Cliente.
    """

    def listar_cliente(self):
        """Método para retornar uma lista de Clientes do banco de dados"""
        conexao = ConexaoDatabase()
        comando_sql = "SELECT contrato_cliente, nome_cliente, endereco_cliente, contato_cliente, telefone_cliente, " \
                      "email_cliente FROM tb_cliente"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def cadastrar_cliente_banco(self, contrato, nome, endereco, contato, telefone, email):
        """Cadastro de cliente

        Método insere no banco de dados o cliente conforme parametros passados pela tela de Cliente.

        :param contrato: int
        :param nome: str
        :param endereco: str
        :param contato: str
        :param telefone: str
        :param email: str
        :return: Cadastra Cliente no banco
        """
        conexao = ConexaoDatabase()
        comando_sql = f"INSERT INTO tb_cliente (contrato_cliente, nome_cliente, endereco_cliente, contato_cliente," \
                      f"telefone_cliente, email_cliente) VALUES ('{contrato}', '{nome}', '{endereco}', '{contato}', " \
                      f"'{telefone}', '{email}')"
        conexao.executar_query(comando_sql)

    def consultar_por_contrato(self, contrato):
        """Consulta por contrato

        Método efetua consulta no banco de dados por número de contrato passado por parametro pela tela de Cliente
        :param contrato: int
        :return: Consulta de cliente por contrato
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT contrato_cliente, nome_cliente, endereco_cliente, contato_cliente, telefone_cliente, " \
                      f"email_cliente FROM tb_cliente WHERE contrato_cliente={contrato}"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def alterar_cliente_banco(self, contrato, nome, endereco, contato, telefone, email):
        """Alterar cliente

        Método de alterar cliente com referência no número do contrato.
        :param contrato: int
        :param nome: str
        :param endereco: str
        :param contato: str
        :param telefone: str
        :param email: str
        :return: Altera um cliente no banco de dados
        """
        conexao = ConexaoDatabase()
        comando_sql = f"UPDATE tb_cliente SET contrato_cliente={contrato}, nome_cliente='{nome}', endereco_cliente=" \
                      f"'{endereco}', contato_cliente='{contato}', telefone_cliente='{telefone}', email_cliente=" \
                      f"'{email}' WHERE contrato_cliente={contrato}"
        conexao.executar_query(comando_sql)

    def excluir_cliente_banco(self, contrato):
        """Excluir cliente

        Excluir um cliente do banco de dados utilizando como parametro o contrato do mesmo.
        :param contrato: int
        :return: Exclusão do cliente
        """
        conexao = ConexaoDatabase()
        comando_sql = f"DELETE FROM tb_cliente WHERE contrato_cliente={contrato}"
        conexao.executar_query(comando_sql)

    def consultar_cliente_contrato_banco(self, contrato):
        """Consultar Cliente por Contrato

        Consulta no banco de dados o cliente com o número de contrato passado como parâmetro pela tela de cliente.
        :param contrato: int
        :return: Cliente com o contrato passado por parametro.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT contrato_cliente, nome_cliente, endereco_cliente, contato_cliente, telefone_cliente," \
                      f"email_cliente FROM tb_cliente WHERE contrato_cliente LIKE '%{contrato}%'"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def consultar_cliente_nome_banco(self, nome):
        """Consultar Cliente por Nome.

        Consulta no banco de dados o cliente com o nome do cliente passado como parâmetro pela tela de cliente.
        :param nome: str
        :return: Cliente com o nome passado por parametro.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT contrato_cliente, nome_cliente, endereco_cliente, contato_cliente, telefone_cliente," \
                      f"email_cliente FROM tb_cliente WHERE nome_cliente LIKE '%{nome}%'"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

