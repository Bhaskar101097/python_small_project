from tkinter import *
self=Tk()
self.geometry("645x434")

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Python Tkinter Progress Bar")
        self.minsize(640,400)


        self.buttonFrame=ttk.LabelFrame(self,text="Progress Bar")
        self.buttonFrame.grid(row=0,column=0)

        self.ProgressBar()