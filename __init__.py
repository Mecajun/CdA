# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 00:27:34 2013

@author: filipe
"""

import gui
import wx
import controller
    
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    Frame1 = gui.MainFrame(None, -1, "")
    app.SetTopWindow(Frame1)

    arduino=controller.Comunica_Arduino()

    Frame1.Show()
    app.MainLoop()