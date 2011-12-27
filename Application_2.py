import Tkinter
from Tkinter import *
import os
TITLE = "editor"
CSI="\x1B["
class application(Text,object):
	
	def __init__(self):
		pass

	def set_initial_value(self):
		self.count=0
		self.current_index=-1
		self.previous_index=-1
		self.next_index=-1
		self.nocase=1
		self.exact=0
		self.empty_string=0
		self.count_flag=0
	
	def set_new_values(self):
		#self.text.delete("%d.%d" % (1,0),END)
		self.pattern=""
		self.misspelled_word=""
		self.previous_search_continued=0
		self.count=0
		self.current_index=-1
		self.empty_string=0
		self.start_index_spell="%d.%d" % (1,0)
		self.start_index_spell_auto="%d.%d" % (1,0)
		self.temp_cache_spell=[]
		self.v=StringVar()
		self.change_to_word=StringVar()
		self.end_of_text=0
		self.end_of_col=0
		self.new_index_spell="%d.%d" % (1,0)
		self.replace_window_opened=0
		self.search_window_opened=0
		self.go_to_line_window_opened=0
		self.match_entire_word_check_previous_value=0
		self.match_case_check_previous_value=0
		self.count_flag=0
		self.spell_check_window_opened=0
		self.filename = None
		#self.text1=""
		self.modified=False
		self.suggestion_list=[]
		self.backspace_pressed_flag=0
		self.key_press_event_flag=0
		self.count_key=0
		self.initialise_import_all_classes()	
		self.disable_undo()	

	def increase_line_value_spell(self,old_index,len_added):
		line=int(float(old_index))
		col=int(old_index.split('.')[-1])
		line=line+len_added
		new_index="%d.%d" % (line,0)
		return new_index

	
	def increase_column_value_spell(self,old_index,len_added):
		line=int(float(old_index))
		col=int(old_index.split('.')[-1])
		col=col+len_added
		new_index="%d.%d" % (line,col)
		return new_index

	def decrease_column_value_spell(self,old_index,len_sub):
		line=int(float(old_index))
		col=int(old_index.split('.')[-1])
		col=col-len_sub
		new_index="%d.%d" % (line,col)
		return new_index

	def button_released(self,event=None):
		self.call_if_text_selected()


		
