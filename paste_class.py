import Tkinter
from Tkinter import *
from Application_2 import *

class paste_class(application):
	def __init__(self):
		print CSI+"39m" + "inside __init__ paste" +CSI+"0m"
	
	def Paste(self,event=None):
		start = self.text.index(INSERT)
		self.text.insert(INSERT,self.text1)
		if self.paste_button.cget("state")=="normal":
			self.paste_button_pressed(start,self.text1) #this function is in undo_redo
	
	def enable_paste(self,event = None):
		self.paste_button.config(state=NORMAL)
		index = self.editmenu.index("Paste")
		self.editmenu.entryconfig(index,state='normal')

	def disable_paste(self):
		self.paste_button.config(state=DISABLED)
		index = self.editmenu.index("Paste")
		self.editmenu.entryconfig(index,state='disabled')

	
