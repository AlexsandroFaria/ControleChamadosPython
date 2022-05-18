from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2 import QtWidgets, QtGui
from components.mensagens import Mensagens
from dao.cliente_dao import ClienteDao
from model.cliente import Cliente
from view.tela_chamado import TelaChamado
from view.ui_tela_cliente import Ui_Cliente
from mysql.connector import IntegrityError, DatabaseError


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

        self.btn_alterar.clicked.connect(self.alterar_cliente)
        """Função que chama o método de alterar Cliente."""

        self.btn_excluir.clicked.connect(self.excluir_cliente)
        """Função que chama o método de excluir Cliente."""

        self.btn_consulta_contrato.clicked.connect(self.consultar_cliente_contrato)
        """Função que chama o método de consultar cliente por contrato."""

        self.btn_carregar_tabela.clicked.connect(self.listar_cliente_tabela)
        """Função para carregar a tabela de cliente com todos os dados."""

        self.btn_consulta_nome.clicked.connect(self.consultar_cliente_nome)
        """Função que chama o método de consultar cliente por nome."""

        self.btn_cadastrar_chamado.clicked.connect(self.abrir_tela_cadastrar_chamado)
        """Função que chama o método de abrir tela de chamado passando alguns parametros conforme descrição 
        do método."""

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
            print(con_erro)
            self.mensagem.mensagem_de_erro()

    def cadastrar_cliente(self):
        """Cadastrar Cliente

        Método para cadastrar cliente no banco de dados.
        """
        if self.txt_contrato.text() == "":
            self.mensagem.mensagem_campo_vazio('CONTRATO')
        elif self.txt_nome.text() == "":
            self.mensagem.mensagem_campo_vazio('NOME CLIENTE')
        elif self.txt_endereco.text() == "":
            self.mensagem.mensagem_campo_vazio('ENDEREÇO')
        elif self.txt_contato.text() == "":
            self.mensagem.mensagem_campo_vazio('CONTATO')
        elif self.txt_telefone.text() == "":
            self.mensagem.mensagem_campo_vazio('TELEFONE')
        elif self.txt_email.text() == "":
            self.mensagem.mensagem_campo_vazio('E-MAIL')
        elif not self.txt_contrato.text().isdigit():
            self.mensagem.mensagem_campo_numerico('CONTRATO')
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
                print(int_erro)
                self.mensagem.mensagem_integrity_error(cliente.contrato)

                self.limpar_formulario()
            except DatabaseError as db_erro:
                print(db_erro)
                self.mensagem.mensagem_campo_numerico('CONTRATO')

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
                    self.txt_contrato.setEnabled(False)

        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_de_erro()
        except AttributeError as att_erro:
            print(att_erro)
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Consultar Clientes")
            msg.setText('Selecione um item da coluna Contrato')
            msg.exec_()

    def alterar_cliente(self):
        """Método alterar CLiente

        Metodo que altera os dados do cliente no banco de dados. O mesmo tb altera o mesmo cliente na tabela de
        chamados.
        :return: Alteração de dados do cliente.
        """
        if self.txt_contrato.text() == "":
            self.mensagem.mensagem_campo_vazio('CONTRATO')
        elif self.txt_nome.text() == "":
            self.mensagem.mensagem_campo_vazio('NOME CLIENTE')
        elif self.txt_endereco.text() == "":
            self.mensagem.mensagem_campo_vazio('ENDEREÇO')
        elif self.txt_contato.text() == "":
            self.mensagem.mensagem_campo_vazio('CONTATO')
        elif self.txt_telefone.text() == "":
            self.mensagem.mensagem_campo_vazio('TELEFONE')
        elif self.txt_email.text() == "":
            self.mensagem.mensagem_campo_vazio('E-MAI')
        elif not self.txt_contrato.text().isdigit():
            self.mensagem.mensagem_campo_numerico('CONTRATO')
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
                cliente_dao.alterar_cliente_banco(cliente.contrato, cliente.nome, cliente.endereco, cliente.contato,
                                                  cliente.telefone, cliente.email)

                self.mensagem.mensagem_alteração(cliente.nome)

                self.tab_widget_cliente.setCurrentWidget(self.tab_cliente_consulta)

                self.limpar_formulario()
                self.listar_cliente_tabela()

                # chamado_dao = ChamadoDao()
                # chamado_dao.alterar_chamado_cliente(cliente.contrato, cliente.nome, cliente.endereco, cliente.contato,
                #                                   cliente.telefone, cliente.email)

            except ConnectionError as con_erro:
                self.mensagem.mensagem_de_erro()
                print(con_erro)
            except IntegrityError as int_erro:
                print(int_erro)
                self.mensagem.mensagem_integrity_error(cliente.contrato)

                self.limpar_formulario()
            except DatabaseError as db_erro:
                print(db_erro)
                self.mensagem.mensagem_campo_numerico('CONTRATO')

    def excluir_cliente(self):
        """Eclusão de cliente

        Excluir um cliente do banco de dados passando como parametro o contrato.
        :return: Exclusão de cliente.
        """
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
        msg.setWindowTitle("Exclusão de Clientes!")
        msg.setText("Tem certeza que deseja excluir o Cliente?")
        msg.setStandardButtons(QMessageBox.Yes)
        msg.addButton(QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        if msg.exec_() == QMessageBox.Yes:
            cliente = Cliente()
            cliente.contrato = self.txt_contrato.text()
            cliente.nome = self.txt_nome.text()

            try:
                cliente_dao = ClienteDao()
                cliente_dao.excluir_cliente_banco(cliente.contrato)

                self.mensagem.mensagem_exclusao(cliente.nome)

                self.limpar_formulario()
                self.listar_cliente_tabela()
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def limpar_formulario(self):
        """Limpar Formulário

        Limpa o formulário da tela de Cliente.
        :return: Limpa os campos da tela de cliente
        """
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
        self.txt_contrato.setEnabled(True)

    def consultar_cliente_contrato(self):
        """Consulta cliente por Contrato

        Consulta o cliente pelo número de contrato, exibindo a informação na tabela de clientes passando como
        parametro o número de contrato.
        :return: Consulta cliente.
        """
        cliente = Cliente()
        cliente.contrato = self.txt_consultar_contrato.text()

        try:
            cliente_dao = ClienteDao()
            resultado = cliente_dao.consultar_cliente_contrato_banco(cliente.contrato)

            if len(resultado) == 0:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Consulta Contrato")
                msg.setText('Numero do Conrato não encontrado!')
                msg.exec_()

                self.txt_consultar_contrato.setText("")
                self.listar_cliente_tabela()
            else:
                self.tabela_clientes.setRowCount(len(resultado))
                self.tabela_clientes.setColumnCount(6)

                for i in range(len(resultado)):
                    for j in range(0, 6):
                        self.tabela_clientes.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))

                        self.txt_consultar_contrato.setText("")
        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_de_erro()

    def consultar_cliente_nome(self):
        """Consulta cluente por Nome

        Consulta o cliente pelo nome do cliente, exibindo a informação na tabela de clientes passando como
        parametro o nome do cliente.
        :return: Consulta cliente.
        """
        cliente = Cliente()
        cliente.nome = self.txt_consulta_nome.text()

        try:
            cliente_dao = ClienteDao()
            resultado = cliente_dao.consultar_cliente_nome_banco(cliente.nome)

            if len(resultado) == 0:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Consulta Contrato")
                msg.setText('Nome Cliene não encontrado!')
                msg.exec_()

                self.txt_consulta_nome.setText("")
                self.listar_cliente_tabela()
            else:
                self.tabela_clientes.setRowCount(len(resultado))
                self.tabela_clientes.setColumnCount(6)

                for i in range(len(resultado)):
                    for j in range(0, 6):
                        self.tabela_clientes.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))

                        self.txt_consulta_nome.setText("")
        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_de_erro()

    def abrir_tela_cadastrar_chamado(self):
        """Abrir tela de Chamados

        Abre a tela de chamados passando como parâmetro os dados dos seguintes campos:
            - contrato,
            - nome,
            - endereço,
            - contato,
            - telefone,
            - e-mail
        :return: Abre a tela de chamado passando os parametros listados acima.
        """
        if self.txt_contrato.text() == "":
            self.mensagem.mensagem_campo_vazio('CONTRATO')
        elif self.txt_nome.text() == "":
            self.mensagem.mensagem_campo_vazio('NOME')
        elif self.txt_endereco.text() == "":
            self.mensagem.mensagem_campo_vazio('ENDEREÇO')
        elif self.txt_contato.text() == "":
            self.mensagem.mensagem_campo_vazio('CONTATO')
        elif self.txt_telefone.text() == "":
            self.mensagem.mensagem_campo_vazio('TELEFONE')
        elif self.txt_email.text() == "":
            self.mensagem.mensagem_campo_vazio('E-MAIL')
        else:
            self.tela_chamado = TelaChamado()
            self.tela_chamado.txt_numero_contrato.setText(self.txt_contrato.text())
            self.tela_chamado.txt_nome_cliente.setText(self.txt_nome.text())
            self.tela_chamado.txt_endereco.setText(self.txt_endereco.text())
            self.tela_chamado.txt_contato.setText(self.txt_contato.text())
            self.tela_chamado.txt_telefone.setText(self.txt_telefone.text())
            self.tela_chamado.txt_email.setText(self.txt_email.text())
            self.tela_chamado.show()
            self.close()
