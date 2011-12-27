import Tkinter
from Tkinter import *
CSI="\x1B["

class assign_event_values():
	def __init__(self,event_type=None,value=None,start=None,end=None,operation=None,selected=None):

		self.event_type=event_type
		self.value=value
		self.start=start
		self.end=end
		self.operation=operation
		self.selected=selected
		
