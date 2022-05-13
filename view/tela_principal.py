from PySide2.QtWidgets import QMainWindow

from view.tela_solucao import TelaSolucao
from view.ui_tela_principal import Ui_TelaPrincipal
from view.tela_usuario import TelaUsuario


class TelaPrincipal(QMainWindow, Ui_TelaPrincipal):
    """Tela Principal do Sistema

    Está é a tela principal do sistema com todos os menus disponíveis para que o usuários possa navegar
    e efetuar as inclusões necessárias, assim como gerar relatórios.
    """
    def __init__(self):
        """Tela principal do sistema

        Esta tela é onde fica o menu da aplicação de acesso a todos os recursos do sistema.
        """
        super(TelaPrincipal, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Controle de Chamados - Tela Principal')
        self.showMaximized()

        """Item do menu que gera a chamada do método de abrir tela de usuários."""
        self.menu_usuarios.triggered.connect(self.abrir_tela_usuario)

        """Item do menu que gera a chamada do método de abrir tela de soluções."""
        self.menu_solucoes.triggered.connect(self.abrir_tela_solucao)

    def abrir_tela_usuario(self):
        """Método para chamar a tela de Usuário.

        Este método chama a tela de usuário e exibe a mesma na tela.
        :return: Tela de Usuário
        """
        self.tela_usuario = TelaUsuario()
        self.tela_usuario.show()

    def abrir_tela_solucao(self):
        self.tela_solucao = TelaSolucao()
        self.tela_solucao.show()
