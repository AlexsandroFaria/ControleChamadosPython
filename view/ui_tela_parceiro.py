# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_tela_parceiro.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TelaParceiro(object):
    def setupUi(self, TelaParceiro):
        if not TelaParceiro.objectName():
            TelaParceiro.setObjectName(u"TelaParceiro")
        TelaParceiro.resize(801, 655)
        icon = QIcon()
        icon.addFile(u"../../ChamadosSimpress/_img/logo_janela.ico", QSize(), QIcon.Normal, QIcon.Off)
        TelaParceiro.setWindowIcon(icon)
        self.frame = QFrame(TelaParceiro)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 791, 111))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 771, 91))
        self.label.setPixmap(QPixmap(u"../../../ChamadosSimpress/_img/banner_parceiro.png"))
        self.label_2 = QLabel(TelaParceiro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 150, 91, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_3 = QLabel(TelaParceiro)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 190, 101, 16))
        self.label_3.setFont(font)
        self.label_4 = QLabel(TelaParceiro)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 230, 61, 16))
        self.label_4.setFont(font)
        self.label_5 = QLabel(TelaParceiro)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 270, 71, 16))
        self.label_5.setFont(font)
        self.txt_id = QLineEdit(TelaParceiro)
        self.txt_id.setObjectName(u"txt_id")
        self.txt_id.setEnabled(False)
        self.txt_id.setGeometry(QRect(160, 150, 113, 25))
        self.txt_id.setMinimumSize(QSize(0, 25))
        self.txt_id.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(227, 227, 227);")
        self.txt_nome_parceiro = QLineEdit(TelaParceiro)
        self.txt_nome_parceiro.setObjectName(u"txt_nome_parceiro")
        self.txt_nome_parceiro.setGeometry(QRect(160, 190, 291, 25))
        self.txt_nome_parceiro.setMinimumSize(QSize(0, 25))
        self.txt_nome_parceiro.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.txt_contato = QLineEdit(TelaParceiro)
        self.txt_contato.setObjectName(u"txt_contato")
        self.txt_contato.setGeometry(QRect(160, 230, 291, 25))
        self.txt_contato.setMinimumSize(QSize(0, 25))
        self.txt_contato.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.txt_telefone = QLineEdit(TelaParceiro)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setGeometry(QRect(160, 270, 291, 25))
        self.txt_telefone.setMinimumSize(QSize(0, 25))
        self.txt_telefone.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.tabela_parceiro = QTableWidget(TelaParceiro)
        if (self.tabela_parceiro.columnCount() < 4):
            self.tabela_parceiro.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tabela_parceiro.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tabela_parceiro.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tabela_parceiro.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tabela_parceiro.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabela_parceiro.setObjectName(u"tabela_parceiro")
        self.tabela_parceiro.setGeometry(QRect(10, 390, 771, 192))
        self.tabela_parceiro.setStyleSheet(u"")
        self.tabela_parceiro.verticalHeader().setVisible(False)
        self.frame_2 = QFrame(TelaParceiro)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 310, 751, 61))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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
        icon1 = QIcon()
        icon1.addFile(u"../../ChamadosSimpress/_img/limpar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_tela.setIcon(icon1)
        self.btn_limpar_tela.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_limpar_tela)

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
        icon2 = QIcon()
        icon2.addFile(u"../../ChamadosSimpress/_img/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar.setIcon(icon2)
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
        icon3 = QIcon()
        icon3.addFile(u"../../ChamadosSimpress/_img/alterar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar.setIcon(icon3)
        self.btn_alterar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_alterar)

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
        icon4 = QIcon()
        icon4.addFile(u"../../ChamadosSimpress/_img/excluir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir.setIcon(icon4)
        self.btn_excluir.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_excluir)

        self.frame_3 = QFrame(TelaParceiro)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 580, 761, 71))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.btn_carregar = QPushButton(self.frame_3)
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
        icon5 = QIcon()
        icon5.addFile(u"../../ChamadosSimpress/_img/carregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar.setIcon(icon5)
        self.btn_carregar.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_carregar)

        self.btn_sair = QPushButton(self.frame_3)
        self.btn_sair.setObjectName(u"btn_sair")
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
        icon6 = QIcon()
        icon6.addFile(u"../../ChamadosSimpress/_img/sair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sair.setIcon(icon6)
        self.btn_sair.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_sair)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(TelaParceiro)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(480, 150, 231, 141))
        self.label_8.setPixmap(QPixmap(u"../../../ChamadosSimpress/_img/img_parceiro.png"))

        self.retranslateUi(TelaParceiro)

        QMetaObject.connectSlotsByName(TelaParceiro)
    # setupUi

    def retranslateUi(self, TelaParceiro):
        TelaParceiro.setWindowTitle(QCoreApplication.translate("TelaParceiro", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("TelaParceiro", u"Identificador:", None))
        self.label_3.setText(QCoreApplication.translate("TelaParceiro", u"Nome Parceiro:", None))
        self.label_4.setText(QCoreApplication.translate("TelaParceiro", u"Contato:", None))
        self.label_5.setText(QCoreApplication.translate("TelaParceiro", u"Telefone:", None))
        ___qtablewidgetitem = self.tabela_parceiro.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TelaParceiro", u"Identificador", None));
        ___qtablewidgetitem1 = self.tabela_parceiro.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TelaParceiro", u"Nome Parceiro", None));
        ___qtablewidgetitem2 = self.tabela_parceiro.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TelaParceiro", u"Contato", None));
        ___qtablewidgetitem3 = self.tabela_parceiro.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TelaParceiro", u"Telefone", None));
        self.btn_limpar_tela.setText(QCoreApplication.translate("TelaParceiro", u"Limpar tela", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("TelaParceiro", u"Cadastrar", None))
        self.btn_alterar.setText(QCoreApplication.translate("TelaParceiro", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("TelaParceiro", u"Excluir", None))
        self.label_6.setText("")
        self.btn_carregar.setText(QCoreApplication.translate("TelaParceiro", u"Carregar", None))
        self.btn_sair.setText(QCoreApplication.translate("TelaParceiro", u"Sair", None))
        self.label_7.setText("")
        self.label_8.setText("")
    # retranslateUi

