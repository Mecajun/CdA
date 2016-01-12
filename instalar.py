# -*- coding: utf-8 -*-
from MySQLdb import Connect
from auxiliares import criptografar_Senha
import datetime

##  Classe de conexão e acesso ao banco de dados
class Connect_MySQL:
    ##  Inicializa o banco de dados
    #   @param host Servidor do banco de dados
    #   @param user Usuario do banco de dados
    #   @param passwd Senha do banco de dados
    def __init__(self,host,user,passwd):

        self.host=host
        self.user=user
        self.passwd=passwd
        self.conecta()
    
    def conecta(self):
        self.conn = Connect(self.host, self.user, self.passwd,charset='utf8',use_unicode=True)
        self.curs = self.conn.cursor()
        self.curs.execute('CREATE DATABASE IF NOT EXISTS controledeacesso')
        self.curs.execute('USE controledeacesso')
        self.conn.commit()
        
    ##  Deleta todas as tabelas se existirem
    def dropar_Tabelas(self):
        self.curs.execute('DROP TABLE IF EXISTS funcionarios')
        self.curs.execute('DROP TABLE IF EXISTS horarios')
        self.curs.execute('DROP TABLE IF EXISTS pontos')
        self.curs.execute('DROP TABLE IF EXISTS log_porta')
        self.curs.execute('DROP TABLE IF EXISTS configuracoes')
        self.conn.commit()

    
    ##  Cria as tabelas do programa na instalação
    def criar_Tabelas(self):
        self.curs.execute("CREATE TABLE IF NOT EXISTS funcionarios (id_funcionario INT NOT NULL AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(100), matricula VARCHAR(40) NOT NULL, rfid VARCHAR(20), ativo BOOLEAN NOT NULL)")
        self.curs.execute("CREATE TABLE IF NOT EXISTS horarios (id_horario INT NOT NULL AUTO_INCREMENT PRIMARY KEY, id_funcionario INT NOT NULL, dia_da_semana INT NOT NULL, hora_inicial TIME NOT NULL, hora_final TIME NOT NULL)")
        self.curs.execute("CREATE TABLE IF Not EXISTS pontos (id_ponto INT NOT NULL AUTO_INCREMENT PRIMARY KEY, id_funcionario INT NOT NULL, id_horario INT NOT NULL, horario_entrada DATETIME NOT NULL, horario_saida DATETIME, presenca INT)")
        self.curs.execute("CREATE TABLE IF NOT EXISTS log_porta (id_log INT NOT NULL AUTO_INCREMENT PRIMARY KEY, id_funcionario INT NOT NULL, horario_entrada DATETIME NOT NULL)")
        self.curs.execute("CREATE TABLE IF NOT EXISTS configuracoes (id_config INT NOT NULL AUTO_INCREMENT PRIMARY KEY, tipo VARCHAR(100) NOT NULL, dado VARCHAR(100) NOT NULL)")
        self.conn.commit()

    ##  Cria as configurações do programa
    #   @param config Nome da configuração
    #   @param dado Dado que vai ser inserido
    def criar_Configuracoes(self,config,dado):
        sql="INSERT INTO configuracoes (tipo,dado) VALUES (%s,%s)"
        self.curs.execute(sql,(config,dado))
        self.conn.commit()

class Instalar():
    def __init__(self,db):
        self.db=db
    def criar(self):      
        db.criar_Tabelas()
    def configurar(self):
        db.criar_Configuracoes('adm_senha',criptografar_Senha('42'))
        db.criar_Configuracoes('tol_ent_ant','00:30:00')
        db.criar_Configuracoes('tol_ent_dep','00:30:00')
        db.criar_Configuracoes('tol_sai_ant','00:30:00')
        db.criar_Configuracoes('tol_sai_dep','00:30:00')
        db.criar_Configuracoes('considerar_atraso','00:10:00')
        db.criar_Configuracoes('ultima_verificacao',str(datetime.datetime.now()))

if __name__ == "__main__":
    db=Connect_MySQL('localhost','root','4242')
    ins=Instalar(db)
    ins.criar()
    ins.configurar()
