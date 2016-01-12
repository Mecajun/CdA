# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Fri Dec  6 16:52:27 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ControleDeAcesso(object):
    def setupUi(self, ControleDeAcesso):
        
        logo = QtGui.QPixmap("logo.png")

        ControleDeAcesso.setObjectName(_fromUtf8("ControleDeAcesso"))
        ControleDeAcesso.resize(599, 292)
        self.centralwidget = QtGui.QWidget(ControleDeAcesso)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget_logo = QtGui.QLabel(self.centralwidget)
        self.widget_logo.setGeometry(QtCore.QRect(20, 10, 201, 121))
        self.widget_logo.setObjectName(_fromUtf8("widget_logo"))
        self.widget_logo.setPixmap(logo)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(240, 10, 341, 231))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_empresa = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_empresa.setFont(font)
        self.label_empresa.setAlignment(QtCore.Qt.AlignCenter)
        self.label_empresa.setObjectName(_fromUtf8("label_empresa"))
        self.verticalLayout.addWidget(self.label_empresa)
        self.label_descricao = QtGui.QLabel(self.widget)
        self.label_descricao.setAlignment(QtCore.Qt.AlignCenter)
        self.label_descricao.setObjectName(_fromUtf8("label_descricao"))
        self.verticalLayout.addWidget(self.label_descricao)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_matricula = QtGui.QLabel(self.widget)
        self.label_matricula.setObjectName(_fromUtf8("label_matricula"))
        self.horizontalLayout.addWidget(self.label_matricula)
        self.lineEdit_matricula = QtGui.QLineEdit(self.widget)
        self.lineEdit_matricula.setObjectName(_fromUtf8("lineEdit_matricula"))
        self.horizontalLayout.addWidget(self.lineEdit_matricula)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_funcionarios = QtGui.QLabel(self.widget)
        self.label_funcionarios.setObjectName(_fromUtf8("label_funcionarios"))
        self.verticalLayout.addWidget(self.label_funcionarios)
        self.listView_funcionarios_horarios = QtGui.QListView(self.widget)
        self.listView_funcionarios_horarios.setObjectName(_fromUtf8("listView_funcionarios_horarios"))
        self.verticalLayout.addWidget(self.listView_funcionarios_horarios)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(30, 140, 171, 101))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_relogio = QtGui.QLabel(self.widget1)
        self.label_relogio.setAlignment(QtCore.Qt.AlignCenter)
        self.label_relogio.setObjectName(_fromUtf8("label_relogio"))
        self.verticalLayout_2.addWidget(self.label_relogio)
        self.pushButton_Administracao = QtGui.QPushButton(self.widget1)
        self.pushButton_Administracao.setObjectName(_fromUtf8("pushButton_Administracao"))
        self.verticalLayout_2.addWidget(self.pushButton_Administracao)
        self.pushButton_horarios = QtGui.QPushButton(self.widget1)
        self.pushButton_horarios.setObjectName(_fromUtf8("pushButton_horarios"))
        self.verticalLayout_2.addWidget(self.pushButton_horarios)
        ControleDeAcesso.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ControleDeAcesso)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        ControleDeAcesso.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ControleDeAcesso)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ControleDeAcesso.setStatusBar(self.statusbar)

        self.retranslateUi(ControleDeAcesso)
        QtCore.QMetaObject.connectSlotsByName(ControleDeAcesso)

    def retranslateUi(self, ControleDeAcesso):
        ControleDeAcesso.setWindowTitle(QtGui.QApplication.translate("ControleDeAcesso", "Controle de Acesso", None, QtGui.QApplication.UnicodeUTF8))
        self.label_empresa.setText(QtGui.QApplication.translate("ControleDeAcesso", "Mecajun\n"
"Mecatrônica Júnior de Brasília", None, QtGui.QApplication.UnicodeUTF8))
        self.label_descricao.setText(QtGui.QApplication.translate("ControleDeAcesso", "Digite sua matrícula e aperte \"Enter\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_matricula.setText(QtGui.QApplication.translate("ControleDeAcesso", "Matricula:     ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_funcionarios.setText(QtGui.QApplication.translate("ControleDeAcesso", "Funcionarios do horario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_relogio.setText(QtGui.QApplication.translate("ControleDeAcesso", "00:00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Administracao.setText(QtGui.QApplication.translate("ControleDeAcesso", "Administração", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_horarios.setText(QtGui.QApplication.translate("ControleDeAcesso", "Horarios", None, QtGui.QApplication.UnicodeUTF8))

