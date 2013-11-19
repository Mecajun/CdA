# -*- coding: utf-8 -*-

import model_mysql
import wx
import threading
import time
import datetime
import os
from wx.lib.pubsub import Publisher
import md5
import csv

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
    
def dia_Semana_Int2str(num,completo=False):
    dias=['Dom','Seg','Ter','Qua','Qui','Sex','Sab']
    dias2=['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sabado']
    if completo==True:
        return dias2[num-1]
    return dias[num-1]

def edita_Funcionario(db,dados):
    if dados['nome']==None and dados['matricula']==None and dados['rfid']==None:
        return
    db.atualizar_Funcionario(dados['id'], nome=dados['nome'], matricula=dados['matricula'], rfid=dados['rfid'])

def detalha_Funcionario(db,nome=None,id_funcionario=None):
    if (nome or id_funcionario) == None:
        return None
    id_func=None
    dados={}
    if nome != None:
        id_func=db.obter_Id_Funcionario_por_Nome(nome)
    else:
        id_func=id_funcionario
    dados['id'],dados['nome'],dados['matricula'],dados['rfid'],dados['ativo']=db.obter_Dados_Funcionario(id_func)
    dados['horarios']=[]
    temp_horarios=db.buscar_Horarios_de_Funcionario(id_func)
    if temp_horarios:
        for horario in temp_horarios:
            dados['horarios'].append({"dia_semana":horario[2],"hora_inicial":str(horario[3].seconds/60/60).zfill(2)+':'+str(horario[3].seconds/60%60).zfill(2),"hora_final":(str(horario[4].seconds/60/60).zfill(2)+':'+str(horario[4].seconds/60%60).zfill(2))})
    return dados

def validar_Criacao_Funcionario(db,dados):
    return db.verifica_Ja_Existe(nome=dados['nome'],matricula=dados['matricula'],rfid=dados['rfid'])

def cadastrar_Funcionario(db,dados):
    db.criar_Funcionario(nome=dados['nome'],matricula=dados['matricula'],rfid=dados['rfid'])
    id_func=db.obter_Id_Funcionario_por_Matricula(matricula=dados['matricula'])
    for horario in dados['horarios']:
        db.criar_Horario(id_funcionario=id_func,dia_da_semana=horario['dia_semana'],hora_inicial=horario['hora_inicial'],hora_final=horario['hora_final'])
    # print  detalha_Funcionario(db,id_funcionario=id_func)
        
def remover_Funcionario(db,id_funcionario):
    db.remover_Funcionario(id_funcionario)

def obter_Rfid(id_funcionario):
    "nada"    

def gerar_Relatorio_Porta(dados):
    vet=[]
    vet.append(["Nome","Matricula","Entrada"])
    for elem in dados:
        vet2=[]
        vet2.append(elem[0])
        vet2.append(elem[1])
        tempo = elem[2].strftime('%d/%m/%Y - %H:%M')
        vet2.append(tempo)
        vet.append(vet2)

    full_path = os.path.realpath(__file__)
    directory=os.path.dirname(full_path)
    if directory[-1]!='/':
        directory="%s/"%(directory)
    extensao='.csv'
    arquivo=datetime.datetime.now().strftime('log_porta_%d_%m_%Y')
    nome_arquivo=directory+"relatorios/"+arquivo+extensao
    saida=csv.writer(file(nome_arquivo, 'w'))
    for linha in vet:
        saida.writerow(linha)

def gerar_Relatorio_Pontos(dados):
    vet=[]
    vet.append(["Nome","Matricula","Entrada","Saida","Atraso Entrada","Atraso Saida","Flag"])
    for elem in dados:
        vet2 = []
        #nome do usuario
        vet2.append(elem[0])
        #matricula
        vet2.append(elem[1])
        #hora de entrada
        hora=""
        if elem[2]!=None:
            hora = elem[2].strftime('%d/%m/%Y - %H:%M')
        #hora de saida
        hora1=""
        if elem[3]!=None:
            hora1 = elem[3].strftime('%d/%m/%Y - %H:%M')
        vet2.append(hora)
        vet2.append(hora1)
        vet2.append(str(elem[4]))
        vet2.append(str(elem[5]))
        if elem[6] == 1:
            vet2.append('sem atraso')
        elif elem[6] == -2:
            vet2.append('nao veio')
            vet2[-3]=None
        elif elem[6] == -3:
            vet2.append('chegou atrasado')
        elif elem[6] == -4:
            vet2.append('saiu com atraso')
        elif elem[6] == -5:
            vet2.append('chegou e saiu com atraso')
        elif elem[6] == -1:
            vet2.append('ponto aberto')
        vet.append(vet2)

    full_path = os.path.realpath(__file__)
    directory=os.path.dirname(full_path)
    if directory[-1]!='/':
        directory="%s/"%(directory)
    extensao='.csv'
    arquivo=datetime.datetime.now().strftime('log_pontos_%d_%m_%Y')
    nome_arquivo=directory+"relatorios/"+arquivo+extensao
    saida=csv.writer(file(nome_arquivo, 'w'))
    for linha in vet:
        saida.writerow(linha)

def gerar_Relatorio(db,inicial,final,condicoes):
    log_porta=db.obter_Log_Porta(inicial,final)
    log_pontos=db.obter_Log_Pontos(inicial,final,condicoes['pontuais'],condicoes['faltas'],condicoes['atrasos'])
    gerar_Relatorio_Porta(log_porta)
    gerar_Relatorio_Pontos(log_pontos)

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
    if data >= (date2-datetime.timedelta(minutes=li)) and data <= (date2+datetime.timedelta(minutes=ls)):
        return True
    else:
        return False

def delta_To_Time_Str(delta):
    return (delta+datetime.datetime.min).time().strftime("%H:%M")

def abrir_Porta():
    print "Sinal de abrir a porta"

def atrazo(a,b):
    return seconds_to_time((a-b).total_seconds())

def atualizar_Horarios(db,dados):
    for horario in dados['horario_adicionado']:
        db.criar_Horario(dados['id'],horario['dia_semana'],horario['hora_inicial'],horario['hora_final'])
    for horario in dados['horario_removido']:
        db.remover_Horario_Data_Hora(dados['id'],horario['dia_semana'],horario['hora_inicial'],horario['hora_final'])

def seconds_to_time(sec):
    sec=int(sec)
    sinal=""
    if sec<0:
        sinal="-"
    sec=abs(sec)
    hora=sec/60/60
    sec=sec-hora*60*60
    mim=sec/60
    sec=sec-mim*60
    return "%s%d:%d:%d"%(sinal,hora,mim,sec)

def atrazo_Entrada(temp,horario):
    agora=temp-datetime.datetime(temp.year,temp.month,temp.day,0,0,0)
    atrazo=agora-horario
    return seconds_to_time(atrazo.total_seconds())

def dar_Ponto(db,matricula):
    id_func=db.obter_Id_Funcionario_por_Matricula(matricula)
    if id_func!=None:
        db.adicionar_Log_Porta(id_func,obter_Data_Hora())
        abrir_Porta()
    else:
        return "nao existe"
    
    horario_atual=obter_Horario_Atual()

    # Obtem os limites de tempo para considerar o ponto entrada
    limite_inferior=int(db.obter_Configuracoes('tol_ent_ant')[2])
    limite_superior=int(db.obter_Configuracoes('tol_ent_dep')[2])

    #  Obtem os limites de tempo para considerar o ponto de saida
    limite_inferior_saida=int(db.obter_Configuracoes('tol_sai_ant')[2])
    limite_superior_saida=int(db.obter_Configuracoes('tol_sai_dep')[2])

    # Verifica se existe algum ponto aberto
    ponto_antigo=db.buscar_Ponto_Aberto_de_Funcionario(id_func)

    agora=datetime.datetime.now()

    if ponto_antigo!=None:
        entrada=ponto_antigo[1]
        entrada_teorico=ponto_antigo[2]
        saida_teorico=ponto_antigo[3]
        entrada_teorico_datatime=datetime.datetime.combine(entrada.date(),(datetime.datetime.min+entrada_teorico).time())
        saida_teorico_datatime=datetime.datetime.combine(entrada.date(),(datetime.datetime.min+saida_teorico).time())
        # Verifica o tipo de ponto

        # Horario de saida
        if verifica_Esta_Faixa_Valores(agora,saida_teorico_datatime,limite_inferior_saida,limite_superior_saida):
            db.finaliza_Ponto(id_func,obter_Data_Hora(),atrazo(agora,saida_teorico_datatime),1)
            return
        # Horario maior que o de saida
        elif agora > (saida_teorico_datatime+datetime.timedelta(minutes=limite_superior_saida)):
            db.finaliza_Ponto(id_func,obter_Data_Hora(),atrazo(agora,saida_teorico_datatime),-3)
        # Horario que não faz nada
        else:
            return

    # Verifica se tem horario para bater o ponto
    horario=db.buscar_Horario_Mais_Proximo_de_Funcionario(int(id_func),horario_atual['dia_semana'],horario_atual['horario'],transforma_Horario_Int_Str(0,limite_inferior),transforma_Horario_Int_Str(0,limite_superior))
    print horario
    # Cria o ponto de entrada
    if horario!=None:
        db.criar_Ponto(id_func,horario[0],obter_Data_Hora(),atrazo_Entrada(agora,horario[3]))
    else:
        return

def obter_Horarios(db):
    horarios=db.obter_Horarios()
    horarios_2=[]
    if horarios!=None:
        for horario in horarios:
            horarios_2.append((horario[0],dia_Semana_Int2str(horario[1],True),delta_To_Time_Str(horario[2]),delta_To_Time_Str(horario[3])))
        return horarios_2
    else:
        return None

class Relogio(threading.Thread):
    def __init__ (self):
        super(Relogio, self).__init__()
        self.start()

    def run (self):
        while True:
            hora=datetime.datetime.now().strftime("     %Y/%m/%d\n     %H:%M:%S")
            wx.CallAfter(Publisher().sendMessage, "evento_mostrar_relogio", hora)
            time.sleep(1)

class Fecha_Pontos(threading.Thread):
    def __init__ (self,db):
        super(Fecha_Pontos, self).__init__()
        self.db=db
        self.esperados=None
        self.anterior=None
        self.alterados=None
        self.start()

    def run (self):
        while True:
            self.atualiza()
            time.sleep(10)

    def atualiza(self):
        limite_superior=transforma_Horario_Int_Str(0,int(self.db.obter_Configuracoes('tol_ent_dep')[2]))
        limite_inferior=transforma_Horario_Int_Str(0,int(self.db.obter_Configuracoes('tol_ent_ant')[2]))
        horario_atual=obter_Horario_Atual()
        self.esperados=self.db.buscar_Funcionarios_Esperados(horario_atual['dia_semana'],limite_inferior,limite_superior)
        self.esperados_n_abertos=self.db.buscar_Funcionarios_Esperados_Nao_Abertos(horario_atual['dia_semana'],limite_inferior,limite_superior)

        temp1=[]
        temp2=[]
        logados=[]
        # print esperados_gui
        if self.esperados!=None:
            temp1=[ x[0] for x in self.esperados]
        if self.esperados_n_abertos!=None:
            temp2=[ x[0] for x in self.esperados_n_abertos]
        logados=[ (x,0) for x in temp1 if x not in temp2]+[ (x,1) for x in temp1 if x in temp2]
            # print logados
        wx.CallAfter(Publisher().sendMessage, "evento_funcionarios_esperados", logados)

        if self.esperados!=None:
            self.agora=[x[1:3] for x in self.esperados]
            if self.anterior!=None:
                self.alterados=[ x for x in self.anterior if x not in self.agora ]
            else:
                self.alterados=None
            self.anterior=self.agora
        else:
            self.alterados=self.anterior
            self.agora=None
            self.anterior=None
        
        if self.alterados!=None and len(self.alterados)>0:
            for alt in self.alterados:
                if self.db.buscar_Ponto_Aberto_de_Funcionario(alt[1])==None:
                    self.db.criar_Ponto(alt[1],alt[0],obter_Data_Hora(),"00:00:00",-2)

class Instalar():
    def __init__(self,db):
        self.db=db
    def criar_Data_Base(self):
        db.dropar_Tabelas()        
        db.criar_Tabelas()
    def configurar_Data_Base(self):
        db.criar_Configuracoes('adm_senha',criptografar_Senha('42'))
        db.criar_Configuracoes('tol_ent_ant','10')
        db.criar_Configuracoes('tol_ent_dep','10')
        db.criar_Configuracoes('tol_sai_ant','10')
        db.criar_Configuracoes('tol_sai_dep','10')
        db.criar_Configuracoes('considerar_atraso','5')

if __name__ == "__main__":
    db=model_mysql.Connect_MySQL('localhost','root','42')
    ins=Instalar(db)
    ins.criar_Data_Base()
    ins.configurar_Data_Base()