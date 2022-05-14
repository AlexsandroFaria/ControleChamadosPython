from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2 import QtWidgets, QtGui
from dao.parceiro_dao import ParceiroDao
from model.parceiro import Parceiro
from view.ui_tela_parceiro import Ui_TelaParceiro
from components.mensagens import Mensagens


class TelaParceiro(QMainWindow, Ui_TelaParceiro):
    def __init__(self):
        super(TelaParceiro, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle de Chamados - Parceiros")
        self.setFixedSize(801, 655)

        self.mensagem = Mensagens()

        self.btn_alterar.setEnabled(False)
        self.btn_excluir.setEnabled(False)

        self.listar_parceiro_tabela()

        self.btn_cadastrar.clicked.connect(self.cadastrar_parceiro)

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

    def cadastrar_parceiro(self):
        if self.txt_nome_parceiro.text() == "":
            self.mensagem.mensagem_campo_vazio()
        elif self.txt_contato.text() == "":
            self.mensagem.mensagem_campo_vazio()
        elif self.txt_telefone.text() == "":
            self.mensagem.mensagem_campo_vazio()
        else:
            parceiro = Parceiro()
            parceiro.nome = self.txt_nome_parceiro.text()
            parceiro.contato = self.txt_contato.text()
            parceiro.telefone = self.txt_telefone.text()

            try:
                parceiro_dao = ParceiroDao()
                parceiro_dao.cadastrar_parceiro_banco(parceiro.nome, parceiro.contato, parceiro.telefone)

                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Inserir Parceiro")
                msg.setText(f'Parceiro {parceiro.nome} inserido com sucesso!')
                msg.exec_()

                self.listar_parceiro_tabela()
                self.limpar_formulario()
            except:
                pass

    def limpar_formulario(self):
        self.txt_id.setText("")
        self.txt_nome_parceiro.setText("")
        self.txt_contato.setText("")
        self.txt_telefone.setText("")

        self.btn_alterar.setEnabled(False)
        self.btn_excluir.setEnabled(False)

