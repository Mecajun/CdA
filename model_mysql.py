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
        self.conn = Connect(host, user, passwd)
        self.curs = self.conn.cursor()
        self.curs.execute('USE controledeacesso')
    
    ##  Cria as tabelas do programa na instalação
    def criar_Tabelas(self):
        self.curs.execute("CREATE TABLE funcionarios (id_funcionario INT NOT NULL AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(100), matricula VARCHAR(40) NOT NULL, rfid VARCHAR(20))")
        self.curs.execute("CREATE TABLE horarios (id_horario INT NOT NULL AUTO_INCREMENT PRIMARY KEY, id_funcionario INT NOT NULL, dia_da_semana INT NOT NULL, hora_inicial TIME NOT NULL, hora_final TIME NOT NULL)")
        self.curs.execute("CREATE TABLE pontos (id_ponto INT NOT NULL AUTO_INCREMENT PRIMARY KEY, id_funcionario INT NOT NULL, id_horario INT NOT NULL, horario_entrada DATETIME NOT NULL, horario_saida DATETIME, atraso_entrada TIME, atraso_saida TIME, presenca INT)")
        self.curs.execute("CREATE TABLE log_porta (id_log INT NOT NULL AUTO_INCREMENT PRIMARY KEY, id_funcionario INT NOT NULL, horario_entrada DATETIME NOT NULL)")
        self.curs.execute("CREATE TABLE configuracoes (id_config INT NOT NULL AUTO_INCREMENT PRIMARY KEY, tipo VARCHAR(100) NOT NULL, dado VARCHAR(100) NOT NULL)")

    ##  Obtem as configurações do programa
    #   @param config Nome da configuração
    def obter_Configuracoes(self,config):
        self.curs.execute("SELECT * FROM configuracoes WHERE tipo=%s",(config))
        linhas = self.curs.fetchall()
        return linhas[0] if len(linhas)>0 else None

    ##  Atualiza as configurações do programa
    #   @param config Nome da configuração
    #   @param dado Dado que vai ser inserido
    def atualizar_Configuracoes(self,config,dado):
        sql="UPDATE configuracoes SET dado=%s WHERE tipo=%s"
        self.curs.execute(sql,(dado,config))
        self.conn.commit()

    ##  Cria as configurações do programa
    #   @param config Nome da configuração
    #   @param dado Dado que vai ser inserido
    def criar_Configuracoes(self,config,dado):
        sql="INSERT INTO configuracoes (tipo,dado) VALUES (%s,%s)"
        self.curs.execute(sql,(config,dado))
        self.conn.commit()

    ##  Cria um funcionario na tabela funcionarios.
    #   @param nome Nome do funcionario
    #   @param matricula Matricula do funcionario
    #   @param rfid RFID do funcionario. Não é obrigatoria
    def criar_Funcionario(self,nome,matricula,rfid=None):
        sql="INSERT INTO funcionarios (nome,matricula,rfid) VALUES (%s,%s,"
        if (rfid !=  None):
            sql=sql+"%s)"
            self.curs.execute(sql,(nome,matricula,rfid))
        else:
            sql=sql+"NULL)"
            self.curs.execute(sql,(nome,matricula))
        self.conn.commit()
    
    ##  Remove um funcionario do banco de dados e os horarios dele
    #   @param id_funcionario Id do funcionario
    def remover_Funcionario(self,id_funcionario):
        self.curs.execute("DELETE FROM funcionarios WHERE id_funcionario=%s",(id_funcionario))
        self.remover_Horario_Funcionario(id_funcionario)
        self.conn.commit()
    
    ##  Retorna todas as informações do funcionario
    #   @param id_funcionario Id do funcionario
    def obter_Funcionario(self,id_funcionario):
        self.curs.execute("SELECT * FROM funcionarios WHERE id_funcionario=%s",(id_funcionario))
        linhas = self.curs.fetchall()
        return linhas[0] if len(linhas)>0 else None
        
    ##  Retorna todas as informações do funcionario
    #   @param id_funcionario Id do funcionario
    def obter_Funcionario_Basico(self,id_funcionario):
        self.curs.execute("SELECT id_funcionario,nome FROM funcionarios WHERE id_funcionario=%s",(id_funcionario))
        linhas = self.curs.fetchall()
        return linhas[0] if len(linhas)>0 else None

    ##  Retorna o Id do funcionario com o nome igual o da entrada
    #   @param nome Nome do funcionario    
    def obter_Id_Funcionario_por_Nome(self, nome):
        self.curs.execute("SELECT id_funcionario FROM funcionarios WHERE nome=%s",(nome))       
        linhas = self.curs.fetchall()
        return linhas[0][0] if len(linhas)>0 else None
    
    ##  Retorna o Id do funcionario com a matricula igual a da entrada
    #   @param matricula Matricula do funcionario    
    def obter_Id_Funcionario_por_Matricula(self, matricula):
        self.curs.execute("SELECT id_funcionario FROM funcionarios WHERE matricula=%s",(matricula))       
        linhas = self.curs.fetchall()
        return linhas[0][0] if len(linhas)>0 else None
        
    ##  Retorna o Id do funcionario com o RFID igual a da entrada
    #   @param rfid RFID do funcionario       
    def obter_Id_Funcionario_por_Rfid(self, rfid):
        self.curs.execute("SELECT id_funcionario FROM funcionarios WHERE rfid=%s",(rfid))
        linhas = self.curs.fetchall()
        return linhas[0][0] if len(linhas)>0 else None

    ##  Retorna os dados de um funcionario
    #   @param id_funcionario Id do funcionario   
    def obter_Dados_Funcionario(self, id_funcionario):
        self.curs.execute("SELECT * FROM funcionarios WHERE id_funcionario=%s",(id_funcionario))
        linhas = self.curs.fetchall()
        return linhas[0] if len(linhas)>0 else None


    ##  Cria um horario para um funcionario
    #   @param id_funcionario Id do funcionario
    #   @param dia_da_semana Dia da semana no formato INT
    #   @param hora_inicial Hora inicial no formato HH:MM:SS
    #   @param hora_final Hora final no formato HH:MM:SS
    def criar_Horario(self,id_funcionario,dia_da_semana,hora_inicial,hora_final):
        sql="INSERT INTO horarios (id_funcionario,dia_da_semana,hora_inicial,hora_final) VALUES (%s,%s,%s,%s)"
        self.curs.execute(sql,(id_funcionario,dia_da_semana,hora_inicial,hora_final))
        self.conn.commit()
        
    ##  Remove um dos horarios de um funcionario
    #   @param id_funcionario Id do funcionario
    #   @param dia_da_semana Dia da semana no formato INT
    #   @param hora_inicial Hora inicial no formato HH:MM:S        
    def remover_Horario_Data_Hora(self,id_funcionario,dia_da_semana,hora_inicial):
        self.curs.execute("DELETE FROM horarios WHERE (id_funcionario=%s AND dia_da_semana=%s AND hora_inicial=%s)",(id_funcionario,dia_da_semana,hora_inicial))
        self.conn.commit()

    ##  Remove todos os horarios de um funcionario
    #   @param id_funcionario Id do funcionario 
    def remover_Horario_Funcionario(self,id_funcionario):
        self.curs.execute("DELETE FROM horarios WHERE id_funcionario=%s",(id_funcionario))
        self.conn.commit()

    ##  Cria o ponto de entrada de um funcionario
    #   @param id_funcionario Id do funcionario 
    #   @param id_horario Id do horario do funcionario
    #   @param horario_entrada Horario de entrada no formato YYYY-MM-DD HH:MM:SS
    #   @param atraso_entrada Atraso da entrada no formato HH:MM:S. Tempo negativo para chegada antecipada e positivo para atraso
    def criar_Ponto(self,id_funcionario,id_horario,horario_entrada,atraso_entrada):
        sql="INSERT INTO pontos (id_funcionario,id_horario,horario_entrada,atraso_entrada,presenca) VALUES (%s,%s,%s,%s,-1)"
        self.curs.execute(sql,(id_funcionario,id_horario,horario_entrada,atraso_entrada))
        self.conn.commit()
        
    ##  Cria o ponto de saida de um funcionario
    #   @param id_funcionario Id do funcionario 
    #   @param horario_saida Horario de saida no formato YYYY-MM-DD HH:MM:SS
    #   @param atraso_saida Atraso da saida no formato HH:MM:SS. Tempo negativo para saida antecipada e positivo para atraso
    #   @presenca 0 para falta. 1 para presença. 2 para presente com atrazo ou saida antecipada.
    def finaliza_Ponto(self,id_funcionario,horario_saida,atraso_saida,presenca):
        sql="UPDATE pontos SET horario_saida=%s, atraso_saida=%s, presenca=%s WHERE id_funcionario=%s"
        self.curs.execute(sql,(horario_saida,atraso_saida,presenca,id_funcionario))
        self.conn.commit()

    ##  Retorna todos os horarios de um funcionario
    #   @param id_funcionario Id do funcionario 
    def buscar_Horarios_de_Funcionario(self,id_funcionario):
        self.curs.execute("SELECT * FROM horarios WHERE id_funcionario=%s",(id_funcionario))
        linhas = self.curs.fetchall()
        return linhas if len(linhas)>0 else None
        
    ##  Retorna o horario mais proximo de um funcionario
    #   @param id_funcionario Id do funcionario 
    #   @param dia_da_semana Dia da semana no formato INT
    #   @param horario_base Horario base para a busca. Referencia para o superiro e inferior. Formato HH:MM:SS
    #   @param limite_inferior Limite inferior para busca. Formato HH:MM:SS
    #   @param limite_superior Limite superior para a busca. Formato HH:MM:SS
    def buscar_Horario_Mais_Proximo_de_Funcionario(self,id_funcionario,dia_da_semana,horario_base,limite_inferior,limite_superior):
        self.curs.execute("SELECT * FROM horarios WHERE (id_funcionario=%s AND dia_da_semana=%s AND hora_inicial >= SUBTIME(%s,%s) AND hora_inicial <= ADDTIME(%s,%s)  ) ORDER BY ABS(SUBTIME(hora_inicial,%s)) LIMIT 1",(id_funcionario,dia_da_semana,horario_base,limite_inferior,horario_base,limite_superior,horario_base))
        linhas = self.curs.fetchall()
        return linhas[0] if len(linhas)>0 else None

    ##  Verifica se existe ponto aberto de um funcionario
    #   @param id_funcionario Id do funcionario 
    def buscar_Ponto_Aberto_de_Funcionario(self,id_funcionario):
        self.curs.execute("SELECT pontos.presenca,pontos.horario_entrada,horarios.hora_inicial,horarios.hora_final FROM pontos INNER JOIN horarios on pontos.id_horario = horarios.id_horario WHERE pontos.presenca=-1 AND pontos.id_funcionario=%s",(id_funcionario))
        linhas = self.curs.fetchall()
        return linhas[0] if len(linhas)>0 else None

    ##  Adiciona no log da porta o funcionario que entrou e o horario
    #   @param id_funcionario Id do funcionario
    #   @param horario_entrada Horario de entrada. Formato YYYY-MM-DD HH:MM:SS
    def adicionar_Log_Porta(self,id_funcionario,horario_entrada):
        sql="INSERT INTO log_porta (id_funcionario,horario_entrada) VALUES (%s,%s)"
        self.curs.execute(sql,(id_funcionario,horario_entrada))
        self.conn.commit()
    
    ##  Obtem o log da porta dentro de um periodo de tempo
    #   @param data_inicial Data inicial do log. Formato YYYY-MM-DD HH:MM:SS
    #   @param data_final Data final do log. Formato YYYY-MM-DD HH:MM:SS    
    #   @return Nome,Matricula,Horario_entrada
    def obter_Log_Porta(self,data_inicial,data_final):
        self.curs.execute("SELECT funcionarios.nome,funcionarios.matricula,log_porta.horario_entrada FROM log_porta INNER JOIN funcionarios on log_porta.id_funcionario = funcionarios.id_funcionario WHERE (log_porta.horario_entrada >= %s AND log_porta.horario_entrada <= %s )",(data_inicial,data_final))
        linhas = self.curs.fetchall()
        return linhas if len(linhas)>0 else None
        
    ##  Obtem o log dos pontos dentro de um periodo de tempo
    #   @param data_inicial Data inicial do log. Formato YYYY-MM-DD HH:MM:SS
    #   @param data_final Data final do log. Formato YYYY-MM-DD HH:MM:SS  
    #   @param presentes Mostrar presença de funcionarios
    #   @param faltas Mostrar falta de funcionarios
    #   @param atrazos Mostrar atrazos de funcionarios
    #   @return Nome,Matricula,Horario_entrada,Horario_saida,Atraso_entrada,Atraso_saida,Presenca
    def obter_Log_Pontos(self,data_inicial,data_final,presentes=True,faltas=True,atrasos=True):
        sql="SELECT funcionarios.nome,funcionarios.matricula,pontos.horario_entrada,pontos.horario_saida,pontos.atraso_entrada,pontos.atraso_saida,pontos.presenca FROM pontos INNER JOIN funcionarios on pontos.id_funcionario = funcionarios.id_funcionario WHERE (pontos.horario_entrada >= %s AND pontos.horario_entrada <= %s AND ("
        if presentes == True:
            sql=sql+" pontos.presenca=1 OR"
        if faltas == True:
            sql=sql+" pontos.presenca=0 OR"
        if "Aberto" == "Aberto":
            sql=sql+" pontos.presenca=-1 OR"
        if atrasos == True:
            sql=sql+" pontos.presenca=2 OR"
        if sql[-1]=='R':
            sql=sql[0:-2]+"))"
        else:
            sql=sql[0:-5]+")"
        self.curs.execute(sql,(data_inicial,data_final))
        linhas = self.curs.fetchall()
        return linhas if len(linhas)>0 else None
    
    ##  Atualiza informações do usuario
    #   @param id_funcionario Id do funcionario
    #   @param nome Nome do funcionario
    #   @param matricula Matricula do funcionario
    #   @param rfid RFID do funcionario
    def atualizar_Funcionario(self,id_funcionario, nome=None, matricula=None, rfid=None):
        sql="UPDATE funcionarios SET "
        if nome != None:
            sql=sql+"nome='"+nome+"',";
        if matricula != None:
            sql=sql+"matricula='"+matricula+"',";
        if rfid != None:
            sql=sql+"rfid='"+rfid+"',";
        sql=sql[0:-1] + " WHERE id_funcionario=%s"
        self.curs.execute(sql,(id_funcionario,))
        self.conn.commit()
    
    ##  Obtem todos os funcionarios cadastrados
    def obter_Funcionarios(self):
        self.curs.execute("SELECT id_funcionario,nome FROM funcionarios")
        linhas = self.curs.fetchall()
        return linhas if len(linhas)>0 else None

