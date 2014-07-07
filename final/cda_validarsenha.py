# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'validarsenha.ui'
#
# Created: Mon Jul  7 12:25:53 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Adm_Senha_Window(object):
    def setupUi(self, Adm_Senha_Window):
        Adm_Senha_Window.setObjectName("Adm_Senha_Window")
        Adm_Senha_Window.resize(268, 92)
        self.centralwidget = QtGui.QWidget(Adm_Senha_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 20, 211, 61))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_senha = QtGui.QLineEdit(self.widget)
        self.lineEdit_senha.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.lineEdit_senha.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.verticalLayout.addWidget(self.lineEdit_senha)
        Adm_Senha_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Adm_Senha_Window)
        QtCore.QMetaObject.connectSlotsByName(Adm_Senha_Window)

    def retranslateUi(self, Adm_Senha_Window):
        Adm_Senha_Window.setWindowTitle(QtGui.QApplication.translate("Adm_Senha_Window", "Validar Senha", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Adm_Senha_Window", "Digite a senha de administrador", None, QtGui.QApplication.UnicodeUTF8))

