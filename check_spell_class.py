import Tkinter
from Tkinter import *
from Application_2 import *
from suggestion_box import *
from find_misspelled_word import *
from spell_buttons import *
CSI="\x1B["

class check_spell_class(suggestion_box, find_misspelled_word, spell_buttons):
	def __init__(self):
		print CSI+"39m" + "inside __init__ check_spell" +CSI+"0m"
		suggestion_box.__init__(self)
		find_misspelled_word.__init__(self)
		spell_buttons.__init__(self)


	def spell_check_window(self,event=None):
		self.start_index_spell_auto="%d.%d" % (1,0)
		self.previous_index_spell_auto=self.start_index_spell_auto
		self.new_index_spell_auto=self.start_index_spell_auto
		self.start_index_spell="%d.%d" % (1,0)
		self.previous_index_spell=self.start_index_spell
		self.new_index_spell=self.start_index_spell
		string_spell=""
		letter=""
		normal_string=""
		self.end_of_col=0
		self.end_of_text=0
		c=self.check_for_misspelled_word()
		if c==10:
			print "window will not be opened as there is no text"
			return
		#if str(self.v.get())=="check finished":
		if self.misspelled_word=="":
			print "no wrong words in the text"
			return
		self.spell_win=Toplevel()

		frame5=Frame(self.spell_win)
		self.add_word_to_dictionary_button = Button(frame5,text="Add word to dictionary",pady=10,command=self.add_word_to_dictionary)
		self.add_word_to_dictionary_button.pack()
		frame5.pack(side=BOTTOM)

		frame4=Frame(self.spell_win)
		self.change_button = Button(frame4,text="Change",padx=5,command=self.change_one,underline=0)
		self.change_button.pack(side=LEFT)
		self.change_all_button = Button(frame4,text="Change All",padx=5,command=self.change_all,underline=0)
		self.change_all_button.pack(side=LEFT)
		frame4.pack(side=BOTTOM)

		frame3=Frame(self.spell_win)
		self.ignore_button = Button(frame3,text="Ignore",padx=5,command=self.ignore_one,underline=0)
		self.ignore_button.pack(side=LEFT)	
		self.ignore_all_button = Button(frame3,text="Ignore All",padx=5,command=self.ignore_all,underline=0)
		self.ignore_all_button.pack(side=LEFT)
		frame3.pack(side=BOTTOM)

		frame2=Frame(self.spell_win)
		suggestions_label = Label(frame2,text="Suggestions :",pady=10)
		suggestions_label.pack()
		scrollbar_suggestion_box = Scrollbar(frame2)
		scrollbar_suggestion_box.pack(side=RIGHT, fill=Y)		
		self.suggestion_box = Listbox(frame2,selectmode=SINGLE,yscrollcommand=scrollbar_suggestion_box.set)
		self.suggestion_box.bind("<ButtonRelease-1>",self.change_value_in_replace_entry_box)		
		self.suggestion_box.pack()
		scrollbar_suggestion_box.config(command = self.suggestion_box.yview )
		self.insert_values_in_suggestion_box(self.suggestion_list)
		
		frame2.pack(side=BOTTOM)

		frame1=Frame(self.spell_win)
		change_to_label = Label(frame1,text="Change to:",padx=5)
		change_to_label.pack(side=LEFT)
		self.change_to_word_entry = Entry(frame1,text="",textvariable=self.change_to_word)
		self.change_to_word_entry.pack(side=LEFT)
		self.check_value_button = Button(frame1,text="Check Value", padx=5, command=self.check_value_button_spell, underline=0)
		self.check_value_button.pack(side=LEFT)
		frame1.pack(side=BOTTOM)

		misspelled_label = Label(self.spell_win,text="Misspelled Word:",padx=5,pady=20)
		misspelled_label.pack(side=LEFT)
		self.misspelled_word_label = Label(self.spell_win,text=self.misspelled_word,padx=5,pady=20,textvariable=self.v)
		self.misspelled_word_label.pack(side=LEFT)
	
		self.spell_win.title("Check Spelling")
		self.spell_check_window_opened=1
		self.spell_win.protocol("WM_DELETE_WINDOW", self.on_spell_check_window_exit)
		self.spell_win.resizable(0,0)
		self.spell_win.mainloop()

	def on_spell_check_window_exit(self):
		self.spell_check_window_opened=0
		self.spell_win.destroy()

	def disable_buttons_spell(self):
		if self.spell_check_window_opened==0:
			return
		self.suggestion_box.delete(0,self.suggestion_box.size()-1)
		self.suggestion_box.config(state=DISABLED)
		self.change_to_word_entry.config(state=DISABLED)
		self.check_value_button.config(state=DISABLED)
		self.add_word_to_dictionary_button.config(state=DISABLED)
		self.change_all_button.config(state=DISABLED)
		self.change_button.config(state=DISABLED)
		self.ignore_all_button.config(state=DISABLED)
		self.ignore_button.config(state=DISABLED)
		
	
