# -*- coding: utf-8 -*-

##  @package view
#   Implementação dos eventos e configurações adicionais das interfaces graficas do programa

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

from auxiliares import dia_Semana_Int2str

##	Altera o nome do processo
#	@parm newname Novo nome do processo
def set_proc_name(newname):
	from ctypes import cdll, byref, create_string_buffer
	libc = cdll.LoadLibrary('libc.so.6')
	buff = create_string_buffer(len(newname)+1)
	buff.value = newname
	libc.prctl(15, byref(buff), 0, 0, 0)

##	Janela principal do programa
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
	#	@parm func_id Id do funcionario que sera adicionado
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
	#	@parm func_id Id do funcionario que sera removido
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
	#	@parm func_id Id do funcionario que sera atualizado
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

##	Janela para digitar senha de administrador
class Adm_Senha_Window(QMainWindow,Ui_Adm_Senha_Window):

	def __init__(self,parent=None):
		super(Adm_Senha_Window, self).__init__(parent)
		self.setupUi(self)
		self.center()
		self._set_connections()
		self.show()

	##	Faz todas a conexões de eventos
	def _set_connections(self):
		self.connect(self.lineEdit_senha,SIGNAL("returnPressed()"),self.validar_Senha)

	##	Centraliza a janela
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	##	Verifica se as senhas esta correta
	def validar_Senha(self):
		if self.lineEdit_senha.text()=="42":
			self.emit(SIGNAL("resultado_Validacao_Senha()"))

##	Janela para alterar senha de administrador
class Altera_Senha_Window(QMainWindow,Ui_Altera_Senha_Window):

	def __init__(self,parent=None):
		super(Altera_Senha_Window, self).__init__(parent)
		self.setupUi(self)
		self.center()
		self._set_connections()
		self.show()

	##	Faz todas a conexões de eventos
	def _set_connections(self):
		self.connect(self.pushButton_salvar,SIGNAL("clicked()"),self.pushButton_Salvar_Clicked)

	##	Centraliza a janela
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	##	Verifica se as senhas correspondem
	def pushButton_Salvar_Clicked(self):
		self.lineEdit_senha.text()
		if self.lineEdit_nova_senha_1.text()!=self.lineEdit_nova_senha_2.text():
			msgBox = QMessageBox()
			msgBox.setText(u"As senhas não conferem")
			msgBox.exec_()

