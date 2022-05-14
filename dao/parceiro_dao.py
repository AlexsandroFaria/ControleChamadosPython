from connection.connection_database import ConexaoDatabase


class ParceiroDao:
    """Classe Parceiro Dao

    Classe que realiza a conexão com o banco de dados, além de consultas sql, inserção,
    alteração e exclusão de Parceiros no banco de dados conforme solicitação da tela de Parceiros.
    """

    def listar_prceiro(self):
        """Método para listar Parceiros

        Método para Listar os parceiro cadastrados no banco de dados e retornar o resultado para a tela de Parceiros
        onde a mesma irá exibir os resultados em uma tabela.
        :return: lista de parceiros
        """
        conexao = ConexaoDatabase()
        comando_sql = "SELECT * FROM tb_parceiro"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def listar_parceiro_id(self, id):
        """Método para listar Parceiros por ID

        Método para Listar os parceiro cadastrados no banco de dados e retornar o resultado para a tela de Parceiros
        onde a mesma irá exibir os resultados em uma tabela.
        :param id: int
        :return: Retorna uma lista de Parceiros do Banco de dados
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT * FROM tb_parceiro WHERE id_parceiro={id}"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def cadastrar_parceiro_banco(self, nome, contato, telefone):
        """Cadastrar Parceiro

        Méto cadastra um Parceiro conforme parametros recebidos da tela de Parceiros
        :param nome: str
        :param contato: str
        :param telefone: str
        """
        conexao = ConexaoDatabase()
        comando_sql = f"INSERT INTO tb_parceiro (nome_parceiro, contato_parceiro, telefone_parceiro) VALUES " \
                      f"('{nome}', '{contato}', '{telefone}')"
        conexao.executar_query(comando_sql)

    def alterar_parceiro_banco(self, id, nome, contato, telefone):
        """Médoto de alterar Parceiro

        Método que altera um Parceiro no banco de dados conforme lidsta de parametros passados pela tela de
        Parceiro
        :param id: int
        :param nome: str
        :param contato: str
        :param telefone: str
        """
        conexao = ConexaoDatabase()
        comando_sql = f"UPDATE tb_parceiro SET nome_parceiro='{nome}', contato_parceiro='{contato}'," \
                      f"telefone_parceiro='{telefone}' WHERE id_parceiro={id}"
        conexao.executar_query(comando_sql)

    def excluir_parceiro_banco(self, id):
        """Método de Excluir Parceiro

        Método exclui um parceiro conforme parametro de ID passado pela tela de Parceiros
        :param id: int
        """
        conexao = ConexaoDatabase()
        comando_sql = f"DELETE FROM tb_parceiro WHERE id_parceiro={id}"
        conexao.executar_query(comando_sql)

