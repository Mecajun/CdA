# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'removerfuncionario.ui'
#
# Created: Thu Feb  6 01:16:33 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Remover_Funcionarios_Window(object):
    def setupUi(self, Remover_Funcionarios_Window):
        Remover_Funcionarios_Window.setObjectName("Remover_Funcionarios_Window")
        Remover_Funcionarios_Window.resize(277, 503)
        Remover_Funcionarios_Window.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.centralwidget = QtGui.QWidget(Remover_Funcionarios_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 258, 421))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.listView_funcionarios = QtGui.QListView(self.layoutWidget)
        self.listView_funcionarios.setObjectName("listView_funcionarios")
        self.verticalLayout_2.addWidget(self.listView_funcionarios)
        self.pushButton_remover_funcionario = QtGui.QPushButton(self.centralwidget)
        self.pushButton_remover_funcionario.setGeometry(QtCore.QRect(50, 440, 180, 27))
        self.pushButton_remover_funcionario.setObjectName("pushButton_remover_funcionario")
        Remover_Funcionarios_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Remover_Funcionarios_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 277, 25))
        self.menubar.setObjectName("menubar")
        Remover_Funcionarios_Window.setMenuBar(self.menubar)

        self.retranslateUi(Remover_Funcionarios_Window)
        QtCore.QMetaObject.connectSlotsByName(Remover_Funcionarios_Window)

    def retranslateUi(self, Remover_Funcionarios_Window):
        Remover_Funcionarios_Window.setWindowTitle(QtGui.QApplication.translate("Remover_Funcionarios_Window", "Remover Funcionarios", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Remover_Funcionarios_Window", "Funcionarios Cadastrados", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_remover_funcionario.setText(QtGui.QApplication.translate("Remover_Funcionarios_Window", "Remover Funcionario", None, QtGui.QApplication.UnicodeUTF8))

