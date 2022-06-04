# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_tela_chamado.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TelaChamado(object):
    def setupUi(self, TelaChamado):
        if not TelaChamado.objectName():
            TelaChamado.setObjectName(u"TelaChamado")
        TelaChamado.resize(1245, 658)
        icon = QIcon()
        icon.addFile(u"_img/logo_janela.ico", QSize(), QIcon.Normal, QIcon.Off)
        TelaChamado.setWindowIcon(icon)
        self.frame = QFrame(TelaChamado)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 1231, 111))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 0, 1221, 101))
        self.label_15.setPixmap(QPixmap(u"_img/banner_chamado.png"))
        self.tab_chamado = QTabWidget(TelaChamado)
        self.tab_chamado.setObjectName(u"tab_chamado")
        self.tab_chamado.setGeometry(QRect(10, 130, 1211, 521))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tab_chamado.setFont(font)
        self.tab_chamado.setStyleSheet(u"background-color: rgb(227, 227, 227);")
        self.tab_chamado.setIconSize(QSize(24, 24))
        self.tab_cadastro_chamado = QWidget()
        self.tab_cadastro_chamado.setObjectName(u"tab_cadastro_chamado")
        self.label = QLabel(self.tab_cadastro_chamado)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 141, 21))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_numero_chamado = QLineEdit(self.tab_cadastro_chamado)
        self.txt_numero_chamado.setObjectName(u"txt_numero_chamado")
        self.txt_numero_chamado.setEnabled(True)
        self.txt_numero_chamado.setGeometry(QRect(160, 30, 91, 25))
        self.txt_numero_chamado.setMinimumSize(QSize(0, 25))
        self.txt_numero_chamado.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.label_2 = QLabel(self.tab_cadastro_chamado)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(330, 30, 121, 21))
        self.label_2.setFont(font)
        self.txt_numero_contrato = QLineEdit(self.tab_cadastro_chamado)
        self.txt_numero_contrato.setObjectName(u"txt_numero_contrato")
        self.txt_numero_contrato.setGeometry(QRect(450, 30, 121, 25))
        self.txt_numero_contrato.setMinimumSize(QSize(0, 25))
        self.txt_numero_contrato.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.btn_buscar_contrato = QPushButton(self.tab_cadastro_chamado)
        self.btn_buscar_contrato.setObjectName(u"btn_buscar_contrato")
        self.btn_buscar_contrato.setGeometry(QRect(580, 10, 151, 41))
        self.btn_buscar_contrato.setMinimumSize(QSize(0, 25))
        self.btn_buscar_contrato.setFont(font)
        self.btn_buscar_contrato.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"_img/contrato.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_buscar_contrato.setIcon(icon1)
        self.btn_buscar_contrato.setIconSize(QSize(24, 24))
        self.label_3 = QLabel(self.tab_cadastro_chamado)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 60, 91, 21))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_nome_cliente = QLineEdit(self.tab_cadastro_chamado)
        self.txt_nome_cliente.setObjectName(u"txt_nome_cliente")
        self.txt_nome_cliente.setEnabled(False)
        self.txt_nome_cliente.setGeometry(QRect(160, 60, 571, 25))
        self.txt_nome_cliente.setMinimumSize(QSize(0, 25))
        self.txt_nome_cliente.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.label_4 = QLabel(self.tab_cadastro_chamado)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 90, 71, 21))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_endereco = QLineEdit(self.tab_cadastro_chamado)
        self.txt_endereco.setObjectName(u"txt_endereco")
        self.txt_endereco.setEnabled(False)
        self.txt_endereco.setGeometry(QRect(160, 90, 571, 25))
        self.txt_endereco.setMinimumSize(QSize(0, 25))
        self.txt_endereco.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.label_5 = QLabel(self.tab_cadastro_chamado)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 120, 61, 21))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_contato = QLineEdit(self.tab_cadastro_chamado)
        self.txt_contato.setObjectName(u"txt_contato")
        self.txt_contato.setEnabled(False)
        self.txt_contato.setGeometry(QRect(160, 120, 571, 25))
        self.txt_contato.setMinimumSize(QSize(0, 25))
        self.txt_contato.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.label_6 = QLabel(self.tab_cadastro_chamado)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 150, 61, 21))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_telefone = QLineEdit(self.tab_cadastro_chamado)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setEnabled(True)
        self.txt_telefone.setGeometry(QRect(160, 150, 251, 25))
        self.txt_telefone.setMinimumSize(QSize(0, 25))
        self.txt_telefone.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.label_7 = QLabel(self.tab_cadastro_chamado)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(420, 150, 47, 21))
        self.label_7.setFont(font)
        self.txt_email = QLineEdit(self.tab_cadastro_chamado)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setEnabled(True)
        self.txt_email.setGeometry(QRect(470, 150, 261, 25))
        self.txt_email.setMinimumSize(QSize(0, 25))
        self.txt_email.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.label_8 = QLabel(self.tab_cadastro_chamado)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(80, 200, 71, 21))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_9 = QLabel(self.tab_cadastro_chamado)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 260, 91, 21))
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_observacao = QLineEdit(self.tab_cadastro_chamado)
        self.txt_observacao.setObjectName(u"txt_observacao")
        self.txt_observacao.setGeometry(QRect(160, 260, 571, 25))
        self.txt_observacao.setMinimumSize(QSize(0, 25))
        self.txt_observacao.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.label_10 = QLabel(self.tab_cadastro_chamado)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 290, 131, 21))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.combo_status_chamado = QComboBox(self.tab_cadastro_chamado)
        self.combo_status_chamado.addItem("")
        self.combo_status_chamado.addItem("")
        self.combo_status_chamado.addItem("")
        self.combo_status_chamado.addItem("")
        self.combo_status_chamado.setObjectName(u"combo_status_chamado")
        self.combo_status_chamado.setGeometry(QRect(160, 290, 161, 25))
        self.combo_status_chamado.setMinimumSize(QSize(0, 25))
        self.combo_status_chamado.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.label_11 = QLabel(self.tab_cadastro_chamado)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 320, 111, 21))
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.combo_tipo_chamado = QComboBox(self.tab_cadastro_chamado)
        self.combo_tipo_chamado.addItem("")
        self.combo_tipo_chamado.addItem("")
        self.combo_tipo_chamado.addItem("")
        self.combo_tipo_chamado.addItem("")
        self.combo_tipo_chamado.setObjectName(u"combo_tipo_chamado")
        self.combo_tipo_chamado.setGeometry(QRect(160, 320, 161, 25))
        self.combo_tipo_chamado.setMinimumSize(QSize(0, 25))
        self.combo_tipo_chamado.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.label_12 = QLabel(self.tab_cadastro_chamado)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(90, 350, 61, 21))
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.combo_solucao = QComboBox(self.tab_cadastro_chamado)
        self.combo_solucao.addItem("")
        self.combo_solucao.setObjectName(u"combo_solucao")
        self.combo_solucao.setGeometry(QRect(160, 350, 161, 25))
        self.combo_solucao.setMinimumSize(QSize(0, 25))
        self.combo_solucao.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.label_13 = QLabel(self.tab_cadastro_chamado)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(340, 300, 131, 21))
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_data_abertura = QLineEdit(self.tab_cadastro_chamado)
        self.txt_data_abertura.setObjectName(u"txt_data_abertura")
        self.txt_data_abertura.setEnabled(False)
        self.txt_data_abertura.setGeometry(QRect(480, 300, 101, 25))
        self.txt_data_abertura.setMinimumSize(QSize(0, 25))
        self.txt_data_abertura.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.label_14 = QLabel(self.tab_cadastro_chamado)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(330, 350, 141, 21))
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_data_atualizacao = QLineEdit(self.tab_cadastro_chamado)
        self.txt_data_atualizacao.setObjectName(u"txt_data_atualizacao")
        self.txt_data_atualizacao.setEnabled(False)
        self.txt_data_atualizacao.setGeometry(QRect(480, 350, 101, 25))
        self.txt_data_atualizacao.setMinimumSize(QSize(0, 25))
        self.txt_data_atualizacao.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.btn_atualizar_data_abertura = QPushButton(self.tab_cadastro_chamado)
        self.btn_atualizar_data_abertura.setObjectName(u"btn_atualizar_data_abertura")
        self.btn_atualizar_data_abertura.setGeometry(QRect(600, 300, 131, 35))
        self.btn_atualizar_data_abertura.setMinimumSize(QSize(0, 35))
        self.btn_atualizar_data_abertura.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(227, 227, 227);")
        icon2 = QIcon()
        icon2.addFile(u"_img/calendario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_atualizar_data_abertura.setIcon(icon2)
        self.btn_atualizar_data_abertura.setIconSize(QSize(24, 24))
        self.btn_atualizar_data = QPushButton(self.tab_cadastro_chamado)
        self.btn_atualizar_data.setObjectName(u"btn_atualizar_data")
        self.btn_atualizar_data.setGeometry(QRect(600, 350, 131, 35))
        self.btn_atualizar_data.setMinimumSize(QSize(0, 35))
        self.btn_atualizar_data.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(227, 227, 227);")
        self.btn_atualizar_data.setIcon(icon2)
        self.btn_atualizar_data.setIconSize(QSize(24, 24))
        self.frame_2 = QFrame(self.tab_cadastro_chamado)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 390, 731, 55))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_cadastrar = QPushButton(self.frame_2)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 35))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"_img/cadastro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar.setIcon(icon3)
        self.btn_cadastrar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_cadastrar)

        self.btn_alterar = QPushButton(self.frame_2)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(0, 35))
        self.btn_alterar.setFont(font)
        self.btn_alterar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"_img/alterar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar.setIcon(icon4)
        self.btn_alterar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_alterar)

        self.btn_limpar_tela = QPushButton(self.frame_2)
        self.btn_limpar_tela.setObjectName(u"btn_limpar_tela")
        self.btn_limpar_tela.setMinimumSize(QSize(0, 35))
        self.btn_limpar_tela.setFont(font)
        self.btn_limpar_tela.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"_img/limpar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_tela.setIcon(icon5)
        self.btn_limpar_tela.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_limpar_tela)

        self.btn_excluir = QPushButton(self.frame_2)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(0, 35))
        self.btn_excluir.setFont(font)
        self.btn_excluir.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"_img/excluir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir.setIcon(icon6)
        self.btn_excluir.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_excluir)

        self.btn_fechar_chamado = QPushButton(self.tab_cadastro_chamado)
        self.btn_fechar_chamado.setObjectName(u"btn_fechar_chamado")
        self.btn_fechar_chamado.setGeometry(QRect(780, 10, 381, 35))
        self.btn_fechar_chamado.setMinimumSize(QSize(0, 35))
        self.btn_fechar_chamado.setFont(font)
        self.btn_fechar_chamado.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	\n"
