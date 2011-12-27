from file_class import *
from edit_class import *
from search_class import *
from tools_class import *

import Tkinter
from tkFileDialog import *
from Tkinter import *
from tkSimpleDialog import *
import tkMessageBox
from tkMessageBox import showwarning
from tkMessageBox import askokcancel 
import os

CSI="\x1B["
class import_all_classes(file_class, edit_class, search_class, tools_class):
	def __init__(self):
		self.initialise_import_all_classes()
		
	def initialise_import_all_classes(self):
		print CSI+"32m" + "inside initialise all of import_all_classes" +CSI+"0m"
		file_class.__init__(self)
		edit_class.__init__(self)
		search_class.__init__(self)
		tools_class.__init__(self)
