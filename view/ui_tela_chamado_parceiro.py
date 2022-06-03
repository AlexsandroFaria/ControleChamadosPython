# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_tela_chamado_parceiro.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TelaChamadoParceiro(object):
    def setupUi(self, TelaChamadoParceiro):
        if not TelaChamadoParceiro.objectName():
            TelaChamadoParceiro.setObjectName(u"TelaChamadoParceiro")
        TelaChamadoParceiro.resize(964, 638)
        icon = QIcon()
        icon.addFile(u"_img/logo_janela.ico", QSize(), QIcon.Normal, QIcon.Off)
        TelaChamadoParceiro.setWindowIcon(icon)
        self.frame = QFrame(TelaChamadoParceiro)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 941, 101))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 941, 101))
        self.label.setPixmap(QPixmap(u"_img/banner_chamado_parceiro.png"))
        self.tab_chamado_parceiro = QTabWidget(TelaChamadoParceiro)
        self.tab_chamado_parceiro.setObjectName(u"tab_chamado_parceiro")
        self.tab_chamado_parceiro.setGeometry(QRect(10, 130, 931, 491))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tab_chamado_parceiro.setFont(font)
        self.tab_chamado_parceiro.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.tab_chamado_parceiro.setIconSize(QSize(24, 24))
        self.tab_cadastro_parceiro = QWidget()
        self.tab_cadastro_parceiro.setObjectName(u"tab_cadastro_parceiro")
        self.label_3 = QLabel(self.tab_cadastro_parceiro)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 141, 21))
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_numero_chamado = QLineEdit(self.tab_cadastro_parceiro)
        self.txt_numero_chamado.setObjectName(u"txt_numero_chamado")
        self.txt_numero_chamado.setGeometry(QRect(190, 70, 101, 25))
        self.txt_numero_chamado.setMinimumSize(QSize(0, 25))
        self.txt_numero_chamado.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.label_7 = QLabel(self.tab_cadastro_parceiro)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 320, 101, 21))
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_responsavel = QLineEdit(self.tab_cadastro_parceiro)
        self.txt_responsavel.setObjectName(u"txt_responsavel")
        self.txt_responsavel.setGeometry(QRect(190, 150, 441, 25))
        self.txt_responsavel.setMinimumSize(QSize(0, 25))
        self.txt_responsavel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.combo_empresa_parceira = QComboBox(self.tab_cadastro_parceiro)
        self.combo_empresa_parceira.addItem("")
        self.combo_empresa_parceira.setObjectName(u"combo_empresa_parceira")
        self.combo_empresa_parceira.setGeometry(QRect(190, 110, 441, 25))
        self.combo_empresa_parceira.setMinimumSize(QSize(0, 25))
        self.combo_empresa_parceira.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(216, 216, 216);\n"
"border:1px solid\n"
"")
        self.label_8 = QLabel(self.tab_cadastro_parceiro)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 360, 111, 21))
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_data_abertura = QLineEdit(self.tab_cadastro_parceiro)
        self.txt_data_abertura.setObjectName(u"txt_data_abertura")
        self.txt_data_abertura.setEnabled(False)
        self.txt_data_abertura.setGeometry(QRect(190, 360, 101, 25))
        self.txt_data_abertura.setMinimumSize(QSize(0, 25))
        self.txt_data_abertura.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.btn_pegar_data = QPushButton(self.tab_cadastro_parceiro)
        self.btn_pegar_data.setObjectName(u"btn_pegar_data")
        self.btn_pegar_data.setGeometry(QRect(320, 360, 121, 31))
        self.btn_pegar_data.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid gray")
        icon1 = QIcon()
        icon1.addFile(u"_img/calendario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pegar_data.setIcon(icon1)
        self.btn_pegar_data.setIconSize(QSize(24, 24))
        self.label_4 = QLabel(self.tab_cadastro_parceiro)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 150, 101, 21))
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_observacao = QLineEdit(self.tab_cadastro_parceiro)
        self.txt_observacao.setObjectName(u"txt_observacao")
        self.txt_observacao.setGeometry(QRect(190, 320, 441, 25))
        self.txt_observacao.setMinimumSize(QSize(0, 25))
        self.txt_observacao.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.label_9 = QLabel(self.tab_cadastro_parceiro)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(310, 73, 131, 20))
        self.label_9.setFont(font)
        self.combo_chamado_simpress = QComboBox(self.tab_cadastro_parceiro)
        self.combo_chamado_simpress.addItem("")
        self.combo_chamado_simpress.setObjectName(u"combo_chamado_simpress")
        self.combo_chamado_simpress.setGeometry(QRect(460, 70, 171, 25))
        self.combo_chamado_simpress.setMinimumSize(QSize(0, 25))
        self.combo_chamado_simpress.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(216, 216, 216);\n"
