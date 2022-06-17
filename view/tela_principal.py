from PySide2.QtWidgets import QMainWindow

from view.tela_chamado import TelaChamado
from view.tela_chamado_parceiro import TelaChamadoParceiro
from view.tela_cliente import TelaCliente
from view.tela_fechar_chamado import TelaFecharChamado
from view.tela_fechar_chamado_parceiro import TelaFecharChamadoParceiro
from view.tela_parceiro import TelaParceiro
from view.tela_relatorio_chamado import TelaRelatorioChamado
from view.tela_solucao import TelaSolucao
from view.ui_tela_principal import Ui_TelaPrincipal
from view.tela_usuario import TelaUsuario


class TelaPrincipal(QMainWindow, Ui_TelaPrincipal):
    """Tela Principal do Sistema

    Está é a tela principal do sistema com todos os menus disponíveis para que o usuários possa navegar
    e efetuar as inclusões necessárias, assim como gerar relatórios.
    """
    def __init__(self):
        """Tela principal do sistema

        Esta tela é onde fica o menu da aplicação de acesso a todos os recursos do sistema.
        """
        super(TelaPrincipal, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Controle de Chamados - Tela Principal')
        self.showMaximized()

        self.menu_usuarios.triggered.connect(self.abrir_tela_usuario)
        """Item do menu que gera a chamada do método de abrir tela de usuário."""

        self.menu_solucoes.triggered.connect(self.abrir_tela_solucao)
        """Item do menu que gera a chamada do método de abrir tela de soluçõe."""

        self.menu_parceiro.triggered.connect(self.abrir_tela_parceiro)
        """Item do menu que gera a chamada do método de abrir a tela de Parceiro."""

        self.menu_clientes.triggered.connect(self.abrir_tela_cliente)
        """Item do menu que gera a chamada do método de abrir a tela de Cliente."""

        self.menu_consultar_clientes.triggered.connect(self.abrir_tela_consulta_cliente)
        """Item do menu que gera a chamada do método de abrir tela de consulta de Clientes."""

        self.menu_novo_chamado.triggered.connect(self.abrir_tela_chamado)
        """Item do menu que gera a chamada do método de abrir tela de Chamados."""

        self.menu_consulta_chamado.triggered.connect(self.abrir_tela_consulta_chamado)
        """Item do menu que gera a chamada do método de abrir a tela de consulta de chamados."""

        self.menu_fechamento_de_Chamados.triggered.connect(self.abrir_tela_fechar_chamado)
        """Item do menu que gera a chamada do método de abrir a tela de fechar chamados."""

        self.menu_Consulta_de_Chamados_Fechados.triggered.connect(self.abrir_tela_consulta_chamados_fechados)
        """Item do menu que gera a chamada do método de abrir a tela de consulta de chamados fechados."""

        self.menu_novo_Chamado_Parceiro.triggered.connect(self.abrir_tela_chamado_parceiro)

        self.menu_consultar_Chamado_Parceiro.triggered.connect(self.abrir_tela_consulta_chamado_parceiro)

        self.menu_fechar_Chamado_Parceiro.triggered.connect(self.abrir_tela_fechar_chamado_parceiro)

        self.menu_consultar_chamado_parceiro_fechado.triggered.connect(self.abrir_tela_fechar_chamado_parceiro_consulta)

        self.menu_relatorios_chamados.triggered.connect(self.abrir_tela_relatorio_chamados)

    def abrir_tela_usuario(self):
        """Método para abrir a tela de Usuário.

        Este método abre a tela de Usuário.
        :return: Tela de Usuário
        """
        self.tela_usuario = TelaUsuario()
        self.tela_usuario.show()

    def abrir_tela_solucao(self):
        """Método para abrir a tela de solução

        Este método abre a tela de Soluções.
        :return: Tela de Solução.
        """
        self.tela_solucao = TelaSolucao()
        self.tela_solucao.show()

    def abrir_tela_parceiro(self):
        """Método para abrir a tela de Parceiro

        Este método abre a tela de Parceiro.
        :return: Tela de Parceiro.
        """
        self.tela_parceiro = TelaParceiro()
        self.tela_parceiro.show()

    def abrir_tela_cliente(self):
        """Método para abrir a tela de Cliente.

        Este método abre a tela de Cliente.
        :return: Tela de Cliente.
        """
        self.tela_cliente = TelaCliente()
        self.tela_cliente.show()

    def abrir_tela_consulta_cliente(self):
        """Método para abrir a tela de consulta de clientes.

        Este método abre a tela de consulta de Cliente
        :return: Tela de consulta de clientes.
        """
        self.tela_cliente = TelaCliente()
        self.tela_cliente.tab_widget_cliente.setCurrentWidget(self.tela_cliente.tab_cliente_consulta)
        self.tela_cliente.show()

    def abrir_tela_chamado(self):
        """Método para abrir a tela de chamados.

        Este método abre a tela de cadastro de chamados.
        :return: Tela de Chamados
        """
        self.tela_chamado = TelaChamado()
        self.tela_chamado.show()

    def abrir_tela_consulta_chamado(self):
        """Método para abrir a tela de consulta de chamados.

        Este método abre a tela de consulta de chamados.
        :return: Tela de consulta de chamados.
        """
        self.tela_chamado = TelaChamado()
        self.tela_chamado.tab_chamado.setCurrentWidget(self.tela_chamado.tab_consulta_chamado)
        self.tela_chamado.show()

    def abrir_tela_fechar_chamado(self):
        """Método para abrir tela de Fechar Chamados.

        Este método abre a tela de Fechar chamados.
        :return: Tela de Fechar chamados.
        """
        self.tela_fechar_chamado = TelaFecharChamado()
        self.tela_fechar_chamado.show()

    def abrir_tela_consulta_chamados_fechados(self):
        """Método para abrir tela de consulta de Chamados fechados.

        Este método abre a tela de consulta de chamados fechados.
        :return: Tela de Fechar chamados.
        """
        self.tela_fechar_chamado = TelaFecharChamado()
        self.tela_fechar_chamado.tab_fechar_chamado.setCurrentWidget(self.tela_fechar_chamado.tab_consulta)
        self.tela_fechar_chamado.show()

    def abrir_tela_chamado_parceiro(self):
        """Abrir tela chamado Parceiro

        Método que abre a tela de chamados de Parceiro.
        :return: Tela de chamados de Parceiro.
        """
        self.tela_chamado_parceiro = TelaChamadoParceiro()
        self.tela_chamado_parceiro.show()

    def abrir_tela_consulta_chamado_parceiro(self):
        """Abrir tela de consultar chamado de Parceiro

        Abre a tela de consultar chamados de Parceiro
        :return: Abrir tela de consulta de chamado de Parceiro.
        """
        self.tela_chamado_parceiro = TelaChamadoParceiro()
        self.tela_chamado_parceiro.tab_chamado_parceiro.setCurrentWidget(self.tela_chamado_parceiro.tab_consulta_parceiro)
        self.tela_chamado_parceiro.show()

    def abrir_tela_fechar_chamado_parceiro(self):
        """Abrir tela de fechamento de chamados de Parceiro.

        Abre a tela de fechamento de chamados de Parceiros.
        :return: Abrir tela de Chamado de Parceiros.
        """
        self.tela_fechar_chamado_parceiro = TelaFecharChamadoParceiro()
        self.tela_fechar_chamado_parceiro.show()

    def abrir_tela_fechar_chamado_parceiro_consulta(self):
        self.tela_fechar_chamado_parceiro = TelaFecharChamadoParceiro()
        self.tela_fechar_chamado_parceiro.tab_fechar_chamados_parceiro.setCurrentWidget(self.tela_fechar_chamado_parceiro.tab_consultar_chamado)
        self.tela_fechar_chamado_parceiro.show()

    def abrir_tela_relatorio_chamados(self):
        self.tela_relatorio_chamados = TelaRelatorioChamado()
        self.tela_relatorio_chamados.show()
