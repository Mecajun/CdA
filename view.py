#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Fri Sep 27 15:34:17 2013

import wx
from wx.lib.pubsub import Publisher
import controller
import time
import os
import datetime
# begin wxGlade: extracode
# end wxGlade

class MainFrame(wx.Frame):     
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)
        full_path = os.path.realpath(__file__)
        self.logo = wx.StaticBitmap(self, -1, wx.Bitmap(os.path.dirname(full_path)+"/logo.png", wx.BITMAP_TYPE_ANY))
        self.button_administracao = wx.Button(self, -1, u"Administração")
        self.button_horarios = wx.Button(self, -1, u"Horários", style=wx.BU_BOTTOM)
        self.label_titulo1 = wx.StaticText(self, -1, u"Mecajun\nMecatrônica Júnior de Brasília", style=wx.ALIGN_CENTRE)
        self.label_Instrucoes = wx.StaticText(self, -1, u"\nDigite sua matrícula e aperte \"Enter\"\n", style=wx.ALIGN_CENTRE)
        self.label_matricula = wx.StaticText(self, -1, "Matricula:     ")
        self.text_box_matricula = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.label_2 = wx.StaticText(self, -1, u"Funcionarios do horário:")
        # self.list_box_funcionarios_esperados = wx.ListBox(self, -1, choices=[])
        self.list_box_funcionarios_esperados = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.list_box_funcionarios_esperados.InsertColumn(0, 'Nome')
        self.list_box_funcionarios_esperados.InsertColumn(1, 'Logado')

        self.label_relogio = wx.StaticText(self, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, "24:59")
        
        Publisher().subscribe(self.atualiza_Relogio, "evento_mostrar_relogio")
        Publisher().subscribe(self.abrir_Adm, "evento_abrir_adm")
        Publisher().subscribe(self.atualiza_list_box_funcionarios_esperados, "evento_funcionarios_esperados")

        self.__set_properties()
        self.__do_layout()

        self.SetBackgroundColour((220, 220, 220))
        self.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)

        self.Bind(wx.EVT_BUTTON, self.adm_Button_Clicked, self.button_administracao)
        self.Bind(wx.EVT_BUTTON, self.horarios_Button_Clicked, self.button_horarios)
        self.Bind(wx.EVT_TEXT_ENTER, self.entrada_Teclado_Matricula, self.text_box_matricula)

        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("Controle de Acesso")
        self.label_titulo1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.text_box_matricula.SetMinSize((220, 27))
        self.label_2.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Times"))
        self.list_box_funcionarios_esperados.SetMinSize((160, 70))
        self.Centre()
        self.text_box_matricula.SetFocus()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_22 = wx.BoxSizer(wx.VERTICAL)
        sizer_23 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.logo, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(self.button_administracao, 0, wx.BOTTOM | wx.EXPAND, 0)
        sizer_5.Add(self.button_horarios, 0, wx.BOTTOM | wx.EXPAND, 0)
        sizer_2.Add(sizer_5, 0, wx.BOTTOM | wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 4, wx.EXPAND, 0)
        sizer_3.Add(self.label_titulo1, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_3.Add(self.label_Instrucoes, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_4.Add(self.label_matricula, 0, 0, 0)
        sizer_4.Add(self.text_box_matricula, 0, 0, 0)
        sizer_3.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_22.Add(self.label_2, 0, 0, 0)
        sizer_23.Add(self.list_box_funcionarios_esperados, 1, wx.EXPAND, 0)
        sizer_23.Add(self.label_relogio, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_22.Add(sizer_23, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_22, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_3, 5, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def set_Db(self,db):
        self.db=db

    def adm_Button_Clicked(self, event):  # wxGlade: MainFrame.<event_handler>
        self.adm_senha_frame = Adm_Senha_Frame(None,-1)
        self.adm_senha_frame.set_Db(self.db)
        self.adm_senha_frame.Show()
        event.Skip()

    def abrir_Adm(self,event):
        self.adm_frame = Adm_Frame(None,-1)
        self.adm_frame.set_Db(self.db)
        self.adm_frame.Show()

    def horarios_Button_Clicked(self, event):  # wxGlade: MainFrame.<event_handler>
        self.horarios_janela = Horarios(None,-1)
        self.horarios_janela.set_Db(self.db)
        self.horarios_janela.Show()
        event.Skip()

    def entrada_Teclado_Matricula(self, event):  # wxGlade: MainFrame.<event_handler>
        ponto=controller.dar_Ponto(self.db,self.text_box_matricula.GetValue())
        if ponto=="nao existe":
            self.text_box_matricula.SetBackgroundColour((255,255,0))
        else:
            self.text_box_matricula.SetBackgroundColour((255,255,255))
            self.text_box_matricula.SetValue("")
        event.Skip()

    def atualiza_Relogio(self,hora):
        self.label_relogio.SetLabel(hora.data)

    def atualiza_list_box_funcionarios_esperados(self,lista):
        self.list_box_funcionarios_esperados.ClearAll()
        self.list_box_funcionarios_esperados.InsertColumn(0, 'Nome')
        self.list_box_funcionarios_esperados.InsertColumn(1, 'Logado')
        horarios=lista.data
        index=0
        sn=(u"Não",u"Sim")
        for data in horarios:
            self.list_box_funcionarios_esperados.InsertStringItem(0,data[0])
            self.list_box_funcionarios_esperados.SetStringItem(0, 1,sn[data[1]])
            index = index + 1
        self.list_box_funcionarios_esperados.SetColumnWidth(0, 100)
        self.list_box_funcionarios_esperados.SetColumnWidth(1, 60)

# end of class MainFrame

class Horarios(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] =  wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)
        self.list_ctrl_horarios = wx.ListCtrl(self, -1, style=wx.LC_REPORT
                         |wx.BORDER_SUNKEN)
        self.list_ctrl_horarios.InsertColumn(0, "Nome")
        self.list_ctrl_horarios.InsertColumn(1, "Dia da semana")
        self.list_ctrl_horarios.InsertColumn(2, "Horario de entrada")
        self.list_ctrl_horarios.InsertColumn(3, "Horario de saida")

        for i in xrange(4):
            self.list_ctrl_horarios.SetColumnWidth(i, 150)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Horarios")
        self.Centre()
        self.SetMinSize((150*4,500))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.list_ctrl_horarios, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def set_Db(self,db):
        self.db=db
        self.configure()

    def configure(self):
        horarios=controller.obter_Horarios(self.db)
        index=0
        if horarios!=None:
            for data in horarios:
                self.list_ctrl_horarios.InsertStringItem(index, data[0])
                self.list_ctrl_horarios.SetStringItem(index, 1, data[1])
                self.list_ctrl_horarios.SetStringItem(index, 2, data[2])
                self.list_ctrl_horarios.SetStringItem(index, 3, data[3])
                self.list_ctrl_horarios.SetItemData(index, index)
                index += 1

class Adm_Frame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Frame.__init__
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook_pages = wx.Notebook(self, -1, style=0)
        self.notebook_relatorio = wx.Panel(self.notebook_pages, -1)
        self.label_data_inicial = wx.StaticText(self.notebook_relatorio, -1, "Data Inicial:    ")
        self.datepicker_box_data_inicial = wx.DatePickerCtrl(self.notebook_relatorio, -1)
        self.label_data_final = wx.StaticText(self.notebook_relatorio, -1, "Data Final:      ")
        self.datepicker_box_data_final = wx.DatePickerCtrl(self.notebook_relatorio, -1)
        self.checkbox_pontuais = wx.CheckBox(self.notebook_relatorio, -1, u"Funcionários Pontuais")
        self.checkbox_atrasos = wx.CheckBox(self.notebook_relatorio, -1, u"Funcionários Atrasados")
        self.checkbox_faltas = wx.CheckBox(self.notebook_relatorio, -1, u"Funcionários Faltosos")
        self.button_gerar_relatorio = wx.Button(self.notebook_relatorio, -1, "Gerar")
        self.panel_9 = wx.Panel(self.notebook_pages, -1)
        self.label_6 = wx.StaticText(self.panel_9, -1, u"Tolerância de Entrada:")
        self.spin_ctrl_1 = wx.SpinCtrl(self.panel_9, -1, "", min=0, max=500)
        self.label_9 = wx.StaticText(self.panel_9, -1, "      antes e")
        self.spin_ctrl_3 = wx.SpinCtrl(self.panel_9, -1, "", min=0, max=500)
        self.label_11 = wx.StaticText(self.panel_9, -1, "    depois")
        self.label_7 = wx.StaticText(self.panel_9, -1, u"Tolerância de Saída:")
        self.spin_ctrl_2 = wx.SpinCtrl(self.panel_9, -1, "", min=0, max=500)
        self.label_10 = wx.StaticText(self.panel_9, -1, "      antes e")
        self.spin_ctrl_4 = wx.SpinCtrl(self.panel_9, -1, "", min=0, max=500)
        self.label_12 = wx.StaticText(self.panel_9, -1, "    depois")
        self.label_8 = wx.StaticText(self.panel_9, -1, u"Considerar atraso após")
        self.spin_ctrl_5 = wx.SpinCtrl(self.panel_9, -1, "", min=0, max=500)
        self.label_13 = wx.StaticText(self.panel_9, -1, "       depois")
        self.panel_1 = wx.Panel(self.panel_9, -1)
        self.button_alterar_senha = wx.Button(self.panel_9, -1, "Alterar senha do Administrador")
        self.panel_17 = wx.Panel(self.panel_9, -1)
        self.notebook_1_funcionarios = wx.Panel(self.notebook_pages, -1)
        self.label_funcionarios_lista = wx.StaticText(self.notebook_1_funcionarios, -1, "\nFuncionarios cadastrados\n", style=wx.ALIGN_CENTRE)
        self.list_funcionarios = wx.ListBox(self.notebook_1_funcionarios, -1, choices=[], style=wx.LB_SINGLE)
        self.button_remover_funcionario = wx.Button(self.notebook_1_funcionarios, -1, "Remover")
        self.button_editar_funcionario = wx.Button(self.notebook_1_funcionarios, -1, "Editar")
        self.button_adicionar_funcionario = wx.Button(self.notebook_1_funcionarios, -1, "Adicionar")
        self.label_Funcionarios_add_desc = wx.StaticText(self.notebook_1_funcionarios, -1, u"\nAdicione um novo funcionário\n", style=wx.ALIGN_CENTRE)
        self.label_funcionarios_add = wx.StaticText(self.notebook_1_funcionarios, -1, "Nome")
        self.text_box_nome_adicionar_func = wx.TextCtrl(self.notebook_1_funcionarios, -1, "")
        self.text_box_nome_adicionar_func.SetMaxLength(100);
        self.label_24 = wx.StaticText(self.notebook_1_funcionarios, -1, u"Informaçôes detalhadas do funcionário:")
        self.label_25 = wx.StaticText(self.notebook_1_funcionarios, -1, u"Matrícula:                                 ")
        self.text_ctrl_4 = wx.TextCtrl(self.notebook_1_funcionarios, -1, "")
        self.text_ctrl_4.SetMaxLength(40);
        self.label_26 = wx.StaticText(self.notebook_1_funcionarios, -1, "RFID                                             ")
        self.button_7 = wx.Button(self.notebook_1_funcionarios, -1, "Obter RFID")
        self.label_27 = wx.StaticText(self.notebook_1_funcionarios, -1, "Data                                            ")
        self.combo_box_data = wx.ComboBox(self.notebook_1_funcionarios, -1, choices=["Domingo", "Segunda", u"Terça", "Quarta", "Quinta", "Sexta", u"Sábado"], style=wx.CB_DROPDOWN)
        self.label_14 = wx.StaticText(self.notebook_1_funcionarios, -1, u"Horários:")
        self.label_15 = wx.StaticText(self.notebook_1_funcionarios, -1, u"         Início  ")
        self.spin_horario_inicio_horas = wx.SpinCtrl(self.notebook_1_funcionarios, -1, "", min=0, max=23)
        self.label_16 = wx.StaticText(self.notebook_1_funcionarios, -1, "      horas e   ")
        self.spin_horario_inicio_minutos = wx.SpinCtrl(self.notebook_1_funcionarios, -1, "", min=0, max=59)
        self.label_17 = wx.StaticText(self.notebook_1_funcionarios, -1, "     minutos")
        self.label_18 = wx.StaticText(self.notebook_1_funcionarios, -1, "Fim      ")
        self.spin_horario_fim_horas = wx.SpinCtrl(self.notebook_1_funcionarios, -1, "", min=0, max=23)
        self.label_19 = wx.StaticText(self.notebook_1_funcionarios, -1, "      horas e   ")
        self.spin_horario_fim_minutos = wx.SpinCtrl(self.notebook_1_funcionarios, -1, "", min=0, max=59)
        self.label_20 = wx.StaticText(self.notebook_1_funcionarios, -1, "     minutos")
        self.list_box_horarios = wx.ListBox(self.notebook_1_funcionarios, -1, choices=[])
        self.button_adicionar = wx.Button(self.notebook_1_funcionarios, -1, "Adicionar")
        self.button_remover = wx.Button(self.notebook_1_funcionarios, -1, "Remover")
        self.button_salvar_alteracoes = wx.Button(self.notebook_1_funcionarios, -1, u"Salvar Alterações")

        self.__set_properties()
        self.__do_layout()

        self.horarios_box=[]
        self.edicao=False

        self.Bind(wx.EVT_BUTTON, self.button_Gerar_Relatorio, self.button_gerar_relatorio)
        self.Bind(wx.EVT_BUTTON, self.alterar_Senha_Adm_Button_Clicked, self.button_alterar_senha)
        self.Bind(wx.EVT_BUTTON, self.button_Remover_Funcionario, self.button_remover_funcionario)
        self.Bind(wx.EVT_BUTTON, self.button_Detalhar_Funcionario, self.button_editar_funcionario)
        self.Bind(wx.EVT_BUTTON, self.button_Adicionar_Funcionario, self.button_adicionar_funcionario)
        self.Bind(wx.EVT_BUTTON, self.button_Obter_Rfid, self.button_7)
        self.Bind(wx.EVT_BUTTON, self.button_Adicionar_Hora, self.button_adicionar)
        self.Bind(wx.EVT_BUTTON, self.button_Remover_Hora, self.button_remover)
        self.Bind(wx.EVT_BUTTON, self.button_Salvar_Alteracoes, self.button_salvar_alteracoes)

        self.Bind(wx.EVT_SPINCTRL, self.muda_Saida_Base, self.spin_horario_inicio_horas)
        self.Bind(wx.EVT_SPINCTRL, self.muda_Saida_Base, self.spin_horario_inicio_minutos)
        self.Bind(wx.EVT_SPINCTRL, self.muda_Saida_Base, self.spin_horario_fim_horas)
        self.Bind(wx.EVT_SPINCTRL, self.muda_Saida_Base, self.spin_horario_fim_minutos)

        self.Bind(wx.EVT_CLOSE,self.OnClose)

        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Frame.__set_properties
        self.SetTitle("Menu Administrativo")
        self.datepicker_box_data_inicial.SetMinSize((300, 27))
        self.datepicker_box_data_final.SetMinSize((300, 27))
        self.checkbox_pontuais.SetValue(1)
        self.checkbox_atrasos.SetValue(1)
        self.checkbox_faltas.SetValue(1)
        self.label_9.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Ubuntu"))
        self.label_7.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Ubuntu"))
        self.label_8.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Ubuntu"))
        self.list_funcionarios.SetMinSize((220, 300))
        self.text_box_nome_adicionar_func.SetMinSize((200, 27))
        self.combo_box_data.SetSelection(0)
        self.spin_horario_inicio_horas.SetMinSize((49, 27))
        self.spin_horario_inicio_minutos.SetMinSize((49, 27))
        self.spin_horario_fim_horas.SetMinSize((49, 27))
        self.spin_horario_fim_minutos.SetMinSize((49, 27))
        self.list_box_horarios.SetMinSize((400, 63))
        self.Centre()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Frame.__do_layout
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        sizer_17 = wx.BoxSizer(wx.VERTICAL)
        sizer_18 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_19 = wx.BoxSizer(wx.VERTICAL)
        sizer_34 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_33 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_35 = wx.BoxSizer(wx.VERTICAL)
        sizer_41 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_40 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_38 = wx.BoxSizer(wx.VERTICAL)
        sizer_39 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_32 = wx.BoxSizer(wx.VERTICAL)
        sizer_36 = wx.BoxSizer(wx.VERTICAL)
        sizer_37 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_2 = wx.GridSizer(3, 3, 0, 0)
        sizer_31 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_30 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_25 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_26 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_24 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        remover_editar_box = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9.Add((20, 20), 0, 0, 0)
        sizer_12.Add(self.label_data_inicial, 0, 0, 0)
        sizer_12.Add(self.datepicker_box_data_inicial, 0, 0, 0)
        sizer_9.Add(sizer_12, 1, wx.EXPAND, 0)
        sizer_9.Add((20, 20), 0, 0, 0)
        sizer_13.Add(self.label_data_final, 0, 0, 0)
        sizer_13.Add(self.datepicker_box_data_final, 0, 0, 0)
        sizer_9.Add(sizer_13, 1, wx.EXPAND, 0)
        sizer_9.Add((20, 20), 0, 0, 0)
        sizer_14.Add(self.checkbox_pontuais, 0, 0, 0)
        sizer_14.Add(self.checkbox_atrasos, 0, 0, 0)
        sizer_14.Add(self.checkbox_faltas, 0, 0, 0)
        sizer_9.Add(sizer_14, 1, wx.EXPAND, 0)
        sizer_9.Add(self.button_gerar_relatorio, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_9.Add((20, 20), 0, 0, 0)
        self.notebook_relatorio.SetSizer(sizer_9)
        sizer_32.Add((20, 20), 0, 0, 0)
        grid_sizer_2.Add(self.label_6, 0, 0, 0)
        sizer_24.Add(self.spin_ctrl_1, 0, 0, 0)
        sizer_24.Add(self.label_9, 0, 0, 0)
        grid_sizer_2.Add(sizer_24, 1, wx.EXPAND, 0)
        sizer_26.Add(self.spin_ctrl_3, 0, 0, 0)
        sizer_26.Add(self.label_11, 0, 0, 0)
        grid_sizer_2.Add(sizer_26, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.label_7, 0, 0, 0)
        sizer_25.Add(self.spin_ctrl_2, 0, 0, 0)
        sizer_25.Add(self.label_10, 0, 0, 0)
        grid_sizer_2.Add(sizer_25, 1, wx.EXPAND, 0)
        sizer_30.Add(self.spin_ctrl_4, 0, 0, 0)
        sizer_30.Add(self.label_12, 0, 0, 0)
        grid_sizer_2.Add(sizer_30, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.label_8, 0, 0, 0)
        sizer_31.Add(self.spin_ctrl_5, 0, 0, 0)
        sizer_31.Add(self.label_13, 0, 0, 0)
        grid_sizer_2.Add(sizer_31, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.panel_1, 1, wx.EXPAND, 0)
        sizer_32.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        sizer_36.Add((20, 20), 0, 0, 0)
        sizer_37.Add(self.button_alterar_senha, 0, 0, 0)
        sizer_37.Add(self.panel_17, 1, 0, 0)
        sizer_36.Add(sizer_37, 1, wx.EXPAND, 0)
        sizer_32.Add(sizer_36, 1, wx.EXPAND, 0)
        self.panel_9.SetSizer(sizer_32)
        sizer_10.Add(self.label_funcionarios_lista, 0, wx.EXPAND, 0)
        sizer_10.Add(self.list_funcionarios, 0, wx.EXPAND, 0)
        remover_editar_box.Add(self.button_remover_funcionario,1)
        remover_editar_box.Add(self.button_editar_funcionario,1)
        remover_editar_box.Add(self.button_adicionar_funcionario,1)
        sizer_10.Add(remover_editar_box, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_10.Add(self.label_Funcionarios_add_desc, 0, wx.EXPAND, 0)
        sizer_11.Add(self.label_funcionarios_add, 0, 0, 0)
        sizer_11.Add(self.text_box_nome_adicionar_func, 0, wx.EXPAND, 0)
        sizer_10.Add(sizer_11, 0, wx.EXPAND, 0)
        sizer_8.Add(sizer_10, 0, 0, 0)
        sizer_6.Add((20, 20), 0, 0, 0)
        sizer_38.Add(self.label_24, 0, 0, 0)
        sizer_39.Add(self.label_25, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_39.Add(self.text_ctrl_4, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_38.Add(sizer_39, 1, wx.EXPAND, 0)
        sizer_15.Add(sizer_38, 1, wx.EXPAND, 0)
        sizer_40.Add(self.label_26, 0, 0, 0)
        sizer_40.Add(self.button_7, 0, 0, 0)
        sizer_35.Add(sizer_40, 1, wx.EXPAND, 0)
        sizer_41.Add(self.label_27, 0, 0, 0)
        sizer_41.Add(self.combo_box_data, 0, 0, 0)
        sizer_35.Add(sizer_41, 1, wx.EXPAND, 0)
        sizer_15.Add(sizer_35, 1, wx.EXPAND, 0)
        sizer_33.Add(self.label_14, 0, 0, 0)
        sizer_33.Add(self.label_15, 0, 0, 0)
        sizer_33.Add(self.spin_horario_inicio_horas, 0, 0, 0)
        sizer_33.Add(self.label_16, 0, 0, 0)
        sizer_33.Add(self.spin_horario_inicio_minutos, 0, 0, 0)
        sizer_33.Add(self.label_17, 0, 0, 0)
        sizer_19.Add(sizer_33, 1, wx.EXPAND, 0)
        sizer_34.Add((90, 40), 0, 0, 0)
        sizer_34.Add(self.label_18, 0, 0, 0)
        sizer_34.Add(self.spin_horario_fim_horas, 0, 0, 0)
        sizer_34.Add(self.label_19, 0, 0, 0)
        sizer_34.Add(self.spin_horario_fim_minutos, 0, 0, 0)
        sizer_34.Add(self.label_20, 0, 0, 0)
        sizer_19.Add(sizer_34, 1, wx.EXPAND, 0)
        sizer_15.Add(sizer_19, 1, wx.EXPAND, 0)
        sizer_17.Add(self.list_box_horarios, 0, 0, 0)
        sizer_18.Add(self.button_adicionar, 0, 0, 0)
        sizer_18.Add(self.button_remover, 0, 0, 0)
        sizer_17.Add(sizer_18, 1, wx.EXPAND, 0)
        sizer_15.Add(sizer_17, 1, wx.EXPAND, 0)
        sizer_15.Add(self.button_salvar_alteracoes, 0, 0, 0)
        sizer_6.Add(sizer_15, 1, wx.EXPAND, 0)
        sizer_6.Add((20, 20), 0, 0, 0)
        sizer_8.Add(sizer_6, 1, wx.EXPAND, 0)
        self.notebook_1_funcionarios.SetSizer(sizer_8)
        self.notebook_pages.AddPage(self.notebook_relatorio, "Relatorio")
        self.notebook_pages.AddPage(self.panel_9, u"Configurações")
        self.notebook_pages.AddPage(self.notebook_1_funcionarios, "Funcionarios")
        sizer_7.Add(self.notebook_pages, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_7)
        sizer_7.Fit(self)
        self.Layout()
        # end wxGlade

    def OnClose(self,event):
        controller.atualizar_Configuracao(self.db, 'tol_ent_ant', self.spin_ctrl_1.GetValue())
        controller.atualizar_Configuracao(self.db, 'tol_ent_dep', self.spin_ctrl_3.GetValue())
        controller.atualizar_Configuracao(self.db, 'tol_sai_ant', self.spin_ctrl_2.GetValue())
        controller.atualizar_Configuracao(self.db, 'tol_sai_dep', self.spin_ctrl_4.GetValue())
        controller.atualizar_Configuracao(self.db, 'considerar_atraso', self.spin_ctrl_5.GetValue())
        event.Skip()

    def muda_Saida_Base(self,event):
        hora=int(self.spin_horario_inicio_horas.GetValue())
        mim=int(self.spin_horario_inicio_minutos.GetValue())
        hora_fim=int(self.spin_horario_fim_horas.GetValue())
        mim_fim=int(self.spin_horario_fim_minutos.GetValue())
        self.spin_horario_fim_horas.SetRange(hora,23)
        if hora==hora_fim:
            self.spin_horario_fim_minutos.SetRange(mim,59)
        else:
            self.spin_horario_fim_minutos.SetRange(0,59)

        hora=int(self.spin_horario_inicio_horas.GetValue())
        mim=int(self.spin_horario_inicio_minutos.GetValue())
        hora_fim=int(self.spin_horario_fim_horas.GetValue())
        mim_fim=int(self.spin_horario_fim_minutos.GetValue())

    def list_Funcionarios(self):
        self.list_funcionarios.Clear()
        self.lista_funcionarios=controller.listar_Funcionarios(self.db)
        if self.lista_funcionarios!=None:
            for x in self.lista_funcionarios:
                self.list_funcionarios.Append(x[1])
            
    def configuracoes_Dados(self):
        dados=controller.obter_Configuracoes(self.db)
        self.spin_ctrl_1.SetValue(dados['tol_ent_ant'])
        self.spin_ctrl_3.SetValue(dados['tol_ent_dep'])
        self.spin_ctrl_2.SetValue(dados['tol_sai_ant'])
        self.spin_ctrl_4.SetValue(dados['tol_sai_dep'])
        self.spin_ctrl_5.SetValue(dados['considerar_atraso'])

    def button_Gerar_Relatorio(self, event):  # wxGlade: Frame.<event_handler>
        inicial = self.datepicker_box_data_inicial.GetValue()
        final = self.datepicker_box_data_final.GetValue()
        pontuais = self.checkbox_pontuais.GetValue()
        atrasos = self.checkbox_atrasos.GetValue()
        faltas = self.checkbox_faltas.GetValue()
        controller.gerar_Relatorio(self.db,inicial.FormatISODate(),final.FormatISODate(),{'pontuais':pontuais,'atrasos':atrasos,'faltas':faltas})
        event.Skip()

    def alterar_Senha_Adm_Button_Clicked(self, event):  # wxGlade: Frame.<event_handler>
        self.troca_senha_frame = Troca_Senha_Frame(None,-1)
        self.troca_senha_frame.set_Db(self.db)
        self.troca_senha_frame.Show()
        event.Skip()

    def button_Detalhar_Funcionario(self, event):  # wxGlade: Frame.<event_handler>
        posicao=self.list_funcionarios.GetSelection()
        atual=self.lista_funcionarios[posicao]
        self.limpa_Campos()
        dados=controller.detalha_Funcionario(self.db,id_funcionario=atual[0])
        self.edicao=dados
        self.edicao['horario_adicionado']=[]
        self.edicao['horario_removido']=[]
        self.text_box_nome_adicionar_func.SetValue(dados['nome'])
        self.text_ctrl_4.SetValue(dados['matricula'])
        self.horarios_box=dados['horarios']
        for horario in self.horarios_box:
            temp_str=controller.dia_Semana_Int2str(horario['dia_semana'])+"\t\t"+horario['hora_inicial']+" - "+horario['hora_final']
            self.list_box_horarios.Append(temp_str)
        event.Skip()

    def button_Remover_Funcionario(self, event):  # wxGlade: Frame.<event_handler>
        posicao=self.list_funcionarios.GetSelection()
        atual=self.lista_funcionarios[posicao]
        controller.remover_Funcionario(self.db,atual[0])
        self.list_Funcionarios()
        self.limpa_Campos()
        event.Skip()

    def button_Adicionar_Funcionario(self, event):  # wxGlade: Frame.<event_handler>
        self.edicao=False
        self.list_Funcionarios()
        self.limpa_Campos()
        event.Skip()

    def button_Obter_Rfid(self, event):  # wxGlade: Frame.<event_handler>
        print "Event handler `button_Obter_Rfid' not implemented!"
        event.Skip()

    def button_Adicionar_Hora(self, event):  # wxGlade: Frame.<event_handler>
        dado={}
        dado['dia_semana']=self.combo_box_data.GetCurrentSelection()+1
        dado['hora_inicial']=str(self.spin_horario_inicio_horas.GetValue()).zfill(2)+":"+str(self.spin_horario_inicio_minutos.GetValue()).zfill(2)
        dado['hora_final']=str(self.spin_horario_fim_horas.GetValue()).zfill(2)+":"+str(self.spin_horario_fim_minutos.GetValue()).zfill(2)
        self.horarios_box.append(dado)
        if self.edicao!=None and self.edicao!=False:
            self.edicao['horario_adicionado'].append(dado)
        temp_str=controller.dia_Semana_Int2str(dado['dia_semana'])+"\t\t"+dado['hora_inicial']+" - "+dado['hora_final']
        self.list_box_horarios.Append(temp_str)
        event.Skip()

    def button_Remover_Hora(self, event):  # wxGlade: Frame.<event_handler>
        posicao=self.list_box_horarios.GetSelection()
        if self.edicao!=None and self.edicao!=False:
            self.edicao['horario_removido'].append(self.horarios_box[posicao])
        del self.horarios_box[posicao]
        self.list_box_horarios.Delete(posicao)
        event.Skip()

    def obter_Detalhes_Usuario(self):
        dados={}
        dados['nome']=self.text_box_nome_adicionar_func.GetValue()
        dados['matricula']=self.text_ctrl_4.GetValue()
        dados['horarios']=self.horarios_box
        dados['rfid']=None
        return dados

    def limpa_Campos(self):
        self.text_box_nome_adicionar_func.Clear()
        self.text_ctrl_4.Clear()
        self.list_box_horarios.Clear()
        self.horarios_box=[]
        self.list_funcionarios.DeselectAll()
        self.spin_horario_inicio_horas.SetValue(0)
        self.spin_horario_inicio_minutos.SetValue(0)
        self.spin_horario_fim_horas.SetRange(0,23)
        self.spin_horario_fim_minutos.SetRange(0,59)
        self.spin_horario_fim_horas.SetValue(0)
        self.spin_horario_fim_minutos.SetValue(0)
        self.text_box_nome_adicionar_func.SetBackgroundColour((255,255,255))
        self.text_ctrl_4.SetBackgroundColour((255,255,255))

    def button_Salvar_Alteracoes(self, event):  # wxGlade: Frame.<event_handler>
        
        if self.edicao==False:
            dados=self.obter_Detalhes_Usuario()
            valida=controller.validar_Criacao_Funcionario(self.db, dados)
            if (dados['nome']!='' and dados['matricula']!='' and valida['existe']==None):
                controller.cadastrar_Funcionario(self.db,dados)
                self.limpa_Campos()
                self.list_Funcionarios()
                self.text_box_nome_adicionar_func.SetBackgroundColour((255,255,255))
                self.text_ctrl_4.SetBackgroundColour((255,255,255))
            else:
                if dados['nome']=='' or valida['nome']==True:
                    self.text_box_nome_adicionar_func.SetBackgroundColour((255,255,0))
                else:
                    self.text_box_nome_adicionar_func.SetBackgroundColour((255,255,255))
                if dados['matricula']=='' or valida['matricula']==True:
                    self.text_ctrl_4.SetBackgroundColour((255,255,0))
                else:
                    self.text_ctrl_4.SetBackgroundColour((255,255,255))
        else:
            dados=self.obter_Detalhes_Usuario()
            
            alterados={}
            if dados['nome']!=self.edicao['nome']:
                alterados['nome']=dados['nome']
            else:
                alterados['nome']=None
            if dados['matricula']!=self.edicao['matricula']:
                alterados['matricula']=dados['matricula']
            else:
                alterados['matricula']=None
            if dados['rfid']!=self.edicao['rfid']:
                alterados['rfid']=dados['rfid']
            else:
                alterados['rfid']=None
            alterados['id']=self.edicao['id']
            valida=controller.validar_Criacao_Funcionario(self.db, alterados)
            if (dados['nome']!='' and dados['matricula']!='' and valida['existe']==None):
                controller.edita_Funcionario(self.db,alterados)
                controller.atualizar_Horarios(self.db,self.edicao)
                self.limpa_Campos()
                self.text_box_nome_adicionar_func.SetBackgroundColour((255,255,255))
                self.text_ctrl_4.SetBackgroundColour((255,255,255))
                self.edicao=False
            else:
                if dados['nome']=='' or valida['nome']==True:
                    self.text_box_nome_adicionar_func.SetBackgroundColour((255,255,0))
                else:
                    self.text_box_nome_adicionar_func.SetBackgroundColour((255,255,255))
                if dados['matricula']=='' or valida['matricula']==True:
                    self.text_ctrl_4.SetBackgroundColour((255,255,0))
                else:
                    self.text_ctrl_4.SetBackgroundColour((255,255,255))
        self.list_Funcionarios()
        event.Skip()

    def set_Db(self,db):
        self.db=db
        self.list_Funcionarios()
        self.configuracoes_Dados()

# end of class Frame

class Adm_Senha_Frame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Adm_Senha_Frame.__init__
        kwds["style"] =  wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, -1, "Digite a senha de administrador")
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "", style=wx.TE_PASSWORD)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.textctr_Senha_Adm, self.text_ctrl_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Adm_Senha_Frame.__set_properties
        self.SetTitle("Senha Administrativo")
        self.text_ctrl_1.SetFocus()
        self.Centre()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Adm_Senha_Frame.__do_layout
        sizer_20 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_21 = wx.BoxSizer(wx.VERTICAL)
        sizer_20.Add((20, 20), 0, 0, 0)
        sizer_21.Add((20, 20), 0, 0, 0)
        sizer_21.Add(self.label_1, 0, 0, 0)
        sizer_21.Add((20, 20), 0, 0, 0)
        sizer_21.Add(self.text_ctrl_1, 0, wx.EXPAND, 0)
        sizer_21.Add((20, 20), 0, 0, 0)
        sizer_20.Add(sizer_21, 1, wx.EXPAND, 0)
        sizer_20.Add((20, 20), 0, 0, 0)
        self.SetSizer(sizer_20)
        sizer_20.Fit(self)
        self.Layout()
        # end wxGlade

    def set_Db(self,db):
        self.db=db

    def textctr_Senha_Adm(self, event):  # wxGlade: Adm_Senha_Frame.<event_handler>
        if controller.verifica_Senha_Adm(self.db,self.text_ctrl_1.GetValue())==True:
            wx.CallAfter(Publisher().sendMessage, "evento_abrir_adm", None)
            self.Destroy()
        event.Skip()

# end of class Adm_Senha_Frame

class Troca_Senha_Frame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Troca_Senha_Frame.__init__
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)
        self.label_3 = wx.StaticText(self, -1, "Nova senha:")
        self.text_ctrl_2 = wx.TextCtrl(self, -1, "", style=wx.TE_PASSWORD)
        self.label_4 = wx.StaticText(self, -1, "Confirmar senha:")
        self.text_ctrl_3 = wx.TextCtrl(self, -1, "", style=wx.TE_PASSWORD)
        self.button_2 = wx.Button(self, -1, "trocar")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.button_TrocouSenha_Clicked, self.button_2)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Troca_Senha_Frame.__set_properties
        self.SetTitle("Troca de senha")
        self.label_3.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Ubuntu"))
        self.label_4.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Ubuntu"))
        self.Centre()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Troca_Senha_Frame.__do_layout
        sizer_27 = wx.BoxSizer(wx.VERTICAL)
        sizer_28 = wx.BoxSizer(wx.VERTICAL)
        sizer_29 = wx.BoxSizer(wx.VERTICAL)
        sizer_28.Add(self.label_3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_28.Add(self.text_ctrl_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_29.Add(self.label_4, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_29.Add(self.text_ctrl_3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_28.Add(sizer_29, 1, wx.EXPAND, 0)
        sizer_28.Add(self.button_2, 0, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_27.Add(sizer_28, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_27)
        sizer_27.Fit(self)
        self.Layout()
        # end wxGlade

    def set_Db(self,db):
        self.db=db   

    def button_TrocouSenha_Clicked(self, event):  # wxGlade: Troca_Senha_Frame.<event_handler>
        senha1=self.text_ctrl_2.GetValue()
        senha2=self.text_ctrl_3.GetValue()
        if senha1==senha2:
            controller.alterar_Senha_Adm(self.db,senha1)
            self.Destroy()
        event.Skip()

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    janela_principal = MainFrame(None, -1, "")
    app.SetTopWindow(janela_principal)
    janela_principal.Show()
    app.MainLoop()