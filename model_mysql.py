# -*- coding: utf-8 -*-

##  @package model_mysql
#   Pacote com todas as funções de acesso ao banco de dados
from MySQLdb import Connect
import datetime

##  Classe de conexão e acesso ao banco de dados
class Connect_Db:
    ##  Inicializa o banco de dados
    #   @param host Servidor do banco de dados
    #   @param user Usuario do banco de dados
    #   @param passwd Senha do banco de dados
    def __init__(self,db_dados):
        self.host=db_dados['host']
        self.user=db_dados['user']
        self.passwd=db_dados['passwd']
        self.conecta()

    def __del__(self):
        self.curs.close()
        self.conn.close()

    def conecta(self):
        self.conn = Connect(self.host, self.user, self.passwd,charset='utf8',use_unicode=True)
        self.curs = self.conn.cursor()
        self.curs.execute('USE controledeacesso')

    ##  Cria um funcionario na tabela funcionarios.
    #   @param nome Nome do funcionario
    #   @param matricula Matricula do funcionario
    #   @param rfid RFID do funcionario. Não é obrigatoria
    def criar_Funcionario(self,nome,matricula,rfid=None):
        if not ( (isinstance(nome, str) or isinstance(nome, unicode)) and (isinstance(matricula, str) or isinstance(matricula, unicode))):
            return False
        sql="INSERT INTO funcionarios (ativo,nome,matricula,rfid) VALUES (true,%s,%s,"
        try:
            if (rfid !=  None):
                sql=sql+"%s)"
                self.curs.execute(sql,(nome,matricula,rfid))
            else:
                sql=sql+"NULL)"
                self.curs.execute(sql,(nome,matricula))
        except Exception:
            raise
        self.conn.commit()
        return True

    ##  Atualiza informações do usuario
    #   @param id_funcionario Id do funcionario
    #   @param nome Nome do funcionario
    #   @param matricula Matricula do funcionario
    #   @param rfid RFID do funcionario
    def atualizar_Funcionario(self,id_funcionario, nome=None, matricula=None, rfid=None):
        sql="UPDATE funcionarios SET "
        lista=[]
        if nome != None:
            sql=sql+"nome=%s,";
            lista.append(nome)
        if matricula != None:
            sql=sql+"matricula=%s,";
            lista.append(matricula)
        sql=sql+"rfid=%s,";
        lista.append(rfid)
        lista.append(id_funcionario)
        sql=sql[0:-1] + " WHERE id_funcionario=%s"
        self.curs.execute(sql,tuple(lista))
        self.conn.commit()

    ##  Retorna o Id do funcionario com o nome igual o da entrada
    #   @param nome Nome do funcionario    
    def obter_Id_Funcionario_por_Nome(self, nome):
        if not (isinstance(nome, str) or isinstance(nome, unicode)):
            return False
        self.curs.execute("SELECT id_funcionario FROM funcionarios WHERE nome=%s AND ativo=true",(nome))       
        linhas = self.curs.fetchall()
        self.conn.commit()
        return linhas[0][0] if len(linhas)>0 else False

    ##  Retorna o Id do funcionario com a matricula igual a da entrada
    #   @param matricula Matricula do funcionario    
    def obter_Id_Funcionario_por_Matricula(self, matricula):
        if not (isinstance(matricula, str) or isinstance(matricula, unicode)):
            return False
        self.curs.execute("SELECT id_funcionario FROM funcionarios WHERE matricula=%s AND ativo=true",(matricula))       
        linhas = self.curs.fetchall()
        self.conn.commit()
        return linhas[0][0] if len(linhas)>0 else False

    ##  Retorna o Id do funcionario com a matricula igual a da entrada
    #   @param matricula Matricula do funcionario    
    def obter_Id_Funcionario_por_Rfid(self, rfid):
        if not (isinstance(rfid, str) or isinstance(rfid, unicode)):
            return False
        self.curs.execute("SELECT id_funcionario FROM funcionarios WHERE rfid=%s AND ativo=true",(rfid))       
        linhas = self.curs.fetchall()
        self.conn.commit()
        return linhas[0][0] if len(linhas)>0 else False

    ##  Cria um horario para um funcionario
    #   @param id_funcionario Id do funcionario
    #   @param dia_da_semana Dia da semana no formato INT
    #   @param hora_inicial Hora inicial no formato HH:MM:SS
    #   @param hora_final Hora final no formato HH:MM:SS
    def criar_Horario(self,id_funcionario,dia_da_semana,hora_inicial,hora_final):
        if not isinstance(id_funcionario, long):
            return False
        if not isinstance(dia_da_semana, int):
            return False
        if not (isinstance(hora_inicial, str) or isinstance(hora_inicial, unicode)):
            return False
        if not (isinstance(hora_final, str) or isinstance(hora_final, unicode)):
            return False
        sql="INSERT INTO horarios (id_funcionario,dia_da_semana,hora_inicial,hora_final) VALUES (%s,%s,%s,%s)"
        self.curs.execute(sql,(id_funcionario,dia_da_semana,hora_inicial,hora_final))
        self.conn.commit()
        return True
     
    ##  Remove um dos horarios de um funcionario
    #   @param id_horario Id do horario  
    def remover_Horario(self,id_horario):
        self.curs.execute("DELETE FROM horarios WHERE id_horario=%s ",(id_horario))
        self.conn.commit()

    ##  Obtem as configurações do programa
    #   @param config Nome da configuração
    def obter_Configuracoes(self,config):
        if not (isinstance(config, str) or isinstance(config, unicode)):
            return False
        self.curs.execute("SELECT dado FROM configuracoes WHERE tipo=%s",(config))
        linhas = self.curs.fetchall()
        self.conn.commit()
        return linhas[0][0] if len(linhas)>0 else False
    
    ##  Atualiza as configurações do programa
    #   @param config Nome da configuração
    #   @param dado Dado que vai ser inserido
    def atualizar_Configuracoes(self,config,dado):
        if not (isinstance(config, str) or isinstance(config, unicode)):
            return False
        if not (isinstance(dado, str) or isinstance(dado, unicode)):
            return False
        sql="UPDATE configuracoes SET dado=%s WHERE tipo=%s"
        self.curs.execute(sql,(dado,config))
        self.conn.commit()
        return True

    ##  Obtem todos os funcionarios cadastrados
    def obter_Funcionarios(self):
        self.curs.execute("SELECT id_funcionario,nome FROM funcionarios WHERE ativo=true")
        linhas = self.curs.fetchall()
        result = []
        for i in range(len(linhas)):
            if len(linhas[i])==2:
                result.append({'id_funcionario':linhas[i][0],'nome':linhas[i][1]})
        self.conn.commit()
        return result if len(result)>0 else False

    ##  Verifica se algun dos dados ja existem
    def verifica_Ja_Existe(self,nome=None,matricula=None,rfid=None,id_funcionario=None):
        if nome:
            sql="SELECT count(*) FROM funcionarios WHERE nome=%s AND ativo=true"
            tup=(nome)
            if id_funcionario!=None:
                sql=sql+" AND id_funcionario!=%s"
                tup=(nome,id_funcionario)
            self.curs.execute(sql,tup)
            nome = self.curs.fetchall()
            nome = nome[0][0]
            if nome==0:
                nome = None
            else: 
                nome = True
        if matricula:
            sql="SELECT count(*) FROM funcionarios WHERE matricula=%s AND ativo=true"
            tup=(matricula)
            if id_funcionario!=None:
                sql=sql+" AND id_funcionario!=%s"
                tup=(matricula,id_funcionario)
            self.curs.execute(sql,tup)
            matricula = self.curs.fetchall()
            matricula = matricula[0][0]
            if matricula==0: 
                matricula = None
            else:
                matricula = True
        if rfid:
            sql="SELECT count(*) FROM funcionarios WHERE rfid=%s AND ativo=true"
            tup=(rfid)
            if id_funcionario!=None:
                sql=sql+" AND id_funcionario!=%s"
                tup=(rfid,id_funcionario)
            self.curs.execute(sql,tup)
            rfid = self.curs.fetchall()
            rfid = rfid[0][0]
            if rfid==0: 
                rfid = None
            else:
                rfid = True

        temp=nome or matricula or rfid;
        if temp==None:
            temp=False
        self.conn.commit()
        return {'nome':nome,'matricula':matricula,'rfid':rfid,'existe':temp}

    ##  Remove um funcionario do banco de dados e os horarios dele
    #   @param id_funcionario Id do funcionario
    def remover_Funcionario(self,id_funcionario):
        if not (isinstance(id_funcionario, long) or isinstance(id_funcionario, int)):
            return False
        self.curs.execute("UPDATE funcionarios set ativo=false WHERE id_funcionario=%s",(id_funcionario))
        self.remover_Horario_Funcionario(id_funcionario)
        self.conn.commit()
        return True

    ##  Remove todos os horarios de um funcionario
    #   @param id_funcionario Id do funcionario 
    def remover_Horario_Funcionario(self,id_funcionario):
        self.curs.execute("DELETE FROM horarios WHERE id_funcionario=%s",(id_funcionario))
        self.conn.commit()

    ##  Obtem todos os horarios cadastrados
    def obter_Horarios(self):
        sql="SELECT funcionarios.nome, horarios.dia_da_semana, horarios.hora_inicial, horarios.hora_final FROM horarios INNER JOIN funcionarios ON funcionarios.id_funcionario=horarios.id_funcionario ORDER BY horarios.dia_da_semana ASC,horarios.hora_inicial ASC"
        self.curs.execute(sql)
        linhas = self.curs.fetchall()
        self.conn.commit()
        return linhas if len(linhas)>0 else False

    ##  Retorna todos os horarios de um funcionario
    #   @param id_funcionario Id do funcionario 
    def buscar_Horarios_de_Funcionario(self,id_funcionario):
        self.curs.execute("SELECT id_horario, dia_da_semana, hora_inicial,hora_final FROM horarios WHERE id_funcionario=%s ORDER BY dia_da_semana ASC, hora_inicial ASC",(id_funcionario))
        linhas = self.curs.fetchall()
        l=[]
        if len(linhas)>0:
            for i in linhas:
                l.append({'id_horario':i[0],'dia_da_semana':i[1],'hora_inicial':i[2],'hora_final':i[3]})
        return l if len(l)>0 else False
        
    ##  Retorna todas as informações do funcionario
    #   @param id_funcionario Id do funcionario
    def obter_Funcionario(self,id_funcionario):
        self.curs.execute("SELECT id_funcionario,nome,matricula,rfid,ativo FROM funcionarios WHERE id_funcionario=%s",(id_funcionario))
        linhas = self.curs.fetchall()
        l={}
        if len(linhas)>0:
            i=linhas[0]
            l={'id_funcionario':i[0],'nome':i[1],'matricula':i[2],'rfid':i[3],'ativo':i[4]}
        return l if len(linhas)>0 else False
    
    ##  Retorna os funcionarios esperados para o horario
    #   @param dia_da_semana Dia da semana no formato INT
    #   @param limite_inferior Limite inferior para busca. Formato HH:MM:SS
    #   @param limite_superior Limite superior para a busca. Formato HH:MM:SS
    def buscar_Funcionarios_Esperados(self,dia_da_semana,limite_inferior,limite_superior):
        #Adicionado campo horarios.id_horario
        self.curs.execute("SELECT funcionarios.nome, funcionarios.id_funcionario, horarios.hora_inicial, horarios.hora_final, horarios.id_horario FROM horarios INNER JOIN funcionarios ON horarios.id_funcionario=funcionarios.id_funcionario WHERE horarios.dia_da_semana=%s AND curtime() >= subtime(horarios.hora_inicial,%s) AND curtime() <= addtime(horarios.hora_final,%s)",(dia_da_semana,limite_inferior,limite_superior))
        linhas = self.curs.fetchall()
        l={}
        if len(linhas)>0:
            for i in linhas:
                l[str(i[1])]={'nome':i[0],'hora_inicial':i[2],'hora_final':i[3],'id_horario':i[4]}
        self.conn.commit()
        return l if len(l)>0 else False

    ##  Retorna os funcionarios logados
    #   @param dia_da_semana Dia da semana no formato INT
    #   @param limite_inferior Limite inferior para busca. Formato HH:MM:SS
    #   @param limite_superior Limite superior para a busca. Formato HH:MM:SS
    def buscar_Funcionarios_Esperados_Logados(self,dia_da_semana,limite_inferior,limite_superior):
        self.curs.execute("SELECT pontos.id_funcionario FROM pontos INNER JOIN horarios ON horarios.id_horario=pontos.id_horario WHERE horarios.dia_da_semana=%s AND curtime() >= subtime(horarios.hora_inicial,%s) AND curtime() <= addtime(horarios.hora_final,%s) AND (pontos.presenca=-1)",(dia_da_semana,limite_inferior,limite_superior))
        linhas = self.curs.fetchall()
        l=[]
        for i in linhas:
            l.append(str(i[0]))
        self.conn.commit()
        return l if len(l)>0 else False

    ##  Verifica se existe ponto aberto de um funcionario
    #   @param id_funcionario Id do funcionario 
    def buscar_Ponto_Aberto_de_Funcionario(self,id_funcionario):
        self.curs.execute("SELECT pontos.horario_entrada,horarios.hora_inicial,horarios.hora_final FROM pontos INNER JOIN horarios on pontos.id_horario = horarios.id_horario WHERE pontos.presenca=-1 AND pontos.id_funcionario=%s ORDER BY pontos.id_ponto DESC",(id_funcionario)) #Otimizado por ORDER BY
        linhas = self.curs.fetchall()
        l=False
        if len(linhas)>0:
            i=linhas[0]
            l={'horario_entrada':i[0],'hora_inicial':datetime.datetime.combine(i[0].date(),(datetime.datetime.min+i[1]).time()),'hora_final':datetime.datetime.combine(i[0].date(),(datetime.datetime.min+i[2]).time())}
        self.conn.commit()
        return l

    ##  Cria o ponto de saida de um funcionario
    #   @param id_funcionario Id do funcionario 
    #   @param horario_saida Horario de saida no formato YYYY-MM-DD HH:MM:SS
    #   @presenca 0 para falta. 1 para presença. 2 para ponto nao fechado
    def finaliza_Ponto(self,id_funcionario,horario_saida,presenca):
        sql="UPDATE pontos SET horario_saida=%s, presenca=%s WHERE id_funcionario=%s AND presenca=-1"
        self.curs.execute(sql,(horario_saida,presenca,id_funcionario))
        self.conn.commit()
        return True

    ##  Retorna o horario mais proximo de um funcionario
    #   @param id_funcionario Id do funcionario 
    #   @param dia_da_semana Dia da semana no formato INT
    #   @param limite_inferior Limite inferior para busca. Formato HH:MM:SS
    #   @param limite_superior Limite superior para a busca. Formato HH:MM:SS
    def buscar_Horario_Mais_Proximo_de_Funcionario(self,id_funcionario,dia_da_semana,limite_inferior,limite_superior):
        sql="SELECT id_horario FROM horarios WHERE (id_funcionario=%s AND dia_da_semana=%s AND curtime()>SUBTIME(time(hora_inicial),time(%s)) AND curtime()<ADDTIME(time(hora_inicial),time(%s))) ORDER BY ABS(SUBTIME(%s,curtime())) LIMIT 1"
        self.curs.execute(sql,(id_funcionario,dia_da_semana,limite_inferior,limite_superior,limite_inferior))
        linhas = self.curs.fetchall()
        self.conn.commit()
        return linhas[0][0] if len(linhas)>0 else False

    ##  Cria o ponto de entrada de um funcionario
    #   @param id_funcionario Id do funcionario 
    #   @param id_horario Id do horario do funcionario
    def criar_Ponto(self,id_funcionario,id_horario,presenca=-1):
        sql="INSERT INTO pontos (id_funcionario,id_horario,horario_entrada,presenca) VALUES (%s,%s,now(),%s)"
        self.curs.execute(sql,(id_funcionario,id_horario,presenca))
        self.conn.commit()
        return True

    ##  Cria o ponto de falta de um funcionario
    #   @param id_funcionario Id do funcionario 
    #   @param id_horario Id do horario do funcionario
    def criar_Ponto_Falta(self,id_funcionario,id_horario,entrada_data,entrada_hora):
        sql="INSERT INTO pontos (id_funcionario,id_horario,horario_entrada,presenca) VALUES (%s,%s,concat(%s,' ',%s),0)"
        self.curs.execute(sql,(id_funcionario,id_horario,entrada_data,entrada_hora))
        self.conn.commit()
        return True

    ##  Adiciona no log da porta o funcionario que entrou e o horario
    #   @param id_funcionario Id do funcionario
    def adicionar_Log_Porta(self,id_funcionario):
        sql="INSERT INTO log_porta (id_funcionario,horario_entrada) VALUES (%s,now())"
        self.curs.execute(sql,(id_funcionario))
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
    #   @return Nome,Matricula,Horario_entrada,Horario_saida,Presenca
    def obter_Log_Pontos(self,data_inicial,data_final):
        sql="SELECT funcionarios.nome,funcionarios.matricula,pontos.horario_entrada,pontos.horario_saida,SUBTIME(TIME(pontos.horario_saida),TIME(pontos.horario_entrada)),pontos.presenca FROM pontos INNER JOIN funcionarios on pontos.id_funcionario = funcionarios.id_funcionario WHERE (pontos.horario_entrada >= %s AND pontos.horario_entrada <= %s)"
        self.curs.execute(sql,(data_inicial,data_final))
        linhas = self.curs.fetchall()
        return linhas if len(linhas)>0 else None
   
    ##  Obtem os pontos que não foram dados
    #   @param data_inicial Data inicial no formato YYYY-MM-DD HH:MM:SS
    #   @param data_final Data final no formato YYYY-MM-DD HH:MM:SS
    #   @param dia_da_semana Dia da semana inteiro
    #   @param limite_superior_ent Limite superior de entrada no formato HH:MM:SS
    def obter_Pontos_Faltando(self,data_inicial,data_final,dia_da_semana=None,limite_superior_ent=None):
        sql='SELECT id_horario_2,id_funcionario, hora_inicial,dia_da_semana FROM (SELECT pontos2.id_horario AS id_horario_1,horarios.id_horario AS id_horario_2, horarios.id_funcionario,horarios.hora_inicial,horarios.dia_da_semana FROM (SELECT pontos.* FROM pontos where horario_entrada>=%s and horario_entrada<=%s) AS pontos2 right join horarios on pontos2.id_horario=horarios.id_horario'
        dados=(data_inicial,data_final)
        if  dia_da_semana!=None:
            sql=sql+" where horarios.dia_da_semana=%s "
            dados=(data_inicial,data_final,dia_da_semana)
        if limite_superior_ent!=None:
            sql=sql+"and SUBTIME(curtime(),time(horarios.hora_inicial))<=time(%s)"
            dados=(data_inicial,data_final,dia_da_semana,limite_superior_ent)
        sql=sql+") AS tabelaTemp where id_horario_1 IS NULL"
        self.curs.execute(sql,dados)
        linhas = self.curs.fetchall()
        return linhas if len(linhas)>0 else False





    ##  Seta o funcionario como presente
    #   @param id_funcionario Id do funcionario 
    #   @param horario_entrada Horario de entrada do funcionario
    #   @param limite_superior_entrada Tempo limite de entrada do funcionario
    def atualiza_Ponto(self, id_funcionario, horario_entrada, limite_inferior_entrada, limite_superior_entrada):        
        sql="UPDATE pontos SET horario_entrada=%s, presenca=%s WHERE id_funcionario=%s AND presenca=0 AND NOW() >= subtime(pontos.horario_entrada,%s) AND NOW() <= addtime(pontos.horario_entrada,%s)"
        self.curs.execute(sql,(horario_entrada,-1,id_funcionario, limite_inferior_entrada, limite_superior_entrada))
        self.conn.commit()
        return True



    ##  Fecha todos os pontos ainda abertos ate o dia anterior
    def fecha_pontos_abertos(self):
        sql="UPDATE pontos SET presenca=%s WHERE presenca=-1 AND subtime(NOW(),'1 0:0:0') > pontos.horario_entrada"
        self.curs.execute(sql,(2))
        self.conn.commit()
        return True


    ##	Procura ponto recente de funcionario
    #   @param id_funcionario Id do funcionario
    #   @param presenca1 Tipo de presenca a ser procurada
    #   @param presenca2 Tipo de presenca a ser procurada
    def procura_ponto_recente(self, id_funcionario, presenca1=-1, presenca2=0):
        #sql="SELECT pontos.id_ponto FROM pontos INNER JOIN horarios ON pontos.id_horario = horarios.id_horario WHERE pontos.id_funcionario = %s AND DATEDIFF(CURDATE(), pontos.horario_entrada) < 1 AND (TIMEDIFF(CURTIME(), horarios.hora_final) < ADDTIME((SELECT dado FROM configuracoes WHERE tipo='tol_sai_dep'), '00:05:00' ) AND ( pontos.presenca = %s OR pontos.presenca = %s )"
        sql="SELECT pontos.id_ponto FROM pontos INNER JOIN horarios ON pontos.id_horario = horarios.id_horario WHERE pontos.id_funcionario = %s AND DATEDIFF(CURDATE(), pontos.horario_entrada) < 1 AND TIMEDIFF(CURTIME(), horarios.hora_final) < '02:00:00'  AND ( pontos.presenca = %s OR pontos.presenca = %s )"   #EU ODEIO O WINDOWS
        self.curs.execute(sql,(id_funcionario, presenca1, presenca2))
        linhas = self.curs.fetchall()
        l=False
        if len(linhas)>0:
            l=linhas[0][0]
        self.conn.commit()
        return l


    ##	Fecha ponto ao deslogar o usuario
    #   @param id_ponto Id do ponto
    def fecha_ponto_ao_deslogar_usuario(self, id_ponto):
    	sql="UPDATE pontos SET presenca=%s WHERE pontos.id_ponto = %s"
        self.curs.execute(sql,(2, id_ponto))
        self.conn.commit()
        return True

