# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'horarios.ui'
#
# Created: Thu Feb  6 01:16:33 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Horarios_Window(object):
    def setupUi(self, Horarios_Window):
        Horarios_Window.setObjectName("Horarios_Window")
        Horarios_Window.resize(640, 594)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Horarios_Window.sizePolicy().hasHeightForWidth())
        Horarios_Window.setSizePolicy(sizePolicy)
        Horarios_Window.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.centralwidget = QtGui.QWidget(Horarios_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView_horarios = QtGui.QTableView(self.centralwidget)
        self.tableView_horarios.setGeometry(QtCore.QRect(10, 10, 621, 571))
        self.tableView_horarios.setObjectName("tableView_horarios")
        Horarios_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Horarios_Window)
        QtCore.QMetaObject.connectSlotsByName(Horarios_Window)

    def retranslateUi(self, Horarios_Window):
        Horarios_Window.setWindowTitle(QtGui.QApplication.translate("Horarios_Window", "Horarios", None, QtGui.QApplication.UnicodeUTF8))

