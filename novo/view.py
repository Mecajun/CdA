# -*- coding: utf-8 -*-
import sys
from datetime import datetime

from PySide.QtGui import *
from PySide.QtCore import *

from cda_alterasenha import Ui_Altera_Senha_Window 
from cda_funcionarios import Ui_Add_Funcionarios_Window 
from cda_horarios import Ui_Horarios_Window
from cda_mainWindow import Ui_Controle_De_Acesso_Window
from cda_relatorios import Ui_Relatorios_Window  
from cda_tolerancias import Ui_Tolerancias_Window
from cda_validarsenha import Ui_Adm_Senha_Window

##	Altera o nome do processo
#	@parm newname Novo nome do processo
def set_proc_name(newname):
	from ctypes import cdll, byref, create_string_buffer
	libc = cdll.LoadLibrary('libc.so.6')
	buff = create_string_buffer(len(newname)+1)
	buff.value = newname
	libc.prctl(15, byref(buff), 0, 0, 0)

##	Classe da janela principal do programa
class Controle_De_Acesso_Window(QMainWindow,Ui_Controle_De_Acesso_Window):
	##	Construtor da classe
	def __init__(self,parent=None):
		super(Controle_De_Acesso_Window, self).__init__(parent)
		self.setupUi(self)
		self._set_connections()

		self.adm_window=None
		self.altera_senha_window=None
		self.add_funcionarios_window=None
		self.tolerancias_window=None
		self.relatorios_window=None
		self.horarios_window=None

		self.funcionarios_horario_list=[]
		
		self._configure()
		self.show()

	##	Faz as configurações basicas
	def _configure(self):
		self.lineEdit_matricula.setMaxLength(30)
		self.center()
		self.model = QStandardItemModel(self.listView_funcionarios_horarios)
		self.adiciona_Funcionarios_Horario("filipe","42",True)
		self.listView_funcionarios_horarios.setModel(self.model)
		self.adiciona_Funcionarios_Horario("filipea","43",False)

	##	Faz todas a conexões de eventos
	def _set_connections(self):
		self.connect(self.pushButton_horarios,SIGNAL("clicked()"),self.pushButton_Horarios_Clicked)
		self.connect(self.lineEdit_matricula,SIGNAL("returnPressed()"),self.lineEdit_Matricula_ReturnPressed)
		self.actionAlterar_Senha.triggered.connect(self.menu_Alterar_Senha_valida)
		self.actionAdicionar_Funcionarios.triggered.connect(self.menu_Adicionar_Funcionarios_valida)
		self.actionRemover_Funcionarios.triggered.connect(self.menu_Remover_Funcionarios_valida)
		self.actionEditar_Funcionarios.triggered.connect(self.menu_Editar_Funcionarios_valida)
		self.actionConfigurar_Tolerancias.triggered.connect(self.menu_Configurar_Tolerancias_valida)
		self.actionGerar_Relatorios.triggered.connect(self.menu_Gerar_Relatorios_valida)
		self.actionManual.triggered.connect(self.menu_Manual)
		self.actionSobre_Mecajun.triggered.connect(self.menu_Sobre_Mecajun)
		self.actionSobre_Qt.triggered.connect(self.menu_Sobre_Qt)

		timer = QTimer(self)
		self.connect(timer, SIGNAL("timeout()"), self.atualiza_Relogio)
		timer.start(100)

	##	Adiciona funcionarios na lista de funcionarios do horario
	#	@parm func Nome do fucionario que sera adicionado
	#	@parm fun_id Id do funcionario que sera adicionado
	#	#param estado Estado de presença True ou False
	def adiciona_Funcionarios_Horario(self,func,func_id,estado):
		if not ( (isinstance(func, str) or isinstance(func, unicode)) and (isinstance(func_id, str) or isinstance(func_id, unicode))):
			return False
		item = QStandardItem(func)
		if estado==True:
			item.setIcon(QPixmap("imagens/yes_icon.png"))
		else:
			item.setIcon(QPixmap("imagens/no_icon.png"))
		self.model.appendRow(item)
		self.funcionarios_horario_list.append({'func':func,'func_id':func_id,'estado':estado})
		return True

	##	Remove funcionarios na lista de funcionarios do horario utilizando como parametro o nome do funcionario ou id, somente um dos dois dados é necessario
	#	@parm func Nome do fucionario que sera removido
	#	@parm fun_id Id do funcionario que sera removido
	def remove_Funcionarios_Horario(self,func=None,func_id=None):
		if len(self.funcionarios_horario_list)<=0:
			return False
		i=0
		for i in range(len(self.funcionarios_horario_list)):
			if isinstance(func_id, str) or isinstance(func_id, unicode):
				if self.funcionarios_horario_list[i]['func_id']==func_id:
					self.model.takeRow(i)
					del self.funcionarios_horario_list[i]
					break
			elif isinstance(func, str) or isinstance(func, unicode):
				if self.funcionarios_horario_list[i]['func']==func:
					self.model.takeRow(i)
					del self.funcionarios_horario_list[i]
					break
		return True

	##	Atualiza funcionarios na lista de funcionarios do horario utilizando como parametro o nome do funcionario ou id, somente um dos dois dados é necessario
	#	@parm func Nome do fucionario que sera atualizado
	#	@parm fun_id Id do funcionario que sera atualizado
	#	#param estado Estado de presença True ou False
	def atualiza_Funcionarios_Horario(self,func=None,func_id=None,estado=True):
		if len(self.funcionarios_horario_list)<=0:
			return False
		i=0
		for i in range(len(self.funcionarios_horario_list)):
			if isinstance(func_id, str) or isinstance(func_id, unicode):
				if self.funcionarios_horario_list[i]['func_id']==func_id:
					self.model.takeRow(i)
					item = QStandardItem(self.funcionarios_horario_list[i]['func'])
					if estado==True:
						item.setIcon(QPixmap("imagens/yes_icon.png"))
					else:
						item.setIcon(QPixmap("imagens/no_icon.png"))
					self.model.insertRow(i,item)
					self.funcionarios_horario_list[i]['estado']=estado
					break
			elif isinstance(func, str) or isinstance(func, unicode):
				if self.funcionarios_horario_list[i]['func']==func:
					self.model.takeRow(i)
					item = QStandardItem(self.funcionarios_horario_list[i]['func'])
					if estado==True:
						item.setIcon(QPixmap("imagens/yes_icon.png"))
					else:
						item.setIcon(QPixmap("imagens/no_icon.png"))
					self.model.insertRow(i,item)
					self.funcionarios_horario_list[i]['estado']=estado
					break
		return True

	##	Centraliza a janela
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	##	Atualiza o relogio a cada segundo
	def atualiza_Relogio(self):
		self.label_relogio.setText(datetime.now().strftime("%Y/%m/%d\n%H:%M:%S"))

	##	Fecha uma das janelas do programa se estiverem abertas
	#	@param window janela que será fechada
	def fechar_Window(self,window):
		try:
			window.close()
		except AttributeError:
			pass
		return

	##	Função chamada quando menu administrativo de abrir a janela de alterar a senha é clicado
	#	A Função chama a janela que pede a senha do adm e conecta o sinal do resultado da validação. Caso a senha esteja correta a função @menu_Alterar_Senha sera chamada
	def menu_Alterar_Senha_valida(self):
		self.fechar_Window(self.adm_window)
		self.adm_window=Adm_Senha_Window(self)
		self.connect(self.adm_window,SIGNAL("resultado_Validacao_Senha()"),self.menu_Alterar_Senha)

	##	Função chamada quando menu administrativo de adicionar funcionarios é clicado
	#	A Função chama a janela que pede a senha do adm e conecta o sinal do resultado da validação. Caso a senha esteja correta a função @menu_Adicionar_Funcionarios sera chamada
	def menu_Adicionar_Funcionarios_valida(self):
		self.fechar_Window(self.adm_window)
		self.adm_window=Adm_Senha_Window(self)
		self.connect(self.adm_window,SIGNAL("resultado_Validacao_Senha()"),self.menu_Adicionar_Funcionarios)

	##	Função chamada quando menu administrativo de remover funcionarios é clicado
	#	A Função chama a janela que pede a senha do adm e conecta o sinal do resultado da validação. Caso a senha esteja correta a função @menu_Remover_Funcionarios sera chamada
	def menu_Remover_Funcionarios_valida(self):
		self.fechar_Window(self.adm_window)
		self.adm_window=Adm_Senha_Window(self)
		self.connect(self.adm_window,SIGNAL("resultado_Validacao_Senha()"),self.menu_Remover_Funcionarios)

	##	Função chamada quando menu administrativo de editar funcionarios é clicado
	#	A Função chama a janela que pede a senha do adm e conecta o sinal do resultado da validação. Caso a senha esteja correta a função @menu_Editar_Funcionarios sera chamada
	def menu_Editar_Funcionarios_valida(self):
		self.fechar_Window(self.adm_window)
		self.adm_window=Adm_Senha_Window(self)
		self.connect(self.adm_window,SIGNAL("resultado_Validacao_Senha()"),self.menu_Editar_Funcionarios)

	##	Função chamada quando menu administrativo de configurar tolerancias é clicado
	#	A Função chama a janela que pede a senha do adm e conecta o sinal do resultado da validação. Caso a senha esteja correta a função @menu_Configurar_Tolerancias sera chamada
	def menu_Configurar_Tolerancias_valida(self):
		self.fechar_Window(self.adm_window)
		self.adm_window=Adm_Senha_Window(self)
		self.connect(self.adm_window,SIGNAL("resultado_Validacao_Senha()"),self.menu_Configurar_Tolerancias)
	
	##	Função chamada quando menu administrativo de gerar relatorios é clicado
	#	A Função chama a janela que pede a senha do adm e conecta o sinal do resultado da validação. Caso a senha esteja correta a função @menu_Gerar_Relatorios sera chamada
	def menu_Gerar_Relatorios_valida(self):
		self.fechar_Window(self.adm_window)
		self.adm_window=Adm_Senha_Window(self)
		self.connect(self.adm_window,SIGNAL("resultado_Validacao_Senha()"),self.menu_Gerar_Relatorios)

	##	Fecha as janelas abertas e chama cria a janela Altera_Senha_Window
	def menu_Alterar_Senha(self):
		self.fechar_Window(self.adm_window)
		self.fechar_Window(self.altera_senha_window)
		self.altera_senha_window=Altera_Senha_Window(self)

	##	Fecha as janelas abertas e chama cria a janela Add_Funcionarios_Window
	def menu_Adicionar_Funcionarios(self):
		self.fechar_Window(self.adm_window)
		self.fechar_Window(self.add_funcionarios_window)
		self.add_funcionarios_window=Add_Funcionarios_Window(self)

	def menu_Remover_Funcionarios(self):
		self.fechar_Window(self.adm_window)
		print "Não implementado"

	def menu_Editar_Funcionarios(self):
		self.fechar_Window(self.adm_window)
		print "Não implementado"

	##	Fecha as janelas abertas e chama cria a janela Tolerancias_Window
	def menu_Configurar_Tolerancias(self):
		self.fechar_Window(self.adm_window)
		self.fechar_Window(self.tolerancias_window)
		self.tolerancias_window=Tolerancias_Window(self)

	##	Fecha as janelas abertas e chama cria a janela Relatorios_Window
	def menu_Gerar_Relatorios(self):
		self.fechar_Window(self.adm_window)
		self.fechar_Window(self.relatorios_window)
		self.relatorios_window=Relatorios_Window(self)

	def menu_Manual(self):
		self.adiciona_Funcionarios_Horario()
		print "Não implementado"

	def menu_Sobre_Mecajun(self):
		print "Não implementado"

	def menu_Sobre_Qt(self):
		print "Não implementado"

	##	Função chamada quando usuario digita uma matricula e tecla enter
	def lineEdit_Matricula_ReturnPressed(self):
		print self.lineEdit_matricula.text()

	##	Fecha a janela Horarios_Window e cria a janela Horarios_Window
	def pushButton_Horarios_Clicked(self):
		self.fechar_Window(self.horarios_window)
		self.horarios_window=Horarios_Window(self)

