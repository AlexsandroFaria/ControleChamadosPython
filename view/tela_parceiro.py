from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2 import QtWidgets, QtGui
from dao.parceiro_dao import ParceiroDao
from model.parceiro import Parceiro
from view.ui_tela_parceiro import Ui_TelaParceiro
from components.mensagens import Mensagens
from mysql.connector import IntegrityError


class TelaParceiro(QMainWindow, Ui_TelaParceiro):
    """Classe tela de Parceiros

    Tela responsavel pela interação do usuário para inclusão, alteração e exclusão de dados de parceiros.
    A mesma também possui área para visualização de parceiros cadastrados.
    """
    def __init__(self):
        super(TelaParceiro, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle de Chamados - Parceiros")
        self.setFixedSize(801, 655)

        self.mensagem = Mensagens()

        self.btn_alterar.setEnabled(False)
        self.btn_excluir.setEnabled(False)

        self.listar_parceiro_tabela()
        """Função que lista os parceiros cadastrados em uma tabela."""

        self.btn_cadastrar.clicked.connect(self.cadastrar_parceiro)
        """Função que chama o método Cadastrar parceiro."""

        self.btn_carregar.clicked.connect(self.carregar_parceiro_formulario)
        """Função que chama o método de popular o formulário de Parceiro com os dados carregados em banco."""

        self.btn_alterar.clicked.connect(self.alterar_parceiro)
        """Função que chama o método para alteraar dados do Parceiro em banco."""

        self.btn_excluir.clicked.connect(self.excluir_parceiro)
        """Função que chama o método de excluir um parceito do banco de dados."""

        self.btn_sair.clicked.connect(self.close)
        """Sai e encerra a aplicação"""

        self.btn_limpar_tela.clicked.connect(self.limpar_formulario)
        """Função para limpar os campos do formulário."""

    def listar_parceiro_tabela(self):
        """Listar Parceiros

        Lista todos os parceiros e insere o resultado na tabela de Parceiros para visualização do Usuário.
        :return: Listagem de Parceiros.
        """
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
        """Cadastrar Parceiro no banco de Dados

        Cadastra o parceiro no banco de Dados
        :return: Cadastro de Paceiro no banco de dados.
        """
        if self.txt_nome_parceiro.text() == "":
            campo = 'NOME'
            self.mensagem.mensagem_campo_vazio(campo)
        elif self.txt_contato.text() == "":
            campo = 'CONTATO'
            self.mensagem.mensagem_campo_vazio(campo)
        elif self.txt_telefone.text() == "":
            campo = 'TELEFONE'
            self.mensagem.mensagem_campo_vazio(campo)
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
            except ConnectionError as con_erro:
                self.mensagem.mensagem_de_erro()
                print(con_erro)
            except IntegrityError as int_erro:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Inserir Parceiro")
                msg.setText(f'Parceiro {parceiro.nome} já está cadastrado!')
                msg.exec_()

                print(int_erro)

                self.limpar_formulario()

    def carregar_parceiro_formulario(self):
        """Metodo Carregar Parceiro

        Carrega os dados do parceiro no formulário de Parceiro com os dados consultados no banco de dados
        """
        linha = self.tabela_parceiro.currentRow()

        try:
            parceiro_dao = ParceiroDao()
            dados_lidos = parceiro_dao.listar_prceiro()
            valor_id = dados_lidos[linha][0]

            resultado = parceiro_dao.listar_parceiro_id(valor_id)

            self.txt_id.setText(str(resultado[0][0]))
            self.txt_nome_parceiro.setText(str(resultado[0][1]))
            self.txt_contato.setText(str(resultado[0][2]))
            self.txt_telefone.setText(str(resultado[0][3]))

            self.btn_alterar.setEnabled(True)
            self.btn_excluir.setEnabled(True)
            self.btn_cadastrar.setEnabled(False)
        except ConnectionError as con_erro:
            self.mensagem.mensagem_de_erro()
            print(con_erro)

    def alterar_parceiro(self):
        """ Método para alterar Parceiro

        Altera os dados de um parceiro já cadastrado no banco de dados.
        """
        if self.txt_nome_parceiro.text() == "":
            campo = 'NOME'
            self.mensagem.mensagem_campo_vazio(campo)
        elif self.txt_contato.text() == "":
            campo = 'CONTATO'
            self.mensagem.mensagem_campo_vazio(campo)
        elif self.txt_telefone.text() == "":
            campo = 'TELEFONE'
            self.mensagem.mensagem_campo_vazio(campo)
        else:
            parceiro = Parceiro()
            parceiro.id = self.txt_id.text()
            parceiro.nome = self.txt_nome_parceiro.text()
            parceiro.contato = self.txt_contato.text()
            parceiro.telefone = self.txt_telefone.text()

            try:
                parceiro_dao = ParceiroDao()
                parceiro_dao.alterar_parceiro_banco(parceiro.id, parceiro.nome, parceiro.contato, parceiro.telefone)

                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Alterar Parceiros!")
                msg.setText(f'Parceiro {parceiro.nome} Alterado com sucesso!')
                msg.exec_()

                self.listar_parceiro_tabela()
                self.limpar_formulario()
                self.btn_alterar.setEnabled(False)
                self.btn_excluir.setEnabled(False)
            except ConnectionError as con_erro:
                self.mensagem.mensagem_de_erro()
                print(con_erro)
            except IntegrityError as int_erro:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Inserir Solução")
                msg.setText(f'Solução {parceiro.nome} já existe no sistema!')
                msg.exec_()

                print(int_erro)

                self.limpar_formulario()

    def excluir_parceiro(self):
        """Método para excluir parceiro

        Método para excluir um parceiro do banco de dados.
        """
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
        msg.setWindowTitle("Exclusão de Parceiro!")
        msg.setText("Tem certeza que deseja excluir o Parceiro?")
        msg.setStandardButtons(QMessageBox.Yes)
        msg.addButton(QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        if msg.exec_() == QMessageBox.Yes:
            parceiro = Parceiro()

            parceiro.id = self.txt_id.text()
            parceiro.nome = self.txt_nome_parceiro.text()

            try:
                parceiro_dao = ParceiroDao()
                parceiro_dao.excluir_parceiro_banco(parceiro.id)

                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Exclusão de Parceiros!")
                msg.setText(f'Parceiro {parceiro.nome} Excluído com sucesso!')
                msg.exec_()

                self.limpar_formulario()
                self.listar_parceiro_tabela()
            except ConnectionError as con_erro:
                self.mensagem.mensagem_de_erro()
                print(con_erro)

    def limpar_formulario(self):
        """Limpar campos

        Limpa os campos do formulário de Parceiro.
        """
        self.txt_id.setText("")
        self.txt_nome_parceiro.setText("")
        self.txt_contato.setText("")
        self.txt_telefone.setText("")

        self.btn_alterar.setEnabled(False)
        self.btn_excluir.setEnabled(False)
        self.btn_cadastrar.setEnabled(True)

