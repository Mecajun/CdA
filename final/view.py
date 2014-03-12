# -*- coding: utf-8 -*-

##  @package view
#   Implementação dos eventos e configurações adicionais das interfaces graficas do programa

import sys
import os
import time
import serial
import time
import platform

from datetime import datetime,timedelta
from PySide.QtGui import *
from PySide.QtCore import *

from auxiliares import *
from model_mysql import Connect_Db
from cda_alterasenha import Ui_Altera_Senha_Window 
from cda_funcionarios import Ui_Add_Funcionarios_Window 
from cda_horarios import Ui_Horarios_Window
from cda_mainWindow import Ui_Controle_De_Acesso_Window
from cda_relatorios import Ui_Relatorios_Window  
from cda_tolerancias import Ui_Tolerancias_Window
from cda_validarsenha import Ui_Adm_Senha_Window
from cda_removerfuncionario import Ui_Remover_Funcionarios_Window
from cda_obterRfid import Ui_Obter_Rfid_Window

caminho=os.path.dirname(os.path.realpath(__file__))

##	Janela principal do programa
class Controle_De_Acesso_Window(QMainWindow,Ui_Controle_De_Acesso_Window):
	##	Construtor da classe
	def __init__(self,parent=None,db_dados=None):
		super(Controle_De_Acesso_Window, self).__init__(parent)
		self.db_dados=db_dados
		self.setupUi(self)
		self.db=Connect_Db(db_dados)
		self._set_connections()
		self.adm_window=None
		self.altera_senha_window=None
		self.add_funcionarios_window=None
		self.atualiza_funcionarios_window=None
		self.tolerancias_window=None
		self.relatorios_window=None
		self.horarios_window=None
		self.remover_funcionarios_window=None
		self.funcionarios_horario_list=[]
		self._configure()
		self.show()

	##	Faz as configurações basicas
	def _configure(self):
		self.lineEdit_matricula.setMaxLength(30)
		self.center()
		self.model = QStandardItemModel(self.listView_funcionarios_horarios)
		self.listView_funcionarios_horarios.setModel(self.model)

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
		timer2 = QTimer(self)
		self.connect(timer2, SIGNAL("timeout()"), self.atualiza_Funcionarios_Esperados)
		timer2.start(200)
		timer3 = QTimer(self)
		self.connect(timer3, SIGNAL("timeout()"), self.verificar_Faltas)
		timer3.start(1000*60)
		self.verificar_Faltas()
		self.conecta_Arduino()

	##	Atualiza a lista de funcionarios esperados
	def atualiza_Funcionarios_Esperados(self):
		tol_ent_ant=self.db.obter_Configuracoes("tol_ent_ant")
		tol_sai_dep=self.db.obter_Configuracoes("tol_sai_dep")
		esperados=self.db.buscar_Funcionarios_Esperados(get_Week_Day(),tol_ent_ant,tol_sai_dep)
		funcionarios_horario_list_ids=[x['id_funcionario'] for x in self.funcionarios_horario_list]

		if esperados==False and len(funcionarios_horario_list_ids)>0:
			for i in funcionarios_horario_list_ids:
				self.remove_Funcionarios_Horario(None,i)

		if esperados==False and len(funcionarios_horario_list_ids)==0:
			return True

		self.logados=self.db.buscar_Funcionarios_Esperados_Logados(get_Week_Day(),tol_ent_ant,tol_sai_dep)
		self.nao_logados=[]
		if self.logados==False:
			try:
				self.nao_logados=[x for x in esperados.keys()]
			except Exception, e:
				pass
			self.logados=[]
		else:
			self.nao_logados=[x for x in esperados.keys() if x not in self.logados]

		for i in esperados.keys():
			if i not in funcionarios_horario_list_ids:
				if i in self.logados:
					self.adiciona_Funcionarios_Horario(esperados[i]['nome'],i,True)
				if i in self.nao_logados:
					self.adiciona_Funcionarios_Horario(esperados[i]['nome'],i,False)
			else:
				if i in self.logados:
					self.atualiza_Funcionarios_Horario(None,i,True)
				if i in self.nao_logados:
					self.atualiza_Funcionarios_Horario(None,i,False) 

		for i in funcionarios_horario_list_ids:
			if i not in esperados.keys():
				self.remove_Funcionarios_Horario(None,i)

	##	Adiciona funcionarios na lista de funcionarios do horario
	#	@parm func Nome do fucionario que sera adicionado
	#	@parm id_funcionario Id do funcionario que sera adicionado
	#	#param estado Estado de presença True ou False
	def adiciona_Funcionarios_Horario(self,func,id_funcionario,estado):
		if not ( (isinstance(func, str) or isinstance(func, unicode)) and (isinstance(id_funcionario, str) or isinstance(id_funcionario, unicode))):
			return False
		item = QStandardItem(func)
		if estado==True:
			item.setIcon(QPixmap(caminho+"/imagens/yes_icon.png"))
		else:
			item.setIcon(QPixmap(caminho+"/imagens/no_icon.png"))
		self.model.appendRow(item)
		self.funcionarios_horario_list.append({'func':func,'id_funcionario':id_funcionario,'estado':estado})
		return True

	##	Remove funcionarios na lista de funcionarios do horario utilizando como parametro o nome do funcionario ou id, somente um dos dois dados é necessario
	#	@parm func Nome do fucionario que sera removido
	#	@parm id_funcionario Id do funcionario que sera removido
	def remove_Funcionarios_Horario(self,func=None,id_funcionario=None):
		if len(self.funcionarios_horario_list)<=0:
			return False
		i=0
		for i in range(len(self.funcionarios_horario_list)):
			if isinstance(id_funcionario, str) or isinstance(id_funcionario, unicode):
				if self.funcionarios_horario_list[i]['id_funcionario']==id_funcionario:
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
	#	@parm id_funcionario Id do funcionario que sera atualizado
	#	#param estado Estado de presença True ou False
	def atualiza_Funcionarios_Horario(self,func=None,id_funcionario=None,estado=True):
		if len(self.funcionarios_horario_list)<=0:
			return False
		i=0
		for i in range(len(self.funcionarios_horario_list)):
			if isinstance(id_funcionario, str) or isinstance(id_funcionario, unicode):
				if self.funcionarios_horario_list[i]['id_funcionario']==id_funcionario:
					if self.funcionarios_horario_list[i]['estado']==estado:
						return True
					self.model.takeRow(i)
					item = QStandardItem(self.funcionarios_horario_list[i]['func'])
					if estado==True:
						item.setIcon(QPixmap(caminho+"/imagens/yes_icon.png"))
					else:
						item.setIcon(QPixmap(caminho+"/imagens/no_icon.png"))
					self.model.insertRow(i,item)
					self.funcionarios_horario_list[i]['estado']=estado
					return True
			elif isinstance(func, str) or isinstance(func, unicode):
				if self.funcionarios_horario_list[i]['func']==func:
					if self.funcionarios_horario_list[i]['estado']==estado:
						return True
					self.model.takeRow(i)
					item = QStandardItem(self.funcionarios_horario_list[i]['func'])
					if estado==True:
						item.setIcon(QPixmap(caminho+"/imagens/yes_icon.png"))
					else:
						item.setIcon(QPixmap(caminho+"/imagens/no_icon.png"))
					self.model.insertRow(i,item)
					self.funcionarios_horario_list[i]['estado']=estado
					return True
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
		self.adm_window=Adm_Senha_Window(self,self.db_dados)
		self.connect(self.adm_window,SIGNAL("resultado_Validacao_Senha()"),self.menu_Alterar_Senha)

	##	Função chamada quando menu administrativo de adicionar funcionarios é clicado
	#	A Função chama a janela que pede a senha do adm e conecta o sinal do resultado da validação. Caso a senha esteja correta a função @menu_Adicionar_Funcionarios sera chamada
	def menu_Adicionar_Funcionarios_valida(self):
		self.fechar_Window(self.adm_window)
		self.adm_window=Adm_Senha_Window(self,self.db_dados)
		self.connect(self.adm_window,SIGNAL("resultado_Validacao_Senha()"),self.menu_Adicionar_Funcionarios)

	##	Função chamada quando menu administrativo de remover funcionarios é clicado
	#	A Função chama a janela que pede a senha do adm e conecta o sinal do resultado da validação. Caso a senha esteja correta a função @menu_Remover_Funcionarios sera chamada
	def menu_Remover_Funcionarios_valida(self):
		self.fechar_Window(self.adm_window)
		self.adm_window=Adm_Senha_Window(self,self.db_dados)
		self.connect(self.adm_window,SIGNAL("resultado_Validacao_Senha()"),self.menu_Remover_Funcionarios)

	##	Função chamada quando menu administrativo de editar funcionarios é clicado
	#	A Função chama a janela que pede a senha do adm e conecta o sinal do resultado da validação. Caso a senha esteja correta a função @menu_Editar_Funcionarios sera chamada
	def menu_Editar_Funcionarios_valida(self):
		self.fechar_Window(self.adm_window)
		self.adm_window=Adm_Senha_Window(self,self.db_dados)
		self.connect(self.adm_window,SIGNAL("resultado_Validacao_Senha()"),self.menu_Editar_Funcionarios)

	##	Função chamada quando menu administrativo de configurar tolerancias é clicado
	#	A Função chama a janela que pede a senha do adm e conecta o sinal do resultado da validação. Caso a senha esteja correta a função @menu_Configurar_Tolerancias sera chamada
	def menu_Configurar_Tolerancias_valida(self):
		self.fechar_Window(self.adm_window)
		self.adm_window=Adm_Senha_Window(self,self.db_dados)
		self.connect(self.adm_window,SIGNAL("resultado_Validacao_Senha()"),self.menu_Configurar_Tolerancias)
	
	##	Função chamada quando menu administrativo de gerar relatorios é clicado
	#	A Função chama a janela que pede a senha do adm e conecta o sinal do resultado da validação. Caso a senha esteja correta a função @menu_Gerar_Relatorios sera chamada
	def menu_Gerar_Relatorios_valida(self):
		self.fechar_Window(self.adm_window)
		self.adm_window=Adm_Senha_Window(self,self.db_dados)
		self.connect(self.adm_window,SIGNAL("resultado_Validacao_Senha()"),self.menu_Gerar_Relatorios)

	##	Fecha as janelas abertas e chama cria a janela Altera_Senha_Window
	def menu_Alterar_Senha(self):
		self.fechar_Window(self.adm_window)
		self.fechar_Window(self.altera_senha_window)
		self.altera_senha_window=Altera_Senha_Window(self,self.db_dados)

	##	Fecha as janelas abertas e chama cria a janela Add_Funcionarios_Window
	def menu_Adicionar_Funcionarios(self):
		self.fechar_Window(self.adm_window)
		self.fechar_Window(self.add_funcionarios_window)
		self.add_funcionarios_window=Add_Funcionarios_Window(self,self.db_dados)

	def menu_Remover_Funcionarios(self):
		self.fechar_Window(self.adm_window)
		self.fechar_Window(self.remover_funcionarios_window)
		self.remover_funcionarios_window=Remover_Funcionarios_Window(self,self.db_dados)

	def menu_Editar_Funcionarios(self):
		self.fechar_Window(self.adm_window)
		self.fechar_Window(self.atualiza_funcionarios_window)
		self.atualiza_funcionarios_window=Atualiza_Funcionarios_Window(self,self.db_dados)

	##	Fecha as janelas abertas e chama cria a janela Tolerancias_Window
	def menu_Configurar_Tolerancias(self):
		self.fechar_Window(self.adm_window)
		self.fechar_Window(self.tolerancias_window)
		self.tolerancias_window=Tolerancias_Window(self,self.db_dados)

	##	Fecha as janelas abertas e chama cria a janela Relatorios_Window
	def menu_Gerar_Relatorios(self):
		self.fechar_Window(self.adm_window)
		self.fechar_Window(self.relatorios_window)
		self.relatorios_window=Relatorios_Window(self,self.db_dados)

	def menu_Manual(self):
		print "Não implementado"

	def menu_Sobre_Mecajun(self):
		print "Não implementado"

	def menu_Sobre_Qt(self):
		print "Não implementado"

	##	Função chamada quando usuario digita uma matricula e tecla enter
	def lineEdit_Matricula_ReturnPressed(self):
		id_funcionario=self.db.obter_Id_Funcionario_por_Matricula(self.lineEdit_matricula.text())
		if id_funcionario!=False:
			ponto=self.dar_Ponto(id_funcionario)
			self.lineEdit_matricula.setText("")
		else:
			print "Erro lineEdit_Matricula_ReturnPressed"
			print self.lineEdit_matricula.text()
			print id_funcionario
			print self.lineEdit_matricula

	##	Fecha a janela Horarios_Window e cria a janela Horarios_Window
	def pushButton_Horarios_Clicked(self):
		self.fechar_Window(self.horarios_window)
		self.horarios_window=Horarios_Window(self,self.db_dados)

	##	Da o ponto de entrada ou saida apartir do id de um funcionario
	##	@parm id_funcionario Id do funcionario 
	def dar_Ponto(self,id_funcionario):
		self.dar_Log_Porta(id_funcionario)
		# Obtem os limites de tempo para considerar o ponto entrada
		limite_inferior_entrada=string_2_Timedelta(self.db.obter_Configuracoes('tol_ent_ant'))
		limite_superior_entrada=string_2_Timedelta(self.db.obter_Configuracoes('tol_ent_dep'))
		#  Obtem os limites de tempo para considerar o ponto de saida
		limite_inferior_saida=string_2_Timedelta(self.db.obter_Configuracoes('tol_sai_ant'))
		limite_superior_saida=string_2_Timedelta(self.db.obter_Configuracoes('tol_sai_dep'))

		ponto_antigo=self.db.buscar_Ponto_Aberto_de_Funcionario(id_funcionario)

		if ponto_antigo!=False:
			#	Ponto que não foi fechado
			if (ponto_antigo['hora_final']+limite_superior_saida) < data_Atual():
				self.db.finaliza_Ponto(id_funcionario,data_Atual(True),2)
			#	Ponto normal
			elif ((ponto_antigo['hora_final']-limite_inferior_saida) <= data_Atual()) and ((ponto_antigo['hora_final']+limite_superior_saida) >= data_Atual()):
				self.db.finaliza_Ponto(id_funcionario,data_Atual(True),1)
				return 3
			else:
				return 1

		id_horario=self.db.buscar_Horario_Mais_Proximo_de_Funcionario(id_funcionario,get_Week_Day(),limite_inferior_entrada,limite_superior_entrada)
		if id_horario!=False:
			self.db.criar_Ponto(id_funcionario,id_horario,-1)
			return 2
		return 1

	##	Registra o log da porta quando um funcionario entra ou sai
	##	@parm id_funcionario Id do funcionario 
	def dar_Log_Porta(self,id_funcionario):
		self.db.adicionar_Log_Porta(id_funcionario)
		return

	##	Chama a thread de verificar faltas
	def verificar_Faltas(self):
		self.thread1=Faltas_e_atrasos(self,self.db_dados)
		self.thread1.start()

	def conecta_Arduino(self):
		self.bufferMensagens={}
		self.bufferMensagens['rfid']=None
		self.bufferMensagens['resposta']=None
		self.thread2=Hardware(self)
		self.connect( self.thread2, SIGNAL("updateBuffer(QString,QString)"), self.atualiza_Buffer_Mensagens )
		self.connect( self.thread2, SIGNAL("atualizaStatusBar(QString)"), self.escreveStatusBar )
		self.thread2.start()
		# self.connect(self.adm_window,SIGNAL("resultado_Validacao_Senha()"),self.menu_Remover_Funcionarios)

	def atualiza_Buffer_Mensagens(self,tipo,mensagem):
		if tipo=="rfid":
			self.emit(SIGNAL('RFID_Novo(QString)'), mensagem)
		self.bufferMensagens[tipo]=(mensagem,datetime.now())
		self.responde_Hardware(mensagem)

	def responde_Hardware(self,mensagem):
		id_funcionario=self.db.obter_Id_Funcionario_por_Rfid(mensagem)
		if id_funcionario==False: # Nao funcionario
			self.emit(SIGNAL('respondeHardware(QString)'), "0")
			return
		resposta=self.dar_Ponto(id_funcionario)
		self.emit(SIGNAL('respondeHardware(QString)'), str(resposta))
		if platform.system()=='Linux':
			dados=self.db.obter_Funcionario(id_funcionario)
			if dados!=False:
				falar(resposta,dados['nome'])
		return

	##	Fecha a conexão com o baco de dados
	def closeEvent(self, event):
		try:
			del self.db
		except Exception, e:
			pass

	##	Recebe uma mansagem para a status bar
	def escreveStatusBar(self,mensagem):
		self.statusbar.showMessage("Arduino conectado="+mensagem)

