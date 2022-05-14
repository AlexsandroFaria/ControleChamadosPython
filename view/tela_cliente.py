from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2 import QtWidgets, QtGui
from components.mensagens import Mensagens
from dao.cliente_dao import ClienteDao
from model.cliente import Cliente
from view.ui_tela_cliente import Ui_Cliente


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

        self.listar_cliente_tabela()
        """Função que carrega a listagem de Clientes assim que tela de Cliente é chamada."""

        self.btn_salvar.clicked.connect(self.cadastrar_cliente)

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

