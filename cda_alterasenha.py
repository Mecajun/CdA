# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alterasenha.ui'
#
# Created: Mon Jul  7 12:25:52 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Altera_Senha_Window(object):
    def setupUi(self, Altera_Senha_Window):
        Altera_Senha_Window.setObjectName("Altera_Senha_Window")
        Altera_Senha_Window.resize(250, 220)
        Altera_Senha_Window.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.centralwidget = QtGui.QWidget(Altera_Senha_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 231, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_senha = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_senha.sizePolicy().hasHeightForWidth())
        self.lineEdit_senha.setSizePolicy(sizePolicy)
        self.lineEdit_senha.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.horizontalLayout.addWidget(self.lineEdit_senha)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_nova_senha_1 = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_nova_senha_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_nova_senha_1.setSizePolicy(sizePolicy)
        self.lineEdit_nova_senha_1.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_nova_senha_1.setObjectName("lineEdit_nova_senha_1")
        self.horizontalLayout_2.addWidget(self.lineEdit_nova_senha_1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_nova_senha_2 = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_nova_senha_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_nova_senha_2.setSizePolicy(sizePolicy)
        self.lineEdit_nova_senha_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_nova_senha_2.setObjectName("lineEdit_nova_senha_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_nova_senha_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButton_salvar = QtGui.QPushButton(self.widget)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        self.verticalLayout.addWidget(self.pushButton_salvar)
        Altera_Senha_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Altera_Senha_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 25))
        self.menubar.setObjectName("menubar")
        Altera_Senha_Window.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(Altera_Senha_Window)
        self.toolBar.setObjectName("toolBar")
        Altera_Senha_Window.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(Altera_Senha_Window)
        QtCore.QMetaObject.connectSlotsByName(Altera_Senha_Window)

    def retranslateUi(self, Altera_Senha_Window):
        Altera_Senha_Window.setWindowTitle(QtGui.QApplication.translate("Altera_Senha_Window", "Alterar Senha", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Altera_Senha_Window", "Senha", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Altera_Senha_Window", "Nova Senha", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Altera_Senha_Window", "Nova Senha", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_salvar.setText(QtGui.QApplication.translate("Altera_Senha_Window", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("Altera_Senha_Window", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