##	Janela para adicionar funcionarios
class Add_Funcionarios_Window(QMainWindow,Ui_Add_Funcionarios_Window):

	def __init__(self,parent=None):
		super(Add_Funcionarios_Window, self).__init__(parent)
		self.setupUi(self)
		self.lista_horarios=[]
		self.center()
		self._set_connections()
		self._configure()
		self.show()

	##	Faz todas a conexões de eventos
	def _set_connections(self):
		self.connect(self.timeEdit_entrada,SIGNAL("editingFinished()"),self.timeEdit_Entrada_Editing_Finished)
		self.connect(self.pushButton_adicionar,SIGNAL("clicked()"),self.pushButton_Adicionar_Clicked)
		self.connect(self.pushButton_adicionar_horario,SIGNAL("clicked()"),self.pushButton_Adicionar_Horario_Clicked)
		self.connect(self.pushButton_remover_horario,SIGNAL("clicked()"),self.pushButton_Remover_Horario_Clicked)

	##	Centraliza a janela
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	##	Faz as configurações basicas
	def _configure(self):
		self.model_horarios = QStandardItemModel (0,3)
		self.model_horarios.setHorizontalHeaderLabels(['Dia da Semana','Entrada','Saida'])
		self.tableView_horarios.setModel(self.model_horarios)
		self.tableView_horarios.setShowGrid(False)

	#	Adiciona um funcionario na lista de funcionarios
	#	@parm func Nome do fucionario que sera atualizado
	#	@parm func_id Id do funcionario que sera atualizado
	def adiciona_ListWidget_Funcionarios(self,func=None,func_id=None):
		if not hasattr(self,'lista_funcionarios'):
			self.lista_funcionarios=[]
		novo = QListWidgetItem()
		novo.setText(func)
		self.lista_funcionarios.append({'func':func,'func_id':func_id})
		self.listWidget_funcionarios.addItem(novo)
	
	#	Remove um funcionario da lista de funcionarios
	#	@parm func Nome do fucionario que sera removido
	#	@parm func_id Id do funcionario que sera removido
	def remove_ListWidget_Funcionarios(self,func,func_id):
		if not hasattr(self,'lista_funcionarios'):
			self.lista_funcionarios=[]
			return False
		if len(self.lista_funcionarios)<=0:
			return False
		for i in range(len(self.lista_funcionarios)):
			if isinstance(func_id, str) or isinstance(func_id, unicode):
				if self.lista_funcionarios[i]['func_id']==func_id:
					self.listWidget_funcionarios.takeItem(i)
					del self.lista_funcionarios[i]
					break
			elif isinstance(func, str) or isinstance(func, unicode):
				if self.lista_funcionarios[i]['func']==func:
					self.listWidget_funcionarios.takeItem(i)
					del self.lista_funcionarios[i]
					break
		return True

	##	Atualiza funcionarios na lista de funcionarios utilizando como parametro o nome do funcionario ou id, somente um dos dois dados é necessario
	#	@parm func Nome do fucionario que sera atualizado
	#	@parm func_id Id do funcionario que sera atualizado
	#	@parm novo_nome Nome atualizado do funcionario
	def atualiza_ListWidget_Funcionarios(self,func=None,func_id=None,novo_nome=None):
		if not hasattr(self,'lista_funcionarios'):
			self.lista_funcionarios=[]
			return False
		if len(self.lista_funcionarios)<=0:
			return False
		if novo_nome==None:
			return False
		for i in range(len(self.lista_funcionarios)):
			if isinstance(func_id, str) or isinstance(func_id, unicode):
				if self.lista_funcionarios[i]['func_id']==func_id:
					self.listWidget_funcionarios.takeItem(i)
					novo = QListWidgetItem()
					novo.setText(novo_nome)
					self.listWidget_funcionarios.insertItem(i,novo)
					self.lista_funcionarios[i]['func']=novo_nome
					break
			elif isinstance(func, str) or isinstance(func, unicode):
				if self.lista_funcionarios[i]['func']==func:
					self.listWidget_funcionarios.takeItem(i)
					novo = QListWidgetItem()
					novo.setText(novo_nome)
					self.listWidget_funcionarios.insertItem(i,novo)
					self.lista_funcionarios[i]['func']=novo_nome
					break
		return True

	##	Adiciona um horario na lista de horarios
	#	@parm dia_da_semana Dia da semana considerando domingo=0, segunda=1 etc
	#	@param horario_inicial Horario inicial no formato hh:mm:ss
	#	@param horario_final Horario final no formato hh:mm:ss
	#	@param horario_id Id para o horario não necessario atualmente
	def adiciona_TableView_Horarios(self,dia_da_semana,horario_inicial,horario_final,horario_id=None):
		if not isinstance(dia_da_semana, int):
			return False
		if not (isinstance(horario_inicial, str) or isinstance(horario_inicial, unicode)):
			return False
		if not (isinstance(horario_final, str) or isinstance(horario_final, unicode)):
			return False
		if not hasattr(self,'lista_horarios'):
			self.lista_horarios=[]
		dia_da_semana_s=dia_Semana_Int2str(dia_da_semana)
		dia_da_semana_s_Item=QStandardItem(dia_da_semana_s)
		dia_da_semana_s_Item.setEditable(False)
		horario_inicial_Item=QStandardItem(horario_inicial)
		horario_inicial_Item.setEditable(False)
		horario_final_Item=QStandardItem(horario_final)
		horario_final_Item.setEditable(False)
		self.model_horarios.appendRow ((dia_da_semana_s_Item,horario_inicial_Item,horario_final_Item))
		self.lista_horarios.append({"dia_da_semana":dia_da_semana,"horario_inicial":horario_inicial,"horario_final":horario_final,"horario_id":horario_id})
		return True

	##	Adiciona um horario na lista de horarios
	#	@parm posicao Indice inteiro do horario na lista
	#	@parm horario_id Id do horario para ser removido
	def remove_TableView_Horarios(self,posicao,horario_id=None):
		if not hasattr(self,'lista_horarios'):
			self.lista_horarios=[]
			return False
		if len(self.lista_horarios)<=0:
			return False

		if isinstance(posicao, int):
			try:
				del self.lista_horarios[posicao]
				self.model_horarios.takeRow(posicao)
				return True
			except Exception:
				return False

		if isinstance(horario_id, int):
			for i in range(len(self.lista_horarios)):
					if self.lista_horarios[i]['horario_id']==horario_id:
						del self.lista_horarios[i]
						self.model_horarios.takeRow(i)
						return True
		return False

	##	Evento chamado para setar o horario minimo de saida maior ou igual ao de entrada
	def timeEdit_Entrada_Editing_Finished (self):
		self.timeEdit_saida.setMinimumTime(self.timeEdit_entrada.time())

	##	Obtem todos os dados do funcionario incluindo os horarios
	def obter_Dados_Janela(self):
		dados={}
		dados['nome']=self.lineEdit_nome.text()
		dados['matricula']=self.lineEdit_matricula.text()
		dados['rfid']=None
		dados['horarios']=self.lista_horarios
		return dados

	##	Obtem os dados do horario atual que esta sendo adicionado
	def obter_Dados_Horarios(self):
		dados={}
		dados['horario_inicial']=self.timeEdit_entrada.time().toString("HH:mm:ss")
		dados['horario_final']=self.timeEdit_saida.time().toString("HH:mm:ss")
		dados['dia_da_semana']=self.comboBox_dias_semana.currentIndex()
		return dados

	##	Adiciona horarios para o funcionario atual
	def pushButton_Adicionar_Horario_Clicked(self):
		if not hasattr(self,'lista_funcionarios'):
			self.lista_funcionarios=[]
		dados=self.obtdia_da_semana_s_Item,horario_inicial_Item,horario_final_Itemer_Dados_Horarios()
		for i in self.lista_horarios:
			if i['dia_da_semana']==dados['dia_da_semana'] and i['horario_inicial']==dados['horario_inicial']:
				msgBox = QMessageBox()
				msgBox.setText(u"Não é possivel adicionar horarios de entrada iguais")
				msgBox.exec_()
				return
		self.adiciona_TableView_Horarios(dados['dia_da_semana'],dados['horario_inicial'],dados['horario_final'],None)

	##	Remove os horarios selecionados do funcionario
	def pushButton_Remover_Horario_Clicked(self):
		index=[]
		for i in self.tableView_horarios.selectionModel().selectedIndexes():
			if i.row() not in index:
				index.append(i.row())
				self.remove_TableView_Horarios(i.row())

	##	Adiciona um funcionario
	def pushButton_Adicionar_Clicked(self):
		"nada"

##	Janela para visualizar os horarios dos funcionarios
class Horarios_Window(QMainWindow,Ui_Horarios_Window):

	def __init__(self,parent=None):
		super(Horarios_Window, self).__init__(parent)
		self.setupUi(self)
		self.center()
		self._configure()
		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	##	Faz as configurações basicas
	def _configure(self):
		self.model_horarios = QStandardItemModel (0,4)
		self.model_horarios.setHorizontalHeaderLabels(['Nome','Dia da Semana','Entrada','Saida'])
		self.tableView_horarios.setShowGrid(True)
		self.tableView_horarios.setSortingEnabled(True)
		self.tableView_horarios.setModel(self.model_horarios)

	##	Adiciona um horario na lista de horarios
	#	@parm dia_da_semana Dia da semana considerando domingo=0, segunda=1 etc
	#	@param horario_inicial Horario inicial no formato hh:mm:ss
	#	@param horario_final Horario final no formato hh:mm:ss
	#	@param horario_id Id para o horario não necessario atualmente
	def adiciona_TableView_Horarios(self,nome,dia_da_semana,horario_inicial,horario_final):
		if not (isinstance(nome, str) or isinstance(nome, unicode)):
			return False
		if not isinstance(dia_da_semana, int):
			return False
		if not (isinstance(horario_inicial, str) or isinstance(horario_inicial, unicode)):
			return False
		if not (isinstance(horario_final, str) or isinstance(horario_final, unicode)):
			return False
		if not hasattr(self,'lista_horarios'):
			self.lista_horarios=[]
		nome_Item=QStandardItem(nome)
		nome_Item.setEditable(False)
		dia_da_semana_s=dia_Semana_Int2str(dia_da_semana)
		dia_da_semana_s_Item=QStandardItem(dia_da_semana_s)
		dia_da_semana_s_Item.setEditable(False)
		horario_inicial_Item=QStandardItem(horario_inicial)
		horario_inicial_Item.setEditable(False)
		horario_final_Item=QStandardItem(horario_final)
		horario_final_Item.setEditable(False)
		self.model_horarios.appendRow ((nome_Item,dia_da_semana_s_Item,horario_inicial_Item,horario_final_Item))
		return True

