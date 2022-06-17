import getpass
import pandas as pd
from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow, QMessageBox
from components.mensagens import Mensagens
from dao.relatorio_dao import RelatorioDao
from view.ui_tela_relatorio_chamados import Ui_RelatorioChamado


class TelaRelatorioChamado(QMainWindow, Ui_RelatorioChamado):
    """Classe da tela de relatório de chamados.

    Esta classe tem por finalidade gerar vários relatórios conforme necessidade do usuário.
    """
    def __init__(self):
        super(TelaRelatorioChamado, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Relatório de Chamados")
        self.setFixedSize(400, 466)

        self.popula_combo_solucao()
        self.mensagem = Mensagens()
        self.btn_cancelar.clicked.connect(self.close)

        self.btn_gerar_solucao.clicked.connect(self.gerar_relatorio_solucao)
        """Função que chamado o método de gerar relatório de soluções."""

        self.btn_gerar_data.clicked.connect(self.gerar_relatorio_chamado_data)
        """Função que chamado o método de gerar relatório por Data."""

        self.btn_gerar_tipo.clicked.connect(self.gerar_relatorio_tipo_chamado)
        """Função que chamado o método de gerar relatório por tipo."""

        self.btn_gerar_status.clicked.connect(self.gerar_relatorio_status_chamado)
        """Função que chamado o método de gerar relatório por Status."""

        self.btn_gerar_relatorio_padrao.clicked.connect(self.gerar_relatorio_padrao)
        """Função que chamado o método de gerar relatório padrão."""

    def popula_combo_solucao(self):
        """Popular combo solução

        Popula a combo de solução com o nome das soluções cadastradas.
        :return: Lista de Soluções.
        """
        relatorio_dao = RelatorioDao()
        resultado = relatorio_dao.consulta_nome_solucao()

        for i in resultado:
            self.combo_solucao.addItem(str(i[0]))

    def gerar_relatorio_chamado_data(self):
        """Gerar relatório por data.

        Gera um relatório tendo como parametro a data e salva em .xlsx.
        :return: Arquivo .xlsx
        """
        user_windows = getpass.getuser()
        if self.txt_data.text() == "":
            self.mensagem.mensagem_campo_vazio('DATA')
        else:
            data = self.txt_data.text()

            if self.radio_numero_chamado.isChecked():
                try:
                    relatorio_dao = RelatorioDao()
                    resultado = relatorio_dao.relatorio_chamado_data_ordenado_por_numero(data)

                    if len(resultado) == 0:
                        msg = QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Relatório de Chamados")
                        msg.setText('Não há dados para gerar este relatório.')
                        msg.exec_()
                    else:
                        dados = pd.DataFrame(resultado)
                        dados.columns = ['Chamado', 'Contrato', 'Cliente', 'Endereço', 'Contato', 'Telefone', 'E-mail',
                                         'Problema', 'Observação', 'Status', 'Tipo de Chamado', 'Solução',
                                         'Data Abertura',
                                         'Data Fechamamento']

                        data_formatada = data.replace('/', '_')

                        dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\'
                                       f'Relatorio_chamados_{data_formatada}_por_numero_chamado.xlsx', index=False)

                        self.mensagem.mensagem_gerar_relatorio()
                except ConnectionError as con_erro:
                    print(con_erro)
                    self.mensagem.mensagem_de_erro()
            else:
                try:
                    relatorio_dao = RelatorioDao()
                    resultado = relatorio_dao.relatorio_chamado_data_ordenado_por_contrato(data)

                    if len(resultado) == 0:
                        msg = QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Relatório de Chamados")
                        msg.setText('Não há dados para gerar este relatório.')
                        msg.exec_()
                    else:
                        dados = pd.DataFrame(resultado)
                        dados.columns = ['Chamado', 'Contrato', 'Cliente', 'Endereço', 'Contato', 'Telefone', 'E-mail',
                                         'Problema', 'Observação', 'Status', 'Tipo de Chamado', 'Solução',
                                         'Data Abertura', 'Data Fechamamento']

                        data_formatada = data.replace('/', '_')

                        dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\'
                                       f'Relatorio_chamados_{data_formatada}_por_contrato.xlsx', index=False)
                        self.mensagem.mensagem_gerar_relatorio()
                except ConnectionError as con_erro:
                    print(con_erro)
                    self.mensagem.mensagem_de_erro()

    def gerar_relatorio_solucao(self):
        """Gerar relatório por solução.

        Gera um relatório tendo como parametro a solução e salva em .xlsx.
        :return: Arquivo .xlsx
        """
        user_windows = getpass.getuser()
        solucao = self.combo_solucao.currentText()

        if self.combo_solucao.currentText() == "Selecione uma opção":
            self.mensagem.mensagem_combo('SOLUÇÃO')
        else:

            if self.radio_numero_chamado.isChecked():
                try:
                    relatorio_dao = RelatorioDao()
                    resultado = relatorio_dao.relatorio_solucao_ordenado_numero_chamado(solucao)

                    if len(resultado) == 0:
                        msg = QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Relatório de Chamados")
                        msg.setText('Não há dados para gerar este relatório.')
                        msg.exec_()
                    else:
                        dados = pd.DataFrame(resultado)
                        dados.columns = ['Chamado', 'Contrato', 'Cliente', 'Endereço', 'Contato', 'Telefone', 'E-mail',
                                         'Problema', 'Observação', 'Status', 'Tipo de Chamado', 'Solução',
                                         'Data Abertura',
                                         'Data Fechamamento']
                        dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\'
                                       f'Relatorio_chamados_{solucao}_por_numero_chamado.xlsx', index=False)

                        self.mensagem.mensagem_gerar_relatorio()
                except ConnectionError as con_erro:
                    print(con_erro)
                    self.mensagem.mensagem_de_erro()
            else:
                try:
                    relatorio_dao = RelatorioDao()
                    resultado = relatorio_dao.relatorio_solucao_ordenado_contrato_chamado(solucao)

                    if len(resultado) == 0:
                        msg = QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Relatório de Chamados")
                        msg.setText('Não há dados para gerar este relatório.')
                        msg.exec_()
                    else:
                        dados = pd.DataFrame(resultado)
                        dados.columns = ['Chamado', 'Contrato', 'Cliente', 'Endereço', 'Contato', 'Telefone', 'E-mail',
                                         'Problema', 'Observação', 'Status', 'Tipo de Chamado', 'Solução',
                                         'Data Abertura',
                                         'Data Fechamamento']
                        dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\'
                                       f'Relatorio_chamados_{solucao}_por_numero_contrato.xlsx', index=False)

                        self.mensagem.mensagem_gerar_relatorio()
                except ConnectionError as con_erro:
                    print(con_erro)
                    self.mensagem.mensagem_de_erro()

    def gerar_relatorio_tipo_chamado(self):
        """Gerar relatório por Tipo de chamado.

        Gera um relatório tendo como parametro a tipo e salva em .xlsx.
        :return: Arquivo .xlsx
        """
        user_windows = getpass.getuser()

        if self.combo_tipo_chamado.currentText() == "Selecione uma opção":
            self.mensagem.mensagem_combo("TIPO DE CHAMADO")
        else:
            tipo_chamado = self.combo_tipo_chamado.currentText()

            if self.radio_numero_chamado.isChecked():
                try:
                    relatorio_dao = RelatorioDao()
                    resultado = relatorio_dao.relatorio_tipo_chamado_por_numero(tipo_chamado)

                    if len(resultado) == 0:
                        msg = QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Relatório de Chamados")
                        msg.setText('Não há dados para gerar este relatório.')
                        msg.exec_()
                    else:
                        dados = pd.DataFrame(resultado)
                        dados.columns = ['Chamado', 'Contrato', 'Cliente', 'Endereço', 'Contato', 'Telefone', 'E-mail',
                                         'Problema', 'Observação', 'Status', 'Tipo de Chamado', 'Solução',
                                         'Data Abertura',
                                         'Data Fechamamento']
                        dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\'
                                       f'Relatorio_chamados_{tipo_chamado}_por_numero_chamado.xlsx', index=False)
                        self.mensagem.mensagem_gerar_relatorio()
                except ConnectionError as con_erro:
                    print(con_erro)
                    self.mensagem.mensagem_de_erro()
            else:
                try:
                    relatorio_dao = RelatorioDao()
                    resultado = relatorio_dao.relatorio_tipo_chamado_por_contrato(tipo_chamado)

                    if len(resultado) == 0:
                        msg = QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Relatório de Chamados")
                        msg.setText('Não há dados para gerar este relatório.')
                        msg.exec_()
                    else:
                        dados = pd.DataFrame(resultado)
                        dados.columns = ['Chamado', 'Contrato', 'Cliente', 'Endereço', 'Contato', 'Telefone', 'E-mail',
                                         'Problema', 'Observação', 'Status', 'Tipo de Chamado', 'Solução',
                                         'Data Abertura',
                                         'Data Fechamamento']
                        dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\'
                                       f'Relatorio_chamados_{tipo_chamado}_por_numero_contrato.xlsx', index=False)
                        self.mensagem.mensagem_gerar_relatorio()
                except ConnectionError as con_erro:
                    print(con_erro)
                    self.mensagem.mensagem_de_erro()

    def gerar_relatorio_status_chamado(self):
        """Gerar relatório por Status.

        Gera um relatório tendo como parametro o status e salva em .xlsx.
        :return: Arquivo .xlsx
        """
        user_windows = getpass.getuser()

        if self.combo_status.currentText() == "Selecione uma opção":
            self.mensagem.mensagem_combo("STATUS DO CHAMADO")
        else:
            status_chamado = self.combo_status.currentText()

            if self.radio_numero_chamado.isChecked():
                try:
                    relatorio_dao = RelatorioDao()
                    resultado = relatorio_dao.relatorio_status_chamado_por_numero(status_chamado)

                    if len(resultado) == 0:
                        msg = QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Relatório de Chamados")
                        msg.setText('Não há dados para gerar este relatório.')
                        msg.exec_()
                    else:
                        dados = pd.DataFrame(resultado)
                        dados.columns = ['Chamado', 'Contrato', 'Cliente', 'Endereço', 'Contato', 'Telefone', 'E-mail',
                                         'Problema', 'Observação', 'Status', 'Tipo de Chamado', 'Solução',
                                         'Data Abertura',
                                         'Data Fechamamento']
                        dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\'
                                       f'Relatorio_chamados_{status_chamado}_por_numero_chamado.xlsx', index=False)
                        self.mensagem.mensagem_gerar_relatorio()
                except ConnectionError as con_erro:
                    print(con_erro)
                    self.mensagem.mensagem_de_erro()
            else:
                try:
                    relatorio_dao = RelatorioDao()
                    resultado = relatorio_dao.relatorio_status_chamado_por_contrato(status_chamado)

                    if len(resultado) == 0:
                        msg = QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Relatório de Chamados")
                        msg.setText('Não há dados para gerar este relatório.')
                        msg.exec_()
                    else:
                        dados = pd.DataFrame(resultado)
                        dados.columns = ['Chamado', 'Contrato', 'Cliente', 'Endereço', 'Contato', 'Telefone', 'E-mail',
                                         'Problema', 'Observação', 'Status', 'Tipo de Chamado', 'Solução',
                                         'Data Abertura',
                                         'Data Fechamamento']
                        dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\'
                                       f'Relatorio_chamados_{status_chamado}_por_numero_contrato.xlsx', index=False)
                        self.mensagem.mensagem_gerar_relatorio()
                except ConnectionError as con_erro:
                    print(con_erro)
                    self.mensagem.mensagem_de_erro()

    def gerar_relatorio_padrao(self):
        """Gerar relatório completo.

        Gera um relatório padrão sem filtros..
        :return: Arquivo .xlsx
        """
        user_windows = getpass.getuser()
        try:
            relatorio_dao = RelatorioDao()
            resultado = relatorio_dao.gerar_relatorio_padrao()

            if len(resultado) == 0:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Relatório de Chamados")
                msg.setText('Não há dados para gerar este relatório.')
                msg.exec_()
            else:
                dados = pd.DataFrame(resultado)
                dados.columns = ['Chamado', 'Contrato', 'Cliente', 'Endereço', 'Contato', 'Telefone', 'E-mail',
                                 'Problema', 'Observação', 'Status', 'Tipo de Chamado', 'Solução',
                                 'Data Abertura',
                                 'Data Fechamamento']
                dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\'
                               f'Relatorio_chamados.xlsx', index=False)
                self.mensagem.mensagem_gerar_relatorio()
        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_de_erro()
