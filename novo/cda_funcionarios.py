# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'funcionarios.ui'
#
# Created: Sun Dec 15 14:38:46 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Add_Funcionarios_Window(object):
    def setupUi(self, Add_Funcionarios_Window):
        Add_Funcionarios_Window.setObjectName("Add_Funcionarios_Window")
        Add_Funcionarios_Window.resize(674, 483)
        Add_Funcionarios_Window.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.centralwidget = QtGui.QWidget(Add_Funcionarios_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_adicionar = QtGui.QPushButton(self.centralwidget)
        self.pushButton_adicionar.setGeometry(QtCore.QRect(480, 410, 181, 27))
        self.pushButton_adicionar.setObjectName("pushButton_adicionar")
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(290, 40, 371, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_nome = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_nome.sizePolicy().hasHeightForWidth())
        self.lineEdit_nome.setSizePolicy(sizePolicy)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.horizontalLayout_2.addWidget(self.lineEdit_nome)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_matricula = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_matricula.sizePolicy().hasHeightForWidth())
        self.lineEdit_matricula.setSizePolicy(sizePolicy)
        self.lineEdit_matricula.setObjectName("lineEdit_matricula")
        self.horizontalLayout.addWidget(self.lineEdit_matricula)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.pushButton_obter_rfid = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_obter_rfid.setObjectName("pushButton_obter_rfid")
        self.horizontalLayout_3.addWidget(self.pushButton_obter_rfid)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_RFID = QtGui.QLabel(self.layoutWidget)
        self.label_RFID.setText("")
        self.label_RFID.setObjectName("label_RFID")
        self.verticalLayout.addWidget(self.label_RFID)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.comboBox_dias_semana = QtGui.QComboBox(self.layoutWidget)
        self.comboBox_dias_semana.setObjectName("comboBox_dias_semana")
        self.comboBox_dias_semana.addItem("")
        self.comboBox_dias_semana.addItem("")
        self.comboBox_dias_semana.addItem("")
        self.comboBox_dias_semana.addItem("")
        self.comboBox_dias_semana.addItem("")
        self.comboBox_dias_semana.addItem("")
        self.comboBox_dias_semana.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_dias_semana)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.timeEdit_entrada = QtGui.QTimeEdit(self.layoutWidget)
        self.timeEdit_entrada.setObjectName("timeEdit_entrada")
        self.horizontalLayout_4.addWidget(self.timeEdit_entrada)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.timeEdit_saida = QtGui.QTimeEdit(self.layoutWidget)
        self.timeEdit_saida.setObjectName("timeEdit_saida")
        self.horizontalLayout_4.addWidget(self.timeEdit_saida)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tableView_horarios = QtGui.QTableView(self.layoutWidget)
        self.tableView_horarios.setObjectName("tableView_horarios")
        self.verticalLayout.addWidget(self.tableView_horarios)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_adicionar_horario = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_adicionar_horario.setObjectName("pushButton_adicionar_horario")
        self.horizontalLayout_6.addWidget(self.pushButton_adicionar_horario)
        self.pushButton_remover_horario = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_remover_horario.setObjectName("pushButton_remover_horario")
        self.horizontalLayout_6.addWidget(self.pushButton_remover_horario)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 258, 421))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.listView_funcionarios = QtGui.QListView(self.layoutWidget1)
        self.listView_funcionarios.setObjectName("listView_funcionarios")
        self.verticalLayout_2.addWidget(self.listView_funcionarios)
        Add_Funcionarios_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Add_Funcionarios_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 25))
        self.menubar.setObjectName("menubar")
        Add_Funcionarios_Window.setMenuBar(self.menubar)

        self.retranslateUi(Add_Funcionarios_Window)
        QtCore.QMetaObject.connectSlotsByName(Add_Funcionarios_Window)
        Add_Funcionarios_Window.setTabOrder(self.lineEdit_nome, self.lineEdit_matricula)
        Add_Funcionarios_Window.setTabOrder(self.lineEdit_matricula, self.pushButton_obter_rfid)
        Add_Funcionarios_Window.setTabOrder(self.pushButton_obter_rfid, self.comboBox_dias_semana)
        Add_Funcionarios_Window.setTabOrder(self.comboBox_dias_semana, self.timeEdit_entrada)
        Add_Funcionarios_Window.setTabOrder(self.timeEdit_entrada, self.timeEdit_saida)
        Add_Funcionarios_Window.setTabOrder(self.timeEdit_saida, self.pushButton_adicionar_horario)
        Add_Funcionarios_Window.setTabOrder(self.pushButton_adicionar_horario, self.pushButton_remover_horario)
        Add_Funcionarios_Window.setTabOrder(self.pushButton_remover_horario, self.pushButton_adicionar)
        Add_Funcionarios_Window.setTabOrder(self.pushButton_adicionar, self.listView_funcionarios)

    def retranslateUi(self, Add_Funcionarios_Window):
        Add_Funcionarios_Window.setWindowTitle(QtGui.QApplication.translate("Add_Funcionarios_Window", "Adicionar Funcionarios", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_adicionar.setText(QtGui.QApplication.translate("Add_Funcionarios_Window", "Adicionar Funcionario", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Add_Funcionarios_Window", "Nome", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Add_Funcionarios_Window", "Matricula", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Add_Funcionarios_Window", "RFID", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_obter_rfid.setText(QtGui.QApplication.translate("Add_Funcionarios_Window", "Obter RFID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Add_Funcionarios_Window", "Dia da Semana", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_dias_semana.setItemText(0, QtGui.QApplication.translate("Add_Funcionarios_Window", "Domingo", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_dias_semana.setItemText(1, QtGui.QApplication.translate("Add_Funcionarios_Window", "Segunda", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_dias_semana.setItemText(2, QtGui.QApplication.translate("Add_Funcionarios_Window", "Terça", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_dias_semana.setItemText(3, QtGui.QApplication.translate("Add_Funcionarios_Window", "Quarta", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_dias_semana.setItemText(4, QtGui.QApplication.translate("Add_Funcionarios_Window", "Quinta", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_dias_semana.setItemText(5, QtGui.QApplication.translate("Add_Funcionarios_Window", "Sexta", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_dias_semana.setItemText(6, QtGui.QApplication.translate("Add_Funcionarios_Window", "Sabado", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Add_Funcionarios_Window", "Entrada", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Add_Funcionarios_Window", "Saida", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_adicionar_horario.setText(QtGui.QApplication.translate("Add_Funcionarios_Window", "Adicionar Horario", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_remover_horario.setText(QtGui.QApplication.translate("Add_Funcionarios_Window", "Remover Horario", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Add_Funcionarios_Window", "Funcionarios Cadastrados", None, QtGui.QApplication.UnicodeUTF8))

