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

class save_class(application):
	def __init__(self):
		print CSI+"39m" + "inside __init__ save_file" +CSI+"0m"

	def save(self, filename=None):
		if filename is None:
			filename = self.filename
        	f = open(filename, "w")
       	 	s = self.text.get(1.0, END)
        	try:
			f.write(s.rstrip())
			f.write("\n")
        	finally:
            		f.close()
        	self.modified = False
       		self.filename = filename

	def save_as(self,event=None):
		f = asksaveasfilename(parent=self.root, defaultextension=".txt")
		if not f:
			return
		self.save(f)

	def save_1(self,event=None):         ########## checks whether filename is already present or not###########
		if self.filename:
			self.save(self.filename)
		else:
			self.save_as()

	def save_if_modified(self,value=None):
		if not self.modified:
			print CSI+"31m" + "the text is not modified" +CSI+"0m"
	      		return
		else:
			c=self.askyesnocancel(TITLE, "Document modified. Save changes?")
			print CSI+"33m" + str(c) +CSI+"0m"
			if str(c)=="yes":
				print CSI+"31m" + "the text is modified" +CSI+"0m"
				self.save_1()
				c="yes"

			return c	 

