from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2 import QtGui, QtWidgets
from dao.usuario_dao import UsuarioDao
from model.usuario import Usuario
from view.ui_tela_usuario import Ui_Usuarios
from components.mensagens import Mensagens


class TelaUsuario(QMainWindow, Ui_Usuarios):
    def __init__(self):
        super(TelaUsuario, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle de Chamados - Usuários")
        self.setFixedSize(768, 644)

        self.mensagem = Mensagens()

        self.btn_salvar.clicked.connect(self.cadastrar_usuario)

        self.btn_excluir.setEnabled(False)
        self.btn_alterar.setEnabled(False)

    def listagem_usuarios(self):
        try:
            usuario_dao = UsuarioDao()
            resultado = usuario_dao.listar_usuario()

            self.tabela_usuarios.setRowCount(len(resultado))
            self.tabela_usuarios.setColumnCount(5)

            for i in range(0, len(resultado)):
                for j in range(0, 5):
                    self.tabela_usuarios.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except ConnectionError:
            self.mensagem.mensagem_de_erro()

    def cadastrar_usuario(self):
        if self.txt_nome_completo.text() == "":
            self.mensagem.mensagem_campo_vazio()
        elif self.txt_login.text() == "":
            self.mensagem.mensagem_campo_vazio()
        elif self.txt_senha.text() == "":
            self.mensagem.mensagem_campo_vazio()
        elif self.txt_confirmar_senha.text() == "":
            self.mensagem.mensagem_campo_vazio()
        else:
            usuario = Usuario()

            usuario.nome = self.txt_nome_completo.text()
            usuario.login = self.txt_login.text()
            usuario.senha = self.txt_senha.text()
            usuario.perfil = self.combo_perfil.currentText()

            if usuario.senha != self.txt_confirmar_senha.text():
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Senhas não conferem")
                msg.setText('Senhas digitadas não são iguais')
                msg.exec_()
            else:
                try:
                    usuario_dao = UsuarioDao()
                    usuario_dao.cadastrar_usuario_banco(usuario.nome. usuario.login, usuario.senha, usuario.perfil)

                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Cadastro de Usuários")
                    msg.setText(f'Usuário {usuario.nome} cadastrado com sucesso!')
                    msg.exec_()

                    self.limpar_campos()
                except ConnectionError:
                    self.mensagem.mensagem_de_erro()



    def limpar_campos(self):
        self.txt_id.setText("")
        self.txt_nome_completo.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_confirmar_senha.setText("")
        self.combo_perfil.setCurrentText("Usuário")

        self.btn_excluir.setEnabled(False)
        self.btn_alterar.setEnabled(False)