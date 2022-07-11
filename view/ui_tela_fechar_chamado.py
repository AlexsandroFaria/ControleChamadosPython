# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_tela_fechar_chamado.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FecharChamado(object):
    def setupUi(self, FecharChamado):
        if not FecharChamado.objectName():
            FecharChamado.setObjectName(u"FecharChamado")
        FecharChamado.resize(1140, 594)
        icon = QIcon()
        icon.addFile(u"_img/logo_janela.ico", QSize(), QIcon.Normal, QIcon.Off)
        FecharChamado.setWindowIcon(icon)
        self.frame = QFrame(FecharChamado)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 1121, 111))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1121, 111))
        self.label.setPixmap(QPixmap(u"_img/banner_fechar_chamado.png"))
        self.tab_fechar_chamado = QTabWidget(FecharChamado)
        self.tab_fechar_chamado.setObjectName(u"tab_fechar_chamado")
        self.tab_fechar_chamado.setEnabled(True)
        self.tab_fechar_chamado.setGeometry(QRect(10, 140, 1121, 431))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tab_fechar_chamado.setFont(font)
        self.tab_fechar_chamado.setStyleSheet(u"background-color: rgb(216, 216, 216);")
        self.tab_fechar_chamado.setIconSize(QSize(24, 24))
        self.tab_fechamento = QWidget()
        self.tab_fechamento.setObjectName(u"tab_fechamento")
        self.label_3 = QLabel(self.tab_fechamento)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 20, 71, 21))
        self.label_3.setFont(font)
        self.txt_nome_cliente = QLineEdit(self.tab_fechamento)
        self.txt_nome_cliente.setObjectName(u"txt_nome_cliente")
        self.txt_nome_cliente.setEnabled(False)
        self.txt_nome_cliente.setGeometry(QRect(190, 60, 331, 25))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.txt_nome_cliente.setFont(font1)
        self.txt_nome_cliente.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.txt_data_fechamento = QLineEdit(self.tab_fechamento)
        self.txt_data_fechamento.setObjectName(u"txt_data_fechamento")
        self.txt_data_fechamento.setEnabled(False)
        self.txt_data_fechamento.setGeometry(QRect(740, 60, 113, 25))
        self.txt_data_fechamento.setFont(font1)
        self.txt_data_fechamento.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.txt_tipo_chamado = QLineEdit(self.tab_fechamento)
        self.txt_tipo_chamado.setObjectName(u"txt_tipo_chamado")
        self.txt_tipo_chamado.setEnabled(False)
        self.txt_tipo_chamado.setGeometry(QRect(190, 260, 331, 25))
        self.txt_tipo_chamado.setFont(font1)
        self.txt_tipo_chamado.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.txt_contato = QLineEdit(self.tab_fechamento)
        self.txt_contato.setObjectName(u"txt_contato")
        self.txt_contato.setEnabled(False)
        self.txt_contato.setGeometry(QRect(190, 100, 331, 25))
        self.txt_contato.setFont(font1)
        self.txt_contato.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.txt_numero_chamado = QLineEdit(self.tab_fechamento)
        self.txt_numero_chamado.setObjectName(u"txt_numero_chamado")
        self.txt_numero_chamado.setEnabled(False)
        self.txt_numero_chamado.setGeometry(QRect(190, 20, 111, 25))
        self.txt_numero_chamado.setFont(font1)
        self.txt_numero_chamado.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.txt_telefone = QLineEdit(self.tab_fechamento)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setEnabled(False)
        self.txt_telefone.setGeometry(QRect(190, 140, 331, 25))
        self.txt_telefone.setFont(font1)
        self.txt_telefone.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.label_11 = QLabel(self.tab_fechamento)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(570, 60, 151, 20))
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_10 = QLabel(self.tab_fechamento)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(550, 20, 171, 21))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.btn_pegar_data = QPushButton(self.tab_fechamento)
        self.btn_pegar_data.setObjectName(u"btn_pegar_data")
        self.btn_pegar_data.setGeometry(QRect(870, 60, 161, 31))
        self.btn_pegar_data.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(227, 227, 227);")
        icon1 = QIcon()
        icon1.addFile(u"_img/calendario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pegar_data.setIcon(icon1)
        self.btn_pegar_data.setIconSize(QSize(24, 24))
        self.combo_status = QComboBox(self.tab_fechamento)
        self.combo_status.addItem("")
        self.combo_status.addItem("")
        self.combo_status.addItem("")
        self.combo_status.addItem("")
        self.combo_status.setObjectName(u"combo_status")
        self.combo_status.setGeometry(QRect(740, 20, 291, 25))
        self.combo_status.setFont(font1)
        self.combo_status.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.frame_2 = QFrame(self.tab_fechamento)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 161, 321))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 141, 21))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 50, 111, 21))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 90, 61, 21))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 130, 61, 21))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 170, 71, 21))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 250, 141, 21))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 290, 91, 21))
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_contrato = QLineEdit(self.tab_fechamento)
        self.txt_contrato.setObjectName(u"txt_contrato")
        self.txt_contrato.setEnabled(False)
        self.txt_contrato.setGeometry(QRect(400, 20, 121, 25))
        self.txt_contrato.setFont(font1)
        self.txt_contrato.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.btn_fechar_chamado = QPushButton(self.tab_fechamento)
        self.btn_fechar_chamado.setObjectName(u"btn_fechar_chamado")
        self.btn_fechar_chamado.setGeometry(QRect(550, 170, 141, 35))
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
        icon2 = QIcon()
        icon2.addFile(u"_img/fechar_chamado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fechar_chamado.setIcon(icon2)
        self.btn_fechar_chamado.setIconSize(QSize(24, 24))
        self.btn_limpar_tela = QPushButton(self.tab_fechamento)
        self.btn_limpar_tela.setObjectName(u"btn_limpar_tela")
        self.btn_limpar_tela.setGeometry(QRect(550, 120, 141, 35))
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
        icon3 = QIcon()
        icon3.addFile(u"_img/limpar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_tela.setIcon(icon3)
        self.btn_limpar_tela.setIconSize(QSize(24, 24))
        self.btn_sair = QPushButton(self.tab_fechamento)
        self.btn_sair.setObjectName(u"btn_sair")
        self.btn_sair.setGeometry(QRect(960, 350, 141, 35))
        self.btn_sair.setMinimumSize(QSize(0, 35))
        self.btn_sair.setFont(font)
        self.btn_sair.setStyleSheet(u"QPushButton{\n"
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
        icon4.addFile(u"_img/sair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sair.setIcon(icon4)
        self.btn_sair.setIconSize(QSize(24, 24))
        self.groupBox = QGroupBox(self.tab_fechamento)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(720, 120, 311, 91))
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px")
        self.txt_consulta_chamado = QLineEdit(self.groupBox)
        self.txt_consulta_chamado.setObjectName(u"txt_consulta_chamado")
        self.txt_consulta_chamado.setGeometry(QRect(10, 34, 141, 31))
        self.txt_consulta_chamado.setMinimumSize(QSize(0, 25))
        self.txt_consulta_chamado.setFont(font1)
        self.txt_consulta_chamado.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.btn_pesquisar_chamado = QPushButton(self.groupBox)
        self.btn_pesquisar_chamado.setObjectName(u"btn_pesquisar_chamado")
        self.btn_pesquisar_chamado.setGeometry(QRect(170, 30, 111, 35))
        self.btn_pesquisar_chamado.setMinimumSize(QSize(0, 35))
        self.btn_pesquisar_chamado.setFont(font)
        self.btn_pesquisar_chamado.setStyleSheet(u"QPushButton{\n"
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
        icon5.addFile(u"_img/buscar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesquisar_chamado.setIcon(icon5)
        self.btn_pesquisar_chamado.setIconSize(QSize(24, 24))
        self.txt_fechamento = QTextEdit(self.tab_fechamento)
        self.txt_fechamento.setObjectName(u"txt_fechamento")
        self.txt_fechamento.setGeometry(QRect(190, 300, 331, 71))
        self.txt_fechamento.setFont(font1)
        self.txt_fechamento.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.txt_problema = QTextEdit(self.tab_fechamento)
        self.txt_problema.setObjectName(u"txt_problema")
        self.txt_problema.setEnabled(False)
        self.txt_problema.setGeometry(QRect(190, 180, 331, 61))
        self.txt_problema.setFont(font1)
        self.txt_problema.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.label_23 = QLabel(self.tab_fechamento)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(570, 230, 451, 131))
        self.label_23.setPixmap(QPixmap(u"_img/tela_chamado2.png"))
        icon6 = QIcon()
        icon6.addFile(u"_img/fechamento_chamado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_fechar_chamado.addTab(self.tab_fechamento, icon6, "")
        self.label_23.raise_()
        self.label_3.raise_()
        self.txt_nome_cliente.raise_()
        self.txt_data_fechamento.raise_()
        self.txt_tipo_chamado.raise_()
        self.txt_contato.raise_()
        self.txt_numero_chamado.raise_()
        self.txt_telefone.raise_()
        self.label_11.raise_()
        self.label_10.raise_()
        self.btn_pegar_data.raise_()
        self.combo_status.raise_()
        self.frame_2.raise_()
        self.txt_contrato.raise_()
        self.btn_fechar_chamado.raise_()
        self.btn_limpar_tela.raise_()
        self.btn_sair.raise_()
        self.groupBox.raise_()
        self.txt_fechamento.raise_()
        self.txt_problema.raise_()
        self.tab_consulta = QWidget()
        self.tab_consulta.setObjectName(u"tab_consulta")
        self.tabela_chamados_fechados = QTableWidget(self.tab_consulta)
        if (self.tabela_chamados_fechados.columnCount() < 10):
            self.tabela_chamados_fechados.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tabela_chamados_fechados.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tabela_chamados_fechados.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tabela_chamados_fechados.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tabela_chamados_fechados.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.tabela_chamados_fechados.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.tabela_chamados_fechados.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.tabela_chamados_fechados.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.tabela_chamados_fechados.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.tabela_chamados_fechados.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font2);
        self.tabela_chamados_fechados.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tabela_chamados_fechados.setObjectName(u"tabela_chamados_fechados")
        self.tabela_chamados_fechados.setGeometry(QRect(10, 111, 1081, 211))
        self.tabela_chamados_fechados.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tabela_chamados_fechados.verticalHeader().setVisible(False)
        self.frame_3 = QFrame(self.tab_consulta)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 10, 1081, 91))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.txt_consulta_numero_chamado_tabela = QLineEdit(self.frame_3)
        self.txt_consulta_numero_chamado_tabela.setObjectName(u"txt_consulta_numero_chamado_tabela")
        self.txt_consulta_numero_chamado_tabela.setGeometry(QRect(20, 30, 191, 25))
        self.txt_consulta_numero_chamado_tabela.setMinimumSize(QSize(0, 25))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setWeight(75)
        self.txt_consulta_numero_chamado_tabela.setFont(font3)
        self.txt_consulta_numero_chamado_tabela.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.btn_consulta_numero_chamado_tabela = QPushButton(self.frame_3)
        self.btn_consulta_numero_chamado_tabela.setObjectName(u"btn_consulta_numero_chamado_tabela")
        self.btn_consulta_numero_chamado_tabela.setGeometry(QRect(220, 30, 101, 26))
        self.btn_consulta_numero_chamado_tabela.setFont(font)
        self.btn_consulta_numero_chamado_tabela.setStyleSheet(u"QPushButton{\n"
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
        self.btn_consulta_numero_chamado_tabela.setIcon(icon5)
        self.btn_consulta_numero_chamado_tabela.setIconSize(QSize(24, 24))
        self.btn_consulta_contrato_tabela = QPushButton(self.frame_3)
        self.btn_consulta_contrato_tabela.setObjectName(u"btn_consulta_contrato_tabela")
        self.btn_consulta_contrato_tabela.setGeometry(QRect(590, 30, 101, 26))
        self.btn_consulta_contrato_tabela.setFont(font)
        self.btn_consulta_contrato_tabela.setStyleSheet(u"QPushButton{\n"
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
        self.btn_consulta_contrato_tabela.setIcon(icon5)
        self.btn_consulta_contrato_tabela.setIconSize(QSize(24, 24))
        self.txt_consultar_contrato_tabela = QLineEdit(self.frame_3)
        self.txt_consultar_contrato_tabela.setObjectName(u"txt_consultar_contrato_tabela")
        self.txt_consultar_contrato_tabela.setGeometry(QRect(390, 30, 191, 25))
        self.txt_consultar_contrato_tabela.setFont(font1)
        self.txt_consultar_contrato_tabela.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.line = QFrame(self.frame_3)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(350, 10, 16, 71))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(720, 10, 16, 71))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.txt_consulta_nome_cliente = QLineEdit(self.frame_3)
        self.txt_consulta_nome_cliente.setObjectName(u"txt_consulta_nome_cliente")
        self.txt_consulta_nome_cliente.setGeometry(QRect(760, 30, 191, 25))
        self.txt_consulta_nome_cliente.setFont(font1)
        self.txt_consulta_nome_cliente.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.btn_consultar_nome_cliente_tabela = QPushButton(self.frame_3)
        self.btn_consultar_nome_cliente_tabela.setObjectName(u"btn_consultar_nome_cliente_tabela")
        self.btn_consultar_nome_cliente_tabela.setGeometry(QRect(960, 30, 101, 26))
        self.btn_consultar_nome_cliente_tabela.setFont(font)
        self.btn_consultar_nome_cliente_tabela.setStyleSheet(u"QPushButton{\n"
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
        self.btn_consultar_nome_cliente_tabela.setIcon(icon5)
        self.btn_consultar_nome_cliente_tabela.setIconSize(QSize(24, 24))
        self.frame_5 = QFrame(self.tab_consulta)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 330, 1071, 55))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_24 = QLabel(self.frame_5)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout.addWidget(self.label_24)

        self.btn_carregar_tabela = QPushButton(self.frame_5)
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
        icon7 = QIcon()
        icon7.addFile(u"_img/consulta.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar_tabela.setIcon(icon7)
        self.btn_carregar_tabela.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_carregar_tabela)

        self.btn_exibir_detalhes = QPushButton(self.frame_5)
        self.btn_exibir_detalhes.setObjectName(u"btn_exibir_detalhes")
        self.btn_exibir_detalhes.setMinimumSize(QSize(0, 35))
        self.btn_exibir_detalhes.setFont(font)
        self.btn_exibir_detalhes.setStyleSheet(u"QPushButton{\n"
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
        icon8.addFile(u"_img/pesquisa_chamado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exibir_detalhes.setIcon(icon8)
        self.btn_exibir_detalhes.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_exibir_detalhes)

        self.btn_gerar_relatorio = QPushButton(self.frame_5)
        self.btn_gerar_relatorio.setObjectName(u"btn_gerar_relatorio")
        self.btn_gerar_relatorio.setMinimumSize(QSize(0, 35))
        self.btn_gerar_relatorio.setFont(font)
        self.btn_gerar_relatorio.setStyleSheet(u"QPushButton{\n"
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
        icon9.addFile(u"_img/relatorio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gerar_relatorio.setIcon(icon9)
        self.btn_gerar_relatorio.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_gerar_relatorio)

        self.label_25 = QLabel(self.frame_5)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout.addWidget(self.label_25)

        self.tab_fechar_chamado.addTab(self.tab_consulta, icon8, "")
        self.tab_detalhes = QWidget()
        self.tab_detalhes.setObjectName(u"tab_detalhes")
        self.frame_4 = QFrame(self.tab_detalhes)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(30, 20, 161, 321))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 141, 21))
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(40, 50, 111, 21))
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(90, 90, 61, 21))
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_15 = QLabel(self.frame_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(90, 130, 61, 21))
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(80, 170, 71, 21))
        self.label_16.setFont(font)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_17 = QLabel(self.frame_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 250, 141, 21))
        self.label_17.setFont(font)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(60, 290, 91, 21))
        self.label_18.setFont(font)
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_contrato_detalhe = QLineEdit(self.tab_detalhes)
        self.txt_contrato_detalhe.setObjectName(u"txt_contrato_detalhe")
        self.txt_contrato_detalhe.setEnabled(False)
        self.txt_contrato_detalhe.setGeometry(QRect(420, 30, 121, 25))
        self.txt_contrato_detalhe.setFont(font)
        self.txt_contrato_detalhe.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(216, 216, 216);\n"
"border: 1px solid gray")
        self.label_19 = QLabel(self.tab_detalhes)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(340, 30, 71, 21))
        self.label_19.setFont(font)
        self.label_20 = QLabel(self.tab_detalhes)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(570, 30, 171, 21))
        self.label_20.setFont(font)
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_telefone_detalhe = QLineEdit(self.tab_detalhes)
        self.txt_telefone_detalhe.setObjectName(u"txt_telefone_detalhe")
        self.txt_telefone_detalhe.setEnabled(False)
        self.txt_telefone_detalhe.setGeometry(QRect(210, 150, 331, 25))
        self.txt_telefone_detalhe.setFont(font)
        self.txt_telefone_detalhe.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(216, 216, 216);\n"
"border: 1px solid gray")
        self.txt_fechamento_detalhe = QTextEdit(self.tab_detalhes)
        self.txt_fechamento_detalhe.setObjectName(u"txt_fechamento_detalhe")
        self.txt_fechamento_detalhe.setEnabled(False)
        self.txt_fechamento_detalhe.setGeometry(QRect(210, 310, 331, 71))
        self.txt_fechamento_detalhe.setFont(font)
        self.txt_fechamento_detalhe.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(216, 216, 216);\n"
"border: 1px solid gray")
        self.label_21 = QLabel(self.tab_detalhes)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(590, 70, 151, 20))
        self.label_21.setFont(font)
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_problema_detalhe = QTextEdit(self.tab_detalhes)
        self.txt_problema_detalhe.setObjectName(u"txt_problema_detalhe")
        self.txt_problema_detalhe.setEnabled(False)
        self.txt_problema_detalhe.setGeometry(QRect(210, 190, 331, 61))
        self.txt_problema_detalhe.setFont(font)
        self.txt_problema_detalhe.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(216, 216, 216);\n"
