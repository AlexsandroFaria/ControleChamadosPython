from PySide2.QtWidgets import QMainWindow
from PySide2 import QtWidgets
from components.mensagens import Mensagens
from dao.chamado_dao import ChamadoDao
from view.ui_tela_chamado import Ui_TelaChamado


class TelaChamado(QMainWindow, Ui_TelaChamado):
    def __init__(self):
        super(TelaChamado, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle de Chamados")
        self.setFixedSize(1245, 658)

        self.mensagem = Mensagens()

        self.popula_campo_solucao()
        """Chama o método para popular a combobox de Solução"""

        self.listar_chamado_tabela()

        self.btn_fechar_tela.clicked.connect(self.close)

    def popula_campo_solucao(self):
        try:
            chamado_dao = ChamadoDao()
            resultado = chamado_dao.popular_combo_solucao()

            for i in resultado:
                self.combo_solucao.addItem(str(i[0]))
        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_de_erro()

    def listar_chamado_tabela(self):
        try:
            chamado_dao = ChamadoDao()
            resultado = chamado_dao.listar_chamado_tabela()

            self.tabela_chamado.setRowCount(len(resultado))
            self.tabela_chamado.setColumnCount(14)

            for i in range(len(resultado)):
                for j in range(0, 14):
                    self.tabela_chamado.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_de_erro()
