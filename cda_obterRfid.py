# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'obterRfid.ui'
#
# Created: Mon Jul  7 12:25:52 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Obter_Rfid_Window(object):
    def setupUi(self, Obter_Rfid_Window):
        Obter_Rfid_Window.setObjectName("Obter_Rfid_Window")
        Obter_Rfid_Window.resize(383, 130)
        self.centralwidget = QtGui.QWidget(Obter_Rfid_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 381, 20))
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_Tempo = QtGui.QLabel(self.centralwidget)
        self.label_Tempo.setGeometry(QtCore.QRect(320, 80, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_Tempo.setFont(font)
        self.label_Tempo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Tempo.setObjectName("label_Tempo")
        self.pushButton_Cancelar = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Cancelar.setGeometry(QtCore.QRect(180, 90, 98, 27))
        self.pushButton_Cancelar.setObjectName("pushButton_Cancelar")
        self.pushButton_Salvar = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Salvar.setGeometry(QtCore.QRect(30, 90, 98, 27))
        self.pushButton_Salvar.setObjectName("pushButton_Salvar")
        self.label_RFID = QtGui.QLabel(self.centralwidget)
        self.label_RFID.setGeometry(QtCore.QRect(30, 50, 321, 17))
        self.label_RFID.setObjectName("label_RFID")
        Obter_Rfid_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Obter_Rfid_Window)
        QtCore.QMetaObject.connectSlotsByName(Obter_Rfid_Window)

    def retranslateUi(self, Obter_Rfid_Window):
        Obter_Rfid_Window.setWindowTitle(QtGui.QApplication.translate("Obter_Rfid_Window", "Obter RFID", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Obter_Rfid_Window", "Passe o cartão para obter o RFID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Tempo.setText(QtGui.QApplication.translate("Obter_Rfid_Window", "60", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Cancelar.setText(QtGui.QApplication.translate("Obter_Rfid_Window", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Salvar.setText(QtGui.QApplication.translate("Obter_Rfid_Window", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_RFID.setText(QtGui.QApplication.translate("Obter_Rfid_Window", "RFID = ", None, QtGui.QApplication.UnicodeUTF8))