"border: 1px solid gray")
        self.txt_numero_chamado_detalhe = QLineEdit(self.tab_detalhes)
        self.txt_numero_chamado_detalhe.setObjectName(u"txt_numero_chamado_detalhe")
        self.txt_numero_chamado_detalhe.setEnabled(False)
        self.txt_numero_chamado_detalhe.setGeometry(QRect(210, 30, 111, 25))
        self.txt_numero_chamado_detalhe.setFont(font)
        self.txt_numero_chamado_detalhe.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(216, 216, 216);\n"
"border: 1px solid gray")
        self.txt_nome_cliente_detalhe = QLineEdit(self.tab_detalhes)
        self.txt_nome_cliente_detalhe.setObjectName(u"txt_nome_cliente_detalhe")
        self.txt_nome_cliente_detalhe.setEnabled(False)
        self.txt_nome_cliente_detalhe.setGeometry(QRect(210, 70, 331, 25))
        self.txt_nome_cliente_detalhe.setFont(font)
        self.txt_nome_cliente_detalhe.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(216, 216, 216);\n"
"border: 1px solid gray")
        self.txt_contato_detalhe = QLineEdit(self.tab_detalhes)
        self.txt_contato_detalhe.setObjectName(u"txt_contato_detalhe")
        self.txt_contato_detalhe.setEnabled(False)
        self.txt_contato_detalhe.setGeometry(QRect(210, 110, 331, 25))
        self.txt_contato_detalhe.setFont(font)
        self.txt_contato_detalhe.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(216, 216, 216);\n"
