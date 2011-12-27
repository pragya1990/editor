import Tkinter
import re
from Tkinter import *
#from Interface_2 import *
from Application_2 import *
from assign_event_values import *
CSI="\x1B["

""" ISSUES: 
1. see the key_press_event(), if something could be optimised in the last 'else' part -- there are too many conditions and see if some of them could be merged
2. make assign_event_values a function(), right now its a separate class
"""
class undo_redo_class(application):
	def __init__(self):
		print CSI+"39m" + "inside __init__ undo_redo" +CSI+"0m"
		application.__init__(self)
		self.disable_undo()
		self.disable_redo()
		self.disable_paste()
		print "value of pattern" + str(self.spell_check_var)
		#c=assign_event_values()
		self.undo_redo_dic={}
		
		self.undo_stack=[]
		self.undo_flag=0
		self.dic_index=0
		self.redo_stack=[]
		self.redo_flag=0
	
		#self.nothing_selected=0		# used only in one line which is commented now -- so use of writing it.
		self.start_of_line_dic=0
		#self.end_of_line_dic=0      #commented because its not used anywhere
		self.event_cache=[]
		#self.index_before_modify="%d.%d" % (1,0)   #commented because its not used anywhere -- dont know why it was written before. 
		#self.key_pressed="space"
		#self.dic_add_event(0)
		
		self.map_keys()

	def disable_undo(self):
		self.undo_button.config(state=DISABLED)
		index = self.editmenu.index("Undo")
		self.editmenu.entryconfig(index,state='disabled')

	def disable_redo(self):
		self.redo_button.config(state=DISABLED)
		index = self.editmenu.index("Redo")
		self.editmenu.entryconfig(index,state='disabled')

	def enable_undo(self,event = None):
		self.undo_button.config(state=NORMAL)
		index = self.editmenu.index("Undo")
		self.editmenu.entryconfig(index,state='normal')

	def enable_redo(self):
		self.redo_button.config(state=NORMAL)
		index = self.editmenu.index("Redo")
		self.editmenu.entryconfig(index,state='normal')

	def undo(self,event=None):
		self.undo_flag=1
		#self.detag(SEL)################## check why this is not working
		print CSI+"31m" + "in the starting of undo function" +CSI+"0m"
		index = self.pop_undo_stack()
		if index == -1:
			return 0
		
		print self.undo_redo_dic[index].event_type
		print self.undo_redo_dic[index].value
		print self.undo_redo_dic[index].start
		print self.undo_redo_dic[index].end
		print self.undo_redo_dic[index].operation
		
		event_type=self.undo_redo_dic[index].event_type
		value=self.undo_redo_dic[index].value
		start=self.undo_redo_dic[index].start
		end=self.undo_redo_dic[index].end
		operation=self.undo_redo_dic[index].operation
		selected=self.undo_redo_dic[index].selected
		if event_type==0:
			if selected==0 and operation==1:
				self.text.delete(start,end)
				self.text.mark_set(INSERT,start)
				self.text.focus_set()
			elif selected==0 and operation==0:             #### backspace or delete pressed
				self.text.mark_set(INSERT,start)
				self.text.insert(INSERT,value)
			elif selected==1 and operation==0:		 #### backspace or delete pressed
				self.text.mark_set(INSERT,start)
				self.text.insert(INSERT,value)	
				
		elif event_type==1:
			if selected==0 and operation==1:
				self.text.delete(start,END)
				col=int(start.split('.')[-1])
				if col==0 and start!="%d.%d" % (1,0):
					self.text.insert(INSERT,"\n")	
				#self.text.mark_set(INSERT,start)
				self.text.insert(INSERT,value)
				self.text.mark_set(INSERT,start)
			elif selected==1 and opearion==1:
				self.text.delete(start,END)
				col=int(start.split('.')[-1])
				if col==0 and start!="%d.%d" % (1,0):
					self.text.insert(INSERT,"\n")
				#self.text.mark_set(INSERT,start)
				self.text.insert(INSERT,operation+value)
				self.text.mark_set(INSERT,end)
			elif operation==0:
				self.text.insert(INSERT,"\n")
				self.text.mark_set(INSERT,start)
				self.text.focus_set()	

		elif event_type == 2 and selected ==1 and operation == 0:  ## return pressed
				self.text.mark_set(INSERT,start)		
				self.text.insert(INSERT,value)
				end_of_line = self.increase_line_value_spell(end,1)
				self.text.delete(end,end_of_line)

		elif event_type == 3 and selected ==1 and operation == 0: ## spacebar pressed
				self.text.mark_set(INSERT,start)		
				self.text.insert(INSERT,value)
				end_of_column = self.increase_column_value_spell(end,1)
				self.text.delete(end,end_of_column)
	
		#elif event_type == 4:          ## delete whatever was pasted in previous step
				
		
		self.enable_redo()
		self.push_redo_stack(index)
		if len(self.undo_stack)==0:
			self.disable_undo()
		self.redo_flag=0
		print CSI+"31m" + "in the end of undo function" +CSI+"0m"
		#self.dic_index=self.dic_index+1
		#self.dic_add_event(self.dic_index)

	def push_redo_stack(self,index):
		self.redo_stack.append(index)

	def pop_redo_stack(self):
		index=self.redo_stack.pop()
		return index

	def redo(self,event=None):
		print CSI+"32m" + "inside redo function" +CSI+"0m"
		if self.redo_button.cget("state") == "disabled":
			return 0
		index=self.pop_redo_stack()

		print self.undo_redo_dic[index].event_type
		print self.undo_redo_dic[index].value
		print "start: " + str(self.undo_redo_dic[index].start)
		print "end: " + str(self.undo_redo_dic[index].end)
		print "operation: " + str(self.undo_redo_dic[index].operation)

		event_type=self.undo_redo_dic[index].event_type
		value=self.undo_redo_dic[index].value
		start=self.undo_redo_dic[index].start
		end=self.undo_redo_dic[index].end
		operation=self.undo_redo_dic[index].operation
		selected=self.undo_redo_dic[index].selected
		if event_type==0:
			if operation==1:
				self.text.insert(start,value)
				self.text.mark_set(INSERT,end)
				self.text.focus_set()
			elif operation==0:
				self.text.delete(start,end)
				self.text.mark_set(INSERT,start)
				self.text.focus_set()
		elif event_type == 1:
			if selected==0 and operation==1:  
				self.text.delete(start,end)
				self.text.insert(INSERT,"\n")
				self.text.insert(INSERT,value)
				focus_index="%d.%d" % (int(float(start))+1,0)
				self.text.mark_set(INSERT,focus_index)
				self.text.focus_set()
			elif selected==1 and operation==1:

				self.text.delete(start,END)
				col=int(start.split('.')[-1])
				if col==0 and start!="%d.%d" % (1,0):
					self.text.insert(INSERT,"\n")
				self.text.insert(INSERT,"\n")
				self.text.insert(INSERT,value)
				focus_index="%d.%d" % (int(float(start))+1,0)
				self.text.mark_set(INSERT,focus_index)
				self.text.focus_set()
			elif operation==0:
				i=start
				#i="%d.%d" % (int(float(i))-1,0)
				#i=self.decrease_column_value_spell(self.text.index(INSERT),1)
				print int(float(i))
				end_index=self.text.index("%d.end" % (int(float(i))-1))
				self.text.mark_set(INSERT,end_index)
				self.text.focus_set()
		elif event_type == 2 and selected ==1 and operation == 0: ## return pressed coz event_type = 2
				self.text.delete(start,end)
				self.text.mark_set(INSERT,start)
				self.text.insert(INSERT,"\n")
		elif event_type == 3 and selected ==1 and operation == 0: ## spacebar pressed, event_type = 3
				self.text.delete(start,end)
				self.text.mark_set(INSERT,start)
				self.text.insert(INSERT," ")
	
		self.push_undo_stack(index)
		if len(self.redo_stack)==0:
			self.disable_redo()
		self.redo_flag=1
		#self.dic_index=self.dic_index-1


	def pop_undo_stack(self):
		print CSI+"36m" + "length of undo stack" +CSI+"0m"
		if len(self.undo_stack) == 0:
			return -1
		#try:
		index=self.undo_stack.pop()
		#except IndexError:
		#	return -1
		print CSI+"36m" + "popped index" +CSI+"0m"
		print index
		print CSI+"36m" + "length of undo stack" +CSI+"0m"
		print len(self.undo_stack)
		
		return index

	def push_undo_stack(self,index):
		self.enable_undo()
		print CSI+"37m" + "inside push undo stack.....index------- " +CSI+"0m",
		print index
		self.undo_stack.append(index)	
	
	def bla_bla(self):
		print "inside blabla"


	def dic_add_values(self,index,event_type,value,start,end,operation,selected):
		print CSI+"33m" + "inside dic_add_values" +CSI+"0m"
		self.undo_redo_dic[index].event_type=event_type
		self.undo_redo_dic[index].value=value
		self.undo_redo_dic[index].start=start
		self.undo_redo_dic[index].end=end
		self.undo_redo_dic[index].operation=operation
		self.undo_redo_dic[index].selected=selected

	def spacebar_pressed(self):

		if len(self.undo_stack)==0 and self.selected==0: #######adding a new event
			print CSI+"36m" + "new event values" +CSI+"0m"
			self.dic_index=0
			start="%d.%d" % (1,0)
			event_type=0
			value=" "
			end=self.increase_column_value_spell(self.text.index(INSERT),1)
			#end=self.text.index(INSERT)
			operation=1
			selected=0
			self.dic_add_event(self.dic_index,event_type,value,start,end,operation,selected)

		#elif self.undo_redo_dic[self.dic_index].end!=(self.decrease_column_value_spell(self.text.index(INSERT),1)) and self.nothing_selected==1: ## mouse position changed, so add new event
		elif self.undo_redo_dic[self.dic_index].end!=self.text.index(INSERT) and self.selected==0: 
			print CSI+"36m" + "mouse position change..new event values" +CSI+"0m"
			self.dic_index=self.dic_index+1  
			start=self.text.index(INSERT)
			end=self.increase_column_value_spell(start,1)
			operation=1
			event_type=0
			value=" "
			selected=0
			self.dic_add_event(self.dic_index,event_type,value,start,end,operation,selected)

		elif self.undo_redo_dic[self.dic_index].event_type==0 and self.undo_redo_dic[self.dic_index].operation==1 and re.compile('.* ').match(self.undo_redo_dic[self.dic_index].value) and self.selected==0 :
			print CSI+"36m" + "last letter of the last value is space ..add space to the current undo list " +CSI+"0m"
			self.undo_redo_dic[self.dic_index].value=self.undo_redo_dic[self.dic_index].value + " "
			end_index=self.undo_redo_dic[self.dic_index].end
			end_index=self.increase_column_value_spell(end_index,1)
			self.undo_redo_dic[self.dic_index].end=end_index

		elif self.undo_redo_dic[self.dic_index].event_type==0 and self.undo_redo_dic[self.dic_index].operation==1 and self.selected==0:
			print CSI+"36m" + "add space to the current undo list assuming insert operation is going" +CSI+"0m"
			self.undo_redo_dic[self.dic_index].value=self.undo_redo_dic[self.dic_index].value + " "
			end_index=self.undo_redo_dic[self.dic_index].end
			end_index=self.increase_column_value_spell(end_index,1)
			self.undo_redo_dic[self.dic_index].end=end_index
			#self.dic_index=self.dic_index+1        ####go to next index
			#self.dic_add_event(self.dic_index)
		

		elif self.selected == 1:
			self.dic_index=self.dic_index+1
			start=self.start_index_dic
			end=self.end_index_dic
			value=self.string_dic
			operation=0
			selected=1
			event_type = 3
			self.dic_add_event(self.dic_index,event_type,value,start,end,operation,selected)

		print CSI+"34m" + "add space to the current undo list assuming insert operation is going" +CSI+"0m"
		print CSI+"34m" + "if last operation==insert, then add new event and add space to it." +CSI+"0m"
		print CSI+"34m" + "shift the pointer to point to next event" +CSI+"0m"

	def dic_add_event(self,index,event_type=None,value=None,start=None,end=None,operation=None,selected=None):
		print CSI+"36m" + "inside dic_add_event" +CSI+"0m"
		print value
		print start
		print end
		self.undo_redo_dic[index]=assign_event_values(event_type,value,start,end,operation,selected)
		print "index",
		print index
		self.push_undo_stack(index)

	def empty_redo_stack(self):
		self.redo_stack=[]

	def key_press_event(self,event=None):
		self.auto_spell_check()
		#if self.modified == False:  # this is added because if we press ctrl+(any key), the letter does nt appear in the editor, but a new event is added in the undo stack showing that letter as pressed, so to avoid that error, this line should be there.
		#	return 0
		print CSI+"32m" + "key_press_event" +CSI+"0m"
		print self.modified
		self.key_press_event_flag=1
		print "current ", 
		print self.text.index(CURRENT)
		print "insert ",
		print self.text.index(INSERT)
		print "end ",
		print self.text.index("end")
		self.start_index_dic=self.text.index(INSERT)
		self.store_index()

		print "event.keysm-- " + event.keysym
		#self.key_pressed=event.keysym # Problem: it saves ';' as semicolon. we cant use self.text.get(some index) to find the letter, because it is a key press event and its not a key release event, so the particular value has not been entered in the text till now, it will get entered only when key-release event has taken place, so we need to find a way to map semicolon to ; -- so we have made a function map_keys()
		try:
			print "inside first try"	
			self.key_pressed_value = self.hash_keys[event.keysym]
		except KeyError:    # error is either bcoz the key is something like f5, ctrl etc or 'a'-'z' or '0'-'9' -- these keys are not mapped to any character in the hash_keys dictionary.
			try:
				print "inside second try"
				v = ord(event.keysym)			
				self.key_pressed_value = event.keysym   # for keys 'a'-'z' and '0'-'9' 
			except TypeError:
				print "inside typeError"
				if event.keysym !="space" and event.keysym !="Return" and event.keysym !="BackSpace" and event.keysym != "Delete": 
					return 0	# we return because pressing these keys does not change anything inside the text, so we do not need to put anything in the undo stack.
				
		self.key_pressed = event.keysym
		if self.key_pressed=="space":
			self.spacebar_pressed()
		elif self.key_pressed=="Return":
			self.return_pressed()
		elif self.key_pressed=="BackSpace":
			self.backspace_pressed()
		elif self.key_pressed=="Delete":
			self.delete_pressed()
		else:
		
			if len(self.undo_stack)==0 and self.selected==0:	
				print CSI+"35m" + "length of dic is 0--adding new event" +CSI+"0m"
				self.dic_add_event(0)
				#self.dic_index=0   ####################### change this ###########################
			if self.undo_redo_dic[self.dic_index].value==None and self.selected==0: ###new event, so initialise all values - this is for when we press those keys for which value is none consecutively -- in this case, new event will be added even if the value of the previous event was null.
				print CSI+"35m" + "when value is None but event has already been initialised" +CSI+"0m"
				start=self.start_index_dic
				end=self.increase_column_value_spell(self.text.index(INSERT),1)
				operation=1
				event_type=0
				value=self.key_pressed_value
				selected=0
				self.dic_add_values(self.dic_index,event_type,value,start,end,operation,selected)
			elif (self.undo_redo_dic[self.dic_index].end!=self.start_index_dic and self.selected==0) or (self.undo_flag==1 and self.redo_flag==0 and self.selected==0): 	## mouse position changed
				print CSI+"35m" + "mouse position changed....new event values" +CSI+"0m"
				self.dic_index=self.dic_index+1 
				start=self.start_index_dic
				end=self.increase_column_value_spell(self.text.index(INSERT),1)
				operation=1
				event_type=0
				value = self.key_pressed_value
				selected=0
				self.dic_add_event(self.dic_index,event_type,value,start,end,operation,selected)
		
			elif re.compile('.* ').match(self.undo_redo_dic[self.dic_index].value) and self.selected==0:   ### last letter was space, so add new event
				self.dic_index=self.dic_index+1        ####go to next index
				start=self.start_index_dic
				end=self.increase_column_value_spell(self.text.index(INSERT),1)
				value=self.key_pressed_value
				operation=1
				event_type=0
				selected=0
				print CSI+"33m" + "value.............." +CSI+"0m",
				print value
				self.dic_add_event(self.dic_index,event_type,value,start,end,operation,selected)
			elif self.undo_flag==1 and self.redo_flag==1 and self.selected==0: #if we press undo and redo exactly the same number of times
				start=self.start_index_dic
				end=self.increase_column_value_spell(self.text.index(INSERT),1)
				value=self.key_pressed_value
				self.undo_redo_dic[self.dic_index].value=self.undo_redo_dic[self.dic_index].value + value
				self.undo_redo_dic[self.dic_index].end=end
			
			else:                          # add the key that is currently pressed to the previous undo_redo_dic[index].value
				start=self.start_index_dic
				end=self.increase_column_value_spell(self.text.index(INSERT),1)
				value=self.key_pressed_value
				self.undo_redo_dic[self.dic_index].value=self.undo_redo_dic[self.dic_index].value + value
				self.undo_redo_dic[self.dic_index].end=end
		self.disable_redo()
		self.empty_redo_stack()
		self.undo_flag=0
		self.redo_flag=0

	def delete_pressed(self):
		pass
		print CSI+"33m" + "delete pressed" +CSI+"0m"
		
		if self.selected==0:
			end_index=self.text.index("%d.end" % (int(float(self.text.index(END)))-1))
			if end_index!=self.text.index(INSERT):      ### cursor at the end of line
				self.dic_index=self.dic_index+1
				start=self.text.index(INSERT)
				end=self.increase_column_value_spell(self.text.index(INSERT),1)
				value=self.text.get(start,end)
				operation=0
				event_type=0
				selected = 0
				self.dic_add_event(self.dic_index,event_type,value,start,end,operation,selected)
		else:
			self.dic_index=self.dic_index+1	
			start=self.start_index_dic
			end=self.end_index_dic
			value=self.string_dic
			operation=0
			selected=1
			event_type=0
			self.dic_add_event(self.dic_index,event_type,value,start,end,operation,selected)

	def cut_button_pressed(self):
		self.store_index()
		self.dic_index=self.dic_index+1	
		start=self.start_index_dic
		end=self.end_index_dic
		value=self.string_dic
		operation=0
		selected=1
		event_type=0
		self.dic_add_event(self.dic_index,event_type,value,start,end,operation,selected)
	
	def paste_button_pressed(self,start,value):
		end = self.text.index(INSERT)
		operation = 1
		event_type = 0                     # for paste button, event_type = 0 coz its function is similar any other keyboard character
		selected = 0
		self.dic_index=self.dic_index+1	
		self.dic_add_event(self.dic_index,event_type,value,start,end,operation,selected)

	def backspace_pressed(self):
		print CSI+"33m" + "backspace pressed" +CSI+"0m"
		
		if self.text.index(INSERT)=="%d.%d" % (1,0):
			return
		self.dic_index=self.dic_index+1
		if self.selected==0:
			#i=self.text.index(INSERT)
			col=int(self.text.index(INSERT).split('.')[-1])
			if col==0:
				event_type=1
			else:
				event_type=0
			if event_type==0:
				start=self.decrease_column_value_spell(self.text.index(INSERT),1)
				end=self.text.index(INSERT)
				value=self.text.get(start,end)
				operation=0
				selected=0
				self.dic_add_event(self.dic_index,event_type,value,start,end,operation,selected)
			else:
				start=self.text.index(INSERT)
				end=None
				value=None
				operation=0
				selected=0
				self.dic_add_event(self.dic_index,event_type,value,start,end,operation,selected)
		else:
			start=self.start_index_dic
			end=self.end_index_dic
			value=self.text.get(start,end)
			operation=0
			selected=1
			event_type=0
			self.dic_add_event(self.dic_index,event_type,value,start,end,operation,selected)

	"""def return_pressed(self):
		print CSI+"33m" + "return pressed" +CSI+"0m"
		if self.selected==0:
			self.dic_index=self.dic_index+1
			start=self.text.index(INSERT)
			end_index=self.text.index(END)
			end=self.text.index("%d.end" % (int(float(end_index))-1))
			value=self.text.get(start,end)
			operation=0
			selected=0
			event_type=1
			self.dic_add_event(self.dic_index,event_type,value,start,end,operation,selected)
		else:
			self.dic_index=self.dic_index+1
			start=self.start_index_dic
			end=self.end_index_dic
			value=self.string_dic
			operation=0
			selected=1
			event_type = 2
			self.dic_add_event(self.dic_index,event_type,value,start,end,operation,selected)"""

	# this code is added today - 5/12/2011 -- the above code was used before.	
	def return_pressed(self):
		print CSI+"33m" + "return pressed" +CSI+"0m"
		if self.selected==0:
			self.dic_index=self.dic_index+1
			start=self.text.index(INSERT)
			end_index=self.text.index(END)
			end=self.text.index("%d.end" % (int(float(end_index))-1))
			value=self.text.get(start,end)
			operation=0
			selected=0
			event_type=1
			self.dic_add_event(self.dic_index,event_type,value,start,end,operation,selected)
		else:
			self.dic_index=self.dic_index+1
			start=self.start_index_dic
			end=self.end_index_dic
			value=self.string_dic
			operation=0
			selected=1
			event_type = 2
			self.dic_add_event(self.dic_index,event_type,value,start,end,operation,selected)
		
	def store_index(self):
		try:
			self.start_index_dic=self.text.index("sel.first")
			print CSI+"33m" + "key_press_event" +CSI+"0m",
			print self.text.index("sel.first")
			self.end_index_dic=self.text.index("sel.last")
			print CSI+"33m" + "key_press_event" +CSI+"0m",
			print self.text.index("sel.last")
			self.string_dic=self.text.get("sel.first","sel.last")
			print CSI+"33m" + "the string is" +CSI+"0m",
			print self.string_dic
			self.selected=1
		except TclError:
			print CSI+"33m" + "no grey selected" +CSI+"0m"
			self.selected=0
			# dont know why the following lines were commented -- removing the comments - date - 5/12/2011
			self.current_index_dic=self.text.index(INSERT)
			new_index=self.decrease_column_value_spell(self.current_index_dic,1)
			self.string_before=self.text.get(new_index,self.current_index_dic)		
			print self.string_before
			new_index= self.increase_column_value_spell(self.current_index_dic,1)
			self.string_after=self.text.get(self.current_index_dic, new_index)
			
			col=int(self.current_index_dic.split('.')[-1])
			if col==0:
				self.start_of_line_dic=1
			end_index="%d.end" % (int(float(self.current_index_dic)))
			if self.current_index_dic==end_index:
				self.end_of_line_dic=1
			# commented till here
			
			return

	def map_keys(self):
		self.hash_keys = {}	
		self.hash_keys = {'grave':"`", 'asciitilde':"~",
				  'exclam':"!", 'at':"@", 'numbersign':"#", 'dollar':"$", 'percent':"%", 'asciicircum':"^", 'ampersand':"&", 'asterisk':"*", 'parenleft':"(", 'parenright':")",		

				  'minus':"-", 'underscore':"_", 'equal':"=", 'plus':"+",
				  'bracketleft':"[", 'braceleft':"{", 'bracketright':"]", 'braceright':"}", 'backslash':"\\", 'bar':"|",
				  'semicolon':";", 'colon':":", 'apostrophe':"'", 'quotedb':"\"",
				  'comma':",", 'less':"<", 'period':".",'greater':">", 'slash':"/", 'question':"?" }




		

			

		
	
