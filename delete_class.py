import Tkinter
from Tkinter import *
from Application_2 import *
CSI="\x1B["

class delete_class(application):
	def __init__(self):
		print CSI+"39m" + "inside __init__ delete" +CSI+"0m"
		self.text.delete("%d.%d" % (1,0),END)

	def Delete(self,event=None):  #the difference betweeen delete and but is that in delete we dont enable the paste button. but new event is added in the undo stack in both cases.
		try:
			self.text1 = self.text.get("sel.first","sel.last")
			self.cut_button_pressed()
			self.text.delete("sel.first","sel.last")
		except TclError : #in case no text is selected
			return 0

	def enable_delete(self,event = None):
		index = self.editmenu.index("Delete")
		self.editmenu.entryconfig(index,state='normal')

	def disable_delete(self):
		index = self.editmenu.index("Delete")
		self.editmenu.entryconfig(index,state='disabled')
