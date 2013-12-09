# -*- coding: utf-8 -*-

##  @package model_mysql
#   Pacote com todas as funções de acesso ao banco de dados
from MySQLdb import Connect

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
        try:
            self.conn.close()
        except Exception:
            pass
        self.conn = Connect(self.host, self.user, self.passwd,charset='utf8',use_unicode=True)
        self.curs = self.conn.cursor()
        self.curs.execute('USE controledeacesso')

    ##  Deleta todas as tabelas se existirem
    def dropar_Tabelas(self):
        self.curs.execute('DROP TABLE IF EXISTS funcionarios')
        self.curs.execute('DROP TABLE IF EXISTS horarios')
        self.curs.execute('DROP TABLE IF EXISTS pontos')
        self.curs.execute('DROP TABLE IF EXISTS log_porta')
        self.curs.execute('DROP TABLE IF EXISTS configuracoes')