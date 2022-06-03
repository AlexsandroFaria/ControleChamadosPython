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
        self.btn_alterar.clicked.connect(self.alterar_chamado_parceiro)
        self.btn_carregar.clicked.connect(self.carregar_chamado_formulario)
        self.btn_excluir.clicked.connect(self.excluir_chamado_parceiro)
        self.btn_pesquisar_numero_chamado.clicked.connect(self.consultar_chamado_tabela_por_numero)
        self.btn_carregar_tabela.clicked.connect(self.listar_chamado_parceiro_tabela)
        self.btn_pesquisar_chamado_simpress.clicked.connect(self.consultar_chamado_tabela_por_numero_chamado_simpress)
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

    def alterar_chamado_parceiro(self):
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
                chamado_parceiro_dao.alterar_chamado_parceiro_banco(chamado_parceiro.numero_chamado,
                                                                    chamado_parceiro.chamado_simpress,
                                                                    chamado_parceiro.empresa_parceira,
                                                                    chamado_parceiro.responsavel,
                                                                    chamado_parceiro.cliente,
                                                                    chamado_parceiro.problema,
                                                                    chamado_parceiro.observacao,
                                                                    chamado_parceiro.data_abertura)

                self.limpar_campos_formulario()
                self.listar_chamado_parceiro_tabela()

                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Alteração de Chamado")
                msg.setText(f'Chamado número {chamado_parceiro.numero_chamado} alterado com sucesso.')
                msg.exec_()
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def carregar_chamado_formulario(self):
        linha = self.tabela_chamado_parceiro.currentItem().text()

        if not linha.isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Carregar Campos Chamados")
            msg.setText('Selecione somente a coluna Número do chamado')
            msg.exec_()
        else:
            try:
                chamado_parceiro_dao = ChamadoParceiroDao()
                resultado = chamado_parceiro_dao.consultar_numero_chamado_por_numero(linha)

                if len(resultado) == 0:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Consultar Chamados")
                    msg.setText('Selecione somente a coluna Número do chamado')
                    msg.exec_()
                else:
                    self.tab_chamado_parceiro.setCurrentWidget(self.tab_cadastro_parceiro)

                    self.txt_numero_chamado.setText(str(resultado[0][0]))
                    self.combo_chamado_simpress.setCurrentText(str(resultado[0][1]))
                    self.combo_empresa_parceira.setCurrentText(str(resultado[0][2]))
                    self.txt_responsavel.setText(str(resultado[0][3]))
                    self.combo_cliente.setCurrentText(str(resultado[0][4]))
                    self.txt_problema.setText(str(resultado[0][5]))
                    self.txt_observacao.setText(str(resultado[0][6]))
                    self.txt_data_abertura.setText(str(resultado[0][7]))

                    self.btn_fechar_chamado.setEnabled(True)
                    self.btn_alterar.setEnabled(True)
                    self.btn_excluir.setEnabled(True)
                    self.btn_cadastrar.setEnabled(False)

            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()
            except AttributeError as at_erro:
                print(at_erro)
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Consultar Chamado de Parceiro")
                msg.setText('Selecione um item da coluna numero do chamado')
                msg.exec_()

    def excluir_chamado_parceiro(self):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
        msg.setWindowTitle("Exclusão de Chamado")
        msg.setText("Tem certeza que deseja excluir o Chamado?")
        msg.setStandardButtons(QMessageBox.Yes)
        msg.addButton(QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        if msg.exec_() == QMessageBox.Yes:
            chamado_parceiro = ChamadoParceiro()
            chamado_parceiro.numero_chamado = self.txt_numero_chamado.text()

            try:
                chamado_parceiro_dao = ChamadoParceiroDao()
                chamado_parceiro_dao.excluir_chamado_parceiro_banco(chamado_parceiro.numero_chamado)

                msg2 = QMessageBox()
                msg2.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg2.setIcon(QMessageBox.Information)
                msg2.setWindowTitle("Exclusão de Chamado")
                msg2.setText(f'chamado {chamado_parceiro.numero_chamado} excluido com sucesso!')
                msg2.exec_()

                self.limpar_campos_formulario()
                self.listar_chamado_parceiro_tabela()
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def consultar_chamado_tabela_por_numero(self):
        if self.txt_consulta_numero_chamado.text() == "":
            self.mensagem.mensagem_campo_vazio('CONSULTA POR NÚMERO DO CHAMADO')
            self.txt_consulta_numero_chamado.setText("")
            self.listar_chamado_parceiro_tabela()
        elif not self.txt_consulta_numero_chamado.text().isdigit():
            self.mensagem.mensagem_campo_numerico('NÚMERO CHAMADO')
            self.txt_consulta_numero_chamado.setText("")
            self.listar_chamado_parceiro_tabela()
        else:
            chamafo_parceiro = ChamadoParceiro()
            chamafo_parceiro.numero_chamado = self.txt_consulta_numero_chamado.text()

            chamado_parceiro_dao = ChamadoParceiroDao()
            resultado = chamado_parceiro_dao.listar_chamado_parceiro_por_numero_chamado_banco(
                chamafo_parceiro.numero_chamado)

            if len(resultado) == 0:
                self.mensagem.mensagem_registro_não_encontrado(chamafo_parceiro.numero_chamado)
                self.txt_consulta_numero_chamado.setText("")
            else:
                self.tabela_chamado_parceiro.setRowCount(len(resultado))
                self.tabela_chamado_parceiro.setColumnCount(8)

                for i in range(len(resultado)):
                    for j in range(0, 8):
                        self.tabela_chamado_parceiro.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))

                self.txt_consulta_numero_chamado.setText("")

    def consultar_chamado_tabela_por_numero_chamado_simpress(self):
        if self.txt_consulta_chamado_simpress.text() == "":
            self.mensagem.mensagem_campo_vazio('CONSULTA POR NÚMERO DO CHAMADO SIMPRESS')
            self.limpar_campos_formulario()
            self.listar_chamado_parceiro_tabela()
        else:
            chamado_parceiro = ChamadoParceiro()
            chamado_parceiro.chamado_simpress = self.txt_consulta_chamado_simpress.text()

            chamado_parceiro_dao = ChamadoParceiroDao()
            resultado = chamado_parceiro_dao.listar_chamado_parceiro_por_numero_chamado_simpress_banco(
                chamado_parceiro.chamado_simpress)

            if len(resultado) == 0:
                self.mensagem.mensagem_registro_não_encontrado(chamado_parceiro.chamado_simpress)
                self.txt_consulta_chamado_simpress.setText("")
            else:

                self.tabela_chamado_parceiro.setRowCount(len(resultado))
                self.tabela_chamado_parceiro.setColumnCount(8)

                for i in range(len(resultado)):
                    for j in range(0, 8):
                        self.tabela_chamado_parceiro.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))

                self.txt_consulta_chamado_simpress.setText("")

    def limpar_campos_formulario(self):
        self.txt_numero_chamado.setText("")
        self.combo_chamado_simpress.setCurrentText("Selecione uma opção")
        self.combo_empresa_parceira.setCurrentText("Selecione uma opção")
        self.txt_responsavel.setText("")
        self.combo_cliente.setCurrentText("Selecione uma opção")
        self.txt_problema.setText("")
        self.txt_observacao.setText("")
        self.txt_data_abertura.setText("")

        self.btn_fechar_chamado.setEnabled(False)
        self.btn_alterar.setEnabled(False)
        self.btn_excluir.setEnabled(False)
        self.btn_cadastrar.setEnabled(True)