##  Testes do modulo
#   @param criar True para criar
#   @param remover True para remover 
def test_Connect_MySQL(criar,remover):
    db=Connect_MySQL('localhost','root','42')
    if criar==True:
        db.curs.execute('DROP TABLE IF EXISTS funcionarios')
        db.curs.execute('DROP TABLE IF EXISTS horarios')
        db.curs.execute('DROP TABLE IF EXISTS pontos')
        db.curs.execute('DROP TABLE IF EXISTS log_porta')
        db.curs.execute('DROP TABLE IF EXISTS configuracoes')
        
        db.criar_Tabelas()
               
        db.criar_Funcionario('filipe','100129706','8001')
        db.criar_Funcionario('bacon da silva','100129707','8002')
        db.criar_Funcionario('pombo raimundo','100129708','8003')
        db.criar_Funcionario('unicornio pereira','100129709')
        print db.obter_Id_Funcionario_por_Nome('bacon da silva')
        print db.obter_Id_Funcionario_por_Matricula('100129707')
        print db.obter_Id_Funcionario_por_Rfid('8003')
        db.criar_Horario(2,1,'12:05:00','14:13:00')
        db.criar_Horario(2,2,'12:00:00','14:00:00')
        db.criar_Horario(2,2,'16:00:00','18:00:00')
        db.criar_Horario(1,3,'14:00:00','15:00:00')
        db.criar_Horario(3,1,'15:00:00','16:00:00')
        db.criar_Horario(0,1,'16:00:00','17:00:00')
        db.criar_Horario(1,1,'17:00:00','18:00:00')
        db.criar_Ponto(0,4,'2013-08-24 16:10:00','00:10:00')
        db.finaliza_Ponto(0,'2013-08-24 17:20:00','00:20:00',1)
        db.criar_Ponto(1,2,'2013-08-25 12:09:00','00:09:00')
        print 'horarios',db.buscar_Horarios_de_Funcionario(2)
        print 'horarios proximo',db.buscar_Horario_Mais_Proximo_de_Funcionario(2,2,'14:00:00','01:00:00','00:50:00')
        print db.buscar_Horario_Mais_Proximo_de_Funcionario(2,2,'15:30:00','01:00:00','00:50:00')
        print db.buscar_Ponto_Aberto_de_Funcionario(1)
        db.adicionar_Log_Porta(0,'2013-08-23 15:30:00')
        db.adicionar_Log_Porta(0,'2013-08-23 15:32:00')
        print db.obter_Log_Porta('2013-08-23 15:20:00','2013-08-25 15:30:00')
        db.atualizar_Funcionario(4,nome='unicornio miranda', rfid='9001')     
        print db.obter_Log_Pontos('2012-08-23 15:20:00','2014-08-25 15:30:00',presentes=True,faltas=False,atrazos=True)
        print db.obter_Dados_Funcionario(2)
            
    if remover==True:
        db.remover_Funcionario(3)
        db.remover_Horario_Data_Hora(1,1,'17:00:00')
        db.remover_Horario_Funcionario(2)

if __name__ == "__main__":
    test_Connect_MySQL(True,False)