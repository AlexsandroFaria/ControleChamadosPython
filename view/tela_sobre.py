from PySide2.QtWidgets import QMainWindow
from view.ui_tela_sobre import Ui_Sobre


class TelaSobre(QMainWindow, Ui_Sobre):
    def __init__(self):
        super(TelaSobre, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle de Chamados - Sobre")
        self.setFixedSize(400, 564)

        self.btn_fechar.clicked.connect(self.close)
