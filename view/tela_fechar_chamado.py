import getpass
from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2 import QtWidgets, QtGui
from dao.chamado_dao import ChamadoDao
from dao.fechar_chamado_dao import FecharChamadoDao
from model.fechar_chamado import FecharChamado
from view.ui_tela_fechar_chamado import Ui_FecharChamado
from components.mensagens import Mensagens
from datetime import datetime
import pandas as pd


class TelaFecharChamado(QMainWindow, Ui_FecharChamado):
    def __init__(self):
        super(TelaFecharChamado, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Controle de Chamados - Fechar chamado')
        self.setFixedSize(1140, 594)

        self.mensagem = Mensagens()

        """Carrega a data atual para a caixa de texto assim que o formulário é aberto."""
        self.pegar_data_atual()

        """Função para chamar o método de listar chamados na tabela."""
        self.listar_chamados_fechados_tabela()

        """Função que fecha a janela atual."""
        self.btn_sair.clicked.connect(self.close)

        """Função que chamado método para pegar a data atual."""
        self.btn_pegar_data.clicked.connect(self.pegar_data_atual)

        """Função que chama o método de pesquisa de chamado."""
        self.btn_pesquisar_chamado.clicked.connect(self.carregar_chamado_formulario)

        """Função que chama o método de fechar chamado."""
        self.btn_fechar_chamado.clicked.connect(self.fechar_chamado)

        """Função que chama a função de limpar os campos do formulário."""
        self.btn_limpar_tela.clicked.connect(self.limpar_campos_formulario)

        """Função que chama o método de exibir o detalhe dos chamados."""
        self.btn_exibir_detalhes.clicked.connect(self.exibir_chamado_detalhes)

        """Função que chama o método de consultar por número do chamado."""
        self.btn_consulta_numero_chamado_tabela.clicked.connect(self.consultar_chamado_fechado_por_numero)

        """Função que chama o método de gerar relatório em excel."""
        self.btn_gerar_relatorio.clicked.connect(self.gerar_relatório_chamados)

        """Função que chama o método de recarregar a tabela de chamados fechados"""
        self.btn_carregar_tabela.clicked.connect(self.listar_chamados_fechados_tabela)

        """Função que chama o método de consultar chamado por número de contrato."""
        self.btn_consulta_contrato_tabela.clicked.connect(self.consultar_chamado_fechado_por_contrato)

        """Função que chama o método de consultar chamado por nome do cliente."""
        self.btn_consultar_nome_cliente_tabela.clicked.connect(self.consultar_chamado_fechado_por_nome_cliente)

        """Função para fechar a janela atual."""
        self.btn_fechar_2.clicked.connect(self.close)

    def listar_chamados_fechados_tabela(self):
        """Listar Chamados

        Método que lista todos os chamados na tabela de chamados fechados.
        :return: Listagem de Chamados fechados.
        """
        try:
            fechar_chamado_dao = FecharChamadoDao()
            resultado = fechar_chamado_dao.listar_chamado_fechado_tabela_banco()

            self.tabela_chamados_fechados.setRowCount(len(resultado))
            self.tabela_chamados_fechados.setRowCount(10)

            for i in range(0, len(resultado)):
                for j in range(0, 10):
                    self.tabela_chamados_fechados.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_de_erro()

    def pegar_data_atual(self):
        """Pegar data atual

        Pega a data atual do sistema e retorna no campo de data.
        :return: Data Atual.
        """
        data = datetime.today().strftime('%d/%m/%Y')
        self.txt_data_fechamento.setText(data)

    def carregar_chamado_formulario(self):
        """Carregar chamado no formulário.

        Carrega o formulário de fechamento com os dados do chamado a ser fechado.
        :return: Dados do Chamado em aberto.
        """
        if not self.txt_consulta_chamado.text().isnumeric():
            self.mensagem.mensagem_campo_numerico('NÚMERO CHAMADO')
        elif self.txt_consulta_chamado.text() == "":
            self.mensagem.mensagem_campo_vazio('NÚMERO CHAMADO')
        else:
            try:
                fechar_chamado = FecharChamado()
                fechar_chamado.numero = self.txt_consulta_chamado.text()

                fechar_chamado_dao = FecharChamadoDao()
                resultado = fechar_chamado_dao.consultar_numero_chamado_formulario(fechar_chamado.numero)

                self.txt_numero_chamado.setText(str(resultado[0][0]))
                self.txt_contrato.setText(str(resultado[0][1]))
                self.txt_nome_cliente.setText(str(resultado[0][2]))
                self.txt_contato.setText(str(resultado[0][3]))
                self.txt_telefone.setText(str(resultado[0][4]))
                self.txt_problema.setText(str(resultado[0][5]))
                self.txt_tipo_chamado.setText(str(resultado[0][6]))

                self.txt_consulta_chamado.setText("")
            except IndexError as i_error:
                print(i_error)
                self.mensagem.mensagem_registro_não_encontrado(fechar_chamado.numero)
                self.txt_consulta_chamado.setText("")

    def fechar_chamado(self):
        """Fechar chamado

        Método que efetua o encerramento do chamado.
        """
        if self.txt_fechamento.toPlainText() == "":
            self.mensagem.mensagem_campo_vazio('FECHAMENTO')
        elif self.combo_status.currentText() == "Selecione uma opção":
            self.mensagem.mensagem_combo('STATUS')
        elif self.txt_data_fechamento.text() == "":
            self.mensagem.mensagem_campo_vazio('DATA DE FECHAMENTO')
        else:
            fechar_chamado = FecharChamado()
            fechar_chamado.numero = self.txt_numero_chamado.text()
            fechar_chamado.contrato = self.txt_contrato.text()
            fechar_chamado.nome_cliente = self.txt_nome_cliente.text()
            fechar_chamado.contato = self.txt_contato.text()
            fechar_chamado.telefone = self.txt_telefone.text()
            fechar_chamado.problema = self.txt_problema.toPlainText()
            fechar_chamado.tipo = self.txt_tipo_chamado.text()
            fechar_chamado.solucao = self.txt_fechamento.toPlainText()
            fechar_chamado.status = self.combo_status.currentText()
            data_fechamento = self.txt_data_fechamento.text()

            fechar_chamado.data_fechamento = datetime.strptime(data_fechamento, '%d/%m/%Y').strftime('%Y-%m-%d')

            try:
                fechar_chamado_dao = FecharChamadoDao()
                fechar_chamado_dao.fechar_chamado(fechar_chamado.numero, fechar_chamado.contrato,
                                                  fechar_chamado.nome_cliente, fechar_chamado.contato,
                                                  fechar_chamado.telefone, fechar_chamado.problema,
                                                  fechar_chamado.tipo, fechar_chamado.solucao, fechar_chamado.status,
                                                  fechar_chamado.data_fechamento)

                chamado_dao = ChamadoDao()
                chamado_dao.excluir_chamado_banco(fechar_chamado.numero)

                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Inserir Solução")
                msg.setText(f'Chamado {fechar_chamado.numero} encerrado com sucesso.')
                msg.exec_()

                self.limpar_campos_formulario()
                self.listar_chamados_fechados_tabela()
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def limpar_campos_formulario(self):
        """Limpar Campos do Formulário.

        Limpa os campos do formulário caso o mesmo esteja preenchido.
        """
        self.txt_numero_chamado.setText("")
        self.txt_contrato.setText("")
        self.txt_nome_cliente.setText("")
        self.txt_contato.setText("")
        self.txt_telefone.setText("")
        self.txt_problema.setText("")
        self.txt_tipo_chamado.setText("")
        self.txt_fechamento.setText("")
        self.combo_status.setCurrentText("Selecione uma opção")
        self.txt_data_fechamento.setText("")

    def exibir_chamado_detalhes(self):
        """Exibir detalhes do chamado fechado.

        Exibe em outro formulário os dados do chamado fechado selecionado pelo usuário.
        :return: Dados do chamado fechado.
        """

        linha = self.tabela_chamados_fechados.currentItem().text()

        if not linha.isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Consultar Chamados")
            msg.setText('Selecione somente a coluna Número do chamado')
            msg.exec_()
        else:
            try:
                fechar_chamado_dao = FecharChamadoDao()
                resultado = fechar_chamado_dao.listar_chamado_por_numero_banco(linha)

                if len(resultado) == 0:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Consulta Contrato")
                    msg.setText('Selecione somente a coluna Número do chamado!')
                    msg.exec_()
                else:
                    self.tab_fechar_chamado.setCurrentWidget(self.tab_detalhes)

                    self.txt_numero_chamado_detalhe.setText(str(resultado[0][0]))
                    self.txt_contrato_detalhe.setText(str(resultado[0][1]))
                    self.txt_nome_cliente_detalhe.setText(str(resultado[0][2]))
                    self.txt_contato_detalhe.setText(str(resultado[0][3]))
                    self.txt_telefone_detalhe.setText(str(resultado[0][4]))
                    self.txt_problema_detalhe.setText(str(resultado[0][5]))
                    self.txt_tipo_chamado_detalhe.setText(str(resultado[0][6]))
                    self.txt_fechamento_detalhe.setText(str(resultado[0][7]))
                    self.txt_status_detalhe.setText(str(resultado[0][8]))
                    self.txt_data_fechamento_detalhe.setText(str(resultado[0][9]))
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def consultar_chamado_fechado_por_numero(self):
        """Consultar chamado fechado por número

        Método que efetua a consulta de um chamado por número do mesmo.
        :return: Chamado conforme número solicitado pelo usuário.
        """
        if not self.txt_consulta_numero_chamado_tabela.text().isnumeric():
            self.mensagem.mensagem_campo_numerico('CONSULTA NUMERO CHAMADO')
            self.txt_consulta_numero_chamado_tabela.setText("")
            self.listar_chamados_fechados_tabela()
        else:
            fechar_chamado = FecharChamado()
            fechar_chamado.numero = self.txt_consulta_numero_chamado_tabela.text()

            try:
                fechar_chamado_dao = FecharChamadoDao()
                resultado = fechar_chamado_dao.consultar_chamado_fechado_por_numero_tabela(fechar_chamado.numero)

                if len(resultado) == 0:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Consulta Contrato")
                    msg.setText('Numero do chamado não encontrado!')
                    msg.exec_()

                    self.txt_consulta_numero_chamado_tabela.setText("")
                    self.listar_chamados_fechados_tabela()
                else:
                    self.tabela_chamados_fechados.setRowCount(len(resultado))
                    self.tabela_chamados_fechados.setColumnCount(10)

                    for i in range(len(resultado)):
                        for j in range(0, 10):
                            self.tabela_chamados_fechados.setItem(i, j,
                                                                  QtWidgets.QTableWidgetItem(str(resultado[i][j])))

                    self.txt_consulta_numero_chamado_tabela.setText("")
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def consultar_chamado_fechado_por_contrato(self):
        """Consultar chamado fechado por número do Contrato

        Método que efetua a consulta de um chamado por número do Contrato.
        :return: Chamado conforme número do contrato solicitado pelo usuário.
        """
        if not self.txt_consultar_contrato_tabela.text().isdigit():
            self.mensagem.mensagem_campo_numerico("CONSULTA NÚMERO CONTRATO")
            self.txt_consultar_contrato_tabela.setText("")
            self.listar_chamados_fechados_tabela()
        else:
            fechar_chamado = FecharChamado()
            fechar_chamado.contrato = self.txt_consultar_contrato_tabela.text()

            try:
                fechar_chamado_dao = FecharChamadoDao()
                resultado = fechar_chamado_dao.consultar_chamado_fechado_por_contrato_tabela(fechar_chamado.contrato)

                if len(resultado) == 0:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Consulta Contrato")
                    msg.setText('Numero do contrato não encontrado!')
                    msg.exec_()

                    self.txt_consultar_nome_cliente.setText("")
                    self.listar_chamados_fechados_tabela()
                else:
                    self.tabela_chamados_fechados.setRowCount(len(resultado))
                    self.tabela_chamados_fechados.setColumnCount(10)

                    for i in range(len(resultado)):
                        for j in range(0, 10):
                            self.tabela_chamados_fechados.setItem(i, j,
                                                                  QtWidgets.QTableWidgetItem(str(resultado[i][j])))
                    self.txt_consultar_contrato_tabela.setText("")
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def consultar_chamado_fechado_por_nome_cliente(self):
        """Consultar chamado fechado por nome do cliente.

        Método que efetua a consulta de um chamado por nome do Cliente.
        :return: Chamado conforme nome do cliente solicitado pelo usuário.
        """
        if self.txt_consulta_nome_cliente.text() == "":
            self.mensagem.mensagem_campo_vazio("CONSULTA NOME CLIENTE")
            self.txt_consulta_nome_cliente.setText("")
            self.listar_chamados_fechados_tabela()
        else:
            fechar_chamado = FecharChamado()
            fechar_chamado.nome_cliente = self.txt_consulta_nome_cliente.text()

            try:
                fechar_chamado_dao = FecharChamadoDao()
                resultado = fechar_chamado_dao.consultar_chamado_fechado_por_nome_cliente_tabela(
                    fechar_chamado.nome_cliente)

                if len(resultado) == 0:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Consulta Nome do Cliente")
                    msg.setText('Nome do Cliente não encontrado!')
                    msg.exec_()

                    self.txt_consultar_nome_cliente.setText("")
                    self.listar_chamados_fechados_tabela()
                else:
                    self.tabela_chamados_fechados.setRowCount(len(resultado))
                    self.tabela_chamados_fechados.setColumnCount(10)

                    for i in range(len(resultado)):
                        for j in range(0, 10):
                            self.tabela_chamados_fechados.setItem(i, j,
                                                                  QtWidgets.QTableWidgetItem(str(resultado[i][j])))
                    self.txt_consulta_nome_cliente.setText("")
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def gerar_relatório_chamados(self):
        """Gerar relatório de Chamados.

       Método que gera um relatório de chamados, converte para o formato .xlsx e salva na pasta download.
       :return: Geração de relatório.
       """
        user_windows = getpass.getuser()

        try:
            fechar_chamado_dao = FecharChamadoDao()
            resultado = fechar_chamado_dao.listar_chamado_fechado_tabela_banco()

            dados = pd.DataFrame(resultado)
            dados.columns = ['Chamado', 'Contrato', 'Cliente', 'Contato', 'Telefone', 'Problema', 'Tipo',
                            'Solução', 'Status', 'Data']

            dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\'
                       f'Relatorio de chamados fechados.xlsx', index=False)

            self.mensagem.mensagem_gerar_relatorio()

        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_de_erro()