##	Thread para verificar funcionarios que faltaram ou estão atrazados
class Faltas_e_atrasos(QThread):
	def __init__(self, parent = None,db_dados = None):
		QThread.__init__(self, parent)
		self.db=Connect_Db(db_dados)

	def run(self):
		self.verificar_Falta()
		del self.db
		self.quit()

	def verificar_Falta(self):
		inicial=string_2_Datetime(self.db.obter_Configuracoes('ultima_verificacao'))
		final=data_Atual()
		dias=(final-inicial).days
		horarios=[]
		for i in xrange(dias//7):
			horarios=self.db.obter_Pontos_Faltando(inicial,inicial+timedelta(days=7))
			temp={}
			for i in range(7):
				temp[get_Week_Day(inicial+timedelta(days=i))]=inicial+timedelta(days=i)
			if horarios!=False:
				for i in horarios:
					self.db.criar_Ponto_Falta(i[1],i[0],str(temp[i[3]].date()),str(i[2]))
			inicial=inicial+timedelta(days=7)
		for i in xrange(dias%7):
			horarios=self.db.obter_Pontos_Faltando(inicial,inicial+timedelta(days=1),get_Week_Day(inicial))
			if horarios!=False:
				for i in horarios:
					self.db.criar_Ponto_Falta(i[1],i[0],str(inicial.date()),str(i[2]))
			inicial=inicial+timedelta(days=1)
		limite_superior_ent=self.db.obter_Configuracoes('tol_ent_dep')
		horarios=self.db.obter_Pontos_Faltando(inicial,inicial+timedelta(days=1),get_Week_Day(inicial),limite_superior_ent)
		if horarios!=False:
			for i in horarios:
				self.db.criar_Ponto_Falta(i[1],i[0],str(inicial.date()),str(i[2]))
		self.db.atualizar_Configuracoes('ultima_verificacao',str(final))

	##	Fecha a conexão com o baco de dados
	def closeEvent(self, event):
		try:
			del self.db
		except Exception, e:
			pass

##	Faz a cominicação com o hardware
class Hardware(QThread):
	def __init__(self, parent = None):
		QThread.__init__(self, parent)
		self.connect( parent, SIGNAL("respondeHardware(QString)"), self.envia)
		self.conecta()
		self.bufferMensagens={}
		self.bufferMensagens['rfid']=None
		self.bufferMensagens['resposta']=None

	def conecta(self):
		portas=('/dev/ttyUSB%d','/dev/ttyACM%d','COM%d')
		self.conectado=False
		linux=platform.system()=='Linux'
		windows=platform.system()=='Windows'
		if linux==False and windows==False:
			linux=True
			windows=True
		for i in xrange(10):
			if linux:
				try:
					self.ser = serial.Serial(portas[0]%(i,), 9600,timeout=2)
					self.conectado = True
					break
				except Exception, e:
					pass
			if linux:
				try:
					self.ser = serial.Serial(portas[1]%(i,), 9600,timeout=2)
					self.conectado = True
					break
				except Exception, e:
					continue
			if windows:
				try:
					self.ser = serial.Serial(portas[2]%(i,), 9600,timeout=2)
					self.conectado = True
					break
				except Exception, e:
					continue
		if self.conectado==True:
			self.r=self.ser.readline
			self.w=self.ser.write
		self.emit(SIGNAL('atualizaStatusBar(QString)'), str(self.conectado))

	def run(self):
		while True:
			self.recebe()		
			if self.conectado==False:
				self.conecta()
				time.sleep(0.1)

	def recebe(self):
		while self.conectado:
			try:
				mensagem=self.r()
				if mensagem[0]=='@' and mensagem[-2]=='#':
					self.bufferMensagens['rfid']=(mensagem[1:-2],datetime.now())
					self.emit(SIGNAL('updateBuffer(QString,QString)'), "rfid",mensagem[1:-2])
				if mensagem[0]=='!' and mensagem[-2]=='$':
					self.bufferMensagens['resposta']=(mensagem[1:-2],datetime.now())
					self.emit(SIGNAL('updateBuffer(QString,QString)'), "resposta",mensagem[1:-2])
				time.sleep(0.1)
			except Exception, e:
				self.conectado=False

	def envia(self,mensagem):
		if self.conectado:
			self.w(str(mensagem))

##	Janela para digitar senha de administrador
class Adm_Senha_Window(QMainWindow,Ui_Adm_Senha_Window):

	def __init__(self,parent=None,db_dados=None):
		super(Adm_Senha_Window, self).__init__(parent)
		self.setupUi(self)
		self.db=Connect_Db(db_dados)
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
		senha=self.db.obter_Configuracoes("adm_senha")
		if len(self.lineEdit_senha.text())>0 and senha!=False:
			if criptografar_Senha(self.lineEdit_senha.text())==senha:
				self.emit(SIGNAL("resultado_Validacao_Senha()"))
			else:
				self.lineEdit_senha.setText("")
				msgBox = QMessageBox(self)
				msgBox.setText(u"Senha errada")
				msgBox.exec_()
	
	##	Fecha a conexão com o baco de dados
	def closeEvent(self, event):
		try:
			del self.db
		except Exception, e:
			print e

##	Janela para alterar senha de administrador
class Altera_Senha_Window(QMainWindow,Ui_Altera_Senha_Window):

	def __init__(self,parent=None,db_dados=None):
		super(Altera_Senha_Window, self).__init__(parent)
		self.setupUi(self)
		self.db=Connect_Db(db_dados)
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
		senha=self.db.obter_Configuracoes("adm_senha")
		if criptografar_Senha(self.lineEdit_senha.text())!=senha:
			self.lineEdit_senha.setText("")
			msgBox = QMessageBox()
			msgBox.setText(u"A senha antiga esta incorreta")
			msgBox.exec_()
			return
		if self.lineEdit_nova_senha_1.text()!=self.lineEdit_nova_senha_2.text():
			msgBox = QMessageBox()
			msgBox.setText(u"As senhas não conferem")
			msgBox.exec_()
			return
		if self.db.atualizar_Configuracoes("adm_senha",criptografar_Senha(self.lineEdit_nova_senha_1.text()))==True:
			msgBox = QMessageBox()
			msgBox.setText(u"A senha foi alterada")
			msgBox.exec_()
			self.close()
		else:
			print "Erro atualizar senha"

	##	Fecha a conexão com o baco de dados
	def closeEvent(self, event):
		try:
			del self.db
		except Exception, e:
			pass

##	Janela base para adicionar ou atualizar funcionarios
class Funcionarios_Window(QMainWindow,Ui_Add_Funcionarios_Window):

	def __init__(self,parent=None,db_dados=None):
		super(Funcionarios_Window, self).__init__(parent)
		self.setupUi(self)
		self.db=Connect_Db(db_dados)
		self.lista_horarios=[]
		self.lista_horarios_removidos=[]
		self.center()
		self._set_connections()
		self._configure()
		self.show()
		self.mostrar_Funcionarios()
		self.mainWindow=parent

	##	Faz todas a conexões de eventos
	def _set_connections(self):
		self.connect(self.timeEdit_entrada,SIGNAL("editingFinished()"),self.timeEdit_Entrada_Editing_Finished)
		self.connect(self.pushButton_adicionar_horario,SIGNAL("clicked()"),self.pushButton_Adicionar_Horario_Clicked)
		self.connect(self.pushButton_remover_horario,SIGNAL("clicked()"),self.pushButton_Remover_Horario_Clicked)
		self.connect(self.pushButton_obter_rfid,SIGNAL("clicked()"),self.pushButton_Obter_Rfid_Clicked)
		self.connect(self.pushButton_apagar,SIGNAL("clicked()"),self.apagar_Rfid)

	##	Centraliza a janela
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	##	Faz as configurações basicas
	def _configure(self):
		self.model_funcionarios = QStandardItemModel(self.listView_funcionarios)
		self.listView_funcionarios.setModel(self.model_funcionarios)
		self.model_horarios = QStandardItemModel (0,3)
		self.model_horarios.setHorizontalHeaderLabels(['Dia da Semana','Entrada','Saida'])
		self.tableView_horarios.setModel(self.model_horarios)
		self.tableView_horarios.setShowGrid(False)
		self.pushButton_apagar.hide()

	##	Mostra todos os funcionarios na lista
	def mostrar_Funcionarios(self):
		funcionarios=self.db.obter_Funcionarios()
		if funcionarios==False:
			return False
		for funcionario in funcionarios:
			self.adiciona_ListView_Funcionarios(funcionario['nome'],funcionario['id_funcionario'])

	#	Adiciona um funcionario na lista de funcionarios
	#	@parm func Nome do fucionario que sera atualizado
	#	@parm id_funcionario Id do funcionario que sera atualizado
	def adiciona_ListView_Funcionarios(self,func=None,id_funcionario=None):
		if not hasattr(self,'lista_funcionarios'):
			self.lista_funcionarios=[]
		novo = QStandardItem(func)
		self.model_funcionarios.appendRow(novo)
		self.lista_funcionarios.append({'func':func,'id_funcionario':id_funcionario})
	
	#	Remove um funcionario da lista de funcionarios
	#	@parm func Nome do fucionario que sera removido
	#	@parm id_funcionario Id do funcionario que sera removido
	def remove_ListView_Funcionarios(self,func,id_funcionario):
		if not hasattr(self,'lista_funcionarios'):
			self.lista_funcionarios=[]
			return False
		if len(self.lista_funcionarios)<=0:
			return False
		for i in range(len(self.lista_funcionarios)):
			if isinstance(id_funcionario, str) or isinstance(id_funcionario, unicode) or isinstance(id_funcionario, long) or isinstance(id_funcionario, int):
				if self.lista_funcionarios[i]['id_funcionario']==id_funcionario:
					self.model_funcionarios.takeRow(i)
					del self.lista_funcionarios[i]
					break
			elif isinstance(func, str) or isinstance(func, unicode):
				if self.lista_funcionarios[i]['func']==func:
					self.model_funcionarios.takeRow(i)
					del self.lista_funcionarios[i]
					break
		return True

	##	Atualiza funcionarios na lista de funcionarios utilizando como parametro o nome do funcionario ou id, somente um dos dois dados é necessario
	#	@parm func Nome do fucionario que sera atualizado
	#	@parm id_funcionario Id do funcionario que sera atualizado
	#	@parm novo_nome Nome atualizado do funcionario
	def atualiza_ListView_Funcionarios(self,func=None,id_funcionario=None,novo_nome=None):
		if not hasattr(self,'lista_funcionarios'):
			self.lista_funcionarios=[]
			return False
		if len(self.lista_funcionarios)<=0:
			return False
		if novo_nome==None:
			return False
		for i in range(len(self.lista_funcionarios)):
			if isinstance(id_funcionario, str) or isinstance(id_funcionario, unicode) or isinstance(id_funcionario, long) or isinstance(id_funcionario, int):
				if self.lista_funcionarios[i]['id_funcionario']==id_funcionario:
					self.model_funcionarios.takeRow(i)
					novo = QStandardItem(novo_nome)
					self.model_funcionarios.insertRow(i,novo)
					self.lista_funcionarios[i]['func']=novo_nome
					break
			elif isinstance(func, str) or isinstance(func, unicode):
				if self.lista_funcionarios[i]['func']==func:
					self.model_funcionarios.takeRow(i)
					novo = QStandardItem(novo_nome)
					self.model_funcionarios.insertRow(i,novo)
					self.lista_funcionarios[i]['func']=novo_nome
					break
		return True

	##	Adiciona um horario na lista de horarios
	#	@parm dia_da_semana Dia da semana considerando domingo=0, segunda=1 etc
	#	@param horario_inicial Horario inicial no formato hh:mm:ss
	#	@param horario_final Horario final no formato hh:mm:ss
	#	@param id_horario Id para o horario não necessario atualmente
	def adiciona_TableView_Horarios(self,dia_da_semana,horario_inicial,horario_final,id_horario=None):
		if not (isinstance(dia_da_semana, int) or isinstance(dia_da_semana, long)):
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
		self.lista_horarios.append({"dia_da_semana":dia_da_semana,"horario_inicial":horario_inicial,"horario_final":horario_final,"id_horario":id_horario})
		return True

	##	Adiciona um horario na lista de horarios
	#	@parm posicao Indice inteiro do horario na lista
	#	@parm id_horario Id do horario para ser removido
	def remove_TableView_Horarios(self,posicao,id_horario=None):
		if not hasattr(self,'lista_horarios'):
			self.lista_horarios=[]
			return False
		if len(self.lista_horarios)<=0:
			return False

		if isinstance(posicao, int):
			try:
				if self.lista_horarios[posicao]['id_horario']!=None:
					self.lista_horarios_removidos.append(self.lista_horarios[posicao])
				del self.lista_horarios[posicao]
				self.model_horarios.takeRow(posicao)
				return True
			except Exception:
				return False

		if isinstance(id_horario, int):
			for i in range(len(self.lista_horarios)):
					if self.lista_horarios[i]['id_horario']==id_horario:
						if self.lista_horarios[i]['id_horario']!=None:
							self.lista_horarios_removidos.append(self.lista_horarios[i])
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
		if self.label_RFID.text()!="":
			dados['rfid']=self.label_RFID.text()
		else:
			dados['rfid']=None
		dados['horarios']=self.lista_horarios
		return dados

	##	Obtem os dados do horario atual que esta sendo adicionado
	def obter_Dados_Horarios(self):
		dados={}
		dados['horario_inicial']=str(string_2_Time(self.timeEdit_entrada.time().toString("HH:mm:ss")))
		dados['horario_final']=str(string_2_Time(self.timeEdit_saida.time().toString("HH:mm:ss")))
		dados['dia_da_semana']=self.comboBox_dias_semana.currentIndex()
		return dados

	##	Adiciona horarios para o funcionario atual
	def pushButton_Adicionar_Horario_Clicked(self):
		if not hasattr(self,'lista_funcionarios'):
			self.lista_funcionarios=[]
		dados=self.obter_Dados_Horarios()
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

	##	Botão de obter o RFID
	def pushButton_Obter_Rfid_Clicked(self):
		self.rfid_window=Obter_Rfid_Window(self,self.mainWindow)
		self.connect(self.rfid_window,SIGNAL("RFID_Obtido(QString)"),self.troca_Label_Rfid)

	def troca_Label_Rfid(self,rfid):
		if rfid!="":
			self.label_RFID.setText(rfid)
			self.pushButton_apagar.show()

	def apagar_Rfid(self):
		self.label_RFID.setText("")
		self.pushButton_apagar.hide()

	##	Limpa os campos
	def limpar_Campos(self):
		self.lineEdit_nome.setText("")
		self.lineEdit_matricula.setText("")
		self.label_RFID.setText("")
		self.pushButton_apagar.hide()
		while len(self.lista_horarios)>0:
			self.remove_TableView_Horarios(0)
		self.lista_horarios_removidos=[]

	##	Limpa os campos
	def inicializa_Campos(self,nome,matricula,rfid,horarios):
		self.limpar_Campos()
		self.lineEdit_nome.setText(nome)
		self.lineEdit_matricula.setText(matricula)
		if rfid!=None:
			self.label_RFID.setText(rfid)
			self.pushButton_apagar.show()
		if horarios!=False:
			for horario in horarios:
				self.adiciona_TableView_Horarios(horario['dia_da_semana'],str(horario['hora_inicial']),str(horario['hora_final']),horario['id_horario'])

##	Janela para obter o RFID
class Obter_Rfid_Window(QMainWindow,Ui_Obter_Rfid_Window):

	def __init__(self,parent=None,mainWindow=None):
		super(Obter_Rfid_Window, self).__init__(parent)
		self.setupUi(self)
		self.tempo=60
		self.rfid=""
		self.mainWindow=mainWindow
		self.inicio=datetime.now()
		self.connect(self.pushButton_Cancelar,SIGNAL("clicked()"),self.pushButton_Cancelar_Clicked)
		self.connect(self.pushButton_Salvar,SIGNAL("clicked()"),self.pushButton_Salvar_Clicked)
		self.connect( mainWindow, SIGNAL("RFID_Novo(QString)"), self.rfid_Novo)
		self.timer = QTimer(self)
		self.connect(self.timer, SIGNAL("timeout()"), self.atualiza_Tempo)
		self.timer.start(1000)
		self.center()
		self.show()

	##	Centraliza a janela
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	##	Cancela tudo e não salva
	def pushButton_Cancelar_Clicked(self):
		self.close()

	##	Salva o RFID
	def pushButton_Salvar_Clicked(self):
		self.emit(SIGNAL('RFID_Obtido(QString)'),self.rfid)
		self.close()

	def rfid_Novo(self,rfid):
		if self.rfid=="":
			self.rfid=rfid
			self.label_RFID.setText("RFID = "+rfid)
			self.tempo=0
			self.disconnect( self.mainWindow, SIGNAL("RFID_Novo(QString)"))

	##	Atualiza o tempo que falta
	def atualiza_Tempo(self):
		if self.tempo<=0:
			self.timer.stop()
			if self.rfid=="":
				self.close()
		else:
			self.tempo=self.tempo-1
		self.label_Tempo.setText(str(self.tempo))

	##	Fecha a conexão com o baco de dados
	def closeEvent(self, event):
		try:
			del self.db
		except Exception, e:
			pass

##	Janela para adicionar funcionarios
class Add_Funcionarios_Window(Funcionarios_Window):

	def __init__(self,parent=None,db_dados=None):
		super(Add_Funcionarios_Window, self).__init__(parent,db_dados)
		self.connect(self.pushButton_adicionar,SIGNAL("clicked()"),self.pushButton_Adicionar_Clicked)

	##	Adiciona um funcionario
	def pushButton_Adicionar_Clicked(self):
		dados=self.obter_Dados_Janela()
		if len(dados['nome'])<1:
			msgBox = QMessageBox()
			msgBox.setText("Digite o nome")
			msgBox.exec_()
			return
		if len(dados['matricula'])<1:
			msgBox = QMessageBox()
			msgBox.setText("Digite a matricula")
			msgBox.exec_()
			return

		existe=self.db.verifica_Ja_Existe(dados['nome'],dados['matricula'],dados['rfid'])
		if existe['existe']==True:
			erro_string=u"Erro\n"
			if existe['nome']:
				erro_string+=u"Nome ja existe\n"
			if existe['matricula']:
				erro_string+=u"Matricula ja existe\n"
			if existe['rfid']:
				erro_string+=u"Rfid ja existe\n"
			msgBox = QMessageBox()
			msgBox.setText(erro_string)
			msgBox.exec_()
		else:
			self.db.criar_Funcionario(dados['nome'],dados['matricula'],dados['rfid'])
			id_funcionario=self.db.obter_Id_Funcionario_por_Nome(dados['nome'])
			for horario in dados['horarios']:
				self.db.criar_Horario(id_funcionario,horario['dia_da_semana'],horario['horario_inicial'],horario['horario_final'])
			self.adiciona_ListView_Funcionarios(dados['nome'],id_funcionario)
			msgBox = QMessageBox()
			msgBox.setText("Funcionario adicionado")
			msgBox.exec_()
			self.limpar_Campos()

	##	Fecha a conexão com o baco de dados
	def closeEvent(self, event):
		try:
			del self.db
		except Exception, e:
			pass

##	Janela para atualizar funcionarios
class Atualiza_Funcionarios_Window(Funcionarios_Window):

	def __init__(self,parent=None,db_dados=None):
		super(Atualiza_Funcionarios_Window, self).__init__(parent,db_dados)
		self.connect(self.pushButton_adicionar,SIGNAL("clicked()"),self.pushButton_Atualizar_Clicked)
		variallixo=self.listView_funcionarios.selectionModel()
		self.listView_funcionarios.selectionModel().selectionChanged.connect(self.model_Funcionarios_Selection_Changed)
		self.troca_Nomes()

	def troca_Nomes(self):
		self.setWindowTitle("Editar Funcionarios")
		self.pushButton_adicionar.setText("Atualizar Funcionario")

	##	Adiciona um funcionario
	def pushButton_Atualizar_Clicked(self):
		funcionario=self.lista_funcionarios[self.listView_funcionarios.selectedIndexes()[0].row()]
		id_funcionario=funcionario['id_funcionario']
		dados=self.obter_Dados_Janela()
		if len(dados['nome'])<1:
			msgBox = QMessageBox()
			msgBox.setText("Digite o nome")
			msgBox.exec_()
			return
		if len(dados['matricula'])<1:
			msgBox = QMessageBox()
			msgBox.setText("Digite a matricula")
			msgBox.exec_()
			return
		existe=self.db.verifica_Ja_Existe(dados['nome'],dados['matricula'],dados['rfid'],id_funcionario)
		if existe['existe']==True:
			erro_string=u"Erro\n"
			if existe['nome']:
				erro_string+=u"Nome ja existe\n"
			if existe['matricula']:
				erro_string+=u"Matricula ja existe\n"
			if existe['rfid']:
				erro_string+=u"Rfid ja existe\n"
			msgBox = QMessageBox()
			msgBox.setText(erro_string)
			msgBox.exec_()
		else:
			self.db.atualizar_Funcionario(id_funcionario,dados['nome'],dados['matricula'],dados['rfid'])
			for horario in dados['horarios']:
				if horario['id_horario']==None:
					self.db.criar_Horario(id_funcionario,horario['dia_da_semana'],horario['horario_inicial'],horario['horario_final'])
			for horario in self.lista_horarios_removidos:
				self.db.remover_Horario(horario['id_horario'])
			self.atualiza_ListView_Funcionarios(None,id_funcionario,dados['nome'])
			msgBox = QMessageBox()
			msgBox.setText("Funcionario atualizado")
			msgBox.exec_()
			self.limpar_Campos()

	def model_Funcionarios_Selection_Changed(self):
		funcionario=self.lista_funcionarios[self.listView_funcionarios.selectedIndexes()[0].row()]
		horarios=self.db.buscar_Horarios_de_Funcionario(funcionario['id_funcionario'])
		dados=self.db.obter_Funcionario(funcionario['id_funcionario'])
		self.inicializa_Campos(dados['nome'],dados['matricula'],dados['rfid'],horarios)

	##	Fecha a conexão com o baco de dados
	def closeEvent(self, event):
		try:
			del self.db
		except Exception, e:
			pass

##	Janela para remover funcionarios
class Remover_Funcionarios_Window(QMainWindow,Ui_Remover_Funcionarios_Window):

	def __init__(self,parent=None,db_dados=None):
		super(Remover_Funcionarios_Window, self).__init__(parent)
		self.setupUi(self)
		self.db=Connect_Db(db_dados)
		self.center()
		self._set_connections()
		self.show()
		self.model_funcionarios = QStandardItemModel(self.listView_funcionarios)
		self.listView_funcionarios.setModel(self.model_funcionarios)
		self.mostrar_Funcionarios()

	##	Faz todas a conexões de eventos
	def _set_connections(self):
		self.connect(self.pushButton_remover_funcionario,SIGNAL("clicked()"),self.pushButton_Remover_Funcionario_Clicked)

	##	Centraliza a janela
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	##	Mostra todos os funcionarios na lista
	def mostrar_Funcionarios(self):
		funcionarios=self.db.obter_Funcionarios()
		if funcionarios==False:
			return False
		for funcionario in funcionarios:
			self.adiciona_ListView_Funcionarios(funcionario['nome'],funcionario['id_funcionario'])

	#	Adiciona um funcionario na lista de funcionarios
	#	@parm func Nome do fucionario que sera atualizado
	#	@parm id_funcionario Id do funcionario que sera atualizado
	def adiciona_ListView_Funcionarios(self,func=None,id_funcionario=None):
		if not hasattr(self,'lista_funcionarios'):
			self.lista_funcionarios=[]
		novo = QStandardItem(func)
		self.model_funcionarios.appendRow(novo)
		self.lista_funcionarios.append({'func':func,'id_funcionario':id_funcionario})
	
	#	Remove um funcionario da lista de funcionarios
	#	@parm func Nome do fucionario que sera removido
	#	@parm id_funcionario Id do funcionario que sera removido
	def remove_ListView_Funcionarios(self,func,id_funcionario):
		if not hasattr(self,'lista_funcionarios'):
			self.lista_funcionarios=[]
			return False
		if len(self.lista_funcionarios)<=0:
			return False
		for i in range(len(self.lista_funcionarios)):
			if isinstance(id_funcionario, str) or isinstance(id_funcionario, unicode) or isinstance(id_funcionario, long) or isinstance(id_funcionario, int):
				if self.lista_funcionarios[i]['id_funcionario']==id_funcionario:
					self.model_funcionarios.takeRow(i)
					del self.lista_funcionarios[i]
					break
			elif isinstance(func, str) or isinstance(func, unicode):
				if self.lista_funcionarios[i]['func']==func:
					self.model_funcionarios.takeRow(i)
					del self.lista_funcionarios[i]
					break
		return True

	##	Remove o funcionario
	def pushButton_Remover_Funcionario_Clicked(self):
		for i in self.listView_funcionarios.selectedIndexes():
			self.db.remover_Funcionario(self.lista_funcionarios[i.row()]['id_funcionario'])
			self.remove_ListView_Funcionarios(None,self.lista_funcionarios[i.row()]['id_funcionario'])

	##	Fecha a conexão com o baco de dados
	def closeEvent(self, event):
		try:
			del self.db
		except Exception, e:
			pass

##	Janela para visualizar os horarios dos funcionarios
class Horarios_Window(QMainWindow,Ui_Horarios_Window):

	def __init__(self,parent=None,db_dados=None):
		super(Horarios_Window, self).__init__(parent)
		self.setupUi(self)
		self.db=Connect_Db(db_dados)
		self.center()
		self._configure()
		self.show()
		self.mostra_Todos()

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
		self.tableView_horarios.setSortingEnabled(False)
		self.tableView_horarios.setModel(self.model_horarios)

	##	Adiciona um horario na lista de horarios
	#	@parm dia_da_semana Dia da semana considerando domingo=0, segunda=1 etc
	#	@param horario_inicial Horario inicial no formato hh:mm:ss
	#	@param horario_final Horario final no formato hh:mm:ss
	#	@param id_horario Id para o horario não necessario atualmente
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

	##	Mostra todos os funcionarios
	def mostra_Todos(self):
		horarios=self.db.obter_Horarios()
		if horarios!=False:
			for horario in horarios:
				self.adiciona_TableView_Horarios(horario[0],int(horario[1]),str(horario[2]),str(horario[3]))

	##	Fecha a conexão com o baco de dados
	def closeEvent(self, event):
		try:
			del self.db
		except Exception, e:
			pass

##	Janela para gerar os relatorios
class Relatorios_Window(QMainWindow,Ui_Relatorios_Window):

	def __init__(self,parent=None,db_dados=None):
		super(Relatorios_Window, self).__init__(parent)
		self.setupUi(self)
		self.db_dados=db_dados
		self.db=Connect_Db(db_dados)
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
		dados=self.obter_Dados()
		self.thread1 = Relatorios(self,self.db_dados,False,True,dados)
		self.thread1.start()

	##	Gera o relatorio de pontos
	def pushButton_Relatorio_Pontos_Clicked(self):
		dados=self.obter_Dados()
		self.thread2 = Relatorios(self,self.db_dados,True,False,dados)
		self.thread2.start()

	##	Fecha a conexão com o baco de dados
	def closeEvent(self, event):
		try:
			del self.db
		except Exception, e:
			pass

##	Thread para gerar os relatorios e não travar a interface grafica
class Relatorios(QThread):
	def __init__(self, parent = None,db_dados = None,pontos=False,porta=False,dados=None):
		QThread.__init__(self, parent)
		self.db=Connect_Db(db_dados)
		self.pontos=pontos
		self.porta=porta
		self.dados=dados

	def run(self):
		if self.pontos!=False:
			self.relatorio_Pontos(self.dados)
		if self.porta!=False:
			self.relatorio_Porta(self.dados)

	##	Gera o relatorio de pontos
	def relatorio_Pontos(self,dados):
		relatorio=self.db.obter_Log_Pontos(dados['data_inicial'],dados['data_final'])
		if relatorio==None:
			return
		linux=platform.system()=='Linux'
		windows=platform.system()=='Windows'
		nome_arquivo=""
		if linux:
			full_path = os.path.realpath(__file__)
			directory=os.path.dirname(full_path)
			if directory[-1]!='/':
				directory="%s/"%(directory)
			extensao='.csv'
			arquivo=datetime.now().strftime('log_pontos_%d_%m_%Y')
			nome_arquivo=directory+"relatorios/"+arquivo+extensao
		if windows:
			directory=os.environ['USERPROFILE']+'\\My Documents\\'
			extensao='.csv'
			arquivo=datetime.now().strftime('log_pontos_%d_%m_%Y')
			nome_arquivo=directory+"relatorios\\"+arquivo+extensao
		print nome_arquivo
		relatorio_csv=CSV(nome_arquivo)
		relatorio_csv.writerow((u"Nome",u"Matricula",u"Horario de entrada",u"Horario de saida",u"Tempo de permanencia",u"Presença"))
		for linha in relatorio:
			relatorio_csv.writerow(linha)
		relatorio_csv.finaliza()

	##	Gera o relatorio de logs da porta
	def relatorio_Porta(self,dados):
		relatorio=self.db.obter_Log_Porta(dados['data_inicial'],dados['data_final'])
		if relatorio==None:
			return
		linux=platform.system()=='Linux'
		windows=platform.system()=='Windows'
		nome_arquivo=""
		if linux:
			full_path = os.path.realpath(__file__)
			directory=os.path.dirname(full_path)
			if directory[-1]!='/':
				directory="%s/"%(directory)
			extensao='.csv'
			arquivo=datetime.now().strftime('log_porta_%d_%m_%Y')
			nome_arquivo=directory+"relatorios/"+arquivo+extensao
		if windows:
			directory=os.environ['USERPROFILE']+'\\My Documents\\'
			extensao='.csv'
			arquivo=datetime.now().strftime('log_porta_%d_%m_%Y')
			nome_arquivo=directory+"relatorios\\"+arquivo+extensao
		relatorio_csv=CSV(nome_arquivo)
		relatorio_csv.writerow((u"Nome",u"Matricula",u"Horario de entrada"))
		for linha in relatorio:
			relatorio_csv.writerow(linha)
		relatorio_csv.finaliza()

##	Janela para configurar as tolerancias
class Tolerancias_Window(QMainWindow,Ui_Tolerancias_Window):

	def __init__(self,parent=None,db_dados=None):
		super(Tolerancias_Window, self).__init__(parent)
		self.setupUi(self)
		self.db=Connect_Db(db_dados)
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
		dados=self.obter_Tolerancias()
		self.timeEdit_entrada_antes.setDisplayFormat("HH:mm:ss")
		self.timeEdit_entrada_depois.setDisplayFormat("HH:mm:ss")
		self.timeEdit_saida_antes.setDisplayFormat("HH:mm:ss")
		self.timeEdit_saida_depois.setDisplayFormat("HH:mm:ss")
		self.timeEdit_atraso.setDisplayFormat("HH:mm:ss")
		self.timeEdit_entrada_antes.setTime(QTime.fromString(dados['entrada_antes'],'HH:mm:ss'))
		self.timeEdit_entrada_depois.setTime(QTime.fromString(dados['entrada_depois'],'HH:mm:ss'))
		self.timeEdit_saida_antes.setTime(QTime.fromString(dados['saida_antes'],'HH:mm:ss'))
		self.timeEdit_saida_depois.setTime(QTime.fromString(dados['saida_depois'],'HH:mm:ss'))
		self.timeEdit_atraso.setTime(QTime.fromString(dados['atraso'],'HH:mm:ss'))

	def obter_Tolerancias(self):
		self.db.obter_Configuracoes('tol_ent_ant')
		dados={}
		dados['entrada_antes']=self.db.obter_Configuracoes('tol_ent_ant')
		dados['entrada_depois']=self.db.obter_Configuracoes('tol_ent_dep')
		dados['saida_antes']=self.db.obter_Configuracoes('tol_sai_ant')
		dados['saida_depois']=self.db.obter_Configuracoes('tol_sai_dep')
		dados['atraso']=self.db.obter_Configuracoes('considerar_atraso')
		return dados

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
		dados['entrada_antes']=str(self.timeEdit_entrada_antes.time().toPython())
		dados['entrada_depois']=str(self.timeEdit_entrada_depois.time().toPython())
		dados['saida_antes']=str(self.timeEdit_saida_antes.time().toPython())
		dados['saida_depois']=str(self.timeEdit_saida_depois.time().toPython())
		dados['atraso']=str(self.timeEdit_atraso.time().toPython())
		return dados

	##	Salva as configurações
	def pushButton_Salvar_Clicked(self):
		dados=self.obter_Dados()
		self.db.atualizar_Configuracoes('tol_ent_ant',dados['entrada_antes'])
		self.db.atualizar_Configuracoes('tol_ent_dep',dados['entrada_depois'])
		self.db.atualizar_Configuracoes('tol_sai_ant',dados['saida_antes'])
		self.db.atualizar_Configuracoes('tol_sai_dep',dados['saida_depois'])
		self.db.atualizar_Configuracoes('considerar_atraso',dados['atraso'])
		msgBox = QMessageBox(self)
		msgBox.setText(u"As tolerancia foram alteradas")
		msgBox.exec_()
		self.close()

	##	Fecha a conexão com o baco de dados
	def closeEvent(self, event):
		try:
			del self.db
		except Exception, e:
			pass