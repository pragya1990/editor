import Tkinter
from Tkinter import *
from Application_2 import *

CSI="\x1B["

class auto_spell_check_class(application):
	def __init__(self):
		print CSI+"39m" + "inside __init__ check_spell" +CSI+"0m"
		
	def auto_spell_check(self):
		self.start_index_spell_auto="%d.%d" % (1,0)
		self.previous_index_spell_auto=self.start_index_spell_auto
		self.new_index_spell_auto=self.start_index_spell_auto
		string_spell=""
		letter=""
		normal_string=""
		self.end_of_col=0
		self.end_of_text=0
		if self.spell_check_var.get()==0:
			self.text.tag_delete("highlight_spell_error")
		elif self.spell_check_var.get()==1:
			self.text.tag_delete("highlight_spell_error")
			self.highlight_all_spelling_errors()
