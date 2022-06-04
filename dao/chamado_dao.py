from connection.connection_database import ConexaoDatabase


class ChamadoDao:
    """Classe de Chamado DAO

    Classe que realiza a conexão com o banco de dados, além de consultas sql, inserção,
    alteração e exclusão de chamados no banco de dados conforme solicitação da tela de Chamados.
    """

    def popular_combo_solucao(self):
        """Método popular solução.

        Método para Listar as soluções em uma combobox, exibindo os resultados para seleção.
        :return: lista de soluções.
        """
        conexao = ConexaoDatabase()
        comando_sql = "SELECT solucao FROM tb_solucao"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def listar_chamado_tabela(self):
        """Método para listar Chamdos

        Método para Listar os chamados cadastrados no banco de dados e retornar o resultado para a tela de chamados
        onde a mesma irá exibir os resultados em uma tabela.
        :return: lista de chamados
        """
        conexao = ConexaoDatabase()
        comando_sql = "SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, endereco_chamado," \
                      "contato_chamado, telefone_chamado, email_chamado, problema_chamado, observacao_chamado," \
                      "status_chamado, tipo_chamado, solucao_chamado, data_abertura_chamado," \
                      "data_atualizacao_chamado FROM tb_chamado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def consultar_contrato_banco(self, contrato):
        """Consultar Contrato

        Consulta e exibe um contrato no banco de dados pegando como referência no número do contrato.
        :param contrato: int
        :return: Contrato pesquisado.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT * FROM tb_chamado WHERE contrato_chamado={contrato}"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def buscar_contrato_cliente_formulario_banco(self, contrato):
        """Buscar contrato do Cliente.

        Efetua uma consulta no banco de dados retornando um cliente pegando como parâmetro o número do contrato
        :param contrato: int
        :return: Cliente pesquisado.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT * FROM tb_cliente WHERE contrato_cliente={contrato}"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def cadastrar_chamado_banco(self, numero, contrato, nome_cliente, endereco, contato, telefone, email, problema,
                                observacao, status, tipo, solucao, data_abertura, data_atualizada):
        """Cadastrar Chamado.

        Cadastra um chamado no banco de dados conforme parametros vindos da tela de Chamados.
        :param numero: int
        :param contrato: int
        :param nome_cliente: str
        :param endereco: str
        :param contato: str
        :param telefone: str
        :param email: str
        :param problema: str
        :param observacao: str
        :param status: str
        :param tipo: str
        :param solucao: str
        :param data_abertura: str
        :param data_atualizada: str
        :return: Cadastro de chamado.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"INSERT INTO tb_chamado (numero_chamado, contrato_chamado, nome_cliente_chamado," \
                      f"endereco_chamado, contato_chamado, telefone_chamado, email_chamado, problema_chamado," \
                      f"observacao_chamado, status_chamado, tipo_chamado, solucao_chamado, data_abertura_chamado," \
                      f"data_atualizacao_chamado) VALUES ({numero}, {contrato}, '{nome_cliente}', '{endereco}'," \
                      f"'{contato}', '{telefone}', '{email}', '{problema}', '{observacao}', '{status}', '{tipo}'," \
                      f"'{solucao}', '{data_abertura}', '{data_atualizada}')"
        conexao.executar_query(comando_sql)

    def consultar_numero_chamado(self, numero_chamado):
        """Consulta Chamado por número do chamado.

        Efetua uma consulta como parâmetro o numero do chamado.
        :param numero_chamado: int
        :return: Retorna um chamado cadastrado.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, endereco_chamado," \
                      f"contato_chamado, telefone_chamado, email_chamado, problema_chamado, observacao_chamado," \
                      f"status_chamado, tipo_chamado, solucao_chamado, data_abertura_chamado," \
                      f"data_atualizacao_chamado FROM tb_chamado WHERE numero_chamado={numero_chamado}"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def alterar_chamado_cliente_banco(self, contrato, nome, endereco, contato, telefone, email):
        """Alterar chamado cliente

        Altera os dados do cliente tendo parametro o número do contrato na tela de chamados.
        :param contrato: int
        :param nome: str
        :param endereco: str
        :param contato: str
        :param telefone: str
        :param email: str
        :return: Alteração dos dados do cliente.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"UPDATE tb_chamado SET contrato_chamado={contrato}, nome_cliente_chamado='{nome}'," \
                      f"endereco_chamado='{endereco}', contato_chamado='{contato}', telefone_chamado='{telefone}'," \
                      f"email_chamado='{email}' WHERE contrato_chamado={contrato}"
        conexao.executar_query(comando_sql)

    def alterar_chamado_banco(self, numero_chamado, telefone, email, problema, observacao, status, tipo,
                              solucao, data_abertura, data_atualizada):
        """Alterar Chamado.

        Altera um chamado no banco de dados como parametro de pesquisa o número do chamado.
        :param numero_chamado: int
        :param telefone: str
        :param email: str
        :param problema: str
        :param observacao: str
        :param status: str
        :param tipo: str
        :param solucao: str
        :param data_abertura: str
        :param data_atualizada: str
        :return: Alteração de chamado.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"UPDATE tb_chamado SET telefone_chamado='{telefone}', email_chamado='{email}'," \
                      f"problema_chamado='{problema}', observacao_chamado='{observacao}', status_chamado='{status}'," \
                      f"tipo_chamado='{tipo}', solucao_chamado='{solucao}', data_abertura_chamado='{data_abertura}'," \
                      f"data_atualizacao_chamado='{data_atualizada}' WHERE numero_chamado={numero_chamado}"
        conexao.executar_query(comando_sql)

    def alterar_cliente_telefone_email(self, contrato, telefone, email):
        """Alterar telefone e email da tabela cliente

        Altera o nome e telefone da tabela cliente caso os dados da tabela chamado sejam alterados.
        :param contrato: int
        :param telefone: str
        :param email: str
        :return: Alteração de telefone e email da tabela de cliente.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"UPDATE tb_cliente SET telefone_cliente='{telefone}'," \
                      f"email_cliente='{email}' WHERE contrato_cliente={contrato}"
        conexao.executar_query(comando_sql)

    def excluir_chamado_banco(self, numero_chamado):
        """Excluir chamado.

        Exclui um chamdo tendo como paramêtro o número do chamado.
        :param numero_chamado: int
        :return: Exclusão de chamado.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"DELETE FROM tb_chamado WHERE numero_chamado={numero_chamado}"
        conexao.executar_query(comando_sql)

    def listar_numero_chamado_tabela(self, numero_chamado):
        """Consulta Chamado por número do chamado.

        Efetua uma consulta como parâmetro o numero do chamado.
        :param numero_chamado: int
        :return: Retorna um chamado cadastrado.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, endereco_chamado," \
                      f"contato_chamado, telefone_chamado, email_chamado, problema_chamado, observacao_chamado," \
                      f"status_chamado, tipo_chamado, solucao_chamado, data_abertura_chamado," \
                      f"data_atualizacao_chamado FROM tb_chamado WHERE numero_chamado LIKE '%{numero_chamado}%'"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def listar_chamado_por_contrato(self, numero_contrato):
        """Listar chamado por Contrato

        Efetua uma consulta como parâmetro o numero do contrato.
        :param numero_contrato: int
        :return: Retorna um chamado cadastrado conforme consulta.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, endereco_chamado," \
                      f"contato_chamado, telefone_chamado, email_chamado, problema_chamado, observacao_chamado," \
                      f"status_chamado, tipo_chamado, solucao_chamado, data_abertura_chamado," \
                      f"data_atualizacao_chamado FROM tb_chamado WHERE contrato_chamado LIKE '%{numero_contrato}%'"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def listar_chamado_por_nome_cliente(self, nome_cliente):
        """Listar chamado por nome do cliente.

        Efetua uma consulta como parâmetro o nome do cliente.
        :param nome_cliente: str
        :return: Retorna um chamado cadastrado conforme consulta.
        """
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, endereco_chamado," \
                      f"contato_chamado, telefone_chamado, email_chamado, problema_chamado, observacao_chamado," \
                      f"status_chamado, tipo_chamado, solucao_chamado, data_abertura_chamado," \
                      f"data_atualizacao_chamado FROM tb_chamado WHERE nome_cliente_chamado LIKE '%{nome_cliente}%'"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado
