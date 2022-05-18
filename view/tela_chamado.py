from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2 import QtWidgets, QtGui
from components.mensagens import Mensagens
from dao.chamado_dao import ChamadoDao
from model.chamado import Chamado
from view.ui_tela_chamado import Ui_TelaChamado


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
        """Chama o método para popular a combobox de Solução"""

        self.listar_chamado_tabela()
        """Função para chamar o método de listar os chamados na tabela da tela de consulta de chamados."""

        self.btn_buscar_contrato.clicked.connect(self.buscar_contrato_cliente_no_formulario)

        self.btn_fechar_tela.clicked.connect(self.close)
        """Fecha e encerra a janela."""

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
        else:
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Consulta Contrato")
            msg.setText('No campo CONTRATO informe somente números!')
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
        elif self.Combo_status_chamado.currentText() == "Selecione uma Opção":
            self.mensagem.mensagem_combo('STATUS DE CHAMADO')
        elif self.combo_tipo_chamado.setCurrentText() == "Selecione uma Opção":
            self.mensagem.mensagem_combo('TIPO CHAMADO')
        elif self.combo_solucao.setCurrentText() == "Selecione uma Opção":
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
            chamado.status = self.Combo_status_chamado.currentText()
            chamado.solucao = self.combo_solucao.currentText()
            chamado.tipo = self.combo_tipo_chamado.currentText()
            chamado.data_abertura = self.txt_data_abertura.text()
            chamado.data_atualizacao = self.txt_data_atualizacao.text()

            try:
                chamado_dao = ChamadoDao()
                chamado_dao.cadastrar_chamado_banco(chamado.numero_chamado, chamado.numero_contrato,
                                                    chamado.nome_cliente, chamado.endereco, chamado.contato,
                                                    chamado.telefone, chamado.email, chamado.problema,
                                                    chamado.observacao, chamado.status, chamado.solucao,
                                                    chamado.tipo, chamado.data_abertura,
                                                    chamado.data_atualizacao)
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Cadastro de Chamado")
                msg.setText(f'Chamado {chamado.numero_chamado} cadastrado com sucesso.')
                msg.exec_()

            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

