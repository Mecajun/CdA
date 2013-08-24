#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Fri Aug 23 20:36:53 2013

import wx

# begin wxGlade: extracode
# end wxGlade


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.logo = wx.StaticBitmap(self, -1, wx.Bitmap("./images/logo.png", wx.BITMAP_TYPE_ANY))
        self.button_administracao = wx.Button(self, -1, u"Administração")
        self.button_horarios = wx.Button(self, -1, u"Horários", style=wx.BU_BOTTOM)
        self.label_titulo1 = wx.StaticText(self, -1, u"Mecajun\nMecatrônica Júnior de Brasília", style=wx.ALIGN_CENTRE)
        self.label_Instrucoes = wx.StaticText(self, -1, u"\nDigite sua matrícula e aperte \"Enter\"\n", style=wx.ALIGN_CENTRE)
        self.label_matricula = wx.StaticText(self, -1, "Matricula:     ")
        self.text_box_matricula = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.label_debug = wx.StaticText(self, -1, "Em desenvolvimento!")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.adm_Button_Clicked, self.button_administracao)
        self.Bind(wx.EVT_BUTTON, self.horarios_Button_Clicked, self.button_horarios)
        self.Bind(wx.EVT_TEXT_ENTER, self.entrada_Teclado_Matricula, self.text_box_matricula)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("Controle de Acesso")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("./images/logo.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.label_titulo1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.text_box_matricula.SetMinSize((220, 27))
        self.label_debug.SetMinSize((220, 50))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.logo, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(self.button_administracao, 0, wx.EXPAND, 0)
        sizer_5.Add(self.button_horarios, 0, wx.EXPAND | wx.ALIGN_BOTTOM, 0)
        sizer_2.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 4, wx.EXPAND, 0)
        sizer_3.Add(self.label_titulo1, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_3.Add(self.label_Instrucoes, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_4.Add(self.label_matricula, 0, 0, 0)
        sizer_4.Add(self.text_box_matricula, 0, 0, 0)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_3.Add(self.label_debug, 0, wx.EXPAND, 0)
        sizer_1.Add(sizer_3, 5, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def adm_Button_Clicked(self, event):  # wxGlade: MainFrame.<event_handler>
        print "Event handler `adm_Button_Clicked' not implemented!"
        event.Skip()

    def horarios_Button_Clicked(self, event):  # wxGlade: MainFrame.<event_handler>
        print "Event handler `horarios_Button_Clicked' not implemented!"
        event.Skip()

    def entrada_Teclado_Matricula(self, event):  # wxGlade: MainFrame.<event_handler>
        print "Event handler `entrada_Teclado_Matricula' not implemented!"
        event.Skip()

# end of class MainFrame

class Frame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Frame.__init__
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.MAXIMIZE | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.RESIZE_BORDER | wx.CLIP_CHILDREN
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
        self.notebook_1_configuracoes = wx.Panel(self.notebook_pages, -1)
        self.notebook_1_funcionarios = wx.Panel(self.notebook_pages, -1)
        self.label_funcionarios_lista = wx.StaticText(self.notebook_1_funcionarios, -1, "\nFuncionarios cadastrados\n", style=wx.ALIGN_CENTRE)
        self.list_funcionarios = wx.ListBox(self.notebook_1_funcionarios, -1, choices=[], style=wx.LB_SINGLE)
        self.button_remover_funcionario = wx.Button(self.notebook_1_funcionarios, -1, "Remover")
        self.label_Funcionarios_add_desc = wx.StaticText(self.notebook_1_funcionarios, -1, u"\nAdicione um novo funcionário\n", style=wx.ALIGN_CENTRE)
        self.label_funcionarios_add = wx.StaticText(self.notebook_1_funcionarios, -1, "Nome")
        self.text_box_nome_adicionar_func = wx.TextCtrl(self.notebook_1_funcionarios, -1, "")
        self.button_adicionar_func = wx.Button(self.notebook_1_funcionarios, -1, "Adicionar")
        self.label_informacao_func = wx.StaticText(self.notebook_1_funcionarios, -1, u"Informações detalhadas do funcionario")
        self.label_matricula_adm = wx.StaticText(self.notebook_1_funcionarios, -1, "Matricula")
        self.text_box_matricula = wx.TextCtrl(self.notebook_1_funcionarios, -1, "")
        self.label_rfid_adm = wx.StaticText(self.notebook_1_funcionarios, -1, "RFID")
        self.button_obter_rfid = wx.Button(self.notebook_1_funcionarios, -1, "Obter RFID")
        self.label_data_adm = wx.StaticText(self.notebook_1_funcionarios, -1, "Data")
        self.combo_box_datas_adm = wx.ComboBox(self.notebook_1_funcionarios, -1, choices=["Segunda", u"Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"], style=wx.CB_DROPDOWN)
        self.label_hora = wx.StaticText(self.notebook_1_funcionarios, -1, "Hora")
        self.label_hora_inicial = wx.StaticText(self.notebook_1_funcionarios, -1, "Inicio")
        self.text_box_hora_inicial = wx.TextCtrl(self.notebook_1_funcionarios, -1, "")
        self.label_hora_final = wx.StaticText(self.notebook_1_funcionarios, -1, "   Fim")
        self.text_box_hora_final = wx.TextCtrl(self.notebook_1_funcionarios, -1, "")
        self.list_box_horarios = wx.ListBox(self.notebook_1_funcionarios, -1, choices=[])
        self.button_adicionar_horario = wx.Button(self.notebook_1_funcionarios, -1, "Adicionar")
        self.button_remover_horario = wx.Button(self.notebook_1_funcionarios, -1, "Remover")
        self.button_salvar_alteracoes = wx.Button(self.notebook_1_funcionarios, -1, u"Salvar alterações", style=wx.BU_RIGHT)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_LISTBOX, self.detalhar_funcionario, self.list_funcionarios)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Frame.__set_properties
        self.SetTitle("Menu Administrativo")
        self.datepicker_box_data_inicial.SetMinSize((300, 27))
        self.datepicker_box_data_final.SetMinSize((300, 27))
        self.checkbox_pontuais.SetValue(1)
        self.checkbox_atrasos.SetValue(1)
        self.checkbox_faltas.SetValue(1)
        self.list_funcionarios.SetMinSize((220, 300))
        self.text_box_nome_adicionar_func.SetMinSize((80, 27))
        self.combo_box_datas_adm.SetSelection(-1)
        self.list_box_horarios.SetMinSize((400, 100))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Frame.__do_layout
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        sizer_17 = wx.BoxSizer(wx.VERTICAL)
        sizer_18 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_16 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_1 = wx.GridSizer(5, 2, 0, 0)
        sizer_19 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
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
        sizer_10.Add(self.label_funcionarios_lista, 0, wx.EXPAND, 0)
        sizer_10.Add(self.list_funcionarios, 0, wx.EXPAND, 0)
        sizer_10.Add(self.button_remover_funcionario, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_10.Add(self.label_Funcionarios_add_desc, 0, wx.EXPAND, 0)
        sizer_11.Add(self.label_funcionarios_add, 0, 0, 0)
        sizer_11.Add(self.text_box_nome_adicionar_func, 0, 0, 0)
        sizer_11.Add(self.button_adicionar_func, 0, 0, 0)
        sizer_10.Add(sizer_11, 0, wx.EXPAND, 0)
        sizer_8.Add(sizer_10, 0, 0, 0)
        sizer_6.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_informacao_func, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_matricula_adm, 0, 0, 0)
        grid_sizer_1.Add(self.text_box_matricula, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_rfid_adm, 0, 0, 0)
        grid_sizer_1.Add(self.button_obter_rfid, 0, 0, 0)
        grid_sizer_1.Add(self.label_data_adm, 0, 0, 0)
        grid_sizer_1.Add(self.combo_box_datas_adm, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_hora, 0, 0, 0)
        sizer_19.Add(self.label_hora_inicial, 0, 0, 0)
        sizer_19.Add(self.text_box_hora_inicial, 0, 0, 0)
        sizer_19.Add(self.label_hora_final, 0, 0, 0)
        sizer_19.Add(self.text_box_hora_final, 0, 0, 0)
        grid_sizer_1.Add(sizer_19, 1, wx.EXPAND, 0)
        sizer_16.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_15.Add(sizer_16, 1, wx.EXPAND, 0)
        sizer_17.Add(self.list_box_horarios, 0, wx.EXPAND, 0)
        sizer_18.Add(self.button_adicionar_horario, 0, 0, 0)
        sizer_18.Add(self.button_remover_horario, 0, 0, 0)
        sizer_17.Add(sizer_18, 1, wx.EXPAND, 0)
        sizer_15.Add(sizer_17, 1, wx.EXPAND, 0)
        sizer_15.Add(self.button_salvar_alteracoes, 0, 0, 0)
        sizer_6.Add(sizer_15, 1, wx.EXPAND, 0)
        sizer_6.Add((20, 20), 0, 0, 0)
        sizer_8.Add(sizer_6, 1, wx.EXPAND, 0)
        self.notebook_1_funcionarios.SetSizer(sizer_8)
        self.notebook_pages.AddPage(self.notebook_relatorio, "Relatorio")
        self.notebook_pages.AddPage(self.notebook_1_configuracoes, u"Configurações")
        self.notebook_pages.AddPage(self.notebook_1_funcionarios, "Funcionarios")
        sizer_7.Add(self.notebook_pages, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_7)
        sizer_7.Fit(self)
        self.Layout()
        # end wxGlade

    def detalhar_funcionario(self, event):  # wxGlade: Frame.<event_handler>
        print "Event handler `detalhar_funcionario' not implemented!"
        event.Skip()

# end of class Frame
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    janela_principal = MainFrame(None, -1, "")
    app.SetTopWindow(janela_principal)
    janela_principal.Show()
    app.MainLoop()