class Adm_Senha_Window(QMainWindow,Ui_Adm_Senha_Window):

	def __init__(self,parent=None):
		super(Adm_Senha_Window, self).__init__(parent)
		self.setupUi(self)
		self.connect(self.lineEdit_senha,SIGNAL("returnPressed()"),self.validar_Senha)
		self.center()
		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def validar_Senha(self):
		if self.lineEdit_senha.text()=="42":
			self.emit(SIGNAL("resultado_Validacao_Senha()"))

class Altera_Senha_Window(QMainWindow,Ui_Altera_Senha_Window):

	def __init__(self,parent=None):
		super(Altera_Senha_Window, self).__init__(parent)
		self.setupUi(self)
		self.center()
		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

class Add_Funcionarios_Window(QMainWindow,Ui_Add_Funcionarios_Window):

	def __init__(self,parent=None):
		super(Add_Funcionarios_Window, self).__init__(parent)
		self.setupUi(self)
		self.center()
		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

class Horarios_Window(QMainWindow,Ui_Horarios_Window):

	def __init__(self,parent=None):
		super(Horarios_Window, self).__init__(parent)
		self.setupUi(self)
		self.center()
		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

class Relatorios_Window(QMainWindow,Ui_Relatorios_Window):

	def __init__(self,parent=None):
		super(Relatorios_Window, self).__init__(parent)
		self.setupUi(self)
		self.center()
		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

class Tolerancias_Window(QMainWindow,Ui_Tolerancias_Window):

	def __init__(self,parent=None):
		super(Tolerancias_Window, self).__init__(parent)
		self.setupUi(self)
		self.center()
		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

def main():

	set_proc_name('Controle de Acesso')

	app = QApplication(sys.argv)
	ex = Controle_De_Acesso_Window()
	sys.exit(app.exec_())

if __name__ == '__main__':
    main()
