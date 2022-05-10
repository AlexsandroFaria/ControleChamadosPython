# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_usuarios.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Usuarios(object):
    def setupUi(self, Usuarios):
        if not Usuarios.objectName():
            Usuarios.setObjectName(u"Usuarios")
        Usuarios.resize(768, 644)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Usuarios.sizePolicy().hasHeightForWidth())
        Usuarios.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"../../ChamadosSimpress/_img/logo_janela.ico", QSize(), QIcon.Normal, QIcon.Off)
        Usuarios.setWindowIcon(icon)
        Usuarios.setStyleSheet(u"background-color: rgb(227, 227, 227);")
        self.centralwidget = QWidget(Usuarios)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"text-shadow: #000 2px 3px 2px;")
        self.label.setPixmap(QPixmap(u"../../../ChamadosSimpress/_img/banner_usuario.png"))

        self.verticalLayout_5.addWidget(self.label)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 25))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 25))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 25))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 25))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 25))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_7)


        self.horizontalLayout.addWidget(self.frame_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txt_id = QLineEdit(self.frame_4)
        self.txt_id.setObjectName(u"txt_id")
        self.txt_id.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.txt_id.sizePolicy().hasHeightForWidth())
        self.txt_id.setSizePolicy(sizePolicy1)
        self.txt_id.setMinimumSize(QSize(30, 25))
        font1 = QFont()
        font1.setPointSize(10)
        self.txt_id.setFont(font1)
        self.txt_id.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(197, 197, 197);\n"
