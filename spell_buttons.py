import Tkinter
from Tkinter import *
from Application_2 import *
CSI="\x1B["

class spell_buttons(application):
	def __init__(self):
		print CSI+"39m" + "inside __init__ suggestion box" +CSI+"0m"

	def change_one(self):
		if self.end_of_col==1:
			end_index_spell=self.new_index_spell
		else:
			end_index_spell=self.decrease_column_value_spell(self.new_index_spell,1)
		start_index_spell=self.decrease_column_value_spell(end_index_spell,len(self.misspelled_word))
		
		self.text.mark_set(INSERT,start_index_spell)	
		self.text.delete(start_index_spell,end_index_spell)
		self.text.insert(INSERT,self.change_to_word_entry.get())
		if self.end_of_text==1:	
			return
		else:
			if self.end_of_col==1:
				line=int(float(self.new_index_spell))
				self.new_index_spell="%d.%d" % (line+1,0)
			self.previous_index_spell=self.new_index_spell
			self.start_index_spell=self.previous_index_spell
			string_spell=""
			normal_string="" 	
			self.check_for_misspelled_word()
		
	def change_all(self):
		line=1
		col=0
		start_index_spell_change="%d.%d" % (line,col)
		self.new_index_spell_change=start_index_spell_change
		
		previous_index_spell_change=start_index_spell_change
	
		string_spell=""
		letter=""
		normal_string=""
		end_of_col_change=0
		end_of_text_change=0
		while(True):
			if int(float(self.new_index_spell_change))==int(float(self.text.index(END))):
				print "inside while loop"
				print "new index spell " + str(float(self.new_index_spell_change))
				print "text index end " + str(float(self.text.index(END)))
				print "reached end"
				end_of_text_change=1
				if self.end_of_col==1:
					line=int(float(self.new_index_spell))
					self.new_index_spell="%d.%d" % (line+1,0)
					self.previous_index_spell=self.new_index_spell
				self.start_index_spell=self.previous_index_spell
				string_spell=""
				normal_string="" 
				self.check_for_misspelled_word()
				break
			
			self.new_index_spell_change=self.increase_column_value_spell(previous_index_spell_change,1)

			end_of_col_change=0
			col1=int(self.new_index_spell_change.split('.')[-1])
			index1=self.text.index("%d.end" % (int(float(self.new_index_spell_change))))
			
			col2=int(index1.split('.')[-1])
			print col1
			print col2		

			if col1==col2:
				end_of_col_change=1
 			letter=self.text.get(previous_index_spell_change,self.new_index_spell_change)
		
	
			if (letter==" " or letter=="." or end_of_text_change==1 or end_of_col_change==1):
				if end_of_col_change==1 and letter!=" " and letter!=".":
					string_spell=self.add_to_string(string_spell,letter)
					
				normal_string=string_spell
				if normal_string!=self.misspelled_word:
					if end_of_col_change==1:
						line=int(float(self.new_index_spell_change))
						self.new_index_spell_change="%d.%d" % (line+1,0)
						
					previous_index_spell_change=self.new_index_spell_change
					start_index_spell_change=previous_index_spell_change
					string_spell=""
					normal_string=""
					
					continue
				else:
					if end_of_col_change==1:
						end_index=self.new_index_spell_change
					else:
						end_index= previous_index_spell_change
				start_index=self.decrease_column_value_spell(end_index,len(self.misspelled_word))
				self.text.mark_set(INSERT,start_index)	
				self.text.delete(start_index,end_index)
				self.text.insert(INSERT,self.change_to_word_entry.get())
		
				if end_of_col_change==1:
						line=int(float(self.new_index_spell_change))
						self.new_index_spell_change="%d.%d" % (line+1,0)
						
				previous_index_spell_change=self.new_index_spell_change
				start_index_spell_change=previous_index_spell_change
				string_spell=""
				normal_string=""
				continue

			elif ((ord(letter)>=65 and ord(letter)<=90) or (ord(letter)>=97 and ord(letter)<=122)):
				
				string_spell=self.add_to_string(string_spell,letter)
				previous_index_spell_change=self.new_index_spell_change

		return
	

	def ignore_one(self):
		start_index=self.decrease_column_value_spell(self.new_index_spell,len(self.v.get())+1)
		print "new_index"+str(self.new_index_spell)
		print "lenght"+str(len(self.v.get()))
		print "end index"+(start_index)
		self.text.tag_remove("highlight_spell_error",start_index,self.new_index_spell)
		if self.end_of_text==1:
			pass
		else:
			if self.end_of_col==1:
				line=int(float(self.new_index_spell))
				self.new_index_spell="%d.%d" % (line+1,0)
			self.previous_index_spell=self.new_index_spell
			self.start_index_spell=self.previous_index_spell
			string_spell=""
			normal_string="" 
			self.check_for_misspelled_word()

	def ignore_all(self):
		self.temp_cache_spell.append(self.misspelled_word)
		if self.end_of_text==1:
			pass
		else:
			if self.end_of_col==1:
				line=int(float(self.new_index_spell))
				self.new_index_spell="%d.%d" % (line+1,0)
			self.previous_index_spell=self.new_index_spell
			self.start_index_spell=self.previous_index_spell
			string_spell=""
			normal_string="" 
			self.check_for_misspelled_word()

	def add_word_to_dictionary(self):
		self.hash_map[self.v.get()]=self.count_dict_words
		self.count_dict_words=self.count_dict_words+1
		self.check_for_misspelled_word()

