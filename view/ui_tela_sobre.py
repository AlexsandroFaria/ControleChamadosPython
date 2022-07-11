# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_sobre.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Sobre(object):
    def setupUi(self, Sobre):
        if not Sobre.objectName():
            Sobre.setObjectName(u"Sobre")
        Sobre.resize(400, 564)
        icon = QIcon()
        icon.addFile(u"_img/logo_janela.ico", QSize(), QIcon.Normal, QIcon.Off)
        Sobre.setWindowIcon(icon)
        self.label = QLabel(Sobre)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 381, 251))
        self.label.setFrameShape(QFrame.Panel)
        self.label.setPixmap(QPixmap(u"_img/sobre.png"))
        self.frame = QFrame(Sobre)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 270, 381, 231))
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(2)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 361, 21))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 60, 361, 20))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(16, 90, 351, 71))
        self.label_4.setMouseTracking(True)
        self.label_4.setTabletTracking(False)
        self.label_4.setAcceptDrops(False)
        self.label_4.setAutoFillBackground(False)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 180, 361, 20))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 200, 361, 20))
        self.btn_fechar = QPushButton(Sobre)
        self.btn_fechar.setObjectName(u"btn_fechar")
        self.btn_fechar.setGeometry(QRect(310, 530, 75, 23))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_fechar.setFont(font1)

        self.retranslateUi(Sobre)

        QMetaObject.connectSlotsByName(Sobre)
    # setupUi

    def retranslateUi(self, Sobre):
        Sobre.setWindowTitle(QCoreApplication.translate("Sobre", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Sobre", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#7d7d7d;\">Controle de Chamado Simpress</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Sobre", u"Vers\u00e3o: 2.0", None))
        self.label_4.setText(QCoreApplication.translate("Sobre", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">OBS: Aplicativo construido para uso Pessoal, </span></p><p align=\"center\"><span style=\" font-size:10pt;\">n\u00e3o sendo responsabilizado por uso de terceiros.</span></p><p align=\"center\"><span style=\" font-size:10pt;\">Aplicativo n\u00e3o comercial.</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Sobre", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Criado por: Alexsandro Luiz de Faria</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Sobre", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Contato: alexsandro.lfaria@gmail.com</span></p></body></html>", None))
        self.btn_fechar.setText(QCoreApplication.translate("Sobre", u"Fechar", None))
    # retranslateUi

