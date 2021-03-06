from connection.connection_database import ConexaoDatabase


class UsuarioDao:
    """Classe Usuário DAO

    Classe que realiza a conexão com o banco de dados, além de consultas sql, inserção de usuários,
    alteração de usuários e exclusão de usuários no banco de dados conforme solicitação da tela de Usuario.
    """

    def checar_usuario(self, login, senha):
        """Método de checar usuário

        Método para verificar se o usuário existe no banco de dados no ato de login. Quando o usuário informar
        o login e a senha na tela de Login, a mesma solicita a verificação da existencia do usuário.

        :param login: str
        :param senha: str
        :return: retorna na consulta se o usuário e senha existem no banco de dados
        """
        try:
            con = ConexaoDatabase()
            sql = f"SELECT * from tb_usuario where login_usuario='{login}' and senha_usuario='{senha}'"
            resultado = con.executar_consulta(sql)
            return resultado
        except:
            pass

    def cadastrar_usuario_banco(self, nome, login, senha, perfil):
        conexao = ConexaoDatabase()
        comando_sql = f"INSERT INTO tb_usuario (nome_usuario, login_usuario, senha_usuario, perfil_usuario) VALUES" \
                      f"('{nome}', '{login}', '{senha}', '{perfil}')"
        resultado = conexao.executar_query(comando_sql)

        return resultado

    def listar_usuario(self):
        conexao = ConexaoDatabase()
        comando_sql = "SELECT * FROM tb_usuario"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def carregar_campos_formulario_id(self, id):
        conexao = ConexaoDatabase()
        comando_sql = f"SELECT * FROM tb_usuario WHERE id_usuario = {id}"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def alterar_usuario(self, id, nome, login, senha, perfil):
        conexao = ConexaoDatabase()
        comando_sql = f"UPDATE tb_usuario SET nome_usuario='{nome}', login_usuario='{login}'," \
                      f"senha_usuario='{senha}', perfil_usuario='{perfil}' WHERE id_usuario={id}"
        conexao.executar_query(comando_sql)

    def excluir_usuario_banco(self, id):
        conexao = ConexaoDatabase()
        comando_sql = f"DELETE FROM tb_usuario WHERE id_usuario={id}"
        conexao.executar_query(comando_sql)
