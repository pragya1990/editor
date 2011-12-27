from Application_2 import *
CSI="\x1B["

class find_class(application):
	def __init__(self):
		print CSI+"39m" + "inside __init__ find" +CSI+"0m"

	def find(self,event=None):
		if self.find_value.get()=="":
			return
		#######for a new search
		elif (self.pattern!=self.find_value.get() or self.match_entire_word_check.get()!=self.match_entire_word_check_previous_value or self.match_case_check.get()!=self.match_case_check_previous_value): 
			if (self.pattern!="" or self.match_entire_word_check.get()!=self.match_entire_word_check_previous_value or self.match_case_check.get()!=self.match_case_check_previous_value):
				self.detag("highlight_current_index")
				self.detag("highlight_all_occurences")
				self.set_initial_value()
			self.count_flag=1
			self.total_occurences=self.string_search(self.find_value.get(),"%d.%d" % (1,0),END)
			print "total"+str(self.total_occurences)
			if self.total_occurences==0:
					return
				
			self.previous_search_continued=0          
			self.pattern=self.find_value.get()                      			
			if self.search_backwards_check.get()==0:       ### if the search backwards checkbox is not selected
				self.count=1
				
			else:
				self.count=self.total_occurences

		else:
			self.count_flag=1
			self.total_occurences=self.string_search(self.find_value.get(),"%d.%d" % (1,0),END)
			if self.total_occurences==0:
				return
			self.detag("highlight_current_index")
			if self.search_backwards_check.get()==0:
				if self.count==self.total_occurences and self.wrap_around_check.get()==0:
					print "wrap around is off--at last occuerence"
					self.detag("highlight_current_index")
					return
				elif self.count==self.total_occurences and self.wrap_around_check.get()==1:
					self.count=1
				else:
					self.count=self.count+1
			else:
				if self.count==1 and self.wrap_around_check.get()==0:
					print "wrap around is off--at first occuerence"
					self.detag("highlight_current_index")
					return
				elif self.count==1 and self.wrap_around_check.get()==1:
					self.count=self.total_occurences
				else:
					self.count=self.count-1

		self.find_index(self.count)    ### Sets value for self.current_index
		self.highlight_one("highlight_current_index","red",self.current_index,len(self.find_value.get()))
		
	def letter_at_previous_index(self,index):
		line=int(float(index))
		col=int(index.split('.')[-1])
		if col==0:
			return 0
		else:
			previous_index="%d.%d" % (line,col-1)
			letter=self.text.get(previous_index,index)
			if ((ord(letter)>=65 and ord(letter)<=90) or (ord(letter)>=97 and ord(letter)<=122)):
				return 1
			else:
				return 0

	def letter_at_next_index(self,index):
		line=int(float(index))
		col=int(index.split('.')[-1])
		col=col+len(self.find_value.get())
		index1=self.text.index("%d.end" % (int(float(index))))
		col2=int(index1.split('.')[-1])
		if col==col2:
			return 0
		else:
			index="%d.%d" % (line,col)
			next_index="%d.%d" % (line,col+1)
			
			letter=self.text.get(index,next_index)
			print CSI+"34m" + str(letter) +CSI+"0m"
			print CSI+"34m" + str(ord(letter)) +CSI+"0m"
			if ((ord(letter)>=65 and ord(letter)<=90) or (ord(letter)>=97 and ord(letter)<=122)):
				print "letter"+letter+"end  "+next_index
				
				return 1
			else:
				return 0	

	def detag(self,tag):
		self.text.tag_delete(tag)

	def find_index(self,count):
		loop_count=count
		new_index="%d.%d" % (1,0)
		while(loop_count>0):
			index=self.string_search(self.pattern,new_index,END)
			new_index=self.increase_column_value_spell(index,len(self.pattern))	
			loop_count=loop_count-1
		self.current_index=index 

	def highlight_one(self,tag,color,index,length):
		new_index=self.increase_column_value_spell(index,length)
		self.text.tag_add(tag,index,new_index)
		self.text.tag_config(tag,background=color)

	def string_search(self,pattern,start_index,end_index):
		count_occurences=0
		if end_index==END:
			end_index=self.text.index(END)
		while(True):
			while(True):
				if start_index==end_index:
					if self.count_flag==1:
						self.count_flag=0
						return count_occurences
					else:
						return ""
				line=int(float(start_index))
				col=int(start_index.split('.')[-1])
				index1=self.text.index("%d.end" % (int(float(start_index))))
				end_col=int(index1.split('.')[-1])
				if (col+len(pattern))>end_col:
					start_index="%d.%d" % (line+1,0)
					continue
				next_index_string="%d.%d" % (line,col+len(pattern))
				break
			text_string=self.text.get(start_index,next_index_string)
			self.match_entire_word_check_previous_value=self.match_entire_word_check.get()
			self.match_case_check_previous_value=self.match_case_check.get()
			if self.match_case_check.get()==1:
				if pattern==text_string:
					if self.match_entire_word_check.get()==0 or ((self.letter_at_previous_index(start_index)==0 and self.letter_at_next_index(start_index)==0)):
						if self.count_flag==1:
							self.highlight_one("highlight_all_occurences","grey",start_index,len(self.find_value.get()))
							count_occurences=count_occurences+1
						else:	
							return start_index

				len_added=1
			else:
				counter=len(pattern)
				i=0
				while(counter>0):
					if ord(text_string[i])==ord(pattern[i]):
						counter=counter-1
						i=i+1
						continue
					elif (ord(pattern[i])>=65 and ord(pattern[i])<=90):
						if (ord(text_string[i])==ord(pattern[i])+32):
							counter=counter-1
							i=i+1
							continue
					elif (ord(pattern[i])>=97 and ord(pattern[i])<=122):
						if (ord(text_string[i])==ord(pattern[i])-32):
							counter=counter-1
							i=i+1
							continue
					if i==0:
						len_added=1
					else:
						len_added=i
					break
				if i==(len(pattern)):
					if self.match_entire_word_check.get()==0 or ((self.letter_at_previous_index(start_index)==0 and self.letter_at_next_index(start_index)==0)):
						if self.count_flag==1: # when the word is checked for the first time, then u need to highlight all occurences.
							self.highlight_one("highlight_all_occurences","grey",start_index,len(self.find_value.get()))
							count_occurences=count_occurences+1
						else:	
							return start_index

			start_index="%d.%d" % (line,col+1)


