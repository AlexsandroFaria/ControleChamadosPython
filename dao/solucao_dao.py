from connection.connection_database import ConexaoDatabase


class SolucaoDao:
    """Classe Solução dao

    Classe que realiza a conexão com o banco de dados, além de consultas sql, inserção,
    alteração e exclusão de Soluções.
    """

    def listar_solucoes(self):
        """Método para retornar uma lista de soluções do banco de dados"""
        conexao = ConexaoDatabase()
        comando_sql = "SELECT * FROM tb_solucao"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def carregar_campos_formulario_id(self, id):
        """Método Carregar Campos Formulário

        Método busca no banco de dados a solução de ID passada por parametro e passa para a classe
        Tela de Soluções o resultado para a mesma popupar o formulário conforme resultado.

        :param id: int
        :return: Retorna uma lista de solução por ID
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT * FROM tb_solucao WHERE id_solucao={id}"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def cadastrar_solucao_banco(self, solucao, descricao):
        """Método Cadastrar Solução

        Método que efetua o cadastro de solução conforme parametros passados pela tela de soluções.

        :param solucao: str
        :param descricao: str
        :return: Cadastra a solução.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"INSERT INTO tb_solucao (solucao, descricao) VALUES ('{solucao}', '{descricao}')"
        conexao.executar_query(comando_sql)

    def alterar_usuario_banco(self, id, solucao, descricao):
        """Método de Alterar solução

        Método para alterar uma informação já cadastrada no Banco de Dados. A mesma recebe parametros da
        tela de Soluções e altera a solução com o ID selecionado.

        :param id: int
        :param solucao: str
        :param descricao: str
        :return: Altera os dados de uma solução conforme ID
        """
        conexao = ConexaoDatabase()
        comando_sql = f"UPDATE tb_solucao SET solucao_solucao='{solucao}', solucao_descricao='{descricao}'" \
                      f"WHERE id_solucao='{id}'"
        conexao.executar_query(comando_sql)

    def excluir_solucao_banco(self, id):
        """Exclusão de Solução

        Exclui uma solução com base no ID passado por parametro pela tela de Soluções.

        :param id: int
        :return: Exclui um dado conforme ID
        """
        conexao = ConexaoDatabase()
        comando_sql = f"DELETE FROM tb_solucao WHERE id_solucao={id}"
        conexao.executar_query(comando_sql)
