from PySide6.QtWidgets import QMainWindow, QMessageBox
from view.ui_tela_principal import Ui_TelaPrincipal


class TelaPrincipal(QMainWindow, Ui_TelaPrincipal):
    def __int__(self):
        super(TelaPrincipal, self).__int__()
        self.setupUi(self)
        self.setWindowTitle('Controle de Chamados - Tela Principal')
        self.showMaximized()
