# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_login.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_UiTelaLogin(object):
    def setupUi(self, UiTelaLogin):
        if not UiTelaLogin.objectName():
            UiTelaLogin.setObjectName(u"UiTelaLogin")
        UiTelaLogin.setWindowModality(Qt.NonModal)
        UiTelaLogin.setEnabled(True)
        UiTelaLogin.resize(408, 517)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UiTelaLogin.sizePolicy().hasHeightForWidth())
        UiTelaLogin.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"_img/logo_janela.ico", QSize(), QIcon.Normal, QIcon.Off)
        UiTelaLogin.setWindowIcon(icon)
        UiTelaLogin.setLayoutDirection(Qt.LeftToRight)
        UiTelaLogin.setAutoFillBackground(False)
        UiTelaLogin.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(UiTelaLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 210, 331, 261))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"_img/user.png"))

        self.horizontalLayout.addWidget(self.label)

        self.txt_login = QLineEdit(self.frame)
        self.txt_login.setObjectName(u"txt_login")
        self.txt_login.setEnabled(True)
        self.txt_login.setMinimumSize(QSize(0, 35))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.txt_login.setFont(font)
        self.txt_login.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid")
        self.txt_login.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.txt_login)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u"_img/password.png"))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.txt_senha = QLineEdit(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setMinimumSize(QSize(0, 35))
        self.txt_senha.setFont(font)
        self.txt_senha.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 5px")
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_senha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.txt_senha)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.bt_entrar = QPushButton(self.frame)
        self.bt_entrar.setObjectName(u"bt_entrar")
        self.bt_entrar.setMinimumSize(QSize(60, 35))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.bt_entrar.setFont(font1)
        self.bt_entrar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 255);\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-radius: 10px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"}")

        self.horizontalLayout_3.addWidget(self.bt_entrar)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.btn_sair = QPushButton(self.frame)
        self.btn_sair.setObjectName(u"btn_sair")
        self.btn_sair.setMinimumSize(QSize(0, 35))
        self.btn_sair.setFont(font1)
        self.btn_sair.setMouseTracking(False)
        self.btn_sair.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-radius: 10px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgb(0, 0, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_sair)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 411, 521))
        self.label_5.setPixmap(QPixmap(u"_img/logo_login.png"))
        UiTelaLogin.setCentralWidget(self.centralwidget)
        self.label_5.raise_()
        self.frame.raise_()

        self.retranslateUi(UiTelaLogin)

        QMetaObject.connectSlotsByName(UiTelaLogin)
    # setupUi

    def retranslateUi(self, UiTelaLogin):
        UiTelaLogin.setWindowTitle(QCoreApplication.translate("UiTelaLogin", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        UiTelaLogin.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label.setText("")
        self.txt_login.setPlaceholderText(QCoreApplication.translate("UiTelaLogin", u"Login", None))
        self.label_2.setText("")
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("UiTelaLogin", u"Senha", None))
        self.label_3.setText("")
        self.bt_entrar.setText(QCoreApplication.translate("UiTelaLogin", u"Entrar", None))
        self.label_4.setText("")
        self.label_6.setText("")
        self.btn_sair.setText(QCoreApplication.translate("UiTelaLogin", u"Sair", None))
        self.label_7.setText("")
        self.label_5.setText("")
    # retranslateUi

