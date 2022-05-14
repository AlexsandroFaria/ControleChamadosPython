from connection.connection_database import ConexaoDatabase


class ClienteDao:
    """Classe Cliente dao

    Classe que realiza a conexão com o banco de dados, além de consultas sql, inserção,
    alteração e exclusão de Clientes no banco de dados conforme solicitação da tela de Cliente.
    """

    def listar_cliente(self):
        """Método para retornar uma lista de Clientes do banco de dados"""
        conexao = ConexaoDatabase()
        comando_sql = "SELECT * FROM tb_cliente"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def listar_cliente_id(self, contrato):
        """Método para retornar uma lista de Clientes por contrato do banco de dados

        :param contrato: int
        :return: Cliente con o número de contrato X
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT * FROM tb_cliente WHERE id_cliente={contrato}"
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
