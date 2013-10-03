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

def falar(texto):
    texto="Olá "+texto+", seja bem vindo a Mecajun"
    print texto
    # os.system('espeak -v brazil "'+texto+'"')

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

def alterar_Senha_Adm(db,senha):
    db.atualizar_Configuracoes("adm_senha",criptografar_Senha(senha))
    
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

def listar_Funcionarios(db):
    funcionarios=db.obter_Funcionarios()
    return funcionarios

def obter_Configuracoes(db):
    dados={}
    dados['tol_ent_ant']=int(db.obter_Configuracoes('tol_ent_ant')[2])
    dados['tol_ent_dep']=int(db.obter_Configuracoes('tol_ent_dep')[2])
    dados['tol_sai_ant']=int(db.obter_Configuracoes('tol_sai_ant')[2])
    dados['tol_sai_dep']=int(db.obter_Configuracoes('tol_sai_dep')[2])
    dados['considerar_atraso']=int(db.obter_Configuracoes('considerar_atraso')[2])
    return dados

def atualizar_Configuracao(db,config,dado):
    db.atualizar_Configuracoes(config,str(dado))

def obter_Horario_Atual():
    horario_atual=datetime.datetime.now()
    dia_semana=horario_atual.weekday()
    dia_semana=dia_semana+2
    if dia_semana==8:
        dia_semana=1
    return {'dia_semana':dia_semana,'horario':horario_atual.strftime("%H:%M:%S"),'data':horario_atual.strftime("%Y:%m:%d")}

def obter_Data_Hora():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def transforma_Horario_Int_Str(hora,minuto):
    return str(hora+minuto//60)+":"+str(minuto%60)+":00"

# Verifica se data esta entre date2-li e date2+ls
def verifica_Esta_Faixa_Valores(data,date2,li,ls):
    print data
    print date2
    print datetime.timedelta(minutes=li)
    if data >= (date2-datetime.timedelta(minutes=li)) and data <= (date2+datetime.timedelta(minutes=ls)):
        return True
    else:
        return False

def dar_Ponto(db,matricula):
    id_func=db.obter_Id_Funcionario_por_Matricula(matricula)
    horario_atual=obter_Horario_Atual()

    # Obtem os limites de tempo para considerar o ponto entrada
    limite_inferior=int(db.obter_Configuracoes('tol_ent_ant')[2])
    limite_superior=int(db.obter_Configuracoes('tol_ent_dep')[2])

    #  Obtem os limites de tempo para considerar o ponto de saida
    limite_inferior_saida=int(db.obter_Configuracoes('tol_sai_ant')[2])
    limite_superior_saida=int(db.obter_Configuracoes('tol_sai_dep')[2])

    # Verifica se existe algum ponto aberto
    ponto_antigo=db.buscar_Ponto_Aberto_de_Funcionario(id_func)

    if ponto_antigo!=None:
        entrada=ponto_antigo[1]
        entrada_teorico=ponto_antigo[2]
        saida_teorico=ponto_antigo[3]
        entrada_teorico_datatime=datetime.datetime.combine(entrada.date(),(datetime.datetime.min+entrada_teorico).time())
        saida_teorico_datatime=datetime.datetime.combine(entrada.date(),(datetime.datetime.min+saida_teorico).time())
        # Verifica o tipo de ponto
        ponto=None
        if ponto_antigo!=None:
            agora=datetime.datetime.now()
            if verifica_Esta_Faixa_Valores(agora,entrada_teorico_datatime,limite_inferior,limite_superior):
                ponto="Entrada"
            elif verifica_Esta_Faixa_Valores(agora,saida_teorico_datatime,limite_inferior_saida,limite_superior_saida):
                ponto="Saida"
            elif agora > (saida_teorico_datatime+datetime.timedelta(minutes=limite_superior_saida)):
                ponto="Nao fexou"
            else:
                ponto="Fora horario"

        # Passou de novo mas o ponto ja esta aberto, so abre a porta e nao faz nada
        if ponto=="Entrada":
            return
        # Da o ponto de saida
        if ponto=="Saida":
            db.finaliza_Ponto(id_func,obter_Data_Hora(),"00:00:00",1)
            return
        # Fecha o ponto
        if ponto=="Nao fexou":
            db.finaliza_Ponto(id_func,obter_Data_Hora(),"00:00:00",-1)
        # Fora do horario, so abre a porta
        if ponto=="Fora horario":
            return

    # Verifica se tem horario para bater o ponto
    horario=db.buscar_Horario_Mais_Proximo_de_Funcionario(int(id_func),horario_atual['dia_semana'],horario_atual['horario'],transforma_Horario_Int_Str(0,limite_inferior),transforma_Horario_Int_Str(0,limite_superior))
    
    # Cria o ponto de entrada
    if horario!=None:
        db.criar_Ponto(id_func,horario[0],obter_Data_Hora(),"00:00:00")
        falar(db.obter_Funcionario_Basico(id_func)[1])
    else:
        print "não tem ponto"

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
