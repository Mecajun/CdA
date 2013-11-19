import datetime
import csv

def gerar_Relatorio_Porta(dados):
	vet=[]
	for elem in dados:
		vet2=[]
		vet2.append(elem[0])
		vet2.append(elem[1])
		tempo = elem[2].strftime('%d/%m/%Y - %H:%M')
		vet2.append(tempo)
		vet.append(vet2)

	extensao='.csv'
	arquivo=datetime.datetime.now().strftime('log_porta_%d_%m_%Y')
	nome_arquivo=arquivo+extensao
	saida=csv.writer(file(nome_arquivo, 'w'))
	for linha in dados:
	    saida.writerow(linha)

def gerar_Relatorio_Pontos(dados):
	vet=[]
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
			vet2.append('nao fechou')
		elif elem[6] == -3:
			vet2.append('chegou atrasado')
		elif elem[6] == -4:
			vet2.append('saiu com atraso')
		elif elem[6] == -5:
			vet2.append('chegou e saiu com atraso')
		elif elem[6] == -1:
			vet2.append('ponto aberto')
		vet.append(vet2)

	extensao='.csv'
	arquivo=datetime.datetime.now().strftime('log_pontos_%d_%m_%Y')
	nome_arquivo=arquivo+extensao
	saida=csv.writer(file(nome_arquivo, 'w'))
	for linha in dados:
	    saida.writerow(linha)


porta=((u'Filipe Alves Caixeta', u'100129706', datetime.datetime(2013, 11, 19, 13, 1)), (u'Filipe Alves Caixeta', u'100129706', datetime.datetime(2013, 11, 19, 13, 1)), (u'Bacon', u'42', datetime.datetime(2013, 11, 19, 13, 1)), (u'Bacon', u'42', datetime.datetime(2013, 11, 19, 13, 1)), (u'Bacon', u'42', datetime.datetime(2013, 11, 19, 13, 1)), (u'Bacon', u'42', datetime.datetime(2013, 11, 19, 13, 1)), (u'Bacon', u'42', datetime.datetime(2013, 11, 19, 13, 1)), (u'Bacon', u'42', datetime.datetime(2013, 11, 19, 13, 1)))
ponto=((u'Filipe Alves Caixeta', u'100129706', datetime.datetime(2013, 11, 19, 13, 1), None, datetime.timedelta(0, 88), None, -1L), (u'Bacon', u'42', datetime.datetime(2013, 11, 19, 13, 1), datetime.datetime(2013, 11, 19, 13, 1), datetime.timedelta(0, 94), datetime.timedelta(0, 501), 1L), (u'Bacon', u'42', datetime.datetime(2013, 11, 19, 13, 1), datetime.datetime(2013, 11, 19, 13, 1), datetime.timedelta(0, 95), datetime.timedelta(0, 501), 1L), (u'Bacon', u'42', datetime.datetime(2013, 11, 19, 13, 1), datetime.datetime(2013, 11, 19, 13, 1), datetime.timedelta(0, 97), datetime.timedelta(0, 501), 1L))
gerar_Relatorio_Porta(porta)
gerar_Relatorio_Pontos(ponto)

