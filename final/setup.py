from distutils.core import setup
import py2exe
import sys
from glob import glob
sys.path.append(".\\Microsoft.VC90.CRT")
data_files = [("Microsoft.VC90.CRT", glob(r'.\Microsoft.VC90.CRT\*.*'))]
setup(data_files=data_files,windows=['instalar.py','main.py'])