##	Janela para gerar os relatorios
class Relatorios_Window(QMainWindow,Ui_Relatorios_Window):

	def __init__(self,parent=None):
		super(Relatorios_Window, self).__init__(parent)
		self.setupUi(self)
		self.center()
		self._configure()
		self._set_connections()
		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	##	Faz todas a conexões de eventos
	def _set_connections(self):
		self.connect(self.pushButton_log_porta,SIGNAL("clicked()"),self.pushButton_Log_Porta_Clicked)
		self.connect(self.pushButton_relatorio_pontos,SIGNAL("clicked()"),self.pushButton_Relatorio_Pontos_Clicked)
		self.connect(self.dateTimeEdit_inicial,SIGNAL("editingFinished()"),self.dateTimeEdit_Inicial_Editing_Finished)

	##	Faz as configurações basicas
	def _configure(self):
		self.dateTimeEdit_inicial.setDisplayFormat("dd MMM yyyy")
		self.dateTimeEdit_final.setDisplayFormat("dd MMM yyyy")
		self.dateTimeEdit_inicial.setCalendarPopup(True)
		self.dateTimeEdit_final.setCalendarPopup(True)
		self.checkBox_faltosos.setCheckState(Qt.CheckState.Checked)
		self.checkBox_pontuais.setCheckState(Qt.CheckState.Checked)
		self.checkBox_atrasados.setCheckState(Qt.CheckState.Checked)
		self.dateTimeEdit_inicial.setDateTime(QDateTime(QDateTime.currentDateTime().addMonths(-1)))
		self.dateTimeEdit_final.setDateTime(QDateTime(QDateTime.currentDateTime()))
		self.dateTimeEdit_final.setMinimumDateTime(self.dateTimeEdit_inicial.dateTime())

	##	Altera a data minima para a data final
	def dateTimeEdit_Inicial_Editing_Finished(self):
		self.dateTimeEdit_final.setMinimumDateTime(self.dateTimeEdit_inicial.dateTime())

	##	Obtem dos dados da janela
	def obter_Dados(self):
		dados={}
		dados['data_inicial']=self.dateTimeEdit_inicial.dateTime().toPython()
		dados['data_final']=self.dateTimeEdit_final.dateTime().toPython()
		dados['pontuais']=self.checkBox_pontuais.isChecked()
		dados['faltosos']=self.checkBox_faltosos.isChecked()
		dados['atrasados']=self.checkBox_atrasados.isChecked()
		return dados

	##	Gera o relatorio de logs da porta
	def pushButton_Log_Porta_Clicked(self):
		print self.obter_Dados()

	##	Gera o relatorio de pontos
	def pushButton_Relatorio_Pontos_Clicked(self):
		print self.obter_Dados()

##	Janela para configurar as tolerancias
class Tolerancias_Window(QMainWindow,Ui_Tolerancias_Window):

	def __init__(self,parent=None):
		super(Tolerancias_Window, self).__init__(parent)
		self.setupUi(self)
		self.center()
		self._configure()
		self._set_connections()
		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	##	Faz as configurações basicas
	def _configure(self):
		self.timeEdit_entrada_antes.setTime(QTime(0, 30, 0))
		self.timeEdit_entrada_depois.setTime(QTime(0, 30, 0))
		self.timeEdit_saida_antes.setTime(QTime(0, 30, 0))
		self.timeEdit_saida_depois.setTime(QTime(0, 30, 0))
		self.timeEdit_atraso.setTime(QTime(0, 10, 0))

	##	Faz todas a conexões de eventos
	def _set_connections(self):
		self.connect(self.pushButton_salvar,SIGNAL("clicked()"),self.pushButton_Salvar_Clicked)
		self.connect(self.timeEdit_entrada_depois,SIGNAL("editingFinished()"),self.altera_Atraso_Minimo)

	##	Altera o atraso maximo para não ser maior que a tolerancia de entrada
	def altera_Atraso_Minimo(self):
		self.timeEdit_atraso.setMaximumTime(self.timeEdit_entrada_depois.time())

	##	Obtem os dados da janela
	def obter_Dados(self):
		dados={}
		dados['entrada_antes']=self.timeEdit_entrada_antes.time().toPython()
		dados['entrada_depois']=self.timeEdit_entrada_depois.time().toPython()
		dados['saida_antes']=self.timeEdit_saida_antes.time().toPython()
		dados['saida_depois']=self.timeEdit_saida_depois.time().toPython()
		dados['atraso']=self.timeEdit_atraso.time().toPython()
		return dados

	##	Salva as configurações
	def pushButton_Salvar_Clicked(self):
		print self.obter_Dados()

def main():

	set_proc_name('Controle de Acesso')

	app = QApplication(sys.argv)
	ex = Controle_De_Acesso_Window()
	sys.exit(app.exec_())

if __name__ == '__main__':
    main()