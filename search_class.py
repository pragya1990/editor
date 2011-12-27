from find_class import *
from replace_class import *
from go_to_line_class import *
CSI="\x1B["

""" ISSUES:
1. Remove the function search_window() and replace_window() from this file and put it in the appropriate file"""

class search_class(find_class, replace_class, go_to_line_class):
	def __init__(self):
		self.initialise_search()
		
	def initialise_search(self):
		print CSI+"32m" + "inside initialise all of search_class" +CSI+"0m"
		find_class.__init__(self)
		replace_class.__init__(self)
		go_to_line_class.__init__(self)

	def search_window(self,event=None):
		if self.replace_window_opened==1:
			print "replace_window"+str(self.replace_window_opened)+"\n"
			self.replace_win.destroy()
			self.replace_window_opened=0
		if self.search_window_opened==1:
			print "search_window already opened"+str(self.replace_window_opened)+"\n"
			return
			#self.replace_win.destroy()
			#self.replace_window_opened=0
		
		self.search_win=Toplevel()
		self.match_case_check = IntVar()
		self.C1 = Checkbutton(self.search_win, text = "Match Case", variable = self.match_case_check, onvalue = 1, offvalue = 0,selectcolor="black")
		self.C1.pack(side=BOTTOM)
		#print "check value" + str(self.match_case_check.get())
		#self.C1.select()
		#print "check value" + str(self.match_case_check.get())
		self.match_entire_word_check = IntVar()
		self.C2 = Checkbutton(self.search_win, text = "Match entire word only", variable = self.match_entire_word_check, onvalue = 1, offvalue = 0,selectcolor="black")
		self.C2.pack(side=BOTTOM)	
		self.search_backwards_check = IntVar()
		self.C3 = Checkbutton(self.search_win, text = "Search backwards", variable = self.search_backwards_check, onvalue = 1, offvalue = 0,selectcolor="black")
		self.C3.pack(side=BOTTOM)
		self.wrap_around_check = IntVar()
		self.C4 = Checkbutton(self.search_win, text = "Wrap Around", variable = self.wrap_around_check, onvalue = 1, offvalue = 0,selectcolor="black")	
		self.C4.select()		
		self.C4.pack(side=BOTTOM)
		find = Label(self.search_win,text="Search for:",padx=20)
		find.pack(side=LEFT)
		self.find_value=Entry(self.search_win)
		self.find_value.pack(side=LEFT)
		find_button = Button(self.search_win,text="find",padx=5,command=self.find,underline=0)
		find_button.pack(side=LEFT)
		self.find_bindings()
		self.search_window_opened=1
		print "search_window"+str(self.search_window_opened)+"\n"
		self.search_win.title("Find...")
		self.search_win.resizable(0,0)
		self.search_win.mainloop()

	def replace_window(self,event=None):
		if self.search_window_opened==1:
			print "search_window"+str(self.search_window_opened)+"\n"
			self.search_win.destroy()
			#self.search_win.config(state=DISABLED)
			self.search_window_opened=0
		if self.replace_window_opened==1:
			print "replace_window already opened"+str(self.replace_window_opened)+"\n"
			return
		self.replace_win=Toplevel()		
		self.wrap_around_check = IntVar()
		self.C4 = Checkbutton(self.replace_win, text = "Wrap Around", variable = self.wrap_around_check, onvalue = 1, offvalue = 0,selectcolor="black")	
		self.C4.select()	
		self.C4.pack(side=BOTTOM)
		self.search_backwards_check = IntVar()
		self.C3 = Checkbutton(self.replace_win, text = "Search backwards", variable = self.search_backwards_check, onvalue = 1, offvalue = 0,selectcolor="black")
		self.C3.pack(side=BOTTOM)
		
		self.match_entire_word_check = IntVar()
		self.C2 = Checkbutton(self.replace_win, text = "Match entire word only", variable = self.match_entire_word_check, onvalue = 1, offvalue = 0,selectcolor="black")
		self.C2.pack(side=BOTTOM)
		self.match_case_check = IntVar()
		self.C1 = Checkbutton(self.replace_win, text = "Match Case", variable = self.match_case_check, onvalue = 1, offvalue = 0,selectcolor="black")
	
		self.C1.pack(side=BOTTOM)
			
		find = Label(self.replace_win,text="Search for:",padx=20)
		find.pack(side=LEFT)
		self.find_value=Entry(self.replace_win)
		self.find_value.pack(side=LEFT)
		find_button_replace = Button(self.replace_win,text="find",padx=5,command=self.find,underline=0)
		find_button_replace.pack(side=LEFT)
	
		replace_with = Label(self.replace_win,text="Replace with:",padx=20)
		replace_with.pack(side=LEFT)
		self.replace_value_entry=Entry(self.replace_win)
		self.replace_value_entry.pack(side=LEFT)
		replace_one_button = Button(self.replace_win,text="Replace",padx=5,command=self.replace_one,underline=0)
		replace_one_button.pack(side=LEFT)
		replace_all_button = Button(self.replace_win,text="Replace All",padx=5,command=self.replace_all,underline=0)
		replace_all_button.pack(side=LEFT)

		self.replace_bindings()
		self.replace_window_opened=1
		print "replace_window"+str(self.replace_window_opened)+"\n"
		self.replace_win.title("Replace")
		self.replace_win.resizable(0,0)
		self.replace_win.mainloop()

	def replace_bindings(self):
		self.replace_win.bind("<Return>", self.find)

	def find_bindings(self):
		self.search_win.bind("<Return>", self.find)

