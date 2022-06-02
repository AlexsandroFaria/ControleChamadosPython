from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2 import QtWidgets, QtGui
from datetime import datetime

from components.mensagens import Mensagens
from dao.chamado_parceiro_dao import ChamadoParceiroDao
from model.chamado_parceiro import ChamadoParceiro
from view.ui_tela_chamado_parceiro import Ui_TelaChamadoParceiro


class TelaChamadoParceiro(QMainWindow, Ui_TelaChamadoParceiro):
    def __init__(self):
        super(TelaChamadoParceiro, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle de Chamados - Chamados de Parceiros")
        self.setFixedSize(964, 638)

        self.mensagem = Mensagens()
        self.listar_chamado_parceiro_tabela()

        self.btn_alterar.setEnabled(False)
        self.btn_excluir.setEnabled(False)
        self.btn_fechar_chamado.setEnabled(False)

        self.popular_combo_numero_chamado()
        self.popular_combo_parceiro()
        self.popular_combo_nome_cliente()

        self.btn_pegar_data.clicked.connect(self.data_atual)
        self.btn_limpar_tela.clicked.connect(self.limpar_campos_formulario)
        self.btn_cadastrar.clicked.connect(self.cadastrar_chamado_parceiro)
        self.btn_fechar.clicked.connect(self.close)
        self.btn_fechar2.clicked.connect(self.close)

    def popular_combo_numero_chamado(self):
        chamado_parceiro_dao = ChamadoParceiroDao()
        resultado = chamado_parceiro_dao.consultar_numero_chamado_para_combo()

        for i in resultado:
            self.combo_chamado_simpress.addItem(str(i[0]))

    def popular_combo_parceiro(self):
        chamado_parceiro_dao = ChamadoParceiroDao()
        resultado = chamado_parceiro_dao.consultar_nome_parceiro_para_combo()

        for i in resultado:
            self.combo_empresa_parceira.addItem(str(i[0]))

    def popular_combo_nome_cliente(self):
        chamado_parceiro_dao = ChamadoParceiroDao()
        resultado = chamado_parceiro_dao.consultar_nome_cliente_para_combo()

        for i in resultado:
            self.combo_cliente.addItem(str(i[0]))

    def data_atual(self):
        data = datetime.today().strftime('%d/%m/%Y')
        self.txt_data_abertura.setText(data)

    def listar_chamado_parceiro_tabela(self):
        chamado_parceiro_dao = ChamadoParceiroDao()
        resultado = chamado_parceiro_dao.listar_chamado_parceiro_banco()

        self.tabela_chamado_parceiro.setRowCount(len(resultado))
        self.tabela_chamado_parceiro.setColumnCount(8)

        for i in range(len(resultado)):
            for j in range(0, 8):
                self.tabela_chamado_parceiro.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))

    def cadastrar_chamado_parceiro(self):
        if not self.txt_numero_chamado.text().isnumeric():
            self.mensagem.mensagem_campo_numerico('NÚMERO DO CHAMADO')
            self.txt_numero_chamado.setText("")
        elif self.combo_chamado_simpress.currentText() == "Selecione uma opção":
            self.mensagem.mensagem_combo('NÚMERO CHAMADO SIMPRESS')
        elif self.combo_empresa_parceira.currentText() =="Selecione uma opção":
            self.mensagem.mensagem_combo('EMPRESA PARCEIRA')
        elif self.txt_responsavel.text() == "":
            self.mensagem.mensagem_campo_vazio('RESPONSÁVEL')
        elif self.combo_cliente.currentText() == "Selecione uma opção":
            self.mensagem.mensagem_combo('CLIENTE')
        elif self.txt_problema.toPlainText() == "":
            self.mensagem.mensagem_campo_vazio('PROBLEMA')
        elif self.txt_observacao.text() == "":
            self.mensagem.mensagem_campo_vazio('OBSERVAÇÃO')
        elif self.txt_data_abertura.text() == "":
            self.mensagem.mensagem_campo_vazio('DATA DE ABERTURA')
        else:
            chamado_parceiro = ChamadoParceiro()

            chamado_parceiro.numero_chamado = self.txt_numero_chamado.text()
            chamado_parceiro.chamado_simpress = self.combo_chamado_simpress.currentText()
            chamado_parceiro.empresa_parceira = self.combo_empresa_parceira.currentText()
            chamado_parceiro.responsavel = self.txt_responsavel.text()
            chamado_parceiro.cliente = self.combo_cliente.currentText()
            chamado_parceiro.problema = self.txt_problema.toPlainText()
            chamado_parceiro.observacao = self.txt_observacao.text()
            chamado_parceiro.data_abertura = self.txt_data_abertura.text()

            try:
                chamado_parceiro_dao = ChamadoParceiroDao()
                chamado_parceiro_dao.cadastrar_chamado_parceiro_banco(chamado_parceiro.numero_chamado,
                                                                      chamado_parceiro.chamado_simpress,
                                                                      chamado_parceiro.empresa_parceira,
                                                                      chamado_parceiro.responsavel,
                                                                      chamado_parceiro.cliente,
                                                                      chamado_parceiro.problema,
                                                                      chamado_parceiro.observacao,
                                                                      chamado_parceiro.data_abertura)
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Cadastro de Chamado")
                msg.setText(f'Chamado na {chamado_parceiro.empresa_parceira} de número {chamado_parceiro.numero_chamado} aberto com sucesso.')
                msg.exec_()

                self.limpar_campos_formulario()
                self.listar_chamado_parceiro_tabela()
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def limpar_campos_formulario(self):
        self.txt_numero_chamado.setText("")
        self.combo_chamado_simpress.setCurrentText("Selecione uma opção")
        self.combo_empresa_parceira.setCurrentText("Selecione uma opção")
        self.txt_responsavel.setText("")
        self.combo_cliente.setCurrentText("Selecione uma opção")
        self.txt_problema.setText("")
        self.txt_observacao.setText("")
        self.txt_data_abertura.setText("")
