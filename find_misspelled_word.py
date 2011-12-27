import Tkinter
from Tkinter import *
from Application_2 import *
CSI="\x1B["

class find_misspelled_word(application):
	def __init__(self):
		print CSI+"39m" + "inside __init__ find_misspelled_word" +CSI+"0m"

	def change_value_in_replace_entry_box(self,event=None):
		print CSI+"31m" + str((self.suggestion_box.curselection())) +CSI+"0m"
		if str(self.suggestion_box.curselection())=="()" :
			return
		word=self.suggestion_box.get(self.suggestion_box.curselection())
		if word=="No Suggestions":
			self.change_to_word.set("")
		else:
			self.change_to_word.set(word)

	def check_value_button_spell(self):
	
		res=self.check_dictionary(self.change_to_word_entry.get())
		if res==0:
			print "value is not there"
		else:
			print "value is there"

	def check_temp_cache(self,value):
		if value in self.temp_cache_spell:
			return 1
		else:
			return 0

	def highlight_all_spelling_errors(self):
		if int(float(self.new_index_spell_auto))==int(float(self.text.index(END))):
			self.end_of_text=1
			return
		self.previous_index_spell_auto=self.start_index_spell_auto
		string_spell=""
		letter=""
		normal_string=""
		self.end_of_col=0
		
		while(True):
			if int(float(self.new_index_spell_auto))==int(float(self.text.index(END))):
				self.end_of_text=1
				return

			self.new_index_spell_auto=self.increase_column_value_spell(self.previous_index_spell_auto,1)
			self.end_of_col=0
			col1=int(self.new_index_spell_auto.split('.')[-1])
			index1=self.text.index("%d.end" % (int(float(self.new_index_spell_auto))))
			col2=int(index1.split('.')[-1])

			if col1==col2:
				self.end_of_col=1
 			letter=self.text.get(self.previous_index_spell_auto,self.new_index_spell_auto)

			if (letter==" " or letter=="." or self.end_of_text==1 or self.end_of_col==1):
				if self.end_of_col==1 and letter!=" " and letter!=".":
					string_spell=self.add_to_string(string_spell,letter)
					
				normal_string=string_spell
				word_found=self.check_dictionary(normal_string)
				
				if word_found==1:
					if self.end_of_col==1:
						line=int(float(self.new_index_spell_auto))
						self.new_index_spell_auto="%d.%d" % (line+1,0)
						
					self.previous_index_spell_auto=self.new_index_spell_auto
					self.start_index_spell_auto=self.previous_index_spell_auto
					string_spell=""
					normal_string=""
					
					continue
				else:
					self.misspelled_word=normal_string
					if self.end_of_col==1:
						index=self.new_index_spell_auto
					else:
						index=self.previous_index_spell_auto
					print "last index of the highlighted text "+ index
					self.highlight_word_spell(self.start_index_spell_auto,index)
					if self.end_of_col==1:
						line=int(float(self.new_index_spell_auto))
						self.new_index_spell_auto="%d.%d" % (line+1,0)
					self.previous_index_spell_auto=self.new_index_spell_auto
					self.start_index_spell_auto=self.previous_index_spell_auto
					string_spell=""
					normal_string=""
					continue
			
			elif ((ord(letter)>=65 and ord(letter)<=90) or (ord(letter)>=97 and ord(letter)<=122)):
				
				string_spell=self.add_to_string(string_spell,letter)
				self.previous_index_spell_auto=self.new_index_spell_auto

		return

	def check_for_misspelled_word(self):                   #### 
		if int(float(self.new_index_spell))==int(float(self.text.index(END))):
			print "new index spell " + str(float(self.new_index_spell))
			print "text index end " + str(float(self.text.index(END)))
			print "reached end"
			self.v.set("check finished")
			self.misspelled_word=""
			self.disable_buttons_spell()
			
			self.end_of_text=1
			
			return
		if len(self.text.get("%d.%d" % (1,0),END))==1:
    			print "TEXT EMPTY"
			return 10
	
		
		self.previous_index_spell=self.start_index_spell
	
		string_spell=""
		letter=""
		normal_string=""
		self.end_of_col=0
		
		while(True):
			if int(float(self.new_index_spell))==int(float(self.text.index(END))):
				print "inside while loop"
				print "new index spell " + str(float(self.new_index_spell))
				print "text index end " + str(float(self.text.index(END)))
				print "reached end"
				self.v.set("check finished")
				self.misspelled_word=""
				self.disable_buttons_spell()
				self.end_of_text=1
				break

			self.new_index_spell=self.increase_column_value_spell(self.previous_index_spell,1)

			self.end_of_col=0
			col1=int(self.new_index_spell.split('.')[-1])
			index1=self.text.index("%d.end" % (int(float(self.new_index_spell))))
			
			col2=int(index1.split('.')[-1])
			print col1
			print col2		
			if col1==col2:
				self.end_of_col=1
 				letter=self.text.get(self.previous_index_spell,self.new_index_spell)
			else:
				letter=self.text.get(self.previous_index_spell,self.new_index_spell)

			print CSI+"33m" + str(letter) +CSI+"0m"
			if (letter==" " or letter=="." or self.end_of_text==1 or self.end_of_col==1):
				if self.end_of_col==1 and letter!=" " and letter!=".":
					string_spell=self.add_to_string(string_spell,letter)
					
				normal_string=string_spell
				word_found=(self.check_dictionary(normal_string) or self.check_temp_cache(normal_string))
				
				if word_found==1:
					if self.end_of_col==1:
						line=int(float(self.new_index_spell))
						self.new_index_spell="%d.%d" % (line+1,0)
						
					self.previous_index_spell=self.new_index_spell
					self.start_index_spell=self.previous_index_spell
					string_spell=""
					normal_string=""
					
					continue
				else:
					self.misspelled_word=normal_string
					self.v.set(self.misspelled_word)
					self.suggestion_list=self.give_suggestions(self.misspelled_word)
					if self.spell_check_window_opened==1:
						self.insert_values_in_suggestion_box(self.suggestion_list)
					break

			elif ((ord(letter)>=65 and ord(letter)<=90) or (ord(letter)>=97 and ord(letter)<=122)):
				
				string_spell=self.add_to_string(string_spell,letter)
				self.previous_index_spell=self.new_index_spell

		return

	def spell_check(self,event=None):
		
		if self.spell_check_var.get()==0:
			return
		index1=self.text.index(INSERT)
		self.previous_index_spell=index1
		self.normal_string_spell=""
		string_spell=""
		letter=""
		word_found=0
		beg_of_line=0
		while(True):
			new_index=self.decrease_column_value_spell(self.previous_index_spell,1)
			line_spell=int(float(new_index))
			col_spell=int(new_index.split('.')[-1])
			if col_spell==-1:
				beg_of_line=1
			else:
				letter=self.text.get("%d.%d" % (line_spell,col_spell),self.previous_index_spell)
			if (beg_of_line==1 or letter==" " or letter=="." ):
				self.normal_string_spell=self.reverse_string(string_spell)
				word_found=self.check_dictionary(self.normal_string_spell)
				if word_found==0:
			    		self.highlight_word_spell(self.previous_index_spell,index1)
					self.misspelled_word=self.normal_string_spell
					break				
				else:
					break
			elif ((ord(letter)>=65 and ord(letter)<=90) or (ord(letter)>=97 and ord(letter)<=122)):
				
				string_spell=self.add_to_string(string_spell,letter)
				self.previous_index_spell= "%d.%d" % (line_spell,col_spell)
			else:
				break
		return
	
	def add_to_string(self,string,letter):
		string=string+letter
		return string
				
	def reverse_string(self,reversed_word):
		res=reversed_word[::-1]
		return res

	def check_dictionary(self,word):
		res=self.hash_map.get(word)
		if res==None:
			print "\n"+word+" not there\n"
			return 0
		else:
			print "\n"+word+" is there\n"
			return 1
		
	def highlight_word_spell(self,start_index_spell,end_index_spell):
		self.text.tag_add("highlight_spell_error",start_index_spell,end_index_spell)
		self.text.tag_config("highlight_spell_error",background="white",underline=1,foreground="red")

	def create_hash(self):
		file1=open("/home/pragya/Documents/text-editor/dictionary.txt")
		self.count_dict_words=1
		self.hash_map={}	
		for line in file1:
			line=line.strip()
			self.hash_map[line]=self.count_dict_words
			self.count_dict_words=self.count_dict_words+1



	

