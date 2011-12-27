import Tkinter
from Tkinter import *
from Application_2 import *
CSI="\x1B["

class select_all_class(application):
	def __init__(self):
		print CSI+"39m" + "inside __init__ cut" +CSI+"0m"
	
	def Select_all(self,event=None):
		try:
			self.text.tag_add("sel","%d.%d" % (1,0),END)
			print "inside sselect alllllllllllllllllllllllllllllllllllllllllllllllllllllllll"
			self.enable_cut()
			self.enable_copy()
			self.enable_delete()
		except TclError:
			print "inside errrrrrrrrrrrrrroooooooooooooorrrrrrrrrrrrrrrrrrrr"

	def call_if_text_selected(self,event = None):
		try:
			start_index=self.text.index("sel.first")
			print CSI+"33m" + "mouse_position_change_event" +CSI+"0m",
			print self.text.index("sel.first")
			end_index=self.text.index("sel.last")
			print CSI+"33m" + "mouse_position_change_event" +CSI+"0m",
			print self.text.index("sel.last")
			string=self.text.get("sel.first","sel.last")
			print CSI+"33m" + "the string is" +CSI+"0m",
			print string
			self.enable_cut()
			self.enable_copy()
			self.enable_delete()
		except TclError:
			self.disable_cut()
			self.disable_copy()
			self.disable_delete()
