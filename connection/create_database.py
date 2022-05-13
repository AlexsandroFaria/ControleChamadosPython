import mysql.connector
from _mysql_connector import MySQLInterfaceError


class CreateDatabase:

    criacao_banco = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="rootalf",
        database=None
    )

    def create_database(self):
        try:
            cursor = self.criacao_banco.cursor()
            cursor.execute("create database IF NOT EXISTS db_controle_chamados")
            print("Banco de dados criado com sucesso.")
        except MySQLInterfaceError as error:
            print("error")

    def create_table_usuarios(self, database="db_controle_chamados"):
        try:
            cursor = self.criacao_banco.cursor()
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS `{database}`.`tb_usuario` (
                `id_usuario` INT NOT NULL AUTO_INCREMENT,
                `nome_usuario` VARCHAR(255) NOT NULL,
                `login_usuario` VARCHAR(255) UNIQUE NOT NULL,
                `senha_usuario` VARCHAR(100) NOT NULL,
                `perfil_usuario` VARCHAR(15) NOT NULL,
                PRIMARY KEY (`id_usuario`));
            """)
            print('Criado tabela de Usuários')
        except:
            pass

    def inserir_usuario_admin_tb_usuario(self, database="db_controle_chamados"):
        try:
            cursor = self.criacao_banco.cursor()
            comando_sql = f"insert into {database}.tb_usuario(nome_usuario, login_usuario, senha_usuario, perfil_usuario) VALUES (%s, %s, %s, %s)"
            dados = ("Administrador", "admin", "admin", "Administrador")
            cursor.execute(comando_sql, dados)
            self.criacao_banco.commit()
            print("inserido usuario admin")
        except:
            pass

    def create_table_solucao(self, database="db_controle_chamados"):
        try:
            cursor = self.criacao_banco.cursor()
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS `{database}`.`tb_solucao` (
                `id_solucao` INT NOT NULL AUTO_INCREMENT,
                `solucao` VARCHAR(50) UNIQUE NULL,
                `descricao` VARCHAR(255) NULL,
                PRIMARY KEY (`id_solucao`));
            """)
        except:
            pass

