# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 00:23:48 2013

@author: filipe
"""

def obter_Dados_Criar_Usuario(win):
    dados={}
    dados['nome']=win.text_box_nome_adicionar_func.GetValue()
    dados['matricula']=win.text_box_matricula.GetValue()
    if win.rfid_temp!=None:
        dados['rfid']=win.rfid_temp
    else:
        dados['rfid']=None
    dados['horarios']=win.temp_lista_horarios;
    return dados
    
def dia_Semana_Int2str(num,completo=False):
    dias=[]    
    if completo == False:    
        dias=['Dom','Seg','Ter','Qua','Qui','Sex','Sab']
    else:
        dias=["Domingo","Segunda", u"Terça", "Quarta", "Quinta", "Sexta", "Sabado"]
    return dias[num-1]
        
def adicionar_Hora(win):
    dados={}
    dados['dia_semana']=win.combo_box_datas_adm.GetCurrentSelection()+1
    dados['hora_inicial']=win.text_box_hora_inicial.GetValue()
    dados['hora_final']=win.text_box_hora_final.GetValue()
    win.list_box_horarios.Append(dia_Semana_Int2str(dados['dia_semana'],True)+" "+dados['hora_inicial']+" - "+dados['hora_final'])
    return dados
    
def remover_Hora(win):
    index=win.list_box_horarios.GetSelection()
    print index
    del win.temp_lista_horarios[index]
    win.list_box_horarios.Delete(index)
    print win.temp_lista_horarios