from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2 import QtWidgets
from dao.parceiro_dao import ParceiroDao
from view.ui_tela_parceiro import Ui_TelaParceiro
from components.mensagens import Mensagens


class TelaParceiro(QMainWindow, Ui_TelaParceiro):
    def __init__(self):
        super(TelaParceiro, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle de Chamados - Parceiros")
        self.setFixedSize(801, 655)

        self.mensagem = Mensagens()

        self.listar_parceiro_tabela()

    def listar_parceiro_tabela(self):
        try:
            parceiro_dao = ParceiroDao()
            resultado = parceiro_dao.listar_prceiro()

            self.tabela_parceiro.setRowCount(len(resultado))
            self.tabela_parceiro.setColumnCount(4)

            for i in range(0, len(resultado)):
                for j in range(0, 4):
                    self.tabela_parceiro.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))

        except ConnectionError as con_erro:
            self.mensagem.mensagem_de_erro()
            print(con_erro)


