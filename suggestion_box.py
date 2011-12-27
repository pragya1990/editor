import Tkinter
from Tkinter import *
from Application_2 import *
CSI="\x1B["

""" See issues marked #1 , #2 , #3
	Suggestion box algo could be improved more:
	a) there is no start+1 as there is end-1
	b) its like a minimum algorithm that is making it work.
 """

class suggestion_box(application):
	def __init__(self):
		print CSI+"39m" + "inside __init__ suggestion box" +CSI+"0m"


	def insert_values_in_suggestion_box(self,suggestion_list):
		if len(suggestion_list)==0:
			self.suggestion_box.delete(0,self.suggestion_box.size()-1)
			self.suggestion_box.insert(0,"No Suggestions")
			self.change_to_word.set("")
			return
		i=0
		for word in suggestion_list:
			self.suggestion_box.insert(i,word)
			i=i+1
		self.change_to_word.set(self.suggestion_list[0])

	def give_suggestions(self,pattern):
		i=0
		pattern_list=[]
		suggestion_list={}
		while(i<len(pattern)): # makes a pattern list like - ['a','p','p','l','e','b','l','a']
			pattern_list.append(pattern[i])
			i=i+1
		for key in self.hash_map: ################ """ #1 try using suffix trees """
			i=0
			search_list=[]
			while(i<len(key)):	# makes a search list like - [ 'a','p','p','l','e'] for every word in dictionary.
				search_list.append(key[i])
				i=i+1
			found_list=[]
			i=0
			while(i<len(pattern_list)):
				if pattern_list[i] in search_list: # if the characters match, then we add those characters to the found_list and remove them from the search list. 
					found_list.append(pattern_list[i])
					search_list.remove(pattern_list[i])
				i=i+1
		
			if (((len(key)>=(len(pattern_list)-1)) and (len(key)<=(len(pattern_list)+1))) and (len(found_list)>=(len(pattern)-1))):
				suggestion_list[key]=len(found_list)*50 # give the score according to the length of the found_list and add the score in the suggestion_list[key]
		end=len(pattern)
		start=1
		max_len=3    # we are not considering substrings smaller than 3 ie score wont be added for them.
		while(end>=max_len and start<=max_len):
			for word in suggestion_list: ####################""" #2 optimization could be done here -- its again searching the whole of suggestion list whose length is equal to the length of the dictionary"""
				new_pattern=pattern[:end]
				res=word.find(new_pattern) # finding substring inside main string.
				c=0
				if res!=-1:
					#suggestion_list[word]=suggestion_list[word]+len(new_pattern)*10
					c=1
					suggestion_list[word]=suggestion_list[word]+30
					if res==0:
						suggestion_list[word]=suggestion_list[word]+(((len(pattern)-1)*10)-20)
					if len(word)==(len(pattern)-1) or len(word)==(len(pattern)+1):
						suggestion_list[word]=suggestion_list[word]+50
		
				new_pattern=pattern[start:]
				res=word.find(new_pattern)
				if res!=-1 and c==0:
					c=1
					suggestion_list[word]=suggestion_list[word]+30
					if res==0:
						suggestion_list[word]=suggestion_list[word]+(((len(pattern)-1)*10)-20)
					if len(word)==(len(pattern)-1) or len(word)==(len(pattern)+1):
						suggestion_list[word]=suggestion_list[word]+50

				new_pattern=pattern[start:end]
				res=word.find(new_pattern)
				if res!=-1 and c==0:
					suggestion_list[word]=suggestion_list[word]+30				
					if res==0:
						suggestion_list[word]=suggestion_list[word]+(((len(pattern)-1)*10)-20)
					if len(word)==(len(pattern)-1) or len(word)==(len(pattern)+1):
						suggestion_list[word]=suggestion_list[word]+50

			end=end-1
		list1=sorted([(value,key) for (key,value) in suggestion_list.items()],reverse=True) #########################""" #3 we are again sorting the whole list, it will take a lot of time -- see if we shorten our suggestion list before only"""
		i=0
		list2=[] 		# final list
		length=len(list1)
		print "length of list "+str(length)
		i=0
		if length==0:
			return list2
		while((i<=10) and (i<len(list1))):
			#print list1[i]
			list2.append(list1[i][1])
			i=i+1
		return list2

	
