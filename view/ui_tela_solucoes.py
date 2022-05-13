# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_tela_solucoes.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TelaSolucoes(object):
    def setupUi(self, TelaSolucoes):
        if not TelaSolucoes.objectName():
            TelaSolucoes.setObjectName(u"TelaSolucoes")
        TelaSolucoes.resize(612, 522)
        icon = QIcon()
        icon.addFile(u"../../ChamadosSimpress/_img/logo_janela.ico", QSize(), QIcon.Normal, QIcon.Off)
        TelaSolucoes.setWindowIcon(icon)
        self.frame = QFrame(TelaSolucoes)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 591, 91))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 591, 91))
        self.label.setPixmap(QPixmap(u"../../../ChamadosSimpress/_img/banner_solucoes.png"))
        self.label_2 = QLabel(TelaSolucoes)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 140, 91, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_3 = QLabel(TelaSolucoes)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 180, 61, 21))
        self.label_3.setFont(font)
        self.label_4 = QLabel(TelaSolucoes)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 220, 81, 16))
        self.label_4.setFont(font)
        self.tabela_solucoes = QTableWidget(TelaSolucoes)
        if (self.tabela_solucoes.columnCount() < 3):
            self.tabela_solucoes.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tabela_solucoes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tabela_solucoes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tabela_solucoes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tabela_solucoes.setObjectName(u"tabela_solucoes")
        self.tabela_solucoes.setGeometry(QRect(50, 260, 541, 192))
        self.tabela_solucoes.verticalHeader().setVisible(False)
        self.txt_id = QLineEdit(TelaSolucoes)
        self.txt_id.setObjectName(u"txt_id")
        self.txt_id.setEnabled(False)
        self.txt_id.setGeometry(QRect(130, 140, 71, 25))
        self.txt_id.setMinimumSize(QSize(0, 25))
        self.txt_id.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(227, 227, 227);")
        self.txt_solucao = QLineEdit(TelaSolucoes)
        self.txt_solucao.setObjectName(u"txt_solucao")
        self.txt_solucao.setGeometry(QRect(130, 180, 461, 25))
        self.txt_solucao.setMinimumSize(QSize(0, 25))
        self.txt_solucao.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.txt_descricao = QLineEdit(TelaSolucoes)
        self.txt_descricao.setObjectName(u"txt_descricao")
        self.txt_descricao.setGeometry(QRect(130, 220, 461, 25))
        self.txt_descricao.setMinimumSize(QSize(0, 25))
        self.txt_descricao.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.btn_cadastrar = QPushButton(TelaSolucoes)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(220, 130, 111, 35))
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
        icon1 = QIcon()
        icon1.addFile(u"../../ChamadosSimpress/_img/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar.setIcon(icon1)
        self.btn_limpar_tela = QPushButton(TelaSolucoes)
        self.btn_limpar_tela.setObjectName(u"btn_limpar_tela")
        self.btn_limpar_tela.setGeometry(QRect(350, 130, 111, 35))
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
        icon2 = QIcon()
        icon2.addFile(u"../../ChamadosSimpress/_img/limpar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_tela.setIcon(icon2)
        self.btn_limpar_tela.setIconSize(QSize(24, 24))
        self.btn_excluir = QPushButton(TelaSolucoes)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setGeometry(QRect(480, 130, 111, 35))
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
        icon3 = QIcon()
        icon3.addFile(u"../../ChamadosSimpress/_img/excluir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir.setIcon(icon3)
        self.layoutWidget = QWidget(TelaSolucoes)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 460, 541, 37))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.btn_carregar = QPushButton(self.layoutWidget)
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
        icon4 = QIcon()
        icon4.addFile(u"../../ChamadosSimpress/_img/carregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar.setIcon(icon4)

        self.horizontalLayout.addWidget(self.btn_carregar)

        self.btn_sair = QPushButton(self.layoutWidget)
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
        icon5 = QIcon()
        icon5.addFile(u"../../ChamadosSimpress/_img/sair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sair.setIcon(icon5)
        self.btn_sair.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_sair)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)


        self.retranslateUi(TelaSolucoes)

        QMetaObject.connectSlotsByName(TelaSolucoes)
    # setupUi

    def retranslateUi(self, TelaSolucoes):
        TelaSolucoes.setWindowTitle(QCoreApplication.translate("TelaSolucoes", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("TelaSolucoes", u"Identificador:", None))
        self.label_3.setText(QCoreApplication.translate("TelaSolucoes", u"Solu\u00e7\u00e3o:", None))
        self.label_4.setText(QCoreApplication.translate("TelaSolucoes", u"Descri\u00e7\u00e3o:", None))
        ___qtablewidgetitem = self.tabela_solucoes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TelaSolucoes", u"Identificador", None));
        ___qtablewidgetitem1 = self.tabela_solucoes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TelaSolucoes", u"Solu\u00e7\u00e3o", None));
        ___qtablewidgetitem2 = self.tabela_solucoes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TelaSolucoes", u"Descri\u00e7\u00e3o", None));
        self.btn_cadastrar.setText(QCoreApplication.translate("TelaSolucoes", u"Cadastrar", None))
        self.btn_limpar_tela.setText(QCoreApplication.translate("TelaSolucoes", u"Limpar tela", None))
        self.btn_excluir.setText(QCoreApplication.translate("TelaSolucoes", u"Excluir", None))
        self.label_5.setText("")
        self.btn_carregar.setText(QCoreApplication.translate("TelaSolucoes", u"Carregar", None))
        self.btn_sair.setText(QCoreApplication.translate("TelaSolucoes", u"Sair", None))
        self.label_6.setText("")
    # retranslateUi

