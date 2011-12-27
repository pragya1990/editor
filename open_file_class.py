import Tkinter
from Tkinter import *
from Application_2 import *
CSI="\x1B["

import Tkinter
from tkFileDialog import *
from Tkinter import *
from tkSimpleDialog import *
import tkMessageBox
from tkMessageBox import showwarning
from tkMessageBox import askokcancel 
import os

class open_file_class(application):
	def __init__(self):
		print CSI+"39m" + "inside __init__ open_file" +CSI+"0m"

	def open_as(self,event=None):
		if str(self.save_if_modified()) == "cancel":
			return 0
		FILETYPES = [("Text files", "*.txt"), ("All files", "*")]
		f = askopenfilename(parent=self.root, filetypes=FILETYPES)
		if not f:
			return
		#text = open(f).read()
		text=open(f,'r')
	        self.set_new_values()
		for line in text:
			#index=int(float(self.text.index(INSERT)))+1
			#print index
			#self.text.mark_set(INSERT,"%d.%d" % (index,0))
			#print line
			#line=line.strip()
			self.text.insert(INSERT,line)
			
			
			#index=self.text.index(INSERT)
			#print index
		
	        #self.text.insert(1.0,text)
	       	self.modified = False
		self.filename = f

