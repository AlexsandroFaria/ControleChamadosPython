from PySide2.QtWidgets import QMainWindow
from view.ui_tela_usuario import Ui_Usuarios
from components.mensagens import Mensagens


class TelaUsuario(QMainWindow, Ui_Usuarios):
    def __init__(self):
        super(TelaUsuario, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle de Chamados - Usuários")
        self.setFixedSize(768, 644)

    def cadastrar_usuario(self):
        pass