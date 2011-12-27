import Tkinter
from Tkinter import *
from Application_2 import *
CSI="\x1B["

class new_class(application):
	def __init__(self):
		print CSI+"39m" + "inside __init__ new" +CSI+"0m"

	def New(self,event=None):
		c=self.save_if_modified()
		if str(c)!="cancel":
			print "It should clear the text"
			self.set_new_values()

	
