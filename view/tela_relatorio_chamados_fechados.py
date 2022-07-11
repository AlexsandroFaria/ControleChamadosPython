import getpass
from datetime import datetime

import pandas as pd
from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow, QMessageBox
from components.mensagens import Mensagens
from dao.relatorio_dao import RelatorioDao
from view.ui_tela_relatorio_chamados_fechados import Ui_TelaRelatoriosChamadosFechados


class TelaRelatorioChamadosFechados(QMainWindow, Ui_TelaRelatoriosChamadosFechados):
    """Classe da tela de relatório de chamados fechados.

    Esta classe tem por finalidade gerar vários relatórios conforme necessidade do usuário.
    """

    def __init__(self):
        super(TelaRelatorioChamadosFechados, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle de Chamados - Relatório de Chamados")
        self.setFixedSize(400, 466)

        self.mensagem = Mensagens()

        self.btn_cancelar.clicked.connect(self.close)
        """Função para fechar a tela."""

        self.btn_gerar_data.clicked.connect(self.gerar_relatorio_chamados_fechados_data)
        """Função para chamar o método de gerar relatório po datas"""

        self.btn_gerar_tipo.clicked.connect(self.gerar_relatorio_chamados_fechados_tipo)
        """Função para chamar o método de gerar relatórios por Tipo"""

        self.btn_gerar_status.clicked.connect(self.gerar_relatorio_chamados_fechados_status)
        """Função para chamar o método de gerar relatórios por Status."""

        self.btn_gerar_relatorio_padrao.clicked.connect(self.gerar_relatorio_chamados_fechados)
        """Função que chama o método de gerar relatórios sem filtro."""

    def gerar_relatorio_chamados_fechados_data(self):
        """Gerar Relatório por data.

        Gera um relatório em .xlsx dos chamados fechados pelo intervalo de datas passados por parâmetro.
        :return: Relatório em .xlsx.
        """
        user_windows = getpass.getuser()

        if self.txt_data_inicial.text() == "//":
            self.mensagem.mensagem_campo_vazio('Data Inicial')
        elif self.txt_data_final.text() == "//":
            self.mensagem.mensagem_campo_vazio('Data Final')
        else:
            data_inicial = self.txt_data_inicial.text()
            data_final = self.txt_data_final.text()

            data_inicial_param = datetime.strptime(data_inicial, '%d/%m/%Y').strftime('%Y-%m-%d')
            data_final_param = datetime.strptime(data_final, '%d/%m/%Y').strftime('%Y-%m-%d')

            if self.radio_numero_chamado.isChecked():
                try:
                    relatorio_dao = RelatorioDao()
                    resultado = relatorio_dao.gerar_relatorio_chamado_fechado_datas_num_chamado(data_inicial_param,
                                                                                                data_final_param)
                    if len(resultado) == 0:
                        msg = QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Relatório de ChamadosmFechados")
                        msg.setText('Não há dados para gerar este relatório.')
                        msg.exec_()

                        self.txt_data_inicial.setText("")
                        self.txt_data_final.setText("")
                    else:
                        dados = pd.DataFrame(resultado)
                        dados.columns = ['Número do Chamado', 'Contrato', 'Cliente', 'Contato', 'Telefone', 'Problema',
                                         'Tipo', 'Solução', 'Status', 'Data Fechamento']

                        data_formatada_inicial = data_inicial_param.replace('/', '_')
                        data_formatada_final = data_final_param.replace('/', '_')

                        dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\'
                                       f'Relatorio_chamados_fechados_{data_formatada_inicial}_{data_formatada_final}_por_numero_chamado.xlsx',
                                       index=False)
                        self.mensagem.mensagem_gerar_relatorio()

                        self.txt_data_inicial.setText("")
                        self.txt_data_final.setText("")
                except ConnectionError as con_erro:
                    print(con_erro)
                    self.mensagem.mensagem_de_erro()
            else:
                try:
                    relatorio_dao = RelatorioDao()
                    resultado = relatorio_dao.gerar_relatorio_chamado_fechado_datas_num_contrato(data_inicial_param,
                                                                                                 data_final_param)
                    if len(resultado) == 0:
                        msg = QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Relatório de Chamados Fechados")
                        msg.setText('Não há dados para gerar este relatório.')
                        msg.exec_()

                        self.txt_data_inicial.setText("")
                        self.txt_data_final.setText("")
                    else:
                        dados = pd.DataFrame(resultado)
                        dados.columns = ['Número do Chamado', 'Contrato', 'Cliente', 'Contato', 'Telefone', 'Problema',
                                         'Tipo', 'Solução', 'Status', 'Data Fechamento']

                        data_formatada_inicial = data_inicial_param.replace('/', '_')
                        data_formatada_final = data_final_param.replace('/', '_')

                        dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\'
                                       f'Relatorio_chamados_fechados_{data_formatada_inicial}_{data_formatada_final}_por_contrato_chamado.xlsx',
                                       index=False)
                        self.mensagem.mensagem_gerar_relatorio()

                        self.txt_data_inicial.setText("")
                        self.txt_data_final.setText("")
                except ConnectionError as con_erro:
                    print(con_erro)
                    self.mensagem.mensagem_de_erro()

    def gerar_relatorio_chamados_fechados_tipo(self):
        """Gerar Relatório por tipo.

        Gera um relatório em .xlsx dos chamados fechados pelo tipo passado por parâmetro.
        :return: Relatório em .xlsx.
        """

        user_windows = getpass.getuser()

        if self.combo_tipo.currentText() == "Selecione uma opção":
            self.mensagem.mensagem_combo('Tipo')
        else:
            tipo = self.combo_tipo.currentText()

            if self.radio_numero_chamado.isChecked():
                try:
                    relatorio_dao = RelatorioDao()
                    resultado = relatorio_dao.gerar_relatorio_chamado_fechado_tipo_num_chamado(tipo)

                    if len(resultado) == 0:
                        msg = QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Relatório de Chamados")
                        msg.setText('Não há dados para gerar este relatório.')
                        msg.exec_()

                        self.combo_tipo.setCurrentText("Selecione uma opção")
                    else:
                        dados = pd.DataFrame(resultado)
                        dados.columns = ['Número do Chamado', 'Contrato', 'Cliente', 'Contato', 'Telefone', 'Problema',
                                         'Tipo', 'Solução', 'Status', 'Data Fechamento']
                        dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\'
                                       f'Relatorio_chamados_por_{tipo}_ordenado_numero_chamado.xlsx', index=False)

                        self.combo_tipo.setCurrentText("Selecione uma opção")
                        self.mensagem.mensagem_gerar_relatorio()
                except ConnectionError as con_erro:
                    print(con_erro)
                    self.mensagem.mensagem_de_erro()
            else:
                try:
                    relatorio_dao = RelatorioDao()
                    resultado = relatorio_dao.gerar_relatorio_chamado_fechado_tipo_num_contrato(tipo)

                    if len(resultado) == 0:
                        msg = QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Relatório de Chamados")
                        msg.setText('Não há dados para gerar este relatório.')
                        msg.exec_()

                        self.combo_tipo.setCurrentText("Selecione uma opção")
                    else:
                        dados = pd.DataFrame(resultado)
                        dados.columns = ['Número do Chamado', 'Contrato', 'Cliente', 'Contato', 'Telefone', 'Problema',
                                         'Tipo', 'Solução', 'Status', 'Data Fechamento']
                        dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\'
                                       f'Relatorio_chamados_por_{tipo}_ordenado_numero_contrato.xlsx', index=False)

                        self.combo_tipo.setCurrentText("Selecione uma opção")
                        self.mensagem.mensagem_gerar_relatorio()
                except ConnectionError as con_erro:
                    print(con_erro)
                    self.mensagem.mensagem_de_erro()

    def gerar_relatorio_chamados_fechados_status(self):
        """Gerar Relatório por status.

        Gera um relatório em .xlsx dos chamados fechados pelo status passado por parâmetro.
        :return: Relatório em .xlsx.
        """
        user_windows = getpass.getuser()

        if self.combo_status.currentText() == "Selecione uma opção":
            self.mensagem.mensagem_combo('Status')
        else:
            status = self.combo_status.currentText()

            if self.radio_numero_chamado.isChecked():
                try:
                    relatorio_dao = RelatorioDao()
                    resultado = relatorio_dao.gerar_relatorio_chamado_fechado_status_num_chamado(status)

                    if len(resultado) == 0:
                        msg = QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Relatório de Chamados")
                        msg.setText('Não há dados para gerar este relatório.')
                        msg.exec_()

                        self.combo_status.setCurrentText("Selecione uma opção")
                    else:
                        dados = pd.DataFrame(resultado)
                        dados.columns = ['Número do Chamado', 'Contrato', 'Cliente', 'Contato', 'Telefone', 'Problema',
                                         'Tipo', 'Solução', 'Status', 'Data Fechamento']
                        dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\'
                                       f'Relatorio_chamados_por_{status}_ordenado_numero_chamado.xlsx', index=False)

                        self.combo_status.setCurrentText("Selecione uma opção")
                        self.mensagem.mensagem_gerar_relatorio()
                except ConnectionError as con_erro:
                    print(con_erro)
                    self.mensagem.mensagem_de_erro()
            else:
                try:
                    relatorio_dao = RelatorioDao()
                    resultado = relatorio_dao.gerar_relatorio_chamado_fechado_status_num_contrato(status)

                    if len(resultado) == 0:
                        msg = QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Relatório de Chamados")
                        msg.setText('Não há dados para gerar este relatório.')
                        msg.exec_()

                        self.combo_status.setCurrentText("Selecione uma opção")
                    else:
                        dados = pd.DataFrame(resultado)
                        dados.columns = ['Número do Chamado', 'Contrato', 'Cliente', 'Contato', 'Telefone', 'Problema',
                                         'Tipo', 'Solução', 'Status', 'Data Fechamento']
                        dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\'
                                       f'Relatorio_chamados_por_{status}_ordenado_numero_contrato.xlsx', index=False)

                        self.combo_status.setCurrentText("Selecione uma opção")
                        self.mensagem.mensagem_gerar_relatorio()
                except ConnectionError as con_erro:
                    print(con_erro)
                    self.mensagem.mensagem_de_erro()

    def gerar_relatorio_chamados_fechados(self):
        """Gerar Relatório de chamados fechados.

        Gera um relatório em .xlsx dos chamados fechados sem filtro.
        :return: Relatório em .xlsx.
        """
        user_windows = getpass.getuser()

        try:
            relatorio_dao = RelatorioDao()
            resultado = relatorio_dao.gerar_relatorio_chamado_fechado()

            if len(resultado) == 0:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Relatório de Chamados")
                msg.setText('Não há dados para gerar este relatório.')
                msg.exec_()
            else:
                dados = pd.DataFrame(resultado)
                dados.columns = ['Número do Chamado', 'Contrato', 'Cliente', 'Contato', 'Telefone', 'Problema',
                                 'Tipo', 'Solução', 'Status', 'Data Fechamento']
                dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\'
                               f'Relatorio_chamados_fechados.xlsx', index=False)

                self.mensagem.mensagem_gerar_relatorio()
        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_de_erro()
