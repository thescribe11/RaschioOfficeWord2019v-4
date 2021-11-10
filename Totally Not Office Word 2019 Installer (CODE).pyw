import requests
import time
import tkinter as tk
from clint.textui import progress
import os
import getpass
from tkinter import filedialog
import time
from tkinter import ttk
class main():
	def __init__(self):
		self.login_name = getpass.getuser()
		self.filename = f"C:\\Users\\{self.login_name}\\Documents"
		self.stage = 0
		self.root = tk.Tk()
		self.root.title("Totally Not Office Word 2019")
		self.root.configure(background="#87C6F4")
		self.root.update()
		self.main_screen = tk.Frame(self.root, width=66, background="#87C6F4")
		self.main_screen.grid(row = 0, column = 1, sticky='nsew')
		self.cancel = tk.Button(self.root, text = "cancel", command = self.quitter)
		self.next = tk.Button(self.root, text = "Next", command = self.deleter)
		self.cancel.grid(row=1, column = 0, sticky='sw')   # TODO transition to .grid()
		self.next.grid(row=1, column = 2, sticky='ew' )
		if self.stage == 0:
			self.introduction()
		self.root.mainloop()

	def download(self):
		### TODO Set the explanation text.
		self.explanation_label = tk.Label(self.main_screen,text = 
"""
Please choose a location to install Totally Not Office Word 2019.       
When you're ready to install, just click the "Next" button.
This might take a few moments.      
""", font="Times 14 bold", background="#87C6F4")
		self.explanation_label.grid(row=0, column=0, sticky='nsew')
		self.to_change = tk.Entry(self.main_screen, width=30)		
		self.to_change.grid()
		self.filename += "\\TotallyNotOfficeWord2019.exe"

		self.to_change.insert(0, str(self.filename))
		self.to_change.grid(row = 1, column = 0)   #30


	def download_file(self):		
		f = open(self.filename, "wb")
		f.write(b"")
		f.close()
		self.next['state'] = 'disabled'
		self.next.update()
		r = requests.get("https://raw.github.com/thescribe11/RaschioOfficeWord2019v-4/master/TotallyNotOfficeWord2019.exe", stream=True)
		with open(self.filename, "ab") as f:
			valuer = 0
			for chunk in r.iter_content( chunk_size=90000 ):
				valuer += 1
				self.progress['value'] = valuer
				self.progress.update()
				f.write(chunk)
		self.next['state'] = 'normal'
		self.next.update()
		self.main_screen.destroy()
		self.main_screen = tk.Frame(self.root, width=66, background="#87C6F4")
		self.main_screen.grid(row = 0, column = 1, sticky='nsew')
		self.next_label = tk.Label(self.main_screen, text="\nThank you for installing Totally Not Office Word 2019.\nClick 'Next' to close the installer.\n", font="Times 14 bold", background="#87C6F4")
		self.next_label.grid(sticky='nsew')		
	def introduction(self):
		self.introlabel = tk.Label(self.main_screen, text = 
		"""Hello.

Welcome to the Installation Wizard for Totally Not Office Word 2019.   
To install, click "Next" and follow instructions.    
You may cancel installation by clicking "cancel" at any point .    
	

	""", font="Times 14 bold", background="#87C6F4")
		self.introlabel.pack()

	def gui_thread(self, *args):
		self.to_change.destroy()
		self.explanation_label.destroy()
		
		self.explanation_2 = tk.Label(self.main_screen, text="\n\n      Installing Totally Not Office Word 2019...    \n", font="Times 14 bold", background="#87C6F4")
		self.explanation_2.grid(sticky='nswe')

		self.progress = ttk.Progressbar(self.main_screen, orient='horizontal', length=500, mode='determinate')
		self.progress.grid()
		self.margin = tk.Label(self.main_screen, text="\n\n", background="#87C6F4")
		self.margin.grid(sticky="sew")


	def deleter(self, *args):

		self.main_screen.destroy()
		self.main_screen = tk.Frame(self.root, width=66, background="#87C6F4")
		self.main_screen.grid(row = 0, column = 1, sticky="nsew")
		self.stage += 1
		if self.stage == 1:
			self.download()
		elif self.stage == 2:
			self.root.after(100, self.gui_thread)
			self.root.after(500,self.download_file)


			
		elif self.stage == 3:
			self.quitter()
	def quitter(self, *args):
		if self.filename == None:
			self.root.destroy()
			quit()
		else:			
			self.root.destroy()
		quit()
if __name__ == '__main__':
	main()
