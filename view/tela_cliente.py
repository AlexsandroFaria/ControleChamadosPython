from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2 import QtWidgets, QtGui
from components.mensagens import Mensagens
from dao.cliente_dao import ClienteDao
from model.cliente import Cliente
from view.ui_tela_cliente import Ui_Cliente
from mysql.connector import IntegrityError


class TelaCliente(QMainWindow, Ui_Cliente):
    """Tela de CLientes

    Tela responsavel pela interação do usuário para inclusão, alteração e exclusão de dados de Clientes.
    A mesma também possui área para visualização de parceiros cadastrados.
    """
    def __init__(self):
        super(TelaCliente, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cadastro de Chamados = Clientes")
        self.setFixedSize(801, 655)

        self.mensagem = Mensagens()

        self.btn_fechar.clicked.connect(self.close)
        """Fecha janela e sai da aplicação."""

        self.listar_cliente_tabela()
        """Função que carrega a listagem de Clientes assim que tela de Cliente é chamada."""

        self.btn_salvar.clicked.connect(self.cadastrar_cliente)
        """Função que chama o método de salvar Cliente no banco de dados."""

        self.btn_carregar.clicked.connect(self.carregar_cliente_formulario)
        """Função que chama o método para carregar os dados para o formulário da tela de CLiente."""

        self.btn_limpar_tela.clicked.connect(self.limpar_formulario)
        """Função para limpar os campos da tela de Cliente."""

        self.btn_alterar.setEnabled(False)
        self.btn_excluir.setEnabled(False)
        self.btn_cadastrar_chamado.setEnabled(False)

    def listar_cliente_tabela(self):
        """Método de listar clientes

        Lista todos os cliente do banco na tabela do formulário de Cliente
        :return: Lista de Clientes
        """
        try:
            cliente_dao = ClienteDao()
            resultado = cliente_dao.listar_cliente()

            self.tabela_clientes.setRowCount(len(resultado))
            self.tabela_clientes.setColumnCount(6)

            for i in range(0, len(resultado)):
                for j in range(0, 6):
                    self.tabela_clientes.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except ConnectionError as con_erro:
            self.mensagem.mensagem_de_erro()
            print(con_erro)

    def cadastrar_cliente(self):
        """Cadastrar Cliente

        Método para cadastrar cliente no banco de dados.
        """
        if self.txt_contrato.text() == "":
            campo = 'CONTRATO'
            self.mensagem.mensagem_campo_vazio(campo)
        elif self.txt_nome.text() == "":
            campo = 'NOME CLIENTE'
            self.mensagem.mensagem_campo_vazio(campo)
        elif self.txt_endereco.text() == "":
            campo = 'ENDEREÇO'
            self.mensagem.mensagem_campo_vazio(campo)
        elif self.txt_contato.text() == "":
            campo = 'CONTATO'
            self.mensagem.mensagem_campo_vazio(campo)
        elif self.txt_telefone.text() == "":
            campo = 'TELEFONE'
            self.mensagem.mensagem_campo_vazio(campo)
        elif self.txt_email.text() == "":
            campo = 'E-MAIL'
            self.mensagem.mensagem_campo_vazio(campo)
        else:
            cliente = Cliente()
            cliente.contrato = self.txt_contrato.text()
            cliente.nome = self.txt_nome.text()
            cliente.endereco = self.txt_endereco.text()
            cliente.contato = self.txt_contato.text()
            cliente.telefone = self.txt_telefone.text()
            cliente.email = self.txt_email.text()

            try:
                cliente_dao = ClienteDao()
                cliente_dao.cadastrar_cliente_banco(cliente.contrato, cliente.nome, cliente.endereco, cliente.contato,
                                                    cliente.telefone, cliente.email)
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Inserir Cliente")
                msg.setText(f'Cliente {cliente.nome} inserido com sucesso!')
                msg.exec_()

                self.tab_widget_cliente.setCurrentWidget(self.tab_cliente_consulta)

                self.listar_cliente_tabela()
                self.limpar_formulario()
            except ConnectionError as con_erro:
                self.mensagem.mensagem_de_erro()
                print(con_erro)
            except IntegrityError as int_erro:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Inserir Solução")
                msg.setText(f'Solução {cliente.contrato} já existe no sistema!')
                msg.exec_()

                print(int_erro)

                self.limpar_formulario()

    def carregar_cliente_formulario(self):
        """Método para carregar dados

        Método para carregar dados para o formulário de cliente
        """
        try:
            linha = self.tabela_clientes.currentItem().text()

            if not linha.isdigit():
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Consultar Clientes")
                msg.setText('Selecione somente a coluna Contrato')
                msg.exec_()
            else:
                cliente_dao = ClienteDao()
                resultado = cliente_dao.consultar_por_contrato(linha)

                if len(resultado) == 0:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Consultar Clientes")
                    msg.setText('Selecione somente a coluna Contrato')
                    msg.exec_()
                else:
                    self.tab_widget_cliente.setCurrentWidget(self.tab_cliente)

                    self.txt_contrato.setText(str(resultado[0][0]))
                    self.txt_nome.setText(str(resultado[0][1]))
                    self.txt_endereco.setText(str(resultado[0][2]))
                    self.txt_contato.setText(str(resultado[0][3]))
                    self.txt_telefone.setText(str(resultado[0][4]))
                    self.txt_email.setText(str(resultado[0][5]))

                    self.btn_excluir.setEnabled(True)
                    self.btn_alterar.setEnabled(True)
                    self.btn_cadastrar_chamado.setEnabled(True)
                    self.btn_salvar.setEnabled(False)

        except ConnectionError as con_erro:
            self.mensagem.mensagem_de_erro()
            print(con_erro)

    def limpar_formulario(self):
        self.txt_contrato.setText("")
        self.txt_nome.setText("")
        self.txt_endereco.setText("")
        self.txt_contato.setText("")
        self.txt_telefone.setText("")
        self.txt_email.setText("")

        self.btn_alterar.setEnabled(False)
        self.btn_excluir.setEnabled(False)
        self.btn_cadastrar_chamado.setEnabled(False)
        self.btn_salvar.setEnabled(True)

