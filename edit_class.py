from undo_redo_class import *
from cut_class import *
from copy_class import *
from paste_class import *
from delete_class import *
from select_all_class import *

import Tkinter
from tkFileDialog import *
from Tkinter import *
from tkSimpleDialog import *
import tkMessageBox
from tkMessageBox import showwarning
from tkMessageBox import askokcancel 
import os

CSI="\x1B["

class edit_class(undo_redo_class, cut_class, copy_class, paste_class, delete_class, select_all_class):
	def __init__(self):
		self.initialise_edit()
		
	def initialise_edit(self):
		print CSI+"32m" + "inside initialise all of edit_class" +CSI+"0m"
		undo_redo_class.__init__(self)
		cut_class.__init__(self)
		copy_class.__init__(self)
		paste_class.__init__(self)
		delete_class.__init__(self)
		select_all_class.__init__(self)
		