"	color: rgb(255, 0, 0);\n"
"	border-radius: 5px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"_img/fechar_chamado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fechar_chamado.setIcon(icon7)
        self.btn_fechar_chamado.setIconSize(QSize(24, 24))
        self.btn_fechar_tela = QPushButton(self.tab_cadastro_chamado)
        self.btn_fechar_tela.setObjectName(u"btn_fechar_tela")
        self.btn_fechar_tela.setGeometry(QRect(850, 400, 271, 35))
        self.btn_fechar_tela.setMinimumSize(QSize(0, 35))
        self.btn_fechar_tela.setFont(font)
        self.btn_fechar_tela.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"_img/sair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fechar_tela.setIcon(icon8)
        self.btn_fechar_tela.setIconSize(QSize(24, 24))
        self.label_16 = QLabel(self.tab_cadastro_chamado)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(760, 70, 401, 281))
        self.label_16.setPixmap(QPixmap(u"_img/img_chamado.png"))
        self.txt_problema = QTextEdit(self.tab_cadastro_chamado)
        self.txt_problema.setObjectName(u"txt_problema")
        self.txt_problema.setGeometry(QRect(160, 180, 571, 71))
        self.txt_problema.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.tab_chamado.addTab(self.tab_cadastro_chamado, icon3, "")
        self.tab_consulta_chamado = QWidget()
        self.tab_consulta_chamado.setObjectName(u"tab_consulta_chamado")
        self.tabela_chamado = QTableWidget(self.tab_consulta_chamado)
        if (self.tabela_chamado.columnCount() < 14):
            self.tabela_chamado.setColumnCount(14)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela_chamado.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_chamado.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela_chamado.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela_chamado.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabela_chamado.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabela_chamado.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabela_chamado.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabela_chamado.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabela_chamado.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabela_chamado.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabela_chamado.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabela_chamado.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabela_chamado.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabela_chamado.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        self.tabela_chamado.setObjectName(u"tabela_chamado")
        self.tabela_chamado.setGeometry(QRect(10, 121, 1171, 271))
        self.tabela_chamado.verticalHeader().setVisible(False)
        self.frame_3 = QFrame(self.tab_consulta_chamado)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 10, 1171, 91))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_consulta_numero_chamado = QLineEdit(self.frame_3)
        self.txt_consulta_numero_chamado.setObjectName(u"txt_consulta_numero_chamado")
        self.txt_consulta_numero_chamado.setMinimumSize(QSize(0, 30))
        self.txt_consulta_numero_chamado.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")

        self.horizontalLayout_2.addWidget(self.txt_consulta_numero_chamado)

        self.btn_consultar_numero_chamado = QPushButton(self.frame_3)
        self.btn_consultar_numero_chamado.setObjectName(u"btn_consultar_numero_chamado")
        self.btn_consultar_numero_chamado.setMinimumSize(QSize(0, 30))
        self.btn_consultar_numero_chamado.setFont(font)
        self.btn_consultar_numero_chamado.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"_img/buscar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_consultar_numero_chamado.setIcon(icon9)
        self.btn_consultar_numero_chamado.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_consultar_numero_chamado)

        self.line = QFrame(self.frame_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.txt_consulta_contrato = QLineEdit(self.frame_3)
        self.txt_consulta_contrato.setObjectName(u"txt_consulta_contrato")
        self.txt_consulta_contrato.setMinimumSize(QSize(0, 30))
        self.txt_consulta_contrato.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")

        self.horizontalLayout_2.addWidget(self.txt_consulta_contrato)

        self.btn_consulta_contrato = QPushButton(self.frame_3)
        self.btn_consulta_contrato.setObjectName(u"btn_consulta_contrato")
        self.btn_consulta_contrato.setFont(font)
        self.btn_consulta_contrato.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        self.btn_consulta_contrato.setIcon(icon9)
        self.btn_consulta_contrato.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_consulta_contrato)

        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.txt_consulta_nome_cliente = QLineEdit(self.frame_3)
        self.txt_consulta_nome_cliente.setObjectName(u"txt_consulta_nome_cliente")
        self.txt_consulta_nome_cliente.setMinimumSize(QSize(0, 30))
        self.txt_consulta_nome_cliente.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")

        self.horizontalLayout_2.addWidget(self.txt_consulta_nome_cliente)

        self.btn_consultar_nome_cliente = QPushButton(self.frame_3)
        self.btn_consultar_nome_cliente.setObjectName(u"btn_consultar_nome_cliente")
        self.btn_consultar_nome_cliente.setFont(font)
        self.btn_consultar_nome_cliente.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        self.btn_consultar_nome_cliente.setIcon(icon9)
        self.btn_consultar_nome_cliente.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_consultar_nome_cliente)

        self.frame_4 = QFrame(self.tab_consulta_chamado)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 410, 1171, 46))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_17 = QLabel(self.frame_4)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_3.addWidget(self.label_17)

        self.btn_carregar_tabela = QPushButton(self.frame_4)
        self.btn_carregar_tabela.setObjectName(u"btn_carregar_tabela")
        self.btn_carregar_tabela.setMinimumSize(QSize(0, 35))
        self.btn_carregar_tabela.setFont(font)
        self.btn_carregar_tabela.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"_img/pesquisa_chamado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar_tabela.setIcon(icon10)
        self.btn_carregar_tabela.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.btn_carregar_tabela)

        self.btn_carregar = QPushButton(self.frame_4)
        self.btn_carregar.setObjectName(u"btn_carregar")
        self.btn_carregar.setMinimumSize(QSize(0, 35))
        self.btn_carregar.setFont(font)
        self.btn_carregar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"_img/carregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar.setIcon(icon11)
        self.btn_carregar.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.btn_carregar)

        self.btn_gerar_relatrio = QPushButton(self.frame_4)
        self.btn_gerar_relatrio.setObjectName(u"btn_gerar_relatrio")
        self.btn_gerar_relatrio.setMinimumSize(QSize(0, 35))
        self.btn_gerar_relatrio.setFont(font)
        self.btn_gerar_relatrio.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"_img/relatorio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gerar_relatrio.setIcon(icon12)
        self.btn_gerar_relatrio.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.btn_gerar_relatrio)

        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_3.addWidget(self.label_18)

        icon13 = QIcon()
        icon13.addFile(u"_img/consulta.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_chamado.addTab(self.tab_consulta_chamado, icon13, "")

        self.retranslateUi(TelaChamado)

        self.tab_chamado.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TelaChamado)
    # setupUi

    def retranslateUi(self, TelaChamado):
        TelaChamado.setWindowTitle(QCoreApplication.translate("TelaChamado", u"Form", None))
        self.label_15.setText("")
        self.label.setText(QCoreApplication.translate("TelaChamado", u"N\u00famero do Chamado:", None))
        self.label_2.setText(QCoreApplication.translate("TelaChamado", u"Contrato Cliente:", None))
        self.btn_buscar_contrato.setText(QCoreApplication.translate("TelaChamado", u"Buscar Contrato", None))
        self.label_3.setText(QCoreApplication.translate("TelaChamado", u"Nome Cliente:", None))
        self.label_4.setText(QCoreApplication.translate("TelaChamado", u"Endere\u00e7o:", None))
        self.label_5.setText(QCoreApplication.translate("TelaChamado", u"Contato:", None))
        self.label_6.setText(QCoreApplication.translate("TelaChamado", u"Telefone:", None))
        self.label_7.setText(QCoreApplication.translate("TelaChamado", u"E-mail:", None))
        self.label_8.setText(QCoreApplication.translate("TelaChamado", u"Problema:", None))
        self.label_9.setText(QCoreApplication.translate("TelaChamado", u"Observa\u00e7\u00e3o:", None))
        self.label_10.setText(QCoreApplication.translate("TelaChamado", u"Status do Chamado:", None))
        self.combo_status_chamado.setItemText(0, QCoreApplication.translate("TelaChamado", u"Selecione uma Op\u00e7\u00e3o", None))
        self.combo_status_chamado.setItemText(1, QCoreApplication.translate("TelaChamado", u"Aberto", None))
        self.combo_status_chamado.setItemText(2, QCoreApplication.translate("TelaChamado", u"Em atendimento", None))
        self.combo_status_chamado.setItemText(3, "")

        self.label_11.setText(QCoreApplication.translate("TelaChamado", u"Tipo do Chamdo:", None))
        self.combo_tipo_chamado.setItemText(0, QCoreApplication.translate("TelaChamado", u"Selecione uma Op\u00e7\u00e3o", None))
        self.combo_tipo_chamado.setItemText(1, QCoreApplication.translate("TelaChamado", u"Incidente", None))
        self.combo_tipo_chamado.setItemText(2, QCoreApplication.translate("TelaChamado", u"Cobran\u00e7a", None))
        self.combo_tipo_chamado.setItemText(3, QCoreApplication.translate("TelaChamado", u"D\u00favida", None))

        self.label_12.setText(QCoreApplication.translate("TelaChamado", u"Solu\u00e7\u00e3o:", None))
        self.combo_solucao.setItemText(0, QCoreApplication.translate("TelaChamado", u"Selecione uma Op\u00e7\u00e3o", None))

        self.label_13.setText(QCoreApplication.translate("TelaChamado", u"Data de Abertura:", None))
        self.txt_data_abertura.setInputMask("")
        self.label_14.setText(QCoreApplication.translate("TelaChamado", u"Data de Atualiza\u00e7\u00e3o:", None))
        self.txt_data_atualizacao.setInputMask("")
        self.btn_atualizar_data_abertura.setText(QCoreApplication.translate("TelaChamado", u"Data Atual", None))
        self.btn_atualizar_data.setText(QCoreApplication.translate("TelaChamado", u"Atualizar Data", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("TelaChamado", u"Cadastrar", None))
        self.btn_alterar.setText(QCoreApplication.translate("TelaChamado", u"Alterar", None))
        self.btn_limpar_tela.setText(QCoreApplication.translate("TelaChamado", u"Limpar Tela", None))
        self.btn_excluir.setText(QCoreApplication.translate("TelaChamado", u"Excluir", None))
        self.btn_fechar_chamado.setText(QCoreApplication.translate("TelaChamado", u"Fechar Chamado", None))
        self.btn_fechar_tela.setText(QCoreApplication.translate("TelaChamado", u"Fechar", None))
        self.label_16.setText("")
        self.tab_chamado.setTabText(self.tab_chamado.indexOf(self.tab_cadastro_chamado), QCoreApplication.translate("TelaChamado", u"Cadastro de Chamados", None))
        ___qtablewidgetitem = self.tabela_chamado.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TelaChamado", u"N\u00famero Chamado", None));
        ___qtablewidgetitem1 = self.tabela_chamado.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TelaChamado", u"N\u00famero do contrato", None));
        ___qtablewidgetitem2 = self.tabela_chamado.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TelaChamado", u"Nome do Cliente", None));
        ___qtablewidgetitem3 = self.tabela_chamado.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TelaChamado", u"Endere\u00e7o", None));
        ___qtablewidgetitem4 = self.tabela_chamado.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TelaChamado", u"Contato", None));
        ___qtablewidgetitem5 = self.tabela_chamado.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TelaChamado", u"Telefone", None));
        ___qtablewidgetitem6 = self.tabela_chamado.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("TelaChamado", u"E-mail", None));
        ___qtablewidgetitem7 = self.tabela_chamado.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("TelaChamado", u"Problema", None));
        ___qtablewidgetitem8 = self.tabela_chamado.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("TelaChamado", u"Observa\u00e7\u00e3o", None));
        ___qtablewidgetitem9 = self.tabela_chamado.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("TelaChamado", u"Status", None));
        ___qtablewidgetitem10 = self.tabela_chamado.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("TelaChamado", u"Solu\u00e7\u00e3o", None));
        ___qtablewidgetitem11 = self.tabela_chamado.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("TelaChamado", u"Tipo", None));
        ___qtablewidgetitem12 = self.tabela_chamado.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("TelaChamado", u"Data Abertura", None));
        ___qtablewidgetitem13 = self.tabela_chamado.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("TelaChamado", u"Atualiza\u00e7\u00e3o", None));
        self.txt_consulta_numero_chamado.setPlaceholderText(QCoreApplication.translate("TelaChamado", u"Consulta por N\u00famero do Chamado", None))
        self.btn_consultar_numero_chamado.setText(QCoreApplication.translate("TelaChamado", u"Consultar", None))
        self.txt_consulta_contrato.setPlaceholderText(QCoreApplication.translate("TelaChamado", u"Consulta por Contrato", None))
        self.btn_consulta_contrato.setText(QCoreApplication.translate("TelaChamado", u"Consultar", None))
        self.txt_consulta_nome_cliente.setPlaceholderText(QCoreApplication.translate("TelaChamado", u"Consultar por Nome do Cliente", None))
        self.btn_consultar_nome_cliente.setText(QCoreApplication.translate("TelaChamado", u"Consultar", None))
        self.label_17.setText("")
        self.btn_carregar_tabela.setText(QCoreApplication.translate("TelaChamado", u"Carregar Tabela", None))
        self.btn_carregar.setText(QCoreApplication.translate("TelaChamado", u"Carregar", None))
        self.btn_gerar_relatrio.setText(QCoreApplication.translate("TelaChamado", u"Gerar Relat\u00f3rio", None))
        self.label_18.setText("")
        self.tab_chamado.setTabText(self.tab_chamado.indexOf(self.tab_consulta_chamado), QCoreApplication.translate("TelaChamado", u"Consulta de Chamados", None))
    # retranslateUi

