from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import pafy
import getpass
import os, glob
import time
import pyperclip
from PIL import ImageTk, Image
import progressbar


bgColor = "#333333"
fgColor = "#505050"
redColor = "#ff0006"

currentUser = getpass.getuser()
message = None

qual = None
qualityVar = 1
index = 1


choicesList = ['Best', 'Worst']
def callback(total, recvd, ratio, rate, eta):
	global timeLeft
	timeLeft = eta
	print("There is " + str(int(timeLeft)) + " time left.")
	global totalBytes
	totalBytes = total

	

def highQual():
	qual = 1 
def lowQual():
	qual = 2
class Window(Frame):

	def __init__(self, master = None):
		Frame.__init__(self,master,bg=fgColor)
		self.master = master
		self.progress = ttk.Progressbar(self, orient="horizontal",
			length=200, mode="determinate")
		self.progress.place(relx=0.17,rely=0.85)

		self.bytes = 0
		self.maxbytes = 12
		'''
		def start(self):
			self.progress["value"] = 0
			self.maxbytes = totalBytes
			self.progress["maximum"] = 50000
			self.read_bytes()

		def read_bytes(self):
			''''''simulate reading 500 bytes; update progress bar''''''
			self.bytes += 500
			self.progress["value"] = self.bytes
		if self.bytes < self.maxbytes:
			# read more bytes after 100 ms
			self.after(100, self.read_bytes)
		'''

		self.init_window()
	def init_window(self):
		self.master.title("Youtube Downloader")
		self.pack(fill=BOTH, expand=1)
		panel = Label(self, image = imag, borderwidth=0,highlightthickness=0,padx=0)
		panel.place(anchor=NE,relx=1.07,y=-20)


		w = Label(self, text='Quality:', anchor=W)
		w.place(anchor=NW,x=0,y=20)
		w.config(bg=fgColor,fg="white",anchor=NW)

		def function():
			selection = var.get()

			if  selection == 1:
				print("Best Quality will be downloaded")
				global qual
				qual = 1
				index=0
				return qual
				return index
			elif selection == 2:
				print("Worst Quality will be downloaded")
				global qual
				qual = 2
				return qual

		
		var = IntVar()


		Radiobutton(self, text = "Best", variable = var, value = 1,bg=fgColor,activebackground=fgColor,foreground='black',indicatoron=True,activeforeground='black',disabledforeground='white').place(anchor=E,relx=.3,y=32)
		Radiobutton(self, text = "Worst", variable = var, value = 2,bg=fgColor,activebackground=fgColor,activeforeground='black',indicatoron=True,disabledforeground='white').place(anchor=E,relx=.5,y=32)
		bestqualLabel = Label(text="Best",fg='white',bg=fgColor).place(anchor=E,relx=.3,y=32)
		worstqualLabel = Label(text="Worst",fg='white',bg=fgColor).place(anchor=E,relx=.5,y=32)

		global v
		v = StringVar()
		e = Entry(self,bg=fgColor,fg="white",relief='sunken')
		e.config(textvariable=v,width=40,justify='center',cursor='X_cursor')
		e.place(x=130,y=100, anchor=CENTER)
		v.set("Paste URL Here",)
		global s
		s = v.get()

		downloadButton = Button(self, text="Quit",command=self.client_exit,bg=bgColor,fg="white",relief='flat',cursor='X_cursor')
		downloadButton.place(x=0, y=124)
		anyButton = Button(self, text="Download",bg=bgColor,fg="white",relief='flat', command=actualDownloader,cursor='pirate')
		anyButton.place(x=335,y=124)
		

	def client_exit(self):
		exit()

def finalAlert():

	downloadDoneAlert = messagebox.showinfo("Download Finished", message)
	downloadDoneAlert.pack()

actualQual = qual

def actualDownloader():
	s = v.get()

	flag=0

	type=1		#input("Hit 1 for video,2 for playlist")
	type=int(type)
		#input("Hit 1 for best clarity, 2 for worst, 3 for other")
	result=s
	quality=actualQual

	c=0
	if type==1:
		url = result
		video = pafy.new(url)
		best = video.streams
		for b in best:
			print(str(c)+str(b))
			c+=1;
		if flag==1:
			index=raw_input("Enter index")
			index=int(index)
		if quality==2:
			global index
			index=c-1
		elif quality==1:
			global index
			index=0
		
		filename = video.streams[index]
		print(filename)
		x=filename.download(filepath=filename.title + "." + filename.extension,callback=callback)

		cwd = os.getcwd()
		global message
		message = filename.title + " was save to " + cwd
		finalAlert()
	else:
		url=result
		video=pafy.get_playlist(url)
		for i in xrange(1,100):
			c=0
			best=video['items'][i]['pafy'].streams
			for b in best:
				print(str(c)+str(b))
				c+=1
			if flag==1:
				index=raw_input("Enter index")
				index=int(index)
			elif quality==2:	
				index=c-1
			elif quality==1:
				index=0
			filename=video['items'][i]['pafy'].streams[index]
			try:
				x=filename.download(filepath="C:/ProgramOut")
			except:
				x=filename.download(filepath="C:/")

root = Tk()
img = Image.open("YouTube-BLACK.png")
img = img.resize((200, 124))
img = img.convert("RGBA")
imag = ImageTk.PhotoImage(img)
root.geometry("400x150")
root.resizable(width=False, height=False)

app = Window(root)
root.mainloop()

