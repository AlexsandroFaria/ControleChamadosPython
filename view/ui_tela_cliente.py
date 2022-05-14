# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_tela_cliente.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Cliente(object):
    def setupUi(self, Cliente):
        if not Cliente.objectName():
            Cliente.setObjectName(u"Cliente")
        Cliente.resize(823, 635)
        icon = QIcon()
        icon.addFile(u"../../ChamadosSimpress/_img/logo_janela.ico", QSize(), QIcon.Normal, QIcon.Off)
        Cliente.setWindowIcon(icon)
        Cliente.setStyleSheet(u"\n"
"background-color: rgba(227, 227, 227, 227);")
        self.frame = QFrame(Cliente)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 801, 121))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 791, 101))
        self.label.setPixmap(QPixmap(u"../../ChamadosSimpress/_img/banner_cliente.png"))
        self.frame_2 = QFrame(Cliente)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 140, 801, 471))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.tab_widget_cliente = QTabWidget(self.frame_2)
        self.tab_widget_cliente.setObjectName(u"tab_widget_cliente")
        self.tab_widget_cliente.setGeometry(QRect(10, 10, 771, 461))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tab_widget_cliente.setFont(font)
        self.tab_widget_cliente.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"")
        self.tab_widget_cliente.setTabShape(QTabWidget.Rounded)
        self.tab_widget_cliente.setIconSize(QSize(24, 24))
        self.tab_widget_cliente.setTabsClosable(False)
        self.tab_cliente = QWidget()
        self.tab_cliente.setObjectName(u"tab_cliente")
        self.label_7 = QLabel(self.tab_cliente)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 270, 71, 16))
        self.label_7.setFont(font)
        self.label_4 = QLabel(self.tab_cliente)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 150, 71, 16))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.tab_cliente)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 190, 71, 16))
        self.label_5.setFont(font)
        self.label_3 = QLabel(self.tab_cliente)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 115, 71, 16))
        self.label_3.setFont(font)
        self.label_6 = QLabel(self.tab_cliente)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 230, 71, 16))
        self.label_6.setFont(font)
        self.txt_nome = QLineEdit(self.tab_cliente)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(110, 110, 361, 25))
        self.txt_nome.setMinimumSize(QSize(0, 25))
        self.txt_nome.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.txt_endereco = QLineEdit(self.tab_cliente)
        self.txt_endereco.setObjectName(u"txt_endereco")
        self.txt_endereco.setGeometry(QRect(110, 150, 361, 25))
        self.txt_endereco.setMinimumSize(QSize(0, 25))
        self.txt_endereco.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.txt_contato = QLineEdit(self.tab_cliente)
        self.txt_contato.setObjectName(u"txt_contato")
        self.txt_contato.setGeometry(QRect(110, 190, 361, 25))
        self.txt_contato.setMinimumSize(QSize(0, 25))
        self.txt_contato.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.txt_telefone = QLineEdit(self.tab_cliente)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setGeometry(QRect(110, 230, 361, 25))
        self.txt_telefone.setMinimumSize(QSize(0, 25))
        self.txt_telefone.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.txt_email = QLineEdit(self.tab_cliente)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(110, 270, 361, 25))
        self.txt_email.setMinimumSize(QSize(0, 25))
        self.txt_email.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.btn_limpar_tela = QPushButton(self.tab_cliente)
        self.btn_limpar_tela.setObjectName(u"btn_limpar_tela")
        self.btn_limpar_tela.setGeometry(QRect(210, 60, 171, 35))
        self.btn_limpar_tela.setMinimumSize(QSize(0, 35))
        self.btn_limpar_tela.setFont(font)
        self.btn_limpar_tela.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 5px;\n"
"	border:1px solid 5px\n"
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
        self.btn_cadastrar_chamado = QPushButton(self.tab_cliente)
        self.btn_cadastrar_chamado.setObjectName(u"btn_cadastrar_chamado")
        self.btn_cadastrar_chamado.setGeometry(QRect(400, 60, 171, 35))
        self.btn_cadastrar_chamado.setMinimumSize(QSize(0, 35))
        self.btn_cadastrar_chamado.setFont(font)
        self.btn_cadastrar_chamado.setStyleSheet(u"QPushButton{\n"
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
        icon2 = QIcon()
        icon2.addFile(u"../../ChamadosSimpress/_img/cadastro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar_chamado.setIcon(icon2)
        self.btn_cadastrar_chamado.setIconSize(QSize(24, 24))
        self.label_8 = QLabel(self.tab_cliente)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(500, 70, 261, 241))
        self.label_8.setPixmap(QPixmap(u"../../ChamadosSimpress/_img/figura_clientes.png"))
        self.label_9 = QLabel(self.tab_cliente)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 70, 71, 16))
        self.label_9.setFont(font)
        self.txt_contrato = QLineEdit(self.tab_cliente)
        self.txt_contrato.setObjectName(u"txt_contrato")
        self.txt_contrato.setGeometry(QRect(110, 70, 81, 25))
        self.txt_contrato.setMinimumSize(QSize(0, 25))
        self.txt_contrato.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.frame_3 = QFrame(self.tab_cliente)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 330, 701, 51))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_salvar = QPushButton(self.frame_3)
        self.btn_salvar.setObjectName(u"btn_salvar")
        self.btn_salvar.setMinimumSize(QSize(0, 35))
        self.btn_salvar.setFont(font)
        self.btn_salvar.setStyleSheet(u"QPushButton{\n"
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
        icon3.addFile(u"../../ChamadosSimpress/_img/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salvar.setIcon(icon3)
        self.btn_salvar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_salvar)

        self.btn_alterar = QPushButton(self.frame_3)
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
        icon4 = QIcon()
        icon4.addFile(u"../../ChamadosSimpress/_img/alterar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar.setIcon(icon4)
        self.btn_alterar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_3)
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
        icon5 = QIcon()
        icon5.addFile(u"../../ChamadosSimpress/_img/excluir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir.setIcon(icon5)
        self.btn_excluir.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_excluir)

        self.btn_fechar = QPushButton(self.frame_3)
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
        icon6 = QIcon()
        icon6.addFile(u"../../ChamadosSimpress/_img/sair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fechar.setIcon(icon6)
        self.btn_fechar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_fechar)

        icon7 = QIcon()
        icon7.addFile(u"../../ChamadosSimpress/_img/cliente.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_widget_cliente.addTab(self.tab_cliente, icon7, "")
        self.label_8.raise_()
        self.label_7.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.txt_nome.raise_()
        self.txt_endereco.raise_()
        self.txt_contato.raise_()
        self.txt_telefone.raise_()
        self.txt_email.raise_()
        self.btn_limpar_tela.raise_()
        self.btn_cadastrar_chamado.raise_()
        self.label_9.raise_()
        self.txt_contrato.raise_()
        self.frame_3.raise_()
        self.tab_cliente_consulta = QWidget()
        self.tab_cliente_consulta.setObjectName(u"tab_cliente_consulta")
        self.tabela_clientes = QTableWidget(self.tab_cliente_consulta)
        if (self.tabela_clientes.columnCount() < 6):
            self.tabela_clientes.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tabela_clientes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tabela_clientes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tabela_clientes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tabela_clientes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.tabela_clientes.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.tabela_clientes.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tabela_clientes.setObjectName(u"tabela_clientes")
        self.tabela_clientes.setGeometry(QRect(10, 111, 741, 221))
        self.tabela_clientes.verticalHeader().setVisible(False)
        self.groupBox = QGroupBox(self.tab_cliente_consulta)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 331, 71))
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"border-color: rgb(0, 0, 255);\n"
"border:1px solid gray")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.btn_consulta_contrato = QPushButton(self.groupBox)
        self.btn_consulta_contrato.setObjectName(u"btn_consulta_contrato")
        self.btn_consulta_contrato.setGeometry(QRect(200, 20, 121, 41))
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
        icon8 = QIcon()
        icon8.addFile(u"../../ChamadosSimpress/_img/consulta.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_consulta_contrato.setIcon(icon8)
        self.btn_consulta_contrato.setIconSize(QSize(24, 24))
        self.txt_consultar_contrato = QLineEdit(self.groupBox)
        self.txt_consultar_contrato.setObjectName(u"txt_consultar_contrato")
        self.txt_consultar_contrato.setGeometry(QRect(10, 30, 171, 25))
        self.txt_consultar_contrato.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setPointSize(10)
        self.txt_consultar_contrato.setFont(font1)
        self.groupBox_2 = QGroupBox(self.tab_cliente_consulta)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(420, 20, 331, 71))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"border-color: rgb(0, 0, 255);\n"
"border:1px solid gray")
        self.txt_consulta_nome = QLineEdit(self.groupBox_2)
        self.txt_consulta_nome.setObjectName(u"txt_consulta_nome")
        self.txt_consulta_nome.setGeometry(QRect(10, 30, 171, 25))
        self.txt_consulta_nome.setMinimumSize(QSize(0, 25))
        self.txt_consulta_nome.setFont(font1)
        self.btn_consulta_nome = QPushButton(self.groupBox_2)
        self.btn_consulta_nome.setObjectName(u"btn_consulta_nome")
        self.btn_consulta_nome.setGeometry(QRect(200, 20, 121, 41))
        self.btn_consulta_nome.setFont(font)
        self.btn_consulta_nome.setStyleSheet(u"QPushButton{\n"
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
        self.btn_consulta_nome.setIcon(icon8)
        self.btn_consulta_nome.setIconSize(QSize(24, 24))
        self.frame_4 = QFrame(self.tab_cliente_consulta)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(19, 340, 731, 55))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

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
        icon9 = QIcon()
        icon9.addFile(u"../../ChamadosSimpress/_img/pesquisa_chamado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar_tabela.setIcon(icon9)
        self.btn_carregar_tabela.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_carregar_tabela)

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
        icon10 = QIcon()
        icon10.addFile(u"../../ChamadosSimpress/_img/carregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar.setIcon(icon10)
        self.btn_carregar.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_carregar)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_2.addWidget(self.label_11)

        self.tab_widget_cliente.addTab(self.tab_cliente_consulta, icon8, "")

        self.retranslateUi(Cliente)

        self.tab_widget_cliente.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Cliente)
    # setupUi

    def retranslateUi(self, Cliente):
        Cliente.setWindowTitle(QCoreApplication.translate("Cliente", u"Form", None))
        self.label.setText("")
        self.label_7.setText(QCoreApplication.translate("Cliente", u"<html><head/><body><p align=\"right\">E-mail:</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Cliente", u"<html><head/><body><p align=\"right\">Endere\u00e7o:</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Cliente", u"<html><head/><body><p align=\"right\">Contato:</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Cliente", u"<html><head/><body><p align=\"right\">Nome:</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Cliente", u"<html><head/><body><p align=\"right\">Telefone:</p></body></html>", None))
        self.btn_limpar_tela.setText(QCoreApplication.translate("Cliente", u"Limpar tela", None))
        self.btn_cadastrar_chamado.setText(QCoreApplication.translate("Cliente", u"Cadastrar Chamado", None))
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("Cliente", u"Contrato:", None))
        self.btn_salvar.setText(QCoreApplication.translate("Cliente", u"Salvar", None))
        self.btn_alterar.setText(QCoreApplication.translate("Cliente", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("Cliente", u"Excluir", None))
        self.btn_fechar.setText(QCoreApplication.translate("Cliente", u"Fechar", None))
        self.tab_widget_cliente.setTabText(self.tab_widget_cliente.indexOf(self.tab_cliente), QCoreApplication.translate("Cliente", u"Cliente", None))
        ___qtablewidgetitem = self.tabela_clientes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Cliente", u"Contrato", None));
        ___qtablewidgetitem1 = self.tabela_clientes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Cliente", u"Nome", None));
        ___qtablewidgetitem2 = self.tabela_clientes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Cliente", u"Endere\u00e7o", None));
        ___qtablewidgetitem3 = self.tabela_clientes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Cliente", u"Contato", None));
        ___qtablewidgetitem4 = self.tabela_clientes.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Cliente", u"Telefone", None));
        ___qtablewidgetitem5 = self.tabela_clientes.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Cliente", u"E-mail", None));
        self.groupBox.setTitle(QCoreApplication.translate("Cliente", u"Consultar por N Contrato", None))
        self.btn_consulta_contrato.setText(QCoreApplication.translate("Cliente", u"Consultar", None))
        self.txt_consultar_contrato.setPlaceholderText(QCoreApplication.translate("Cliente", u"Consultar Contrato", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Cliente", u"Consulta por nome", None))
        self.txt_consulta_nome.setPlaceholderText(QCoreApplication.translate("Cliente", u"Consulta por Nome", None))
        self.btn_consulta_nome.setText(QCoreApplication.translate("Cliente", u"Consultar", None))
        self.label_10.setText("")
        self.btn_carregar_tabela.setText(QCoreApplication.translate("Cliente", u"Carregar Tabela", None))
        self.btn_carregar.setText(QCoreApplication.translate("Cliente", u"Carregar Item", None))
        self.label_11.setText("")
        self.tab_widget_cliente.setTabText(self.tab_widget_cliente.indexOf(self.tab_cliente_consulta), QCoreApplication.translate("Cliente", u"Consulta de Clientes", None))
    # retranslateUi

