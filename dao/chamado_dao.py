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
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT * FROM tb_chamado WHERE contrato_chamado={contrato}"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def buscar_contrato_cliente_formulario_banco(self, contrato):
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT * FROM tb_cliente WHERE contrato_cliente={contrato}"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def cadastrar_chamado_banco(self, numero, contrato, nome_cliente, endereco, contato, telefone, email, problema,
                                observacao, status, tipo, solucao, data_abertura, data_atualizada):
        conexao = ConexaoDatabase()
        comando_sql = f"INSERT INTO tb_chamado (numero_chamado, contrato_chamado, nome_cliente_chamado," \
                      f"endereco_chamado, contato_chamado, telefone_chamado, email_chamado, problema_chamado," \
                      f"observacao_chamado, status_chamado, tipo_chamado, data_abertura_chamado," \
                      f"data_atualizacao_chamado) VALUES ({numero}, {contrato}, '{nome_cliente}', '{endereco}'," \
                      f"'{contato}', '{telefone}', '{email}', '{problema}', '{observacao}', '{status}', '{tipo}'," \
                      f"'{solucao}', '{data_abertura}', '{data_atualizada}')"
        conexao.executar_query(comando_sql)
