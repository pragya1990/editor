import Tkinter
from Tkinter import *
from Application_2 import *

class copy_class(application):
	def __init__(self):
		print CSI+"39m" + "inside __init__ copy" +CSI+"0m"
		self.text1=""

	def Copy(self,event=None):
		try:
			self.text1 = self.text.get("sel.first","sel.last")
			self.enable_paste()
		except TclError : #in case no text is selected
			return 0

	def enable_copy(self,event = None):
		self.copy_button.config(state=NORMAL)
		index = self.editmenu.index("Copy")
		self.editmenu.entryconfig(index,state='normal')

	def disable_copy(self):
		self.copy_button.config(state=DISABLED)
		index = self.editmenu.index("Copy")
		self.editmenu.entryconfig(index,state='disabled')


	
