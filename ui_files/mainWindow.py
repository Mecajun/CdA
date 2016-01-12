# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Fri Dec  6 20:36:30 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Controle_De_Acesso_Window(object):
    def setupUi(self, Controle_De_Acesso_Window):
        Controle_De_Acesso_Window.setObjectName("Controle_De_Acesso_Window")
        Controle_De_Acesso_Window.resize(599, 292)
        Controle_De_Acesso_Window.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.centralwidget = QtGui.QWidget(Controle_De_Acesso_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_logo = QtGui.QWidget(self.centralwidget)
        self.widget_logo.setGeometry(QtCore.QRect(20, 10, 201, 121))
        self.widget_logo.setObjectName("widget_logo")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(240, 10, 341, 231))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_empresa = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_empresa.setFont(font)
        self.label_empresa.setAlignment(QtCore.Qt.AlignCenter)
        self.label_empresa.setObjectName("label_empresa")
        self.verticalLayout.addWidget(self.label_empresa)
        self.label_descricao = QtGui.QLabel(self.widget)
        self.label_descricao.setAlignment(QtCore.Qt.AlignCenter)
        self.label_descricao.setObjectName("label_descricao")
        self.verticalLayout.addWidget(self.label_descricao)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_matricula = QtGui.QLabel(self.widget)
        self.label_matricula.setObjectName("label_matricula")
        self.horizontalLayout.addWidget(self.label_matricula)
        self.lineEdit_matricula = QtGui.QLineEdit(self.widget)
        self.lineEdit_matricula.setObjectName("lineEdit_matricula")
        self.horizontalLayout.addWidget(self.lineEdit_matricula)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_funcionarios = QtGui.QLabel(self.widget)
        self.label_funcionarios.setObjectName("label_funcionarios")
        self.verticalLayout.addWidget(self.label_funcionarios)
        self.listView_funcionarios_horarios = QtGui.QListView(self.widget)
        self.listView_funcionarios_horarios.setObjectName("listView_funcionarios_horarios")
        self.verticalLayout.addWidget(self.listView_funcionarios_horarios)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(30, 140, 181, 101))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_relogio = QtGui.QLabel(self.widget1)
        self.label_relogio.setAlignment(QtCore.Qt.AlignCenter)
        self.label_relogio.setObjectName("label_relogio")
        self.verticalLayout_2.addWidget(self.label_relogio)
        self.pushButton_horarios = QtGui.QPushButton(self.widget1)
        self.pushButton_horarios.setObjectName("pushButton_horarios")
        self.verticalLayout_2.addWidget(self.pushButton_horarios)
        Controle_De_Acesso_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Controle_De_Acesso_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 25))
        self.menubar.setObjectName("menubar")
        Controle_De_Acesso_Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Controle_De_Acesso_Window)
        self.statusbar.setObjectName("statusbar")
        Controle_De_Acesso_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Controle_De_Acesso_Window)
        QtCore.QMetaObject.connectSlotsByName(Controle_De_Acesso_Window)

    def retranslateUi(self, Controle_De_Acesso_Window):
        Controle_De_Acesso_Window.setWindowTitle(QtGui.QApplication.translate("Controle_De_Acesso_Window", "Controle de Acesso", None, QtGui.QApplication.UnicodeUTF8))
        self.label_empresa.setText(QtGui.QApplication.translate("Controle_De_Acesso_Window", "Mecajun\n"
"Mecatrônica Júnior de Brasília", None, QtGui.QApplication.UnicodeUTF8))
        self.label_descricao.setText(QtGui.QApplication.translate("Controle_De_Acesso_Window", "Digite sua matrícula e aperte \"Enter\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_matricula.setText(QtGui.QApplication.translate("Controle_De_Acesso_Window", "Matricula:     ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_funcionarios.setText(QtGui.QApplication.translate("Controle_De_Acesso_Window", "Funcionarios do horario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_relogio.setText(QtGui.QApplication.translate("Controle_De_Acesso_Window", "00:00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_horarios.setText(QtGui.QApplication.translate("Controle_De_Acesso_Window", "Horarios", None, QtGui.QApplication.UnicodeUTF8))

