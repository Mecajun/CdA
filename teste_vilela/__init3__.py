# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 00:27:34 2013

@author: filipe
"""

import gui5
import wx
import controller3
    
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    Frame1 = gui5.MainFrame(None, -1, "")
    app.SetTopWindow(Frame1)

    #arduino=controller.Comunica_Arduino()
    hora=controller.Relogio()
    hora.start()

    Frame1.Show()
    app.MainLoop()