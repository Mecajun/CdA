# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'relatorios.ui'
#
# Created: Sat Dec 14 23:43:29 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Relatorios_Window(object):
    def setupUi(self, Relatorios_Window):
        Relatorios_Window.setObjectName("Relatorios_Window")
        Relatorios_Window.resize(442, 243)
        self.centralwidget = QtGui.QWidget(Relatorios_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 181, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.dateTimeEdit_inicial = QtGui.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit_inicial.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.dateTimeEdit_inicial.setObjectName("dateTimeEdit_inicial")
        self.verticalLayout.addWidget(self.dateTimeEdit_inicial)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.dateTimeEdit_final = QtGui.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit_final.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.dateTimeEdit_final.setObjectName("dateTimeEdit_final")
        self.verticalLayout.addWidget(self.dateTimeEdit_final)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(240, 60, 188, 101))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_pontuais = QtGui.QCheckBox(self.layoutWidget1)
        self.checkBox_pontuais.setObjectName("checkBox_pontuais")
        self.verticalLayout_2.addWidget(self.checkBox_pontuais)
        self.checkBox_faltosos = QtGui.QCheckBox(self.layoutWidget1)
        self.checkBox_faltosos.setObjectName("checkBox_faltosos")
        self.verticalLayout_2.addWidget(self.checkBox_faltosos)
        self.checkBox_atrasados = QtGui.QCheckBox(self.layoutWidget1)
        self.checkBox_atrasados.setObjectName("checkBox_atrasados")
        self.verticalLayout_2.addWidget(self.checkBox_atrasados)
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 180, 421, 29))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_log_porta = QtGui.QPushButton(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_log_porta.sizePolicy().hasHeightForWidth())
        self.pushButton_log_porta.setSizePolicy(sizePolicy)
        self.pushButton_log_porta.setObjectName("pushButton_log_porta")
        self.horizontalLayout.addWidget(self.pushButton_log_porta)
        self.pushButton_relatorio_pontos = QtGui.QPushButton(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_relatorio_pontos.sizePolicy().hasHeightForWidth())
        self.pushButton_relatorio_pontos.setSizePolicy(sizePolicy)
        self.pushButton_relatorio_pontos.setObjectName("pushButton_relatorio_pontos")
        self.horizontalLayout.addWidget(self.pushButton_relatorio_pontos)
        Relatorios_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Relatorios_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 25))
        self.menubar.setObjectName("menubar")
        Relatorios_Window.setMenuBar(self.menubar)

        self.retranslateUi(Relatorios_Window)
        QtCore.QMetaObject.connectSlotsByName(Relatorios_Window)

    def retranslateUi(self, Relatorios_Window):
        Relatorios_Window.setWindowTitle(QtGui.QApplication.translate("Relatorios_Window", "Relatorios", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Relatorios_Window", "Data Inicial", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Relatorios_Window", "Data Final", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_pontuais.setText(QtGui.QApplication.translate("Relatorios_Window", "Funcionarios Pontuais", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_faltosos.setText(QtGui.QApplication.translate("Relatorios_Window", "Funcionarios Faltosos", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_atrasados.setText(QtGui.QApplication.translate("Relatorios_Window", "Funcionarios Atrasados", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_log_porta.setText(QtGui.QApplication.translate("Relatorios_Window", "Gerar Logs da Porta", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_relatorio_pontos.setText(QtGui.QApplication.translate("Relatorios_Window", "Gerar Relatorio Pontos", None, QtGui.QApplication.UnicodeUTF8))

