# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:36:30 2013

@author: filipe
"""

from MySQLdb import Connect

class Connect_MySQL:

    def __init__(self,host,user,passwd):
        self.conn = Connect(host, user, passwd)
        self.curs = self.conn.cursor()
        self.curs.execute('USE controledeacesso')

    def criar_Tabelas(self):
        self.curs.execute("CREATE TABLE funcionarios (id_funcionario INT NOT NULL AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(100), matricula VARCHAR(40) NOT NULL', rfid VARCHAR(20))")
        self.curs.execute("CREATE TABLE horarios (id_horario INT NOT NULL AUTO_INCREMENT PRIMARY KEY, id_funcionario INT NOT NULL, dia_da_semana INT NOT NULL, hora TIME NOT NULL)")
        self.curs.execute("CREATE TABLE pontos (id_ponto INT NOT NULL AUTO_INCREMENT PRIMARY KEY, id_funcionario INT NOT NULL, id_horario INT NOT NULL, horario_entrada DATETIME NOT NULL, horario_saida DATETIME, atraso_entrada TIME, atraso_saida TIME, presenca INT)")

    def criar_Funcionario(self,nome,matricula,rfid=None):
        sql="INSERT INTO funcionarios (nome,matricula,rfid) VALUES ('%s','%s',"%(nome,matricula)
        if (rfid !=  None):
            sql=sql+"'%s')"
        else:
            sql=sql+"NULL)"
        self.curs.execute(sql)
            
    def remover_Funcionario(self,id_funcionario):
        self.curs.execute("DELETE FROM funcionarios WHERE id_funcionario=%d"%(id_funcionario))
            
    def obter_Id_Funcionario_por_Matricula(self, matricula):
        self.curs.execute("SELECT id_funcionario FROM funcionarios WHERE matricula='%s'"%(matricula))       
        linhas = self.curs.fetchall()
        return linhas[0]
       
    def obter_Id_Funcionario_por_Rfid(self, rfid):
        self.curs.execute("SELECT id_funcionario FROM funcionarios WHERE rfid='%s'"%(rfid))
        linhas = self.curs.fetchall()
        return linhas[0]

    def criar_Horario(self,id_funcionario,dia_semana,hora):
        sql="INSERT INTO horarios (id_funcionario,dia_semana,hora) VALUES (%d,%d,'%s')"%(id_funcionario,dia_semana,hora)
        self.curs.execute(sql)
        
  #  def remover_horario_data_hora(self,id_funcionario,dia_semana,hora):
  #      self.curs.execute("DELETE FROM funcionarios WHERE id_funcionario=%d"%(id_funcionario))
               
            
'''
    def select(self):
        curs.execute('select * from people')
        for row in curs.fetchall():
            print(row)
        curs.execute('select * from people where name = %s', ('Bob',))
        print(curs.description)
        colnames = [desc[0] for desc in curs.description]
        while True:
            print('-' * 30)
            row = curs.fetchone()
            if not row: break
            for (name, value) in zip(colnames, row):
                print('%s => %s' % (name, value))
        conn.commit()
'''