# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_tela_fechar_chamado_parceiro.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FecharChamadoParceiro(object):
    def setupUi(self, FecharChamadoParceiro):
        if not FecharChamadoParceiro.objectName():
            FecharChamadoParceiro.setObjectName(u"FecharChamadoParceiro")
        FecharChamadoParceiro.resize(965, 640)
        icon = QIcon()
        icon.addFile(u"_img/logo_janela.ico", QSize(), QIcon.Normal, QIcon.Off)
        FecharChamadoParceiro.setWindowIcon(icon)
        self.frame = QFrame(FecharChamadoParceiro)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 941, 91))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 941, 91))
        self.label.setPixmap(QPixmap(u"_img/banner_fecharChamado_parceiro.png"))
        self.tab_fechar_chamados_parceiro = QTabWidget(FecharChamadoParceiro)
        self.tab_fechar_chamados_parceiro.setObjectName(u"tab_fechar_chamados_parceiro")
        self.tab_fechar_chamados_parceiro.setGeometry(QRect(10, 120, 941, 501))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tab_fechar_chamados_parceiro.setFont(font)
        self.tab_fechar_chamados_parceiro.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.tab_fechar_chamado = QWidget()
        self.tab_fechar_chamado.setObjectName(u"tab_fechar_chamado")
        self.groupBox = QGroupBox(self.tab_fechar_chamado)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 551, 80))
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 141, 21))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"border: none")
        self.txt_pesquisar_chamado = QLineEdit(self.groupBox)
        self.txt_pesquisar_chamado.setObjectName(u"txt_pesquisar_chamado")
        self.txt_pesquisar_chamado.setGeometry(QRect(160, 20, 161, 25))
        self.txt_pesquisar_chamado.setMinimumSize(QSize(0, 25))
        self.txt_pesquisar_chamado.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.btn_pesquisa_chamado = QPushButton(self.groupBox)
        self.btn_pesquisa_chamado.setObjectName(u"btn_pesquisa_chamado")
        self.btn_pesquisa_chamado.setGeometry(QRect(360, 20, 131, 31))
        self.btn_pesquisa_chamado.setMinimumSize(QSize(0, 25))
        self.btn_pesquisa_chamado.setFont(font)
        self.btn_pesquisa_chamado.setStyleSheet(u"QPushButton{\n"
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
        icon1 = QIcon()
        icon1.addFile(u"_img/buscar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesquisa_chamado.setIcon(icon1)
        self.btn_pesquisa_chamado.setIconSize(QSize(24, 24))
        self.label_3 = QLabel(self.tab_fechar_chamado)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 120, 131, 16))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(self.tab_fechar_chamado)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 160, 141, 20))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.tab_fechar_chamado)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(310, 160, 131, 20))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6 = QLabel(self.tab_fechar_chamado)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 200, 91, 16))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7 = QLabel(self.tab_fechar_chamado)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 240, 61, 16))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_8 = QLabel(self.tab_fechar_chamado)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(100, 300, 61, 20))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_9 = QLabel(self.tab_fechar_chamado)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 370, 141, 21))
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_empresa_parceira = QLineEdit(self.tab_fechar_chamado)
        self.txt_empresa_parceira.setObjectName(u"txt_empresa_parceira")
        self.txt_empresa_parceira.setEnabled(True)
        self.txt_empresa_parceira.setGeometry(QRect(180, 120, 381, 25))
        self.txt_empresa_parceira.setMinimumSize(QSize(0, 25))
        self.txt_empresa_parceira.setAcceptDrops(False)
        self.txt_empresa_parceira.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.txt_numero_chamado = QLineEdit(self.tab_fechar_chamado)
        self.txt_numero_chamado.setObjectName(u"txt_numero_chamado")
        self.txt_numero_chamado.setGeometry(QRect(180, 160, 113, 25))
        self.txt_numero_chamado.setMinimumSize(QSize(0, 25))
        self.txt_numero_chamado.setAcceptDrops(False)
        self.txt_numero_chamado.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.txt_chamado_simpress = QLineEdit(self.tab_fechar_chamado)
        self.txt_chamado_simpress.setObjectName(u"txt_chamado_simpress")
        self.txt_chamado_simpress.setGeometry(QRect(450, 160, 111, 25))
        self.txt_chamado_simpress.setMinimumSize(QSize(0, 25))
        self.txt_chamado_simpress.setAcceptDrops(False)
        self.txt_chamado_simpress.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.txt_responsavel = QLineEdit(self.tab_fechar_chamado)
        self.txt_responsavel.setObjectName(u"txt_responsavel")
        self.txt_responsavel.setGeometry(QRect(180, 200, 381, 25))
        self.txt_responsavel.setMinimumSize(QSize(0, 25))
        self.txt_responsavel.setAcceptDrops(False)
        self.txt_responsavel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.txt_cliente = QLineEdit(self.tab_fechar_chamado)
        self.txt_cliente.setObjectName(u"txt_cliente")
        self.txt_cliente.setGeometry(QRect(180, 240, 381, 25))
        self.txt_cliente.setMinimumSize(QSize(0, 25))
        self.txt_cliente.setAcceptDrops(False)
        self.txt_cliente.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.txt_solucao = QTextEdit(self.tab_fechar_chamado)
        self.txt_solucao.setObjectName(u"txt_solucao")
        self.txt_solucao.setGeometry(QRect(180, 280, 381, 71))
        self.txt_solucao.setAcceptDrops(False)
        self.txt_solucao.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.txt_data_fechamento = QLineEdit(self.tab_fechar_chamado)
        self.txt_data_fechamento.setObjectName(u"txt_data_fechamento")
        self.txt_data_fechamento.setGeometry(QRect(180, 370, 121, 25))
        self.txt_data_fechamento.setMinimumSize(QSize(0, 25))
        self.txt_data_fechamento.setAcceptDrops(False)
        self.txt_data_fechamento.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.btn_data_atual = QPushButton(self.tab_fechar_chamado)
        self.btn_data_atual.setObjectName(u"btn_data_atual")
        self.btn_data_atual.setGeometry(QRect(320, 360, 151, 35))
        self.btn_data_atual.setMinimumSize(QSize(0, 35))
        self.btn_data_atual.setFont(font)
        self.btn_data_atual.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid gray")
        icon2 = QIcon()
        icon2.addFile(u"_img/calendario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_data_atual.setIcon(icon2)
        self.btn_data_atual.setIconSize(QSize(24, 24))
        self.btn_sair = QPushButton(self.tab_fechar_chamado)
        self.btn_sair.setObjectName(u"btn_sair")
        self.btn_sair.setGeometry(QRect(800, 380, 121, 31))
        self.btn_sair.setFont(font)
        self.btn_sair.setStyleSheet(u"QPushButton{\n"
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
        icon3.addFile(u"_img/sair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sair.setIcon(icon3)
        self.btn_sair.setIconSize(QSize(24, 24))
        self.btn_fechar_chamado = QPushButton(self.tab_fechar_chamado)
        self.btn_fechar_chamado.setObjectName(u"btn_fechar_chamado")
        self.btn_fechar_chamado.setGeometry(QRect(570, 30, 161, 31))
        self.btn_fechar_chamado.setFont(font)
        self.btn_fechar_chamado.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 0, 0);\n"
"	border-radius: 5px;\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(85, 0, 0);\n"
"	background-color: rgb(0, 0, 255);\n"
"	border: solid 5p\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"_img/fechar_chamado_parceiro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fechar_chamado.setIcon(icon4)
        self.btn_fechar_chamado.setIconSize(QSize(24, 24))
        self.btn_limpar_tela = QPushButton(self.tab_fechar_chamado)
        self.btn_limpar_tela.setObjectName(u"btn_limpar_tela")
        self.btn_limpar_tela.setGeometry(QRect(740, 30, 161, 31))
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
        icon5 = QIcon()
        icon5.addFile(u"_img/limpar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_tela.setIcon(icon5)
        self.btn_limpar_tela.setIconSize(QSize(24, 24))
        self.label_12 = QLabel(self.tab_fechar_chamado)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(590, 90, 301, 251))
        self.label_12.setPixmap(QPixmap(u"_img/parceiro.png"))
        self.tab_fechar_chamados_parceiro.addTab(self.tab_fechar_chamado, "")
        self.tab_consultar_chamado = QWidget()
        self.tab_consultar_chamado.setObjectName(u"tab_consultar_chamado")
        self.tabela_chamado_parceiro_fechado = QTableWidget(self.tab_consultar_chamado)
        if (self.tabela_chamado_parceiro_fechado.columnCount() < 7):
            self.tabela_chamado_parceiro_fechado.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tabela_chamado_parceiro_fechado.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tabela_chamado_parceiro_fechado.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tabela_chamado_parceiro_fechado.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tabela_chamado_parceiro_fechado.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.tabela_chamado_parceiro_fechado.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.tabela_chamado_parceiro_fechado.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.tabela_chamado_parceiro_fechado.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabela_chamado_parceiro_fechado.setObjectName(u"tabela_chamado_parceiro_fechado")
        self.tabela_chamado_parceiro_fechado.setGeometry(QRect(10, 121, 911, 241))
        self.tabela_chamado_parceiro_fechado.verticalHeader().setVisible(False)
        self.groupBox_2 = QGroupBox(self.tab_consultar_chamado)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 20, 271, 80))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px")
        self.btn_pesquisar_chamado_tabela = QPushButton(self.groupBox_2)
        self.btn_pesquisar_chamado_tabela.setObjectName(u"btn_pesquisar_chamado_tabela")
        self.btn_pesquisar_chamado_tabela.setGeometry(QRect(160, 30, 101, 31))
        self.btn_pesquisar_chamado_tabela.setFont(font)
        self.btn_pesquisar_chamado_tabela.setStyleSheet(u"QPushButton{\n"
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
        self.btn_pesquisar_chamado_tabela.setIcon(icon1)
        self.btn_pesquisar_chamado_tabela.setIconSize(QSize(24, 24))
        self.txt_consulta_chamado_tabela = QLineEdit(self.groupBox_2)
        self.txt_consulta_chamado_tabela.setObjectName(u"txt_consulta_chamado_tabela")
        self.txt_consulta_chamado_tabela.setGeometry(QRect(20, 30, 121, 25))
        self.txt_consulta_chamado_tabela.setMinimumSize(QSize(0, 25))
        self.txt_consulta_chamado_tabela.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.groupBox_3 = QGroupBox(self.tab_consultar_chamado)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(300, 20, 271, 80))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px")
        self.txt_consulta_cliente_tabela = QLineEdit(self.groupBox_3)
        self.txt_consulta_cliente_tabela.setObjectName(u"txt_consulta_cliente_tabela")
        self.txt_consulta_cliente_tabela.setGeometry(QRect(20, 30, 121, 25))
        self.txt_consulta_cliente_tabela.setMinimumSize(QSize(0, 25))
        self.txt_consulta_cliente_tabela.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.btn_pesquisa_cliente_tabela = QPushButton(self.groupBox_3)
        self.btn_pesquisa_cliente_tabela.setObjectName(u"btn_pesquisa_cliente_tabela")
        self.btn_pesquisa_cliente_tabela.setGeometry(QRect(160, 30, 101, 31))
        self.btn_pesquisa_cliente_tabela.setFont(font)
        self.btn_pesquisa_cliente_tabela.setStyleSheet(u"QPushButton{\n"
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
        self.btn_pesquisa_cliente_tabela.setIcon(icon1)
        self.btn_pesquisa_cliente_tabela.setIconSize(QSize(24, 24))
        self.groupBox_4 = QGroupBox(self.tab_consultar_chamado)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(600, 20, 271, 80))
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px")
        self.txt_consulta_data_tabela = QLineEdit(self.groupBox_4)
        self.txt_consulta_data_tabela.setObjectName(u"txt_consulta_data_tabela")
        self.txt_consulta_data_tabela.setGeometry(QRect(20, 30, 121, 25))
        self.txt_consulta_data_tabela.setMinimumSize(QSize(0, 25))
        self.txt_consulta_data_tabela.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.btn_consulta_data_tabela = QPushButton(self.groupBox_4)
        self.btn_consulta_data_tabela.setObjectName(u"btn_consulta_data_tabela")
        self.btn_consulta_data_tabela.setGeometry(QRect(160, 30, 101, 31))
        self.btn_consulta_data_tabela.setFont(font)
        self.btn_consulta_data_tabela.setStyleSheet(u"QPushButton{\n"
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
        self.btn_consulta_data_tabela.setIcon(icon1)
        self.btn_consulta_data_tabela.setIconSize(QSize(24, 24))
        self.frame_2 = QFrame(self.tab_consultar_chamado)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 390, 901, 55))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout.addWidget(self.label_10)

        self.btn_carregar_tabela = QPushButton(self.frame_2)
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
        icon6 = QIcon()
        icon6.addFile(u"_img/pesquisa_chamado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar_tabela.setIcon(icon6)
        self.btn_carregar_tabela.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_carregar_tabela)

        self.btn_carregar = QPushButton(self.frame_2)
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
        icon7 = QIcon()
        icon7.addFile(u"_img/carregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar.setIcon(icon7)
        self.btn_carregar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_carregar)

        self.btn_gerar_relatorio = QPushButton(self.frame_2)
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
        icon8 = QIcon()
        icon8.addFile(u"_img/relatorio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gerar_relatorio.setIcon(icon8)
        self.btn_gerar_relatorio.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_gerar_relatorio)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout.addWidget(self.label_11)

        self.tab_fechar_chamados_parceiro.addTab(self.tab_consultar_chamado, "")

        self.retranslateUi(FecharChamadoParceiro)

        self.tab_fechar_chamados_parceiro.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FecharChamadoParceiro)
    # setupUi

    def retranslateUi(self, FecharChamadoParceiro):
        FecharChamadoParceiro.setWindowTitle(QCoreApplication.translate("FecharChamadoParceiro", u"Form", None))
        self.label.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("FecharChamadoParceiro", u"Pesquisar Chamado", None))
        self.label_2.setText(QCoreApplication.translate("FecharChamadoParceiro", u"N\u00famero do Chamado:", None))
        self.txt_pesquisar_chamado.setPlaceholderText(QCoreApplication.translate("FecharChamadoParceiro", u"N\u00famero do chamado", None))
        self.btn_pesquisa_chamado.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Pesquisar", None))
        self.label_3.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Empresa Parceira:", None))
        self.label_4.setText(QCoreApplication.translate("FecharChamadoParceiro", u"N\u00famero do Chamado:", None))
        self.label_5.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Chamado Simpress:", None))
        self.label_6.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Respons\u00e1vel:", None))
        self.label_7.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Cliente:", None))
        self.label_8.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Solu\u00e7\u00e3o:", None))
        self.label_9.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Data de Fechamento:", None))
        self.btn_data_atual.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Pegar data atual", None))
        self.btn_sair.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Sair", None))
        self.btn_fechar_chamado.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Fechar Chamado", None))
        self.btn_limpar_tela.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Limpar Tela", None))
        self.label_12.setText("")
        self.tab_fechar_chamados_parceiro.setTabText(self.tab_fechar_chamados_parceiro.indexOf(self.tab_fechar_chamado), QCoreApplication.translate("FecharChamadoParceiro", u"Fechar chamado de Parceiros", None))
        ___qtablewidgetitem = self.tabela_chamado_parceiro_fechado.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Empresa", None));
        ___qtablewidgetitem1 = self.tabela_chamado_parceiro_fechado.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FecharChamadoParceiro", u"N\u00famero do Chamado", None));
        ___qtablewidgetitem2 = self.tabela_chamado_parceiro_fechado.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Chamado Simpress", None));
        ___qtablewidgetitem3 = self.tabela_chamado_parceiro_fechado.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Responsavel", None));
        ___qtablewidgetitem4 = self.tabela_chamado_parceiro_fechado.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Cliente", None));
        ___qtablewidgetitem5 = self.tabela_chamado_parceiro_fechado.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem6 = self.tabela_chamado_parceiro_fechado.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Data Fechamento", None));
        self.groupBox_2.setTitle(QCoreApplication.translate("FecharChamadoParceiro", u"Consultar por n\u00famero do chamado", None))
        self.btn_pesquisar_chamado_tabela.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Pesquisar", None))
        self.txt_consulta_chamado_tabela.setPlaceholderText(QCoreApplication.translate("FecharChamadoParceiro", u"N\u00famero do Chamado", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("FecharChamadoParceiro", u"Consulta por cliente", None))
        self.txt_consulta_cliente_tabela.setPlaceholderText(QCoreApplication.translate("FecharChamadoParceiro", u"Nome do Cliente", None))
        self.btn_pesquisa_cliente_tabela.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Pesquisar", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("FecharChamadoParceiro", u"Consultar por data", None))
        self.txt_consulta_data_tabela.setInputMask(QCoreApplication.translate("FecharChamadoParceiro", u"##/##/####", None))
        self.btn_consulta_data_tabela.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Pesquisar", None))
        self.label_10.setText("")
        self.btn_carregar_tabela.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Carregar Tabela", None))
        self.btn_carregar.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Carregar", None))
        self.btn_gerar_relatorio.setText(QCoreApplication.translate("FecharChamadoParceiro", u"Gerar Relat\u00f3rio", None))
        self.label_11.setText("")
        self.tab_fechar_chamados_parceiro.setTabText(self.tab_fechar_chamados_parceiro.indexOf(self.tab_consultar_chamado), QCoreApplication.translate("FecharChamadoParceiro", u"Consultar Chamados Parceiros", None))
    # retranslateUi

