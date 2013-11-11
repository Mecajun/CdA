import datetime
import csv

def relatorio(dados):
    extensao='.csv'
    arquivo=datetime.datetime.now().strftime('%d_%m_%Y')
    nome_arquivo=arquivo+extensao
    saida=csv.writer(file(nome_arquivo, 'w'))
    for linha in dados:
        saida.writerow(linha)      

b=((u'a', u'42', datetime.datetime(2013, 11, 5, 16, 47)), (u'b', u'24', datetime.datetime(2013, 11, 5, 16, 47)), (u'b', u'24', datetime.datetime(2013, 11, 5, 16, 47)), (u'um', u'1', datetime.datetime(2013, 11, 5, 17, 14)), (u'b', u'24', datetime.datetime(2013, 11, 5, 17, 25)), (u'a', u'42', datetime.datetime(2013, 11, 5, 17, 25)))
a=b[0]
vet=[]
for elem in b:
	vet2=[]
	vet2.append(elem[0])
	vet2.append(elem[1])
	tempo = elem[2].strftime('%d/%m/%Y - %H:%M')
	vet2.append(tempo)
	vet.append(vet2)

for i in vet:
	print i
	relatorio(i)



