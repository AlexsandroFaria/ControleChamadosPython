from connection.connection_database import ConexaoDatabase


class ChamadoDao:

    def popular_combo_solucao(self):
        conexao = ConexaoDatabase()
        comando_sql = "SELECT solucao FROM tb_solucao"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def listar_chamado_tabela(self):
        conexao = ConexaoDatabase()
        comando_sql = "SELECT numero_chamado, contrato_chamado, nome_cliente_chamado, endereco_chamado," \
                      "contato_chamado, telefone_chamado, email_chamado, problema_chamado, observacao_chamado," \
                      "status_chamado, tipo_chamado, solucao_chamado, data_abertura_chamado," \
                      "data_atualizacao_chamado FROM tb_chamado"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado
