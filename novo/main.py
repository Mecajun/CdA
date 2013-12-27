import view
import model_mysql
import sys

from auxiliares import set_proc_name
from PySide.QtGui import *
from PySide.QtCore import *


set_proc_name('Controle de Acesso')

db_dados={'host':'localhost','user':'root','passwd':'42'}

try:
	app = QApplication(sys.argv)
	ex = view.Controle_De_Acesso_Window(None,db_dados)
	sys.exit(app.exec_())
except Exception:
	pass