"border:1px solid")

        self.verticalLayout_2.addWidget(self.txt_id)

        self.txt_nome_completo = QLineEdit(self.frame_4)
        self.txt_nome_completo.setObjectName(u"txt_nome_completo")
        self.txt_nome_completo.setMinimumSize(QSize(0, 25))
        self.txt_nome_completo.setFont(font1)
        self.txt_nome_completo.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")

        self.verticalLayout_2.addWidget(self.txt_nome_completo)

        self.txt_login = QLineEdit(self.frame_4)
        self.txt_login.setObjectName(u"txt_login")
        self.txt_login.setMinimumSize(QSize(0, 25))
        self.txt_login.setFont(font1)
        self.txt_login.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")

        self.verticalLayout_2.addWidget(self.txt_login)

        self.txt_senha = QLineEdit(self.frame_4)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setMinimumSize(QSize(0, 25))
        self.txt_senha.setFont(font1)
        self.txt_senha.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.txt_senha)

        self.txt_confirmar_senha = QLineEdit(self.frame_4)
        self.txt_confirmar_senha.setObjectName(u"txt_confirmar_senha")
        self.txt_confirmar_senha.setMinimumSize(QSize(0, 25))
        self.txt_confirmar_senha.setFont(font1)
        self.txt_confirmar_senha.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")
        self.txt_confirmar_senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.txt_confirmar_senha)

        self.combo_perfil = QComboBox(self.frame_4)
        self.combo_perfil.addItem("")
        self.combo_perfil.addItem("")
        self.combo_perfil.setObjectName(u"combo_perfil")
        sizePolicy1.setHeightForWidth(self.combo_perfil.sizePolicy().hasHeightForWidth())
        self.combo_perfil.setSizePolicy(sizePolicy1)
        self.combo_perfil.setMinimumSize(QSize(150, 25))
        self.combo_perfil.setFont(font1)
        self.combo_perfil.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid")

        self.verticalLayout_2.addWidget(self.combo_perfil)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.btn_salvar = QPushButton(self.frame_5)
        self.btn_salvar.setObjectName(u"btn_salvar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_salvar.sizePolicy().hasHeightForWidth())
        self.btn_salvar.setSizePolicy(sizePolicy2)
        self.btn_salvar.setMinimumSize(QSize(0, 40))
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
        icon1 = QIcon()
        icon1.addFile(u"../../ChamadosSimpress/_img/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salvar.setIcon(icon1)
        self.btn_salvar.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.btn_salvar)

        self.btn_alterar = QPushButton(self.frame_5)
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
        icon2 = QIcon()
        icon2.addFile(u"../../ChamadosSimpress/_img/alterar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar.setIcon(icon2)
        self.btn_alterar.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.btn_alterar)

        self.btn_limpar_tela = QPushButton(self.frame_5)
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
        icon3.addFile(u"../../ChamadosSimpress/_img/limpar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_tela.setIcon(icon3)
        self.btn_limpar_tela.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.btn_limpar_tela)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabela_usuarios = QTableWidget(self.frame_2)
        if (self.tabela_usuarios.columnCount() < 5):
            self.tabela_usuarios.setColumnCount(5)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.tabela_usuarios.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tabela_usuarios.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.tabela_usuarios.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.tabela_usuarios.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.tabela_usuarios.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabela_usuarios.setObjectName(u"tabela_usuarios")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tabela_usuarios.sizePolicy().hasHeightForWidth())
        self.tabela_usuarios.setSizePolicy(sizePolicy3)
        self.tabela_usuarios.setFont(font1)
        self.tabela_usuarios.setFrameShape(QFrame.Box)
        self.tabela_usuarios.verticalHeader().setVisible(False)

        self.horizontalLayout_2.addWidget(self.tabela_usuarios)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy4)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_carregar = QPushButton(self.frame_6)
        self.btn_carregar.setObjectName(u"btn_carregar")
        self.btn_carregar.setMinimumSize(QSize(0, 40))
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
        icon4 = QIcon()
        icon4.addFile(u"../../ChamadosSimpress/_img/carregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar.setIcon(icon4)
        self.btn_carregar.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.btn_carregar)

        self.btn_excluir = QPushButton(self.frame_6)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(0, 40))
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

        self.verticalLayout_3.addWidget(self.btn_excluir)

        self.btn_sair = QPushButton(self.frame_6)
        self.btn_sair.setObjectName(u"btn_sair")
        sizePolicy2.setHeightForWidth(self.btn_sair.sizePolicy().hasHeightForWidth())
        self.btn_sair.setSizePolicy(sizePolicy2)
        self.btn_sair.setMinimumSize(QSize(0, 40))
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
        icon6 = QIcon()
        icon6.addFile(u"../../ChamadosSimpress/_img/sair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sair.setIcon(icon6)
        self.btn_sair.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.btn_sair)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_6.addWidget(self.frame_2)

        Usuarios.setCentralWidget(self.centralwidget)

        self.retranslateUi(Usuarios)

        QMetaObject.connectSlotsByName(Usuarios)
    # setupUi

    def retranslateUi(self, Usuarios):
        Usuarios.setWindowTitle(QCoreApplication.translate("Usuarios", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Usuarios", u"ID:", None))
        self.label_3.setText(QCoreApplication.translate("Usuarios", u"Nome conpleto:", None))
        self.label_4.setText(QCoreApplication.translate("Usuarios", u"Login:", None))
        self.label_5.setText(QCoreApplication.translate("Usuarios", u"Senha:", None))
        self.label_6.setText(QCoreApplication.translate("Usuarios", u"Confirmar Senha:", None))
        self.label_7.setText(QCoreApplication.translate("Usuarios", u"Perfil:", None))
        self.txt_nome_completo.setPlaceholderText("")
        self.txt_login.setPlaceholderText("")
        self.txt_confirmar_senha.setPlaceholderText(QCoreApplication.translate("Usuarios", u"Confirmar Senha", None))
        self.combo_perfil.setItemText(0, QCoreApplication.translate("Usuarios", u"Usu\u00e1rio", None))
        self.combo_perfil.setItemText(1, QCoreApplication.translate("Usuarios", u"Administrador", None))

        self.label_8.setText("")
        self.btn_salvar.setText(QCoreApplication.translate("Usuarios", u"Salvar", None))
        self.btn_alterar.setText(QCoreApplication.translate("Usuarios", u"Alterar", None))
        self.btn_limpar_tela.setText(QCoreApplication.translate("Usuarios", u"Limpar Campos", None))
        self.label_9.setText("")
        ___qtablewidgetitem = self.tabela_usuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Usuarios", u"ID", None));
        ___qtablewidgetitem1 = self.tabela_usuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Usuarios", u"Nome", None));
        ___qtablewidgetitem2 = self.tabela_usuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Usuarios", u"Usuario", None));
        ___qtablewidgetitem3 = self.tabela_usuarios.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Usuarios", u"Senha", None));
        ___qtablewidgetitem4 = self.tabela_usuarios.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Usuarios", u"Perfil", None));
        self.btn_carregar.setText(QCoreApplication.translate("Usuarios", u"carregar", None))
        self.btn_excluir.setText(QCoreApplication.translate("Usuarios", u"Excluir", None))
        self.btn_sair.setText(QCoreApplication.translate("Usuarios", u"Sair", None))
    # retranslateUi

