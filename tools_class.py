from check_spell_class import *
from auto_spell_check_class import *

CSI="\x1B["

class tools_class(check_spell_class, auto_spell_check_class):
	def __init__(self):
		self.initialise_tools()
		
	def initialise_tools(self):
		print CSI+"32m" + "inside initialise all of tools_class" +CSI+"0m"
		check_spell_class.__init__(self)
		auto_spell_check_class.__init__(self)