"border:1px solid\n"
"")
        self.btn_fechar_chamado = QPushButton(self.tab_cadastro_parceiro)
        self.btn_fechar_chamado.setObjectName(u"btn_fechar_chamado")
        self.btn_fechar_chamado.setGeometry(QRect(460, 360, 171, 31))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_fechar_chamado.setFont(font1)
        self.btn_fechar_chamado.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	\n"
"	color: rgb(255, 0, 0);\n"
"	border-radius: 5px;\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"_img/fechar_chamado_parceiro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fechar_chamado.setIcon(icon2)
        self.btn_fechar_chamado.setIconSize(QSize(24, 24))
        self.combo_cliente = QComboBox(self.tab_cadastro_parceiro)
        self.combo_cliente.addItem("")
        self.combo_cliente.setObjectName(u"combo_cliente")
        self.combo_cliente.setGeometry(QRect(190, 190, 441, 25))
        self.combo_cliente.setMinimumSize(QSize(0, 25))
        self.combo_cliente.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(216, 216, 216);\n"
"border:1px solid\n"
"")
        self.txt_problema = QTextEdit(self.tab_cadastro_parceiro)
        self.txt_problema.setObjectName(u"txt_problema")
        self.txt_problema.setGeometry(QRect(190, 230, 441, 71))
        self.txt_problema.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.label_2 = QLabel(self.tab_cadastro_parceiro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 161, 21))
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6 = QLabel(self.tab_cadastro_parceiro)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 250, 161, 21))
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.tab_cadastro_parceiro)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 190, 71, 21))
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_2 = QFrame(self.tab_cadastro_parceiro)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(680, 60, 161, 311))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_limpar_tela = QPushButton(self.frame_2)
        self.btn_limpar_tela.setObjectName(u"btn_limpar_tela")
        self.btn_limpar_tela.setMinimumSize(QSize(0, 35))
        self.btn_limpar_tela.setFont(font)
        self.btn_limpar_tela.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"_img/limpar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_tela.setIcon(icon3)
        self.btn_limpar_tela.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_limpar_tela)

        self.btn_cadastrar = QPushButton(self.frame_2)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 35))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"_img/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar.setIcon(icon4)
        self.btn_cadastrar.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_cadastrar)

        self.btn_alterar = QPushButton(self.frame_2)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(0, 35))
        self.btn_alterar.setFont(font)
        self.btn_alterar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"_img/alterar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar.setIcon(icon5)
        self.btn_alterar.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_2)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(0, 35))
        self.btn_excluir.setFont(font)
        self.btn_excluir.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border:1px solid\n"
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

        self.verticalLayout.addWidget(self.btn_excluir)

        self.btn_fechar = QPushButton(self.frame_2)
        self.btn_fechar.setObjectName(u"btn_fechar")
        self.btn_fechar.setMinimumSize(QSize(0, 35))
        self.btn_fechar.setFont(font)
        self.btn_fechar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"_img/sair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fechar.setIcon(icon7)
        self.btn_fechar.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_fechar)

        icon8 = QIcon()
        icon8.addFile(u"_img/abrir_chamado_parceiro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_chamado_parceiro.addTab(self.tab_cadastro_parceiro, icon8, "")
        self.tab_consulta_parceiro = QWidget()
        self.tab_consulta_parceiro.setObjectName(u"tab_consulta_parceiro")
        self.tabela_chamado_parceiro = QTableWidget(self.tab_consulta_parceiro)
        if (self.tabela_chamado_parceiro.columnCount() < 8):
            self.tabela_chamado_parceiro.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tabela_chamado_parceiro.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tabela_chamado_parceiro.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tabela_chamado_parceiro.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tabela_chamado_parceiro.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.tabela_chamado_parceiro.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.tabela_chamado_parceiro.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.tabela_chamado_parceiro.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.tabela_chamado_parceiro.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tabela_chamado_parceiro.setObjectName(u"tabela_chamado_parceiro")
        self.tabela_chamado_parceiro.setGeometry(QRect(10, 111, 891, 271))
        self.tabela_chamado_parceiro.verticalHeader().setVisible(False)
        self.frame_3 = QFrame(self.tab_consulta_parceiro)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 10, 891, 80))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.txt_consulta_numero_chamado = QLineEdit(self.frame_3)
        self.txt_consulta_numero_chamado.setObjectName(u"txt_consulta_numero_chamado")
        self.txt_consulta_numero_chamado.setGeometry(QRect(20, 24, 231, 31))
        self.txt_consulta_numero_chamado.setMinimumSize(QSize(0, 25))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.txt_consulta_numero_chamado.setFont(font2)
        self.txt_consulta_numero_chamado.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.btn_pesquisar_numero_chamado = QPushButton(self.frame_3)
        self.btn_pesquisar_numero_chamado.setObjectName(u"btn_pesquisar_numero_chamado")
        self.btn_pesquisar_numero_chamado.setGeometry(QRect(260, 20, 111, 35))
        self.btn_pesquisar_numero_chamado.setMinimumSize(QSize(0, 35))
        self.btn_pesquisar_numero_chamado.setFont(font)
        self.btn_pesquisar_numero_chamado.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"_img/buscar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesquisar_numero_chamado.setIcon(icon9)
        self.btn_pesquisar_numero_chamado.setIconSize(QSize(24, 24))
        self.txt_consulta_chamado_simpress = QLineEdit(self.frame_3)
        self.txt_consulta_chamado_simpress.setObjectName(u"txt_consulta_chamado_simpress")
        self.txt_consulta_chamado_simpress.setGeometry(QRect(480, 24, 231, 31))
        self.txt_consulta_chamado_simpress.setMinimumSize(QSize(0, 25))
        self.txt_consulta_chamado_simpress.setFont(font2)
        self.txt_consulta_chamado_simpress.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.btn_pesquisar_chamado_simpress = QPushButton(self.frame_3)
        self.btn_pesquisar_chamado_simpress.setObjectName(u"btn_pesquisar_chamado_simpress")
        self.btn_pesquisar_chamado_simpress.setGeometry(QRect(720, 20, 121, 35))
        self.btn_pesquisar_chamado_simpress.setMinimumSize(QSize(0, 35))
        self.btn_pesquisar_chamado_simpress.setFont(font)
        self.btn_pesquisar_chamado_simpress.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        self.btn_pesquisar_chamado_simpress.setIcon(icon9)
        self.btn_pesquisar_chamado_simpress.setIconSize(QSize(24, 24))
        self.frame_4 = QFrame(self.tab_consulta_parceiro)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 390, 891, 55))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout.addWidget(self.label_10)

        self.btn_carregar_tabela = QPushButton(self.frame_4)
        self.btn_carregar_tabela.setObjectName(u"btn_carregar_tabela")
        self.btn_carregar_tabela.setMinimumSize(QSize(0, 35))
        self.btn_carregar_tabela.setFont(font)
        self.btn_carregar_tabela.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border:1px solid\n"
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

        self.horizontalLayout.addWidget(self.btn_carregar_tabela)

        self.btn_carregar = QPushButton(self.frame_4)
        self.btn_carregar.setObjectName(u"btn_carregar")
        self.btn_carregar.setMinimumSize(QSize(0, 35))
        self.btn_carregar.setFont(font)
        self.btn_carregar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border:1px solid\n"
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

        self.horizontalLayout.addWidget(self.btn_carregar)

        self.btn_gerar_relatorio = QPushButton(self.frame_4)
        self.btn_gerar_relatorio.setObjectName(u"btn_gerar_relatorio")
        self.btn_gerar_relatorio.setMinimumSize(QSize(0, 35))
        self.btn_gerar_relatorio.setFont(font)
        self.btn_gerar_relatorio.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"_img/relatorio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gerar_relatorio.setIcon(icon12)
        self.btn_gerar_relatorio.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_gerar_relatorio)

        self.btn_fechar2 = QPushButton(self.frame_4)
        self.btn_fechar2.setObjectName(u"btn_fechar2")
        self.btn_fechar2.setMinimumSize(QSize(0, 35))
        self.btn_fechar2.setFont(font)
        self.btn_fechar2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        self.btn_fechar2.setIcon(icon7)
        self.btn_fechar2.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_fechar2)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout.addWidget(self.label_11)

        icon13 = QIcon()
        icon13.addFile(u"_img/consultar_chamado_parceiro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_chamado_parceiro.addTab(self.tab_consulta_parceiro, icon13, "")

        self.retranslateUi(TelaChamadoParceiro)

        self.tab_chamado_parceiro.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TelaChamadoParceiro)
    # setupUi

    def retranslateUi(self, TelaChamadoParceiro):
        TelaChamadoParceiro.setWindowTitle(QCoreApplication.translate("TelaChamadoParceiro", u"Form", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Empresa Parceira:", None))
        self.label_7.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Observa\u00e7\u00e3o:", None))
        self.combo_empresa_parceira.setItemText(0, QCoreApplication.translate("TelaChamadoParceiro", u"Selecione uma op\u00e7\u00e3o", None))

        self.label_8.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Data Abertura:", None))
        self.btn_pegar_data.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Data atual", None))
        self.label_4.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Respons\u00e1vel:", None))
        self.label_9.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Chamado Simpress:", None))
        self.combo_chamado_simpress.setItemText(0, QCoreApplication.translate("TelaChamadoParceiro", u"Selecione uma op\u00e7\u00e3o", None))

        self.btn_fechar_chamado.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Fechar chamado", None))
        self.combo_cliente.setItemText(0, QCoreApplication.translate("TelaChamadoParceiro", u"Selecione uma op\u00e7\u00e3o", None))

        self.label_2.setText(QCoreApplication.translate("TelaChamadoParceiro", u"N\u00famero do Chamado:", None))
        self.label_6.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Descri\u00e7\u00e3o do Problema:", None))
        self.label_5.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Cliente:", None))
        self.btn_limpar_tela.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Limpar Tela", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Cadastrar", None))
        self.btn_alterar.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Excluir", None))
        self.btn_fechar.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Fechar", None))
        self.tab_chamado_parceiro.setTabText(self.tab_chamado_parceiro.indexOf(self.tab_cadastro_parceiro), QCoreApplication.translate("TelaChamadoParceiro", u"Abertura chamado Parceiro", None))
        ___qtablewidgetitem = self.tabela_chamado_parceiro.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TelaChamadoParceiro", u"N\u00famero Chamado", None));
        ___qtablewidgetitem1 = self.tabela_chamado_parceiro.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Chamado Simpress", None));
        ___qtablewidgetitem2 = self.tabela_chamado_parceiro.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Empresa Parceira", None));
        ___qtablewidgetitem3 = self.tabela_chamado_parceiro.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Respons\u00e1vel", None));
        ___qtablewidgetitem4 = self.tabela_chamado_parceiro.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Cliente", None));
        ___qtablewidgetitem5 = self.tabela_chamado_parceiro.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem6 = self.tabela_chamado_parceiro.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Observa\u00e7\u00e3o", None));
        ___qtablewidgetitem7 = self.tabela_chamado_parceiro.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Data abertura", None));
        self.txt_consulta_numero_chamado.setPlaceholderText(QCoreApplication.translate("TelaChamadoParceiro", u"Pesquisar por N\u00famero do Chamado", None))
        self.btn_pesquisar_numero_chamado.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Pesquisar", None))
        self.txt_consulta_chamado_simpress.setPlaceholderText(QCoreApplication.translate("TelaChamadoParceiro", u"Pesquisar Chamado Simpress", None))
        self.btn_pesquisar_chamado_simpress.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Pesquisar", None))
        self.label_10.setText("")
        self.btn_carregar_tabela.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Carregar Tabela", None))
        self.btn_carregar.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Carregar", None))
        self.btn_gerar_relatorio.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Gerar Relat\u00f3rio", None))
        self.btn_fechar2.setText(QCoreApplication.translate("TelaChamadoParceiro", u"Fechar", None))
        self.label_11.setText("")
        self.tab_chamado_parceiro.setTabText(self.tab_chamado_parceiro.indexOf(self.tab_consulta_parceiro), QCoreApplication.translate("TelaChamadoParceiro", u"Consulta Chamado Parceiro", None))
    # retranslateUi

