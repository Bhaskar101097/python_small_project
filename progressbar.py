from tkinter import *
from tkinter import ttk
self.geometry("654x456")
class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Python Tkinter ProgressBar")
        self.minsize(640,400)


        self.buttonFrame=ttk.LabelFrame(self,text="Progress Bar")
        self.buttonFrame.grid(row=0,column=0)
        self.progressBar()


