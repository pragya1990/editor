from Application_2 import *
CSI="\x1B["

class replace_class(application):
	def __init__(self):
		print CSI+"39m" + "inside __init__ replace" +CSI+"0m"

	def replace_one(self):
		if self.total_occurences==0:
				return
		new_index=self.increase_column_value_spell(self.current_index,len(self.find_value.get()))
		self.text.delete(self.current_index,new_index)

		self.text.mark_set(INSERT,self.current_index)
		self.text.insert(INSERT,self.replace_value_entry.get())

		str_replace=self.replace_value_entry.get()
		str_find=self.find_value.get()
		if self.search_backwards_check.get()==0:
			if (str_replace.count(str_find)!=0):
				pass
			else:
				self.count=self.count-1
		else:
			pass
		self.find()

	def replace_all(self):
		self.count_flag=1
		self.total_occurences=self.string_search(self.find_value.get(),"%d.%d" % (1,0),END)
		if self.total_occurences==0:
			return
		count=0
		new_index="%d.%d" % (1,0)
		while(count<self.total_occurences):
			index=self.string_search(self.find_value.get(),new_index, END)
			new_index=self.increase_column_value_spell(index,len(self.find_value.get()))
			self.text.delete(index,new_index)
			self.text.mark_set(INSERT,index)
			self.text.insert(INSERT,self.replace_value_entry.get())
			new_index=self.increase_column_value_spell(index,len(self.replace_value_entry.get()))
			count=count+1	