"border: 1px solid gray")
        self.txt_tipo_chamado_detalhe = QLineEdit(self.tab_detalhes)
        self.txt_tipo_chamado_detalhe.setObjectName(u"txt_tipo_chamado_detalhe")
        self.txt_tipo_chamado_detalhe.setEnabled(False)
        self.txt_tipo_chamado_detalhe.setGeometry(QRect(210, 270, 331, 25))
        self.txt_tipo_chamado_detalhe.setFont(font)
        self.txt_tipo_chamado_detalhe.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(216, 216, 216);\n"
"border: 1px solid gray")
        self.txt_data_fechamento_detalhe = QLineEdit(self.tab_detalhes)
        self.txt_data_fechamento_detalhe.setObjectName(u"txt_data_fechamento_detalhe")
        self.txt_data_fechamento_detalhe.setEnabled(False)
        self.txt_data_fechamento_detalhe.setGeometry(QRect(760, 70, 113, 25))
        self.txt_data_fechamento_detalhe.setFont(font)
        self.txt_data_fechamento_detalhe.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(216, 216, 216);\n"
"border: 1px solid gray")
        self.txt_status_detalhe = QLineEdit(self.tab_detalhes)
        self.txt_status_detalhe.setObjectName(u"txt_status_detalhe")
        self.txt_status_detalhe.setEnabled(False)
        self.txt_status_detalhe.setGeometry(QRect(760, 30, 251, 25))
        self.txt_status_detalhe.setMinimumSize(QSize(0, 25))
        self.txt_status_detalhe.setFont(font)
        self.txt_status_detalhe.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(216, 216, 216);\n"
