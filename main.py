from PySide2.QtWidgets import QApplication
from view.tela_login import TelaLogin
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tela_login = TelaLogin()
    tela_login.show()

    app.exec_()
