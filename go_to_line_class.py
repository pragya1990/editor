from Application_2 import *
CSI="\x1B["

class go_to_line_class(application):
	def __init__(self):
		print CSI+"39m" + "inside __init__ go_to_line" +CSI+"0m"

	def go_to_line(self,event = None):
		end_line=self.text.index(END)
		if self.go_to_line_entry.get()=="" or int(float(self.go_to_line_entry.get()))>int(float(end_line)) or int(float(self.go_to_line_entry.get()))<=0 :
			print "out of index"
			return
		line_index=int(float(self.go_to_line_entry.get()))
		index="%d.%d" % (line_index,0)
		self.text.mark_set(INSERT,index)
		self.text.focus_set()
		self.text.yview(index)	
			

	def on_go_to_line_exit(self):
		self.go_to_line_window_opened=0
		self.go_to_line_win.destroy()

	def go_to_line_window(self,event=None):
		if self.go_to_line_window_opened==1:
			print "window already opened"
			return
		self.go_to_line_win=Toplevel()
		frame_go_to_line_win=Frame(self.go_to_line_win)

		self.go_to_line_entry = Entry(frame_go_to_line_win)
		self.go_to_line_entry.pack(side=LEFT)
	
		self.go_to_line_button = Button(frame_go_to_line_win,text="Find",command=self.go_to_line)
		self.go_to_line_button.pack(side=LEFT)
		self.go_to_line_win.title("Go to line")
		self.go_to_line_window_opened=1
		frame_go_to_line_win.pack()	
		self.go_to_line_win.protocol("WM_DELETE_WINDOW", self.on_go_to_line_exit)
		self.go_to_line_win.resizable(0,0)
		self.go_to_line_win.mainloop()
		

