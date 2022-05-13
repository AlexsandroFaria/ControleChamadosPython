from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow, QMessageBox
from dao.usuario_dao import UsuarioDao
from model.usuario import Usuario
from view.ui_tela_login import Ui_UiTelaLogin
from view.tela_principal import TelaPrincipal
from connection.create_database import CreateDatabase


class TelaLogin(QMainWindow, Ui_UiTelaLogin):
    """Classe Tela de Login

    Classe responsável pelo login no sistema e primeira tela a ser exibida para o
    usuário do sistema.
    """

    def __init__(self):
        super(TelaLogin, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle Chamados - Login")
        self.setFixedSize(408, 517)

        """Chamada para o método de criação de banco de dados"""
        # self.criacao_banco()

        """Chamada do método para efetuar Login"""
        self.bt_entrar.clicked.connect(self.logar)

        """Chamada do método de fechar a tela"""
        self.btn_sair.clicked.connect(self.sair)

        """Comando para se autenticar ao clicar na tecla ENTER quando o mouse estiver no campo senha"""
        self.txt_senha.returnPressed.connect(self.logar)  # ao apertar enter se loga

    def logar(self):
        """Método de login do sistema:

        Método de login do sistema baseado em dois parametros: usuário e senha.
        O sistema irá verificar se os campos usuário e sennha estão devidamente preenchidos,
        caso sim, será feito uma consulta no banco de dados a procura das credenciais digitadas,
        encontrando o sistema redireciona o usuário para a tela principal do sistema, caso contrário
        uma mensagem é exibida para o usuário informando que suas credenciais não
        estão corretas.

        :return: Exibição da tela Principal.
        """
        if self.txt_login.text() == '' or self.txt_senha.text() == '':
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campos em branco!")
            msg.setText('Campos Login ou senha em Branco')
            msg.exec_()
        else:
            usuario = Usuario()
            # usuario.nome = None
            usuario.login = self.txt_login.text()
            usuario.senha = self.txt_senha.text()

            resultado = UsuarioDao().checar_usuario(usuario.login, usuario.senha)

            if resultado:
                self.tela_principal = TelaPrincipal()
                self.tela_principal.show()
                self.tela_principal.lbl_usuario.setText(str(resultado[0][1]))
                if str(resultado[0][4]) == 'Usuário':
                    self.tp.menu_usuarios.setEnabled(False)
                self.close()
            else:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar!")
                msg.setText('Login ou senha Incorretos')
                msg.exec_()

                self.txt_senha.setText("")

    def sair(self):
        """Método de fechar a tela e finalizar o programa"""
        self.close()

    def criacao_banco(self):
        """Método para criação de banco de dados

        Este método efetua a criação de banco de dados automaticamente.
        :return:
        """
        creation = CreateDatabase()
        creation.create_database()
        creation.create_table_usuarios()
        creation.inserir_usuario_admin_tb_usuario()
