from PySide2.QtWidgets import QMainWindow
from PySide2 import QtWidgets, QtGui
from datetime import datetime
from PySide2.QtWidgets import QMessageBox
from components.mensagens import Mensagens
from dao.chamado_parceiro_dao import ChamadoParceiroDao
from dao.fechar_chamado_parceiro_dao import FecharChamadoParceiroDao
from model.fechar_chamado_parceiro import FecharChamadoParceiro
from view.ui_tela_fechar_chamado_parceiro import Ui_FecharChamadoParceiro


class TelaFecharChamadoParceiro(QMainWindow, Ui_FecharChamadoParceiro):
    """Classe Tela de fechar Chamados.

    Tela responsavel pela interação do usuário para inclusão, alteração e exclusão de dados de chamados de parceiros
    fechados. A mesma também possui área para visualização de chamados para consulta.
    """
    def __init__(self):
        super(TelaFecharChamadoParceiro, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle de Chamados - Fechar Chamado Parceiro")
        self.setFixedSize(965, 640)

        self.mensagem = Mensagens()
        self.pegar_data_atual()

        self.listar_chamados_fechados_parceiro_tabela()
        """Função que chama o método para listar os chamados fechados."""

        self.btn_pesquisa_chamado.clicked.connect(self.consultar_chamado_para_fechamento)
        """Função que chama o método para pesquisar chamados"""

        self.btn_limpar_tela.clicked.connect(self.limpar_campos_formulario)
        """Função que chama o método para limpar os campos dos formulários."""

        self.btn_data_atual.clicked.connect(self.pegar_data_atual)
        """Função que chama o método de pegar data atual."""

        self.btn_fechar_chamado.clicked.connect(self.fechar_chamado_parceiro)
        """Função que chama o método de encerrar chamado."""

        self.btn_pesquisar_chamado_tabela.clicked.connect(self.consultar_chamado_parceiro_numero)
        """Função que chama o método de efetuar pesquisa por número do chamado"""

        self.btn_carregar_tabela.clicked.connect(self.listar_chamados_fechados_parceiro_tabela)
        """Função que chama o método de listar os chamados"""

        self.btn_pesquisa_cliente_tabela.clicked.connect(self.consultar_chamado_nome_cliente)
        """Função que chama o método de pesquisar chamado por nome do cliente"""

        self.btn_consulta_data_tabela.clicked.connect(self.consulta_chamado_data)
        """Função que chama o método de consultar os chamados por data"""

        self.btn_sair.clicked.connect(self.close)
        """Função que fecha a tela."""

        self.btn_fechar_chamado.setEnabled(False)

    def pegar_data_atual(self):
        """Pegar data atual.

        Método que pega a data atual do sistema e insere a mesma no campo de data de fechamento.
        :return: data
        """
        data = datetime.today().strftime('%d/%m/%Y')
        self.txt_data_fechamento.setText(data)

    def consultar_chamado_para_fechamento(self):
        """Consultar Chamado para Fechamento.

        Retorna uma consulta do Banco de dados e popula os campos do formulário com os dados necessários.
        :return: Dados para preenchimento automático do formulário.
        """
        if self.txt_pesquisar_chamado.text() == "":
            self.mensagem.mensagem_campo_vazio('NÚMERO CHAMADO')
        elif not self.txt_pesquisar_chamado.text().isdigit():
            self.mensagem.mensagem_campo_numerico('NÚMERO CHAMADO')
            self.txt_pesquisar_chamado.setText("")
        else:
            fechar_chamado_parceiro = FecharChamadoParceiro()
            fechar_chamado_parceiro.numero_chamado_parceiro = self.txt_pesquisar_chamado.text()

            try:
                fechar_chamado_parceiro_dao = FecharChamadoParceiroDao()
                resultado = fechar_chamado_parceiro_dao.consultar_chamado_para_fechamento(
                    fechar_chamado_parceiro.numero_chamado_parceiro)

                if len(resultado) == 0:
                    self.mensagem.mensagem_registro_não_encontrado(fechar_chamado_parceiro.numero_chamado_parceiro)
                    self.txt_pesquisar_chamado.setText("")
                else:
                    self.txt_empresa_parceira.setText(str(resultado[0][0]))
                    self.txt_numero_chamado.setText(str(resultado[0][1]))
                    self.txt_chamado_simpress.setText(str(resultado[0][2]))
                    self.txt_responsavel.setText(str(resultado[0][3]))
                    self.txt_cliente.setText(str(resultado[0][4]))

                    self.txt_empresa_parceira.setEnabled(False)
                    self.txt_numero_chamado.setEnabled(False)
                    self.txt_chamado_simpress.setEnabled(False)
                    self.txt_responsavel.setEnabled(False)
                    self.txt_cliente.setEnabled(False)

                    self.txt_pesquisar_chamado.setText("")
                    self.btn_fechar_chamado.setEnabled(True)
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def listar_chamados_fechados_parceiro_tabela(self):
        """Listar chamados de Parceiros Fechados
        
        Método que lista os chamados fechado dos parceiros e exibe o mesmo em uma tabela na tela de Chamados fechados
        de parceiro.
        :return: Lista de chamados de parceiros fechados.
        """
        try:
            fechar_chamado_parceiro_dao = FecharChamadoParceiroDao()
            resultado = fechar_chamado_parceiro_dao.listar_chamado_fechado_parceiro_banco()

            self.tabela_chamado_parceiro_fechado.setRowCount(len(resultado))
            self.tabela_chamado_parceiro_fechado.setColumnCount(7)

            for i in range(len(resultado)):
                for j in range(0, 7):
                    self.tabela_chamado_parceiro_fechado.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_de_erro()

    def fechar_chamado_parceiro(self):
        """Fechar chamado de Parceiro.

        Cadastra no banco de dados o chamado a ser encerrado excluindo o mesmo da tabela de chamados abertos.
        """
        if self.txt_solucao.toPlainText() == "":
            self.mensagem.mensagem_campo_vazio("SOLUÇÃO")
        else:
            fcp = FecharChamadoParceiro()
            fcp.empresa_parceira = self.txt_empresa_parceira.text()
            fcp.numero_chamado_parceiro = self.txt_numero_chamado.text()
            fcp.chamado_simpress = self.txt_chamado_simpress.text()
            fcp.responsavel_parceiro = self.txt_responsavel.text()
            fcp.nome_cliente = self.txt_cliente.text()
            fcp.solucao_chamado_parceiro = self.txt_solucao.toPlainText()
            fcp.data_fechamento_chamado_parceiro = self.txt_data_fechamento.text()

            try:
                fechar_cp_dao = FecharChamadoParceiroDao()
                fechar_cp_dao.cadastrar_chamado_parceiro_fechado_banco(fcp.empresa_parceira,
                                                                       fcp.numero_chamado_parceiro,
                                                                       fcp.chamado_simpress,
                                                                       fcp.responsavel_parceiro,
                                                                       fcp.nome_cliente,
                                                                       fcp.solucao_chamado_parceiro,
                                                                       fcp.data_fechamento_chamado_parceiro)

                chamado_parceiro_dao = ChamadoParceiroDao()
                chamado_parceiro_dao.excluir_chamado_parceiro_banco(fcp.numero_chamado_parceiro)

                mensagem = QMessageBox()
                mensagem.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                mensagem.setIcon(QMessageBox.Information)
                mensagem.setWindowTitle("Fechamento de Chamados Parceiros")
                mensagem.setText("Chamado fechado com sucesso!")
                mensagem.exec_()

                self.limpar_campos_formulario()
                self.listar_chamados_fechados_parceiro_tabela()

            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def consultar_chamado_parceiro_numero(self):
        """Consultar Chamado por Número

        Método que efetua uma consulta no banco de dados tendo como parâmetro o número de chamado.
        :return: Lista de chamados por número de chamado
        """
        if not self.txt_consulta_chamado_tabela.text().isdigit():
            self.mensagem.mensagem_campo_numerico("NÚMERO DO CHAMADO")
            self.txt_consulta_chamado_tabela.setText("")
        else:
            fcp = FecharChamadoParceiro()
            fcp.numero_chamado_parceiro = self.txt_consulta_chamado_tabela.text()

            try:
                fcp_dao = FecharChamadoParceiroDao()
                resultado = fcp_dao.consultar_chamado_parceiro_numero_banco(fcp.numero_chamado_parceiro)

                if len(resultado) == 0:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Pesquisa por Número do Chamado")
                    msg.setText('Número do chamado não encontrado!')
                    msg.exec_()

                    self.txt_consulta_chamado_tabela.setText("")
                else:
                    self.tabela_chamado_parceiro_fechado.setRowCount(len(resultado))
                    self.tabela_chamado_parceiro_fechado.setColumnCount(7)

                    for i in range(len(resultado)):
                        for j in range(0, 7):
                            self.tabela_chamado_parceiro_fechado.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
                    self.txt_consulta_chamado_tabela.setText("")
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def consultar_chamado_nome_cliente(self):
        """COnsultar chamado por nome do cliente.

        Método que efetua uma consulta no banco de dados tendo como parâmetro o nome do cliente.
        :return: Lista de chamados por nome do cliente.
        """
        if self.txt_consulta_cliente_tabela.text() == "":
            self.mensagem.mensagem_campo_vazio('Consulta Nome Cliente')
            self.txt_consulta_cliente_tabela.setText("")
        else:
            fcp = FecharChamadoParceiro()
            fcp.nome_cliente = self.txt_consulta_cliente_tabela.text()

            try:
                fcp_dao = FecharChamadoParceiroDao()
                resultado = fcp_dao.consultar_chamado_nome_cliente_banco(fcp.nome_cliente)

                if len(resultado) == 0:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Pesquisa por Nome do Cliente.")
                    msg.setText('Nome do cliente não encontrado!')
                    msg.exec_()

                    self.txt_consulta_cliente_tabela.setText("")
                else:
                    self.tabela_chamado_parceiro_fechado.setRowCount(len(resultado))
                    self.tabela_chamado_parceiro_fechado.setColumnCount(7)

                    for i in range(len(resultado)):
                        for j in range(0, 7):
                            self.tabela_chamado_parceiro_fechado.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
                    self.txt_consulta_cliente_tabela.setText("")
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def consulta_chamado_data(self):
        """Consulta Chamado por data.

        Método que efetua uma consulta no banco de dados tendo como parâmetro a data de encerramento.
        :return: Lista de chamados por data.
        """
        if self.txt_consulta_data_tabela.text() == "":
            self.mensagem.mensagem_campo_vazio('DATA')
            self.txt_consulta_data_tabela.setText("")
        else:
            fcp = FecharChamadoParceiro()
            fcp.data_fechamento_chamado_parceiro = self.txt_consulta_data_tabela.text()

            try:
                fcp_dao = FecharChamadoParceiroDao()
                resultado = fcp_dao.consulta_chamado_data_banco(fcp.data_fechamento_chamado_parceiro)

                if len(resultado) == 0:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Pesquisa por Data.")
                    msg.setText('Data não encontrado!')
                    msg.exec_()

                    self.txt_consulta_data_tabela.setText("")
                else:
                    self.tabela_chamado_parceiro_fechado.setRowCount(len(resultado))
                    self.tabela_chamado_parceiro_fechado.setColumnCount(7)

                    for i in range(len(resultado)):
                        for j in range(0, 7):
                            self.tabela_chamado_parceiro_fechado.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
                    self.txt_consulta_data_tabela.setText("")
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def limpar_campos_formulario(self):
        """Limpar Campos Formulário

        Limpa os campos do formulário e habilita ou desabilita alguns componentes da tela.
        """
        self.txt_empresa_parceira.setText("")
        self.txt_numero_chamado.setText("")
        self.txt_chamado_simpress.setText("")
        self.txt_responsavel.setText("")
        self.txt_cliente.setText("")
        self.txt_solucao.setText("")
        self.txt_data_fechamento.setText("")

        self.txt_empresa_parceira.setEnabled(True)
        self.txt_numero_chamado.setEnabled(True)
        self.txt_chamado_simpress.setEnabled(True)
        self.txt_responsavel.setEnabled(True)
        self.txt_cliente.setEnabled(True)

        self.btn_fechar_chamado.setEnabled(False)
