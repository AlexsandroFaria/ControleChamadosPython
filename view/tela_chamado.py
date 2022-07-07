import getpass

from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2 import QtWidgets, QtGui
from components.mensagens import Mensagens
from dao.chamado_dao import ChamadoDao
from model.chamado import Chamado
from view.tela_fechar_chamado import TelaFecharChamado
from view.ui_tela_chamado import Ui_TelaChamado
from datetime import datetime
import pandas as pd


class TelaChamado(QMainWindow, Ui_TelaChamado):
    """Tela de Chamados

    Tela responsavel pela interação do usuário para inclusão, alteração e exclusão de dados chamados.
    A mesma também possui área para visualização de chamados para consulta.
    """
    def __init__(self):
        super(TelaChamado, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle de Chamados")
        self.setFixedSize(1245, 658)

        self.mensagem = Mensagens()

        self.popula_campo_solucao()
        """Chama o método para popular a combobox de Solução."""

        self.pegar_data_atual()
        """Popula o campo de data atual com a data do dia."""

        self.btn_atualizar_data.clicked.connect(self.atualizar_data)
        """Atualiza o campo com a data do dia."""

        self.listar_chamado_tabela()
        """Função para chamar o método de listar os chamados na tabela da tela de consulta de chamados."""

        self.btn_cadastrar.clicked.connect(self.cadastrar_chamado)
        """Função que chama o método para cadastrar um chamado e salvar em banco de dados."""

        self.btn_buscar_contrato.clicked.connect(self.buscar_contrato_cliente_no_formulario)
        """Função que chama o método de consulta a clientes e popula o formulário de Chamado com alguns dados."""

        self.btn_carregar.clicked.connect(self.carregar_dados_tabela_para_formulario)
        """Função que chama o método de popular o formulário com os dados selecionados."""

        self.btn_limpar_tela.clicked.connect(self.limpar_campos_formulario)
        """Função que chama o método de limpar os campos do formulário."""

        self.btn_atualizar_data_abertura.clicked.connect(self.pegar_data_atual)
        """Função que chama o método para atualizar a data atual."""

        self.btn_alterar.clicked.connect(self.alterar_chamado)
        """Função que chama o método para alterar os dados do formulário."""

        self.btn_excluir.clicked.connect(self.excluir_chamado)
        """Função que chama o métodod e excluir chamado."""

        self.btn_fechar_chamado.clicked.connect(self.fechar_chamado)
        """Função que chama o método de fechar chamado."""

        self.btn_consultar_numero_chamado.clicked.connect(self.listar_chamado_tabela_por_numero_chamado)
        """Função que chama o método de listar chamados e retornar na tabela de chamados."""

        self.btn_carregar_tabela.clicked.connect(self.listar_chamado_tabela)
        """Função que chama o método que recarrega a lista de chamados."""

        self.btn_consulta_contrato.clicked.connect(self.listar_chamado_tabela_por_contrato)
        """Função que chama o método de listar chamados por número de contrato."""

        self.btn_consultar_nome_cliente.clicked.connect(self.listar_chamado_por_nome_cliente)
        """Função que chamado o método de listar chamado por nome do cliente."""

        self.btn_gerar_relatrio.clicked.connect(self.gerar_relatorio_chamados)
        """Função que chama o método para geração de Relatórios"""

        self.btn_fechar_tela.clicked.connect(self.close)
        """Fecha e encerra a janela."""

        self.btn_alterar.setEnabled(False)
        self.btn_excluir.setEnabled(False)
        self.btn_fechar_chamado.setEnabled(False)

    def popula_campo_solucao(self):
        """Popular Campo de solução

        Este método popula a comboBox com o nome das soluções cadastradas.
        :return: Lista de soluções.
        """
        try:
            chamado_dao = ChamadoDao()
            resultado = chamado_dao.popular_combo_solucao()

            for i in resultado:
                self.combo_solucao.addItem(str(i[0]))
        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_de_erro()

    def listar_chamado_tabela(self):
        """Listar chamado

        Este Método lista os chamados na tabela de consulta de chamados.
        :return: Lista de chamados cadastrados.
        """
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

    def pegar_data_atual(self):
        """Pegar Data Atual.

        Método para capturar a data atual.
        """
        data = datetime.today().strftime('%d/%m/%Y')
        self.txt_data_abertura.setText(data)

    def atualizar_data(self):
        """Atualizar data.

        Método para atualizar a data do chamado.
        """
        data = datetime.today().strftime('%d/%m/%Y')
        self.txt_data_atualizacao.setText(data)

    def buscar_contrato_cliente_no_formulario(self):
        """Consultar contrato no Formulário

        Efetua uma consulta por contrato na tabela de cliente e retorna os valores para popular o formulário
        da tela de chamados.
        :return: Retorna um cliente por número de contrato.
        """
        if self.txt_numero_contrato.text() == "":
            self.mensagem.mensagem_campo_vazio('NÚMERO CONTRATO')
        elif self.txt_numero_contrato.text().isnumeric():
            try:
                chamado = Chamado()
                chamado.numero_contrato = self.txt_numero_contrato.text()

                chamado_dao = ChamadoDao()
                resultado = chamado_dao.buscar_contrato_cliente_formulario_banco(chamado.numero_contrato)

                self.txt_nome_cliente.setText(str(resultado[0][2]))
                self.txt_endereco.setText(str(resultado[0][3]))
                self.txt_contato.setText(str(resultado[0][4]))
                self.txt_telefone.setText(str(resultado[0][5]))
                self.txt_email.setText(str(resultado[0][6]))
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()
            except IndexError as i_error:
                print(i_error)
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Consulta Contrato")
                msg.setText('Contrato não encontrado!')
                msg.exec_()

                self.limpar_campos_formulario()
        else:
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Consulta Contrato")
            msg.setText('No campo CONTRATO informe somente números!')
            msg.exec_()

    def carregar_dados_tabela_para_formulario(self):
        """Carregar dados para o formulário.

        Carrega os dados do chamado no formulário com os dados consultados no banco de dados.
        :return:
        """
        try:

            linha = self.tabela_chamado.currentItem().text()

            if not linha.isdigit():
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Consultar Chamados")
                msg.setText('Selecione somente a coluna Número do chamado')
                msg.exec_()
            else:
                chamado_dao = ChamadoDao()
                resultado = chamado_dao.consultar_numero_chamado(linha)

                if len(resultado) == 0:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Consulta Contrato")
                    msg.setText('Selecione somente a coluna Número do chamado!')
                    msg.exec_()
                else:
                    self.tab_chamado.setCurrentWidget(self.tab_cadastro_chamado)

                    self.txt_numero_chamado.setText(str(resultado[0][0]))
                    self.txt_numero_contrato.setText(str(resultado[0][1]))
                    self.txt_nome_cliente.setText(str(resultado[0][2]))
                    self.txt_endereco.setText(str(resultado[0][3]))
                    self.txt_contato.setText(str(resultado[0][4]))
                    self.txt_telefone.setText(str(resultado[0][5]))
                    self.txt_email.setText(str(resultado[0][6]))
                    self.txt_problema.setText(str(resultado[0][7]))
                    self.txt_observacao.setText(str(resultado[0][8]))
                    self.combo_status_chamado.setCurrentText(resultado[0][9])
                    self.combo_tipo_chamado.setCurrentText(str(resultado[0][10]))
                    self.combo_solucao.setCurrentText(str(resultado[0][11]))
                    self.txt_data_abertura.setText(str(resultado[0][12]))
                    self.txt_data_atualizacao.setText(str(resultado[0][13]))

                    self.btn_alterar.setEnabled(True)
                    self.btn_excluir.setEnabled(True)
                    self.btn_cadastrar.setEnabled(False)
                    self.txt_numero_contrato.setEnabled(False)
                    self.btn_fechar_chamado.setEnabled(True)

        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_de_erro()
        except AttributeError as at_erro:
            print(at_erro)
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Consultar Chamado")
            msg.setText('Selecione um item da coluna Número do chamado.')
            msg.exec_()

    def consultar_numero_contrato(self):
        """Consultar Número de contrato

        Efetua uma consulta por número de contrato e retorna os possíveis resultados na tabela de chamados.
        :return: Lista de chamados por número de contrato.
        """
        if self.txt_consulta_contrato.text() == "":
            self.mensagem.mensagem_campo_vazio('NÚMERO DO CONTRATO')
        elif self.txt_contato.text().isnumeric():
            try:
                chamado = Chamado()
                chamado.numero_contrato = self.txt_consulta_contrato.text()

                chamado_dao = ChamadoDao()
                resultado = chamado_dao.consultar_contrato_banco(chamado.numero_contrato)

                if len(resultado) == 0:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Consulta Contrato")
                    msg.setText('Numero do contrato não encontrado!')
                    msg.exec_()

                    self.txt_consulta_contrato.setText("")
                    self.listar_chamado_tabela()
                else:
                    self.tabela_chamado.setRowCount(len(resultado))
                    self.tabela_chamado.setColumnCount(14)

                    for i in range(len(resultado)):
                        for j in range(0, 14):
                            self.tabela_chamado.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
                    self.txt_consulta_contrato.setText()
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def cadastrar_chamado(self):
        """Cadastrar Chamado.

        Método que cadastra um chamado no banco de dados e exibe o resultado na tabela da tela de chamados.
        :return: Cadastro de Chamado
        """
        if self.txt_numero_chamado.text() == "":
            self.mensagem.mensagem_campo_vazio("NÚMERO CHAMADO")
        elif self.txt_numero_contrato.text() == "":
            self.mensagem.mensagem_campo_vazio('NÚMERO CONTRATO')
        elif self.txt_nome_cliente.text() == "":
            self.mensagem.mensagem_campo_vazio('NOME CLIENTE')
        elif self.txt_contato.text() == "":
            self.mensagem.mensagem_campo_vazio('CONTATO')
        elif self.txt_telefone.text() == "":
            self.mensagem.mensagem_campo_vazio('TELEFONE')
        elif self.txt_email.text() == "":
            self.mensagem.mensagem_campo_vazio("E-MAIL")
        elif self.txt_problema.toPlainText() == "":
            self.mensagem.mensagem_campo_vazio("PROBLEMA")
        elif self.combo_status_chamado.currentText() == "Selecione uma Opção":
            self.mensagem.mensagem_combo('STATUS DE CHAMADO')
        elif self.combo_tipo_chamado.currentText() == "Selecione uma Opção":
            self.mensagem.mensagem_combo('TIPO CHAMADO')
        elif self.combo_solucao.currentText() == "Selecione uma Opção":
            self.mensagem.mensagem_combo('SOLUÇÃO')
        elif self.txt_data_atualizacao.text() == "":
            self.mensagem.mensagem_campo_vazio('DATA ATUALIZAÇÃO')
        else:
            chamado = Chamado()
            chamado.numero_chamado = self.txt_numero_chamado.text()
            chamado.numero_contrato = self.txt_numero_contrato.text()
            chamado.nome_cliente = self.txt_nome_cliente.text()
            chamado.endereco = self.txt_endereco.text()
            chamado.contato = self.txt_contato.text()
            chamado.telefone = self.txt_telefone.text()
            chamado.email = self.txt_email.text()
            chamado.problema = self.txt_problema.toPlainText()
            chamado.observacao = self.txt_observacao.text()
            chamado.status = self.combo_status_chamado.currentText()
            chamado.tipo = self.combo_tipo_chamado.currentText()
            chamado.solucao = self.combo_solucao.currentText()
            data_abertura = self.txt_data_abertura.text()
            data_atualizacao = self.txt_data_atualizacao.text()

            chamado.data_abertura = datetime.strptime(data_abertura, '%d/%m/%Y').strftime('%Y-%m-%d')
            chamado.data_atualizacao = datetime.strptime(data_atualizacao, '%d/%m/%Y').strftime('%Y-%m-%d')

            try:
                chamado_dao = ChamadoDao()
                chamado_dao.cadastrar_chamado_banco(chamado.numero_chamado, chamado.numero_contrato,
                                                    chamado.nome_cliente, chamado.endereco, chamado.contato,
                                                    chamado.telefone, chamado.email, chamado.problema,
                                                    chamado.observacao, chamado.status, chamado.tipo,
                                                    chamado.solucao, chamado.data_abertura,
                                                    chamado.data_atualizacao)
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Cadastro de Chamado")
                msg.setText(f'Chamado {chamado.numero_chamado} cadastrado com sucesso.')
                msg.exec_()

                self.listar_chamado_tabela()
                self.limpar_campos_formulario()
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def alterar_chamado(self):
        """Alterar Chamado.

        Método que altera os dados do chamado caso necessário.
        :return: Alteração chamado
        """
        if self.txt_numero_chamado.text() == "":
            self.mensagem.mensagem_campo_vazio("NÚMERO CHAMADO")
        elif self.txt_numero_contrato.text() == "":
            self.mensagem.mensagem_campo_vazio('NÚMERO CONTRATO')
        elif self.txt_nome_cliente.text() == "":
            self.mensagem.mensagem_campo_vazio('NOME CLIENTE')
        elif self.txt_contato.text() == "":
            self.mensagem.mensagem_campo_vazio('CONTATO')
        elif self.txt_telefone.text() == "":
            self.mensagem.mensagem_campo_vazio('TELEFONE')
        elif self.txt_email.text() == "":
            self.mensagem.mensagem_campo_vazio("E-MAIL")
        elif self.txt_problema.toPlainText() == "":
            self.mensagem.mensagem_campo_vazio("PROBLEMA")
        elif self.combo_status_chamado.currentText() == "Selecione uma Opção":
            self.mensagem.mensagem_combo('STATUS DE CHAMADO')
        elif self.combo_tipo_chamado.currentText() == "Selecione uma Opção":
            self.mensagem.mensagem_combo('TIPO CHAMADO')
        elif self.combo_solucao.currentText() == "Selecione uma Opção":
            self.mensagem.mensagem_combo('SOLUÇÃO')
        elif self.txt_data_atualizacao.text() == "":
            self.mensagem.mensagem_campo_vazio('DATA ATUALIZAÇÃO')
        else:
            chamado = Chamado()
            chamado.numero_chamado = self.txt_numero_chamado.text()
            chamado.numero_contrato = self.txt_numero_contrato.text()
            chamado.telefone = self.txt_telefone.text()
            chamado.email = self.txt_email.text()
            chamado.problema = self.txt_problema.toPlainText()
            chamado.observacao = self.txt_observacao.text()
            chamado.status = self.combo_status_chamado.currentText()
            chamado.tipo = self.combo_tipo_chamado.currentText()
            chamado.solucao = self.combo_solucao.currentText()
            data_abertura = self.txt_data_abertura.text()
            data_atualizacao = self.txt_data_atualizacao.text()

            chamado.data_abertura = datetime.strptime(data_abertura, '%d/%m/%Y').strftime('%Y-%m-%d')
            chamado.data_atualizacao = datetime.strptime(data_atualizacao, '%d/%m/%Y').strftime('%Y-%m-%d')

            try:
                chamado_dao = ChamadoDao()
                chamado_dao.alterar_chamado_banco(chamado.numero_chamado, chamado.telefone, chamado.email,
                                                  chamado.problema, chamado.observacao, chamado.status, chamado.tipo,
                                                  chamado.solucao, chamado.data_abertura, chamado.data_atualizacao)

                chamado_dao.alterar_cliente_telefone_email(chamado.numero_contrato, chamado.telefone, chamado.email)

                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Alterar Chamado")
                msg.setText(f'Chamado {chamado.numero_chamado} alterado com sucesso.')
                msg.exec_()

                self.limpar_campos_formulario()
                self.listar_chamado_tabela()
                self.txt_numero_contrato.setEnabled(True)
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def excluir_chamado(self):
        """Excluir Chamado

        Método que exclui um chamado passando como referência o número do chamado.
        :return: Exclusão de chamado.
        """
        if self.txt_numero_chamado.text() == "":
            self.mensagem.mensagem_campo_vazio('NÚMERO CHAMADO')
        else:
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
            msg.setWindowTitle("Exclusão de Chamado!")
            msg.setText("Tem certeza que deseja excluir o Chamado?")
            msg.setStandardButtons(QMessageBox.Yes)
            msg.addButton(QMessageBox.No)
            msg.setDefaultButton(QMessageBox.No)
            if msg.exec_() == QMessageBox.Yes:
                chamado = Chamado()
                chamado.numero_chamado = self.txt_numero_chamado.text()

                try:
                    chamado_dao = ChamadoDao()
                    chamado_dao.excluir_chamado_banco(chamado.numero_chamado)

                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Exclusão de Chamado")
                    msg.setText(f'Chamado {chamado.numero_chamado} excluido com sucesso.')
                    msg.exec_()

                    self.limpar_campos_formulario()
                    self.listar_chamado_tabela()
                except ConnectionError as con_erro:
                    print(con_erro)
                    self.mensagem.mensagem_de_erro()

    def fechar_chamado(self):
        """Fechar Chamado

        Método que abre a tela de fechamento de chamados passando alguns parâmetros para encerramento do mesmo.
        :return: Tela fechar chamado
        """
        if not self.txt_numero_chamado.text().isnumeric():
            self.mensagem.mensagem_campo_numerico('NÚMERO CHAMADO')
        elif not self.txt_numero_contrato.text().isnumeric():
            self.mensagem.mensagem_campo_numerico('NÚMERO CONTRATO')
        elif self.txt_nome_cliente.text() == "":
            self.mensagem.mensagem_campo_vazio('NOME CLIENTE')
        elif self.txt_contato.text() == "":
            self.mensagem.mensagem_campo_vazio('CONTATO')
        elif self.txt_telefone.text() == "":
            self.mensagem.mensagem_campo_vazio('TELEFONE')
        elif self.txt_problema.toPlainText() == "":
            self.mensagem.mensagem_campo_vazio('PROBLEMA')
        elif self.combo_tipo_chamado.currentText() == 'Selecione uma Opção':
            self.mensagem.mensagem_combo('TIPO CHAMADO')
        elif self.combo_solucao.currentText() == 'Selecione uma opção':
            self.mensagem.mensagem_combo('SOLUÇÃO')
        elif self.combo_status_chamado.currentText() == 'Selecione uma opção':
            self.mensagem.mensagem_combo('STATUS DO CHAMADO')
        else:
            self.tela_fechar_chamado = TelaFecharChamado()
            self.tela_fechar_chamado.txt_numero_chamado.setText(self.txt_numero_chamado.text())
            self.tela_fechar_chamado.txt_contrato.setText(self.txt_numero_contrato.text())
            self.tela_fechar_chamado.txt_nome_cliente.setText(self.txt_nome_cliente.text())
            self.tela_fechar_chamado.txt_contato.setText(self.txt_contato.text())
            self.tela_fechar_chamado.txt_telefone.setText(self.txt_telefone.text())
            self.tela_fechar_chamado.txt_problema.setText(self.txt_problema.toPlainText())
            self.tela_fechar_chamado.txt_tipo_chamado.setText(self.combo_tipo_chamado.currentText())
            self.tela_fechar_chamado.show()
            self.close()

    def listar_chamado_tabela_por_numero_chamado(self):
        """Listar Chamado tabela

        Método que efetua uma consulta conforme parâmetro informado pelo usuário e retorna o resultado na tabela.
        :return: lista de chamados conforme parâmetro passado.
        """
        if self.txt_consulta_numero_chamado.text() == "":
            self.mensagem.mensagem_campo_vazio('CONCULTA NÚMERO CHAMADO')
        elif not self.txt_consulta_numero_chamado.text().isdigit():
            self.mensagem.mensagem_campo_numerico("CONSULTA NÚMERO CHAMADO")
            self.txt_consulta_numero_chamado.setText("")
        else:
            chamado = Chamado()
            chamado.numero_chamado = self.txt_consulta_numero_chamado.text()

            try:
                chamado_dao = ChamadoDao()
                resultado = chamado_dao.listar_numero_chamado_tabela(chamado.numero_chamado)

                if len(resultado) == 0:
                    self.mensagem.mensagem_registro_não_encontrado(chamado.numero_chamado)
                    self.txt_consulta_numero_chamado.setText("")
                    self.listar_chamado_tabela()
                else:
                    self.tabela_chamado.setRowCount(len(resultado))
                    self.tabela_chamado.setColumnCount(14)

                    for i in range(len(resultado)):
                        for j in range(0, 14):
                            self.tabela_chamado.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
                    self.txt_consulta_numero_chamado.setText("")

            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def listar_chamado_tabela_por_contrato(self):
        """Listar chamado por contrato

        Método que lista os chamados conforme número do contrato passado como parâmetro.
        :return: Lista de chamados conforme parâmetro.
        """
        if self.txt_consulta_contrato.text() == "":
            self.mensagem.mensagem_campo_vazio('NÚMERO DO CONTRATO')
        elif not self.txt_consulta_contrato.text().isdigit():
            self.mensagem.mensagem_campo_numerico('NÚMERO DO CONTRATO')
            self.txt_consulta_contrato.setText("")
        else:
            chamado = Chamado()
            chamado.numero_contrato = self.txt_consulta_contrato.text()

            try:
                chamado_dao = ChamadoDao()
                resultado = chamado_dao.listar_chamado_por_contrato(chamado.numero_contrato)

                if len(resultado) == 0:
                    self.mensagem.mensagem_registro_não_encontrado(chamado.numero_contrato)
                    self.txt_consulta_contrato.setText("")
                else:
                    self.tabela_chamado.setRowCount(len(resultado))
                    self.tabela_chamado.setColumnCount(14)

                    for i in range(len(resultado)):
                        for j in range(0, 14):
                            self.tabela_chamado.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
                    self.txt_consulta_contrato.setText("")
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def listar_chamado_por_nome_cliente(self):
        """Listar Chamado por nome do cliente.

        Lista os chamados por nome do cliente passado como parâmetro.
        :return: Listagem de camados conforme parâmetro.
        """
        if self.txt_consulta_nome_cliente.text() == "":
            self.mensagem.mensagem_campo_vazio('NOME DO CLIENTE')
        else:
            chamado = Chamado()
            chamado.nome_cliente = self.txt_consulta_nome_cliente.text()

            try:
                chamado_dao = ChamadoDao()
                resultado = chamado_dao.listar_chamado_por_nome_cliente(chamado.nome_cliente)

                if len(resultado) == 0:
                    self.mensagem.mensagem_registro_não_encontrado(chamado.nome_cliente)
                    self.txt_consulta_nome_cliente.setText("")
                else:
                    self.tabela_chamado.setRowCount(len(resultado))
                    self.tabela_chamado.setColumnCount(14)

                    for i in range(len(resultado)):
                        for j in range(0, 14):
                            self.tabela_chamado.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
                    self.txt_consulta_nome_cliente.setText("")

            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def gerar_relatorio_chamados(self):
        """Gerar Relatório

        Método que gera um relatório em .xlsx e salva na pasta download do usuário.
        :return: Geração de relatório.
        """
        user_windows = getpass.getuser()

        try:
            chamado_dao = ChamadoDao()
            resultado = chamado_dao.listar_chamado_tabela()

            dados = pd.DataFrame(resultado)
            dados.columns = ['Número do Chamado', 'Número do Contrato', 'Nome do Cliente', 'Endereço', 'Contato',
                             'Telefone', 'E-mail', 'Problema', 'Observação', 'Status do Chamado', 'Tipo do Chamado',
                             'Solução do Problema', 'Data de Abertura', 'Data de atualização']
            dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\Controle de Chamados - Relatorio de chamados.xlsx',
                           index=False)

            self.mensagem.mensagem_gerar_relatorio()
        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_de_erro()

    def limpar_campos_formulario(self):
        """Limpar campos do Formulário.

        Limpa os campos da tela de chamados e seta alguns botões para serem desabilitados ou habilitados
        conforme necessidade.

        - btn_cadastrar: Habilita
        - btn_alterar: desabilita
        - btn_excluir: desabilita
        - btn_fechar_chamado: desabilita
        - txt_numero_contrato: habilita edição
        """
        self.txt_numero_chamado.setText("")
        self.txt_numero_contrato.setText("")
        self.txt_nome_cliente.setText("")
        self.txt_endereco.setText("")
        self.txt_contato.setText("")
        self.txt_telefone.setText("")
        self.txt_email.setText("")
        self.txt_problema.setText("")
        self.txt_observacao.setText("")
        self.combo_solucao.setCurrentText("Selecione uma Opção")
        self.combo_tipo_chamado.setCurrentText("Selecione uma Opção")
        self.combo_status_chamado.setCurrentText("Selecione uma Opção")
        self.txt_data_abertura.setText("")
        self.txt_data_atualizacao.setText("")

        self.btn_cadastrar.setEnabled(True)
        self.btn_alterar.setEnabled(False)
        self.btn_excluir.setEnabled(False)
        self.btn_fechar_chamado.setEnabled(False)
        self.txt_numero_contrato.setEnabled(True)
