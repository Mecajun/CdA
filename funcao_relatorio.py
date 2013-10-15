import datetime
import csv

def relatorio(dados):
    extensao='.csv'
    arquivo=datetime.datetime.now().strftime('%d_%m_%Y')
    nome_arquivo=arquivo+extensao
    saida=csv.writer(file(nome_arquivo, 'w'))
    for linha in dados:
        saida.writerow(linha)            