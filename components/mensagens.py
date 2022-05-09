from PySide2 import QtGui
from PySide2.QtWidgets import QMessageBox


class Mensagens:
    """Script de mensagens padrão do sistema

    Esse módulo é responsável por gerar as mensagens padrões do sistema para evitar repetições
    de mensagens pelo código.
    """

    def mensagem_campo_vazio(self):
        """Mensagem padrão de campo vazio

        Mensagem de alerta para o usuário informando que um determinado campo do formulário está em branco.
        """
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Campos em branco!")
        msg.setText('Existem campos em branco!')
        msg.exec_()

    def mensagem_de_erro(self):
        """Mensagem padrão de erro

        Mensagem de erro do sistema, apresentada quando algum problema inesperado ocorre.
        """
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Erro na aplicação.")
        msg.setText('Erro ou falha no banco de dados. Consulte o admin do sistema.')
        msg.exec_()

    def mensagem_exclusao(self):
        """Mensagem padrão de exclusão

        Mensagem padrão informando que algum registro foi apagado do sistema e assim deletado do banco de
        dados.
        """
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Exclusão de Clientes!")
        msg.setText('Exclusão efetuada com sucesso.')
        msg.exec_()

    def mensagem_campo_numerico(self):
        """Mensagem padrão de campo númérico

        Mensagem dee padrão que alerta o usuário de que o campo informado só permite digitação de números.
        """
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Dados incorretos")
        msg.setText('Informe somente números')
        msg.exec_()

    def mensagem_alteração(self):
        """Mensagem padrão de alteração

        Mensagem padrão que informa quando os dados de um formulário é alterada.
        """
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Alteração de Dados")
        msg.setText('Dados alterados com sucesso')
        msg.exec_()

    def mensagem_gerar_relatorio(self):
        """Mensagem padrão de gerar relatório

        Mensagem padrão que alerta ao usuário quando um relatório já foi processado e gerado.
        """
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Relatório de Chamados Fechados")
        msg.setText('Relatório gerado com sucesso! Verifique o mesmo na pasta Downloads')
        msg.exec_()
