# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Sat Dec 14 23:43:29 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Controle_De_Acesso_Window(object):
    def setupUi(self, Controle_De_Acesso_Window):
        Controle_De_Acesso_Window.setObjectName("Controle_De_Acesso_Window")
        Controle_De_Acesso_Window.resize(599, 292)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imagens/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Controle_De_Acesso_Window.setWindowIcon(icon)
        Controle_De_Acesso_Window.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.centralwidget = QtGui.QWidget(Controle_De_Acesso_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_logo = QtGui.QWidget(self.centralwidget)
        self.widget_logo.setGeometry(QtCore.QRect(20, 10, 201, 121))
        self.widget_logo.setObjectName("widget_logo")
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 10, 341, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_empresa = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_empresa.setFont(font)
        self.label_empresa.setAlignment(QtCore.Qt.AlignCenter)
        self.label_empresa.setObjectName("label_empresa")
        self.verticalLayout.addWidget(self.label_empresa)
        self.label_descricao = QtGui.QLabel(self.layoutWidget)
        self.label_descricao.setAlignment(QtCore.Qt.AlignCenter)
        self.label_descricao.setObjectName("label_descricao")
        self.verticalLayout.addWidget(self.label_descricao)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_matricula = QtGui.QLabel(self.layoutWidget)
        self.label_matricula.setObjectName("label_matricula")
        self.horizontalLayout.addWidget(self.label_matricula)
        self.lineEdit_matricula = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_matricula.setObjectName("lineEdit_matricula")
        self.horizontalLayout.addWidget(self.lineEdit_matricula)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_funcionarios = QtGui.QLabel(self.layoutWidget)
        self.label_funcionarios.setObjectName("label_funcionarios")
        self.verticalLayout.addWidget(self.label_funcionarios)
        self.listView_funcionarios_horarios = QtGui.QListView(self.layoutWidget)
        self.listView_funcionarios_horarios.setObjectName("listView_funcionarios_horarios")
        self.verticalLayout.addWidget(self.listView_funcionarios_horarios)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 140, 181, 101))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_relogio = QtGui.QLabel(self.layoutWidget1)
        self.label_relogio.setAlignment(QtCore.Qt.AlignCenter)
        self.label_relogio.setObjectName("label_relogio")
        self.verticalLayout_2.addWidget(self.label_relogio)
        self.pushButton_horarios = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_horarios.setObjectName("pushButton_horarios")
        self.verticalLayout_2.addWidget(self.pushButton_horarios)
        Controle_De_Acesso_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Controle_De_Acesso_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 25))
        self.menubar.setObjectName("menubar")
        self.menuAdministra_o = QtGui.QMenu(self.menubar)
        self.menuAdministra_o.setObjectName("menuAdministra_o")
        self.menuAjuda = QtGui.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        Controle_De_Acesso_Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Controle_De_Acesso_Window)
        self.statusbar.setObjectName("statusbar")
        Controle_De_Acesso_Window.setStatusBar(self.statusbar)
        self.actionAlterar_Senha = QtGui.QAction(Controle_De_Acesso_Window)
        self.actionAlterar_Senha.setObjectName("actionAlterar_Senha")
        self.actionAdicionar_Funcionarios = QtGui.QAction(Controle_De_Acesso_Window)
        self.actionAdicionar_Funcionarios.setObjectName("actionAdicionar_Funcionarios")
        self.actionRemover_Funcionarios = QtGui.QAction(Controle_De_Acesso_Window)
        self.actionRemover_Funcionarios.setObjectName("actionRemover_Funcionarios")
        self.actionEditar_Funcionarios = QtGui.QAction(Controle_De_Acesso_Window)
        self.actionEditar_Funcionarios.setObjectName("actionEditar_Funcionarios")
        self.actionConfigurar_Tolerancias = QtGui.QAction(Controle_De_Acesso_Window)
        self.actionConfigurar_Tolerancias.setObjectName("actionConfigurar_Tolerancias")
        self.actionGerar_Relatorios = QtGui.QAction(Controle_De_Acesso_Window)
        self.actionGerar_Relatorios.setObjectName("actionGerar_Relatorios")
        self.actionManual = QtGui.QAction(Controle_De_Acesso_Window)
        self.actionManual.setObjectName("actionManual")
        self.actionSobre_Mecajun = QtGui.QAction(Controle_De_Acesso_Window)
        self.actionSobre_Mecajun.setObjectName("actionSobre_Mecajun")
        self.actionSobre_Qt = QtGui.QAction(Controle_De_Acesso_Window)
        self.actionSobre_Qt.setObjectName("actionSobre_Qt")
        self.menuAdministra_o.addAction(self.actionAlterar_Senha)
        self.menuAdministra_o.addSeparator()
        self.menuAdministra_o.addAction(self.actionAdicionar_Funcionarios)
        self.menuAdministra_o.addAction(self.actionEditar_Funcionarios)
        self.menuAdministra_o.addAction(self.actionRemover_Funcionarios)
        self.menuAdministra_o.addSeparator()
        self.menuAdministra_o.addAction(self.actionConfigurar_Tolerancias)
        self.menuAdministra_o.addSeparator()
        self.menuAdministra_o.addAction(self.actionGerar_Relatorios)
        self.menuAjuda.addAction(self.actionManual)
        self.menuAjuda.addSeparator()
        self.menuAjuda.addAction(self.actionSobre_Mecajun)
        self.menuAjuda.addAction(self.actionSobre_Qt)
        self.menubar.addAction(self.menuAdministra_o.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

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
        self.menuAdministra_o.setTitle(QtGui.QApplication.translate("Controle_De_Acesso_Window", "Administração", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAjuda.setTitle(QtGui.QApplication.translate("Controle_De_Acesso_Window", "Ajuda", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlterar_Senha.setText(QtGui.QApplication.translate("Controle_De_Acesso_Window", "Alterar Senha", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdicionar_Funcionarios.setText(QtGui.QApplication.translate("Controle_De_Acesso_Window", "Adicionar Funcionarios", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemover_Funcionarios.setText(QtGui.QApplication.translate("Controle_De_Acesso_Window", "Remover Funcionarios", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditar_Funcionarios.setText(QtGui.QApplication.translate("Controle_De_Acesso_Window", "Editar Funcionarios", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfigurar_Tolerancias.setText(QtGui.QApplication.translate("Controle_De_Acesso_Window", "Configurar Tolerancias", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGerar_Relatorios.setText(QtGui.QApplication.translate("Controle_De_Acesso_Window", "Gerar Relatorios", None, QtGui.QApplication.UnicodeUTF8))
        self.actionManual.setText(QtGui.QApplication.translate("Controle_De_Acesso_Window", "Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSobre_Mecajun.setText(QtGui.QApplication.translate("Controle_De_Acesso_Window", "Sobre Mecajun", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSobre_Qt.setText(QtGui.QApplication.translate("Controle_De_Acesso_Window", "Sobre Qt", None, QtGui.QApplication.UnicodeUTF8))