from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2 import QtGui, QtWidgets
from dao.usuario_dao import UsuarioDao
from model.usuario import Usuario
from view.ui_tela_usuario import Ui_Usuarios
from components.mensagens import Mensagens
from mysql.connector import IntegrityError


class TelaUsuario(QMainWindow, Ui_Usuarios):
    """Classe da tela de Usuários

    Esta tela tem por finalidade a interação com o susuário e a solicitação de inserção, alteração e exclusão
    de dados conforme necessidade.
    """
    def __init__(self):
        super(TelaUsuario, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle de Chamados - Usuários")
        self.setFixedSize(768, 644)

        self.mensagem = Mensagens()
        """Instância da classe de mensagens padrão"""

        self.listagem_usuarios_tabela()
        """Função de inicialização da lista de usuários assim que a janela é chamada, listando todos os usuários
        em uma tabela para a isualização do usuário.
        """

        self.btn_salvar.clicked.connect(self.cadastrar_usuario)
        """Função para a chamada do método de cadastrar um usuário no banco de dados."""

        self.btn_carregar.clicked.connect(self.carregar_usuario_formulario)
        """Função para a chamada do método de carregar Usuários"""

        self.btn_alterar.clicked.connect(self.alterar_usuario)
        """Função para a chamado do método alterar usuário"""

        self.btn_excluir.clicked.connect(self.excluir_usuario)
        """Função para a chamada do método de excluir usuário"""

        self.btn_limpar_tela.clicked.connect(self.limpar_formulario)
        """Função para a chamado do método de limpar os campos do formulário de usuario."""

        self.btn_sair.clicked.connect(self.close)
        """Finaliza e fecha a aplicação."""

        """Função para desabilitar o botão de Excluir na inicialização da Janela."""
        self.btn_excluir.setEnabled(False)
        """Função para desabilitar o botão Alterar na inicialização da Janela."""
        self.btn_alterar.setEnabled(False)

    def listagem_usuarios_tabela(self):
        """Método para Listar Usuários

        Método para listar usuários na tabela para visualização dos usuários, para a exibição é feita uma
        consulta no banco de dados retornando os valores.

        :return: lista de usuários.
        """
        try:
            usuario_dao = UsuarioDao()
            resultado = usuario_dao.listar_usuario()

            self.tabela_usuarios.setRowCount(len(resultado))
            self.tabela_usuarios.setColumnCount(5)

            for i in range(0, len(resultado)):
                for j in range(0, 5):
                    self.tabela_usuarios.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_de_erro()

    def cadastrar_usuario(self):
        """Método para cadastrar Usuários

        Este metodo insere um determinado usuário no banco de dados.

        :return: inserção de usuários no banco.
        """
        if self.txt_nome_completo.text() == "":
            self.mensagem.mensagem_campo_vazio('NOME')
        elif self.txt_login.text() == "":
            self.mensagem.mensagem_campo_vazio('LOGIN')
        elif self.txt_senha.text() == "":
            self.mensagem.mensagem_campo_vazio('SENHA')
        elif self.txt_confirmar_senha.text() == "":
            self.mensagem.mensagem_campo_vazio('CONFIRMAR SENHA')
        else:
            usuario = Usuario()

            usuario.nome = self.txt_nome_completo.text()
            usuario.login = self.txt_login.text()
            usuario.senha = self.txt_senha.text()
            usuario.perfil = self.combo_perfil.currentText()

            if usuario.senha != self.txt_confirmar_senha.text():
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Senhas não conferem")
                msg.setText('Senhas digitadas não são iguais')
                msg.exec_()
            else:
                try:
                    usuario_dao = UsuarioDao()
                    usuario_dao.cadastrar_usuario_banco(usuario.nome, usuario.login, usuario.senha, usuario.perfil)

                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Cadastro de Usuários")
                    msg.setText(f'Usuário {usuario.nome} cadastrado com sucesso!')
                    msg.exec_()

                    self.limpar_formulario()
                    self.listagem_usuarios_tabela()
                except ConnectionError as con_erro:
                    self.mensagem.mensagem_de_erro()
                    print(con_erro)
                except IntegrityError as int_erro:
                    print(int_erro)
                    self.mensagem.mensagem_integrity_error(usuario.nome)

                    self.limpar_formulario()

    def alterar_usuario(self):
        """Método para alterar Usuários

        Método para alterar algum dado de um usuário selecionado.
        :return: Usuário para alteração.
        """
        if self.txt_nome_completo.text() == "":
            self.mensagem.mensagem_campo_vazio('NOME')
        elif self.txt_login.text() == "":
            self.mensagem.mensagem_campo_vazio('LOGIN')
        elif self.txt_senha.text() == "":
            self.mensagem.mensagem_campo_vazio('SENHA')
        elif self.txt_confirmar_senha.text() == "":
            self.mensagem.mensagem_campo_vazio('CONFIRMAR SENHA')
        else:
            usuario = Usuario()

            usuario.id = self.txt_id.text()
            usuario.nome = self.txt_nome_completo.text()
            usuario.login = self.txt_login.text()
            usuario.senha = self.txt_senha.text()
            usuario.perfil = self.combo_perfil.currentText()

            if usuario.senha != self.txt_confirmar_senha.text():
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Senhas não conferem")
                msg.setText('Senhas digitadas não são iguais')
                msg.exec_()
            else:
                if self.txt_login.text() == "admin":
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIcon(QMessageBox.Warning)
                    msg.setWindowTitle("Usuario Admin")
                    msg.setText('Usuário admin não pode ser alterado!')
                    msg.exec_()
                else:
                    try:
                        usuario_dao = UsuarioDao()
                        usuario_dao.alterar_usuario(usuario.id, usuario.nome, usuario.login, usuario.senha,
                                                    usuario.perfil)

                        msg = QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Alteração de Usuários")
                        msg.setText(f'Usuário {usuario.nome} alterado com sucesso!')
                        msg.exec_()

                        self.listagem_usuarios_tabela()
                        self.limpar_formulario()
                    except ConnectionError as con_erro:
                        self.mensagem.mensagem_de_erro()
                        print(con_erro)
                    except IntegrityError as int_erro:
                        print(int_erro)
                        self.mensagem.mensagem_integrity_error(usuario.nome)

                        self.limpar_formulario()

    def carregar_usuario_formulario(self):
        """Carrega dados e popula o formulário

        Consulta os dados no banco através do ID e popula o formulário dando a possibilidade de efetuar a
        atualização ou a exclusão do dado.
        """
        linha = self.tabela_usuarios.currentRow()

        try:
            usuario_dao = UsuarioDao()
            dados_lidos = usuario_dao.listar_usuario()

            valor_id = dados_lidos[linha][0]

            resultado = usuario_dao.carregar_campos_formulario_id(valor_id)

            self.txt_id.setText(str(resultado[0][0]))
            self.txt_nome_completo.setText(str(resultado[0][1]))
            self.txt_login.setText(str(resultado[0][2]))
            self.txt_senha.setText(str(resultado[0][3]))
            self.combo_perfil.setCurrentText(str(resultado[0][4]))

            self.btn_excluir.setEnabled(True)
            self.btn_alterar.setEnabled(True)
            self.btn_salvar.setEnabled(False)
        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_de_erro()

    def excluir_usuario(self):
        """Exclusão de Usuários.

        Método para excluir uma solução selecionada.
        :return: solução para exclusão.
        """
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
        msg.setText("Tem certeza que deseja excluir o Usuário?")
        msg.setStandardButtons(QMessageBox.Yes)
        msg.addButton(QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        if msg.exec_() == QMessageBox.Yes:
            linha = self.tabela_usuarios.currentRow()

            try:
                usuario_dao = UsuarioDao()
                dados_lidos = usuario_dao.listar_usuario()

                if dados_lidos[linha][2] == "admin":
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIcon(QMessageBox.Warning)
                    msg.setWindowTitle("Exclusão de Usuários!")
                    msg.setText('Usuário Administrador não pode ser excluído!')
                    msg.exec_()
                else:
                    self.tabela_usuarios.removeRow(linha)

                    valor_id = dados_lidos[linha][0]

                    usuario_dao.excluir_usuario_banco(valor_id)

                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Exclusão de Usuários!")
                    msg.setText('Usuário excluido com sucesso!')
                    msg.exec_()

                    self.listagem_usuarios_tabela()
                    self.limpar_formulario()
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_de_erro()

    def limpar_formulario(self):
        """Método para limpar os campos do formulário após determinada iteração com o usuário

        :return: parametros em branco para apagar as informações dos campos do formulário.
        """
        self.txt_id.setText("")
        self.txt_nome_completo.setText("")
        self.txt_login.setText("")
        self.txt_senha.setText("")
        self.txt_confirmar_senha.setText("")
        self.combo_perfil.setCurrentText("Usuário")

        self.btn_excluir.setEnabled(False)
        self.btn_alterar.setEnabled(False)
        self.btn_salvar.setEnabled(True)
