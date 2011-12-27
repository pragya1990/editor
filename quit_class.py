import Tkinter
from Tkinter import *
from Application_2 import *
CSI="\x1B["

class quit_class(application):
	def __init__(self):
		print CSI+"39m" + "inside __init__ quit_file" +CSI+"0m"

	def Quit(self,event=None):
		if str(self.save_if_modified())!="cancel":
			print CSI+"31m" + "inside quit function" +CSI+"0m"
			#self.root.quit()
			self.root.destroy()
