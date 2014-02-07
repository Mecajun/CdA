# -*- coding: utf-8 -*-
import md5
import sys
import os
from datetime import datetime,timedelta

class CSV():
    """docstring for CSV"""
    def __init__(self, file_name, mode='w+', separador=','):
        try:
            self.file=open(file_name,mode)
        except Exception:
            full_path = os.path.realpath(__file__)
            directory=os.path.dirname(full_path)
            os.makedirs(directory+"/relatorios")
        finally:
            self.file=open(file_name,mode)
        self.separador=separador
    def writerow(self,linha):
        temp_str=u""
        for elem in linha:
            try:
                if not (isinstance(elem, str) or isinstance(elem, unicode)):
                    temp_str=temp_str+str(elem)+self.separador
                else:
                    temp_str=temp_str+elem+self.separador
            except UnicodeDecodeError:
                print elem
        temp_str=temp_str[:-len(self.separador)]+'\n'
        self.file.write(temp_str.encode('utf8'))
    
    def finaliza(self):
        self.file.close()

def criptografar_Senha(senha):
    m = md5.new()
    for i in range(32):
        m.update(senha)
    return m.hexdigest()

def dia_Semana_Int2str(num,completo=True):
    dias=[u'Dom',u'Seg',u'Ter',u'Qua',u'Qui',u'Sex',u'Sab']
    dias2=[u'Domingo',u'Segunda',u'Terça',u'Quarta',u'Quinta',u'Sexta',u'Sabado']
    if completo==True:
        return dias2[num]
    return dias[num]

##  Altera o nome do processo
#   @parm newname Novo nome do processo
def set_proc_name(newname):
    from ctypes import cdll, byref, create_string_buffer
    libc = cdll.LoadLibrary('libc.so.6')
    buff = create_string_buffer(len(newname)+1)
    buff.value = newname
    libc.prctl(15, byref(buff), 0, 0, 0)

def get_Week_Day(data=None):
    wd=None
    if data==None:
        wd=datetime.now().weekday()+1
    else:
        wd=data.weekday()+1
    return wd if wd!=7 else 0

def string_2_Timedelta(tempo):
    t1 = datetime.strptime(tempo, '%H:%M:%S')
    t2 = datetime.strptime("00:00:00", '%H:%M:%S')
    return t1-t2

def string_2_Time(tempo):
    return str(string_2_Timedelta(tempo))

def string_2_Datetime(data):
    return datetime.strptime(data, "%Y-%m-%d %H:%M:%S.%f")

def data_Atual(string=False):
    if string==True:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return datetime.now()

def falar(ponto,nome):
    mensagem=u""
    if ponto==2:
        mensagem='Ola '.encode('utf-8')+nome+" , seu ponto de entrada foi registrado".encode('utf-8')
    if ponto==3:
        mensagem=u"Tiau ".encode('utf-8')+nome+" , seu ponto de saida foi registrado".encode('utf-8')
    if ponto==1:
        mensagem=u'Ola '+nome+" , voce nao tem ponto nesse horario mas vou abrir a porta para voce, s2"
    comando=u'espeak -v brazil "'+mensagem+'"'
    os.system(comando)