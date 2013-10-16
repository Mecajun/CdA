# -*- coding: utf-8 -*-
"""
# Created on Mon Aug 26 00:27:34 2013

@author: filipe
"""

import view
import wx
import controller
import model_mysql

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    Frame1 = view.MainFrame(None, -1, "")

    db=model_mysql.Connect_MySQL("localhost","root","42")
    Frame1.set_Db(db)
    
    app.SetTopWindow(Frame1)

    #arduino=controller.Comunica_Arduino()
    
    controller.Relogio()
    controller.Fecha_Pontos(db)

    Frame1.Show()
    app.MainLoop()
