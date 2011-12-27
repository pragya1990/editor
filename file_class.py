from tkSimpleDialog import *
import tkMessageBox
from tkMessageBox import showwarning
from tkMessageBox import askokcancel 
from tkFileDialog import *

from new_class import *
from open_file_class import *
from save_class import *
from quit_class import *

CSI="\x1B["

class file_class(new_class, open_file_class, save_class, quit_class):
	def __init__(self):
		self.initialise_file()
		
	def initialise_file(self):
		print CSI+"32m" + "inside initialise all of file_class" +CSI+"0m"
		new_class.__init__(self)
		open_file_class.__init__(self)
		save_class.__init__(self)
		quit_class.__init__(self)

	def _getfilename(self):
		print "inside __getfilename"
        	return self._filename
	
	def _setfilename(self, filename):
		print "inside __setfilename"
		self._filename = filename
		title = os.path.basename(filename or "(new document)")
		title = title + " - " + TITLE
		self.root.title(title)
	filename = property(_getfilename, _setfilename)	

	def edit_modified(self, value=None):
        	return self.text.tk.call(self.text, "edit", "modified", value)

	modified = property(edit_modified,edit_modified)

	def askyesnocancel(self,title=None, message=None, **options):
		s = tkMessageBox.Message(title=title, message=message,icon=tkMessageBox.QUESTION,type=tkMessageBox.YESNOCANCEL,**options).show()
		return s


