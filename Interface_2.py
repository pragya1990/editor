import Tkinter
from Tkinter import *
from Application_2 import *
from import_all_classes import *
CSI="\x1B["

"""1. Error: I have commented keyboard shortcuts for alt-f, alt-t, alt-s -- but still these are working
 """

class interface(import_all_classes):
	def __init__(self):
		pass

	def resize(self,event=None):
		self.conf_win_counter=self.conf_win_counter+1
		if self.conf_win_counter==1:
			return
		
		self.text.config(height=50,width=180)
		print str(self.conf_win_counter)

	def add_scroll_bars(self,text_frame):
		self.vertical_scrollbar = Scrollbar(text_frame)
		self.vertical_scrollbar.pack(side=RIGHT,fill=Y)
		self.vertical_scrollbar.config(command = self.text.yview)

		
	def add_buttons(self):
		button_frame=Frame(self.root)
		self.add_file_buttons(button_frame)
		self.add_edit_buttons(button_frame)
		button_frame.pack(fill=X)

	def add_file_buttons(self,button_frame):
		self.new_image= PhotoImage(file="/home/pragya/Documents/text-editor/images/new.gif",master=button_frame)
		new=Button(button_frame,image=self.new_image,command=self.New,width=30,height=30,relief=FLAT).pack(side=LEFT)
		self.open_image= PhotoImage(file="/home/pragya/Documents/text-editor/images/open.gif",master=button_frame)
		openfile=Button(button_frame,text="Open",image=self.open_image,command=self.open_as,width=55,height=30,compound=LEFT,relief=FLAT).pack(side=LEFT)
		self.save_image= PhotoImage(file="/home/pragya/Documents/text-editor/images/save.gif",master=button_frame)
		save=Button(button_frame,text="Save",image=self.save_image,command=self.save_1,width=55,height=30,compound=LEFT,relief=FLAT).pack(side=LEFT)
		#photo2 = Tkinter.PhotoImage(file="/home/pragya/Pictures/new.jpg")
	
	def add_edit_buttons(self,button_frame):
		self.undo_image= PhotoImage(file="/home/pragya/Documents/text-editor/images/undo.gif",master=button_frame)
		self.undo_button=Button(button_frame, text="Undo", image=self.undo_image, command=self.undo, width=55, height=30, compound=LEFT, relief=FLAT)
		self.undo_button.pack(side=LEFT)
		self.redo_image= PhotoImage(file="/home/pragya/Documents/text-editor/images/redo.gif",master=button_frame)
		self.redo_button=Button(button_frame,image=self.redo_image,command=self.redo,width=40,height=38,relief=FLAT)
		self.redo_button.pack(side=LEFT)
		self.cut_image= PhotoImage(file="/home/pragya/Documents/text-editor/images/cut.gif")
		self.cut_button=Button(button_frame,image=self.cut_image,command=self.Cut,width=40,height=38,relief=FLAT,state=DISABLED)
		self.cut_button.pack(side=LEFT)
		self.copy_button=Button(button_frame,text="Copy",command=self.Copy,relief=FLAT,state=DISABLED)
		self.copy_button.pack(side=LEFT)
		#self.text.bind("<Shift>",lambda event:c.Copy)
		self.paste_button=Button(button_frame,text="Paste",command=self.Paste,relief=FLAT,state=DISABLED)
		self.paste_button.pack(side=LEFT)

	def add_bindings(self):
		self.file_menu_bindings()
		self.edit_menu_bindings()
		self.search_menu_bindings()
		self.tools_menu_bindings()
	
	def file_menu_bindings(self):
		#self.text.bind("<Alt-f>", self.menubar.invoke(self.menubar.index("File")))
		self.text.bind("<Control-n>", self.New)
		self.text.bind("<Control-o>", self.open_as)
		self.text.bind("<Control-s>", self.save_1)
		self.text.bind("<Shift-Control-S>", self.save_as)
		self.text.bind("<Control-q>", self.Quit) # havnt written self.root.quit coz it contains 2 arguments and self.root.quit() (which is an inbuilt function needs only one function, though self.root.quit should be written. It is not making a difference here because we are not using any tab windows, so destroying one window(which is happening in self.Quit) is same as destroying all the windows(which is happening in self.root.quit).

	def edit_menu_bindings(self):
		#self.text.bind("<Alt-e>", self.menubar.invoke(self.menubar.index("Edit"))) 
		self.text.bind("<Control-z>", self.undo)
		self.text.bind("<Control-m>", self.redo) #ctrl-Shift-z not working -- so changed it to ctrl-m
		self.text.bind("<Control-c>", self.Copy)
		self.text.bind("<Control-x>", self.Cut)
		self.text.bind("<Control-v>", self.Paste)
		self.text.bind("<Control-g>", self.Select_all) #changed from 'ctrl-a' as it was not working.
	
	def search_menu_bindings(self):           
		#self.text.bind("<Alt-s>", self.menubar.invoke(self.menubar.index("Search")))
		self.text.bind("<Control-f>",self.search_window)
		#self.text.bind("<Control-g>",c.find_menu)
		self.text.bind("<Control-h>",self.replace_window)
		self.text.bind("<Control-i>",self.go_to_line)
		
	def tools_menu_bindings(self):
		#self.text.bind("<Alt-t>", self.menubar.invoke(self.menubar.index("Tools")))
		self.text.bind("<space>",self.spell_check) ##########################################3 change this(MAy) -- (Sept) working properly now. 
		#self.text.bind("<Return>",self.Split)		
		self.text.bind(".",self.spell_check)
		self.text.bind("<Control-F7>",self.spell_check_window) 

	def file_menu(self):
		self.filemenu = Menu(self.menubar, tearoff=0)
		new=self.filemenu.add_command(label="New", command=self.New,underline=0,accelerator="Ctrl+n")
		self.filemenu.add_command(label="Open", command=self.open_as,underline=0,accelerator="Ctrl+o")
		self.filemenu.add_command(label="Save", command=self.save_1,underline=0,accelerator="Ctrl+s")
		self.filemenu.add_command(label="Save as...", command=self.save_as,underline=0,accelerator="Shift+Ctrl+s")
		#filemenu.add_command(label="Close", command=self.Quit,underline=0,accelerator="Ctrl+q")
	
		self.filemenu.add_separator()
	
		self.filemenu.add_command(label="Exit", command=self.Quit) #different from Quit() inside file_class because it does not check whehter the file is saved or not before quitting.
		self.menubar.add_cascade(label="File", menu=self.filemenu,underline=0)
	

	def edit_menu(self):
		self.editmenu = Menu(self.menubar, tearoff=0)
		self.editmenu.add_command(label="Undo", command=self.undo,underline=0,accelerator="Ctrl+z",state=DISABLED)
		self.editmenu.add_command(label="Redo", command=self.redo,underline=0,accelerator="Ctrl+Shift+z",state=DISABLED)
		self.editmenu.add_separator()
	
		self.editmenu.add_command(label="Cut", command=self.Cut,underline=0,accelerator="Ctrl+x",state=DISABLED)
		self.editmenu.add_command(label="Copy", command=self.Copy,underline=0,accelerator="Ctrl+c",state=DISABLED)
		self.editmenu.add_command(label="Paste", command=self.Paste,underline=0,accelerator="Ctrl+v",state=DISABLED)
		self.editmenu.add_command(label="Delete", command=self.Delete,state=DISABLED)
		self.editmenu.add_command(label="Select All", command=self.Select_all,underline=7,accelerator="Ctrl+g") #changed from 'ctrl-a' as it was not working.
	
		self.menubar.add_cascade(label="Edit", menu=self.editmenu)
	
	def help_menu(self):
		helpmenu = Menu(self.menubar, tearoff=0)
		helpmenu.add_command(label="Help Index", command=self.Cut)
		helpmenu.add_command(label="About...", command=self.Cut)
		self.menubar.add_cascade(label="Help", menu=helpmenu)
		
	
	def search_menu(self):
		searchmenu = Menu(self.menubar, tearoff=0)
		searchmenu.add_command(label="find...", command=self.search_window,underline=0,accelerator="Ctrl+f")
		#searchmenu.add_command(label="find Next", command=c.find,accelerator="Ctrl+g")
		#searchmenu.add_command(label="find Previous", command=c.Cut)
		searchmenu.add_command(label="find and Replace", command=self.replace_window,underline=0,accelerator="Ctrl+h")
		searchmenu.add_separator()	
		searchmenu.add_command(label="Go to Line", command=self.go_to_line_window,underline=0,accelerator="Ctrl+I")
		self.menubar.add_cascade(label="Search", menu=searchmenu,underline=0)
	
	def tools_menu(self):
		toolsmenu = Menu(self.menubar, tearoff=0)
		toolsmenu.add_command(label="Check Spelling...", command=self.spell_check_window,underline=0,accelerator="Ctrl+F7")

		c1=Checkbutton(toolsmenu,variable=self.spell_check_var)	
		toolsmenu.add_checkbutton(label="Auto SpellCheck", command=self.auto_spell_check,variable=self.spell_check_var)
		#c1.select()	
		#searchmenu.add_command(label="find Previous", command=c.Cut)
		#searchmenu.add_command(label="find and Replace", command=c.Replace_window,underline=0,accelerator="Ctrl+h")	
		self.menubar.add_cascade(label="Tools", menu=toolsmenu,underline=0)
	
	
	def add_menus(self):
		self.menubar = Menu(self.root)
		self.file_menu()
		self.edit_menu()
		#self.help_menu()
		self.search_menu()
		self.tools_menu()	
		self.root.config(menu=self.menubar)

	def split(self, event = None):
		print "bla"

	def main(self):
		
		self.root=Tkinter.Tk()
		self.root.title("Sample Text Editor")
		self.conf_win_counter=0
		self.undo_counter=0
		text_frame=Frame(self.root)	
		self.text=Text(text_frame,bg="WHITE",exportselection=1,wrap=WORD) # self.text is an instance of the class Text.
		
		self.text.bind("<Control-Key>",self.split) #definitely controls some behaviour	
		self.text.bind("<Control-Shift-Key>",self.split)
		self.text.bind("<Alt-Key>",self.split)

		self.add_scroll_bars(text_frame)
		self.text.pack()
		
		self.text.config(yscrollcommand=self.vertical_scrollbar.set,undo=False)
		
		self.spell_check_var = IntVar()

		self.create_hash()
		self.add_buttons()
		self.add_menus()
		self.add_bindings()

		application.__init__(self)
		import_all_classes.__init__(self)
		application.set_new_values(self)
		
		self.text.focus_set()
		self.root.protocol("WM_DELETE_WINDOW", self.Quit)
		text_frame.pack()
		
		text_frame.bind('<Configure>', self.resize)
		
		self.text.bind('<<Modified>>',self.enable_undo)
		#self.text.bind("<Button-1>", self.button_pressed)
		self.text.bind("<ButtonRelease-1>", self.button_released)
		#self.text.bind('<Double-Button-1>', self.button_pressed)
		#self.text.bind('<Double-ButtonRelease-1>', self.button_released)
		#self.text.bind('<Triple-Button-1>', self.button_pressed)
		#self.text.bind('<Triple-ButtonRelease-1>', self.button_released)
		#self.text.bind('<Key>',self.key_pressed)
		self.text.bind('<KeyPress>',self.key_press_event)
		#self.text.bind('<KeyPress>', self.Split)
		
		self.text.bind('<space>',self.key_press_event) # we explicitly have to write for these two keys coz they are not getting detected normally.
		self.text.bind('<period>',self.key_press_event)
		
		self.text.bind('<Motion>', self.call_if_text_selected)
		self.root.mainloop()

	
		

