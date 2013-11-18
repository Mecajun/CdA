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
		hora = elem[2].strftime('%d/%m/%Y - %H:%M')
		#hora de saida
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
		else elem[6] == -1:
			vet2.append('ponto aberto')
		vet.append(vet2)

	extensao='.csv'
	arquivo=datetime.datetime.now().strftime('log_pontos_%d_%m_%Y')
	nome_arquivo=arquivo+extensao
	saida=csv.writer(file(nome_arquivo, 'w'))
	for linha in dados:
	    saida.writerow(linha)



