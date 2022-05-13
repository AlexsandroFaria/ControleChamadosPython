from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QMainWindow, QMessageBox
from components.mensagens import Mensagens
from model.solucao import Solucao
from view.ui_tela_solucoes import Ui_TelaSolucoes
from dao.solucao_dao import SolucaoDao


class TelaSolucao(QMainWindow, Ui_TelaSolucoes):
    """Classe da Tela de soluções

    Esta tela tem por finalidade a interação com o susuário para a solicitação de inserção e exclusão
    de dados conforme necessidade.
    O usuário pode cadastrar as soluções utilizadas para o dar suporte, podendo cadastrar nomes de softwares,
    aplicativos entre outros.
    """
    def __init__(self):
        super(TelaSolucao, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle de Chamados - Soluções")
        self.setFixedSize(615, 525)

        self.mensagem = Mensagens()

        self.btn_excluir.setEnabled(False)

        self.listar_solucoes_tabela()
        """Ao abrir a tela de Soluçãoes, este método é automaticamente carregado
        chamando o método de Listar soluções.
        """

        self.btn_sair.clicked.connect(self.close)
        """Função para fechar e finalizar a aplicação."""

        self.btn_carregar.clicked.connect(self.carregar_campos_formulario)
        """Função para chamar o método de carregar informações no formulário."""

        self.btn_cadastrar.clicked.connect(self.cadastrar_solucao)
        """Função que chama o método para cadastrar solução."""

        self.btn_limpar_tela.clicked.connect(self.limpar_tela)
        """Função para chamado o método de limpar os campos do formulário."""

        self.btn_excluir.clicked.connect(self.excluir_solucao)
        """Função para chamar o método de excluir solução."""

    def listar_solucoes_tabela(self):
        """Método para listar as soluções

        Método para listar todas as soluções na tabela e retornar na tela para o usuário.
        :return: Lista de soluções exibidas na tela.
        """
        try:
            solucao_dao = SolucaoDao()
            resultado = solucao_dao.listar_solucoes()

            self.tabela_solucoes.setRowCount(len(resultado))
            self.tabela_solucoes.setColumnCount(3)

            for i in range(0, len(resultado)):
                for j in range(0, 3):
                    self.tabela_solucoes.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except ConnectionError:
            self.mensagem.mensagem_de_erro()

    def cadastrar_solucao(self):
        """Método para cadastrar Solução

        Método para cadastrar uma solução no banco de dados.
        :return: Inserção de usuário no banco de dados.
        """
        if self.txt_solucao.text() == "":
            self.mensagem.mensagem_campo_vazio()
        elif self.txt_descricao.text() == "":
            self.mensagem.mensagem_campo_vazio()
        else:
            solucao = Solucao()

            solucao.solucao = self.txt_solucao.text()
            solucao.descricao = self.txt_descricao.text()

            try:
                solucao_dao = SolucaoDao()
                solucao_dao.cadastrar_solucao_banco(solucao.solucao, solucao.descricao)

                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Inserir Solução")
                msg.setText(f'Solução {solucao.solucao} inserido com sucesso!')
                msg.exec_()

                self.limpar_tela()
                self.listar_solucoes_tabela()
            except ConnectionError:
                self.mensagem.mensagem_de_erro()

    def carregar_campos_formulario(self):
        """Método para carregar dados e popular o Formulário

        Método que carrega a solução selecionada e exibe suas informações nos campos do formulário para
        visualização do usuário.
        :return: Solução selecionada.
        """
        linha = self.tabela_solucoes.currentRow()

        try:
            solucao_dao = SolucaoDao()
            dados_lidos = solucao_dao.listar_solucoes()

            valor_id = dados_lidos[linha][0]

            resultado = solucao_dao.carregar_campos_formulario_id(valor_id)

            self.txt_id.setText(str(resultado[0][0]))
            self.txt_solucao.setText(str(resultado[0][1]))
            self.txt_descricao.setText(str(resultado[0][2]))

            self.btn_excluir.setEnabled(True)

        except ConnectionError as con_erro:
            self.mensagem.mensagem_de_erro()
            print(con_erro)

    def excluir_solucao(self):
        """Exclusão de Soluções.

        Método para excluir uma solução selecionada.
        :return: solução para exclusão.
        """
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
        msg.setWindowTitle("Exclusão de Solução")
        msg.setText("Tem certeza que deseja excluir a Solução?")
        msg.setStandardButtons(QMessageBox.Yes)
        msg.addButton(QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        if msg.exec_() == QMessageBox.Yes:
            solucao = Solucao()
            solucao.id = self.txt_id.text()

            try:
                solucao_dao = SolucaoDao()
                solucao_dao.excluir_solucao_banco(solucao.id)

                self.mensagem.mensagem_exclusao()

                self.listar_solucoes_tabela()
                self.limpar_tela()
            except ConnectionError as con_erro:
                self.mensagem.mensagem_de_erro()
                print(con_erro)

    def limpar_tela(self):
        """Método para limpar os campos do Formulário.

        :return: parametros em branco para apagar as informações dos campos do formulário.
        """
        self.txt_id.setText("")
        self.txt_solucao.setText("")
        self.txt_descricao.setText("")

        self.btn_excluir.setEnabled(False)
