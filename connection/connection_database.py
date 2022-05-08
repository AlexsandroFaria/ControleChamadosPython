import mysql.connector


class ConexaoDatabase:
    """Classe de conexão com o banco de dados Mysql

    Classe de conexão com o banco de dados mysql, a mesma é responsável por efetuar a conexão e desconexão com
    o banco e controlar o fluxo de dados.
    """

    """Parametros de conexão com o Banco."""
    def __init__(self, host="localhost", user="root", pwd="rootalf", db="db_controle_chamados"):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def conecta(self):
        """
        Método que efetua a conexão com o banco de dados utilizando-se dos parametros passados no construtor
        """
        self.con = mysql.connector.connect(host=self.host, user=self.user, password=self.pwd, database=self.db)
        self.cur = self.con.cursor()

    def desconecta(self):
        """
        Método responsável pela desonexão com o banco.
        """
        self.con.close()

    def executar_consulta(self, sql):
        """
        Método para execução de consultas sql diretamente no Banco de dados Mysql

        :param sql: str
        :return: retorna uma consulta em sql
        """
        self.conecta()
        self.cur.execute(sql)
        resultado = self.cur.fetchall()
        self.desconecta()
        return resultado

    def executar_query(self, sql):
        """
        Método para execução de querys do typo cadastrar, alterar e excluir dados do banco mysql

        :param sql: str
        :return: retorna uma consulta em sql
        """
        self.conecta()
        self.cur.execute(sql)
        self.con.commit()
        self.desconecta()