"border: 1px solid gray")
        self.label_22 = QLabel(self.tab_detalhes)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(670, 110, 321, 241))
        self.label_22.setPixmap(QPixmap(u"_img/tela_chamado.png"))
        self.btn_fechar_2 = QPushButton(self.tab_detalhes)
        self.btn_fechar_2.setObjectName(u"btn_fechar_2")
        self.btn_fechar_2.setGeometry(QRect(974, 342, 121, 31))
        self.btn_fechar_2.setFont(font)
        self.btn_fechar_2.setStyleSheet(u"QPushButton{\n"
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
        self.btn_fechar_2.setIcon(icon4)
        self.btn_fechar_2.setIconSize(QSize(24, 24))
        icon10 = QIcon()
        icon10.addFile(u"_img/contrato.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_fechar_chamado.addTab(self.tab_detalhes, icon10, "")

        self.retranslateUi(FecharChamado)

        self.tab_fechar_chamado.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FecharChamado)
    # setupUi

    def retranslateUi(self, FecharChamado):
        FecharChamado.setWindowTitle(QCoreApplication.translate("FecharChamado", u"Form", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("FecharChamado", u"Contrato:", None))
        self.label_11.setText(QCoreApplication.translate("FecharChamado", u"Data de Fechamento:", None))
        self.label_10.setText(QCoreApplication.translate("FecharChamado", u"Status do Encerramento:", None))
        self.btn_pegar_data.setText(QCoreApplication.translate("FecharChamado", u"Pegar Data Atual", None))
        self.combo_status.setItemText(0, QCoreApplication.translate("FecharChamado", u"Selecione uma op\u00e7\u00e3o", None))
        self.combo_status.setItemText(1, QCoreApplication.translate("FecharChamado", u"Fechado", None))
        self.combo_status.setItemText(2, QCoreApplication.translate("FecharChamado", u"Reagendado", None))
        self.combo_status.setItemText(3, QCoreApplication.translate("FecharChamado", u"Cancelado", None))

        self.label_2.setText(QCoreApplication.translate("FecharChamado", u"N\u00famero do chamado:", None))
        self.label_4.setText(QCoreApplication.translate("FecharChamado", u"Nome do Cliente:", None))
        self.label_5.setText(QCoreApplication.translate("FecharChamado", u"Contato:", None))
        self.label_6.setText(QCoreApplication.translate("FecharChamado", u"Telefone:", None))
        self.label_7.setText(QCoreApplication.translate("FecharChamado", u"Problema:", None))
        self.label_8.setText(QCoreApplication.translate("FecharChamado", u"Tipo de Chamado:", None))
        self.label_9.setText(QCoreApplication.translate("FecharChamado", u"Fechamento:", None))
        self.btn_fechar_chamado.setText(QCoreApplication.translate("FecharChamado", u"Fechar Chamado", None))
        self.btn_limpar_tela.setText(QCoreApplication.translate("FecharChamado", u"Limpar tela", None))
        self.btn_sair.setText(QCoreApplication.translate("FecharChamado", u"Fechar", None))
        self.groupBox.setTitle(QCoreApplication.translate("FecharChamado", u"Consultar Chamado", None))
        self.txt_consulta_chamado.setPlaceholderText(QCoreApplication.translate("FecharChamado", u"Consulta por N\u00famero ", None))
        self.btn_pesquisar_chamado.setText(QCoreApplication.translate("FecharChamado", u"Pesquisar", None))
        self.label_23.setText("")
        self.tab_fechar_chamado.setTabText(self.tab_fechar_chamado.indexOf(self.tab_fechamento), QCoreApplication.translate("FecharChamado", u"Fechamento Chamados", None))
        ___qtablewidgetitem = self.tabela_chamados_fechados.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FecharChamado", u"N\u00famero do Chamado", None));
        ___qtablewidgetitem1 = self.tabela_chamados_fechados.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FecharChamado", u"Contrato", None));
        ___qtablewidgetitem2 = self.tabela_chamados_fechados.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FecharChamado", u"Nome do Cliente", None));
        ___qtablewidgetitem3 = self.tabela_chamados_fechados.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FecharChamado", u"Contato", None));
        ___qtablewidgetitem4 = self.tabela_chamados_fechados.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FecharChamado", u"Telefone", None));
        ___qtablewidgetitem5 = self.tabela_chamados_fechados.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FecharChamado", u"Problema", None));
        ___qtablewidgetitem6 = self.tabela_chamados_fechados.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("FecharChamado", u"Tipo de Fechamento", None));
        ___qtablewidgetitem7 = self.tabela_chamados_fechados.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("FecharChamado", u"Fechamento", None));
        ___qtablewidgetitem8 = self.tabela_chamados_fechados.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("FecharChamado", u"Status", None));
        ___qtablewidgetitem9 = self.tabela_chamados_fechados.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("FecharChamado", u"Data de Fechamento", None));
        self.txt_consulta_numero_chamado_tabela.setPlaceholderText(QCoreApplication.translate("FecharChamado", u"Pesquisar por N\u00famero do Chamado", None))
        self.btn_consulta_numero_chamado_tabela.setText(QCoreApplication.translate("FecharChamado", u"Pesquisar", None))
        self.btn_consulta_contrato_tabela.setText(QCoreApplication.translate("FecharChamado", u"Pesquisar", None))
        self.txt_consultar_contrato_tabela.setPlaceholderText(QCoreApplication.translate("FecharChamado", u"Pesquisar por Contrato", None))
        self.txt_consulta_nome_cliente.setPlaceholderText(QCoreApplication.translate("FecharChamado", u"Pesquisar por nome do Cliente", None))
        self.btn_consultar_nome_cliente_tabela.setText(QCoreApplication.translate("FecharChamado", u"Pesquisar", None))
        self.label_24.setText("")
        self.btn_carregar_tabela.setText(QCoreApplication.translate("FecharChamado", u"Carregar Tabela", None))
        self.btn_exibir_detalhes.setText(QCoreApplication.translate("FecharChamado", u"Exibir Detalhes", None))
        self.btn_gerar_relatorio.setText(QCoreApplication.translate("FecharChamado", u"Gerar Relat\u00f3rio", None))
        self.label_25.setText("")
        self.tab_fechar_chamado.setTabText(self.tab_fechar_chamado.indexOf(self.tab_consulta), QCoreApplication.translate("FecharChamado", u"Consultar Chamados Fechados", None))
        self.label_12.setText(QCoreApplication.translate("FecharChamado", u"N\u00famero do chamado:", None))
        self.label_13.setText(QCoreApplication.translate("FecharChamado", u"Nome do Cliente:", None))
        self.label_14.setText(QCoreApplication.translate("FecharChamado", u"Contato:", None))
        self.label_15.setText(QCoreApplication.translate("FecharChamado", u"Telefone:", None))
        self.label_16.setText(QCoreApplication.translate("FecharChamado", u"Problema:", None))
        self.label_17.setText(QCoreApplication.translate("FecharChamado", u"Tipo do chamado:", None))
        self.label_18.setText(QCoreApplication.translate("FecharChamado", u"Fechamento:", None))
        self.label_19.setText(QCoreApplication.translate("FecharChamado", u"Contrato:", None))
        self.label_20.setText(QCoreApplication.translate("FecharChamado", u"Status do Encerramento:", None))
        self.label_21.setText(QCoreApplication.translate("FecharChamado", u"Data de Fechamento:", None))
        self.label_22.setText("")
        self.btn_fechar_2.setText(QCoreApplication.translate("FecharChamado", u"Fechar", None))
        self.tab_fechar_chamado.setTabText(self.tab_fechar_chamado.indexOf(self.tab_detalhes), QCoreApplication.translate("FecharChamado", u"Detalhamento do Chamado", None))
    # retranslateUi

