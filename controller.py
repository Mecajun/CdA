# -*- coding: utf-8 -*-

import model_mysql
import wx
import threading
import time
import datetime
import os
from wx.lib.pubsub import Publisher
import md5

class Comunica_Arduino(threading.Thread):
    def __init__(self):
        super(Comunica_Arduino, self).__init__()
        import serial
        try:
            self.ser = serial.Serial('/dev/ttyUSB0', 9600)
        except:
            print "Arduino não conectado"
        Publisher().subscribe(self.mandar_Dados, "evento_enviar_dados_arduino")
        self.start()

    def run(self):
         while True:
             wx.CallAfter(Publisher().sendMessage, "evento_chegaram_dados_arduino", self.obter_Dados())

    def obter_Dados(self):
        time.sleep(1)
        try:
            return self.ser.readline()
        except:
            return "Falha ao obter dados do arduino"

    def mandar_Dados(self,dados):
        try:
            self.ser.write(dados.data)
        except:
            return "Falha ao obter mandar dados para o arduino"

class Main_Controller():
    horarios_temp=None
    
    def falar(texto):
        os.system('espeak -v brazil "'+texto+'"')

def criptografar_Senha(senha):
    m = md5.new()
    for i in range(32):
        m.update(senha)
    return m.hexdigest()

def verifica_Senha_Adm(db,senha):
    temp_senha = db.obter_Configuracoes("adm_senha")
    if temp_senha[2] == criptografar_Senha(senha):
        return True
    else:
        return False
    
def dia_Semana_Int2str(num):
    dias=['Dom','Seg','Ter','Qua','Qui','Sex','Sab']
    return dias[num-1]
        
def detalha_Funcionario(db,nome=None,id_funcionario=None):
    if (nome or id_funcionario) == None:
        return None
    id_func=None
    dados={}
    if nome != None:
        id_func=db.obter_Id_Funcionario_por_Nome(nome)
    else:
        id_func=id_funcionario
    dados['id'],dados['nome'],dados['matricula'],dados['rfid']=db.obter_Dados_Funcionario(id_func)
    dados['horarios']=[]
    temp_horarios=db.buscar_Horarios_de_Funcionario(id_func)
    for horario in temp_horarios:
        dados['horarios'].append(dia_Semana_Int2str(horario[2])+' '+str(horario[3].seconds/60/60)+':'+str(horario[3].seconds/60%60)+' - '+str(horario[4].seconds/60/60)+':'+str(horario[4].seconds/60%60))
    return dados

def cadastrar_Funcionario(db,dados):
    db.criar_Funcionario(nome=dados['nome'],matricula=dados['matricula'],rfid=dados['rfid'])
    id_func=db.obter_Id_Funcionario_por_Matricula(matricula=dados['matricula'])
    for horario in dados['horarios']:
        db.criar_Horario(id_funcionario=id_func,dia_da_semana=horario['dia_semana'],hora_inicial=horario['hora_inicial'],hora_final=horario['hora_final'])
    print  detalha_Funcionario(db,id_funcionario=id_func)
        
def remover_Funcionario(db,id_funcionario):
    db.remover_Funcionario(id_funcionario)

def obter_Rfid(id_funcionario):
    "nada"    

def gerar_Relatorio(db,inicial,final,condicoes):
    log_porta=db.obter_Log_Porta(inicial,final)
    log_pontos=db.obter_Log_Pontos(inicial,final,condicoes['pontuais'],condicoes['faltas'],condicoes['atrasos'])
    print log_porta
    print log_pontos

def atualizar_Rfid(db,id_funcionario,rfid):
    db.atualizar_Funcionario(id_funcionario,rfid=rfid)

class Relogio(threading.Thread):
    def __init__ (self):
        super(Relogio, self).__init__()
        self.start()

    def run (self):
        while True:
            hora=time.asctime()
            wx.CallAfter(Publisher().sendMessage, "evento_mostrar_relogio", hora)
            time.sleep(1)

class Instalar():
    def __init__(self,db):
        self.db=db
    def criar_Data_Base(self):
        db.criar_Tabelas()
    def configurar_Data_Base(self):
        db.criar_Configuracoes('adm_senha',criptografar_Senha('42'))

if __name__ == "__main__":
    db=model_mysql.Connect_MySQL('localhost','root','42')
    ins=Instalar(db)
    ins.criar_Data_Base()
    ins.configurar_Data_Base()
