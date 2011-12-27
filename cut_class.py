import Tkinter
from Tkinter import *
from Application_2 import *
CSI="\x1B["

class cut_class(application):
	def __init__(self):
		print CSI+"39m" + "inside __init__ cut" +CSI+"0m"

	def Cut(self,event=None):
		try:
			self.text1 = self.text.get("sel.first","sel.last")		
			self.cut_button_pressed()		
			self.text.delete("sel.first","sel.last")
			self.paste_button.config(state=NORMAL)
			print "insssssssssssssssssssssssssssssside cccccccccccccccccut"
		except TclError :                          #in case no text is selected
			return 0

	def enable_cut(self,event = None):
		self.cut_button.config(state=NORMAL)
		index = self.editmenu.index("Cut")
		self.editmenu.entryconfig(index,state='normal')
	
	def disable_cut(self):
		self.cut_button.config(state=DISABLED)
		index = self.editmenu.index("Cut")
		self.editmenu.entryconfig(index,state='disabled')
	

