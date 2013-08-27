# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 00:27:34 2013

@author: filipe
"""

import model_mysql
import gui
import wx
import threading
import time


class Controller_main(threading.Thread):
    def __init__(self):
        super(Controller_main, self).__init__()
    
    def run(self):
        while True:
            time.sleep(1)
            print time.asctime()
    
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    Frame1 = gui.MainFrame(None, -1, "")
    app.SetTopWindow(Frame1)
    a=Controller_main()
    a.start()    
    Frame1.Show()
    app.MainLoop()