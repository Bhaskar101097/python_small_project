from tkinter import*
root=Tk()
root.geometry("655x333")
f1=Frame(root,borderwidth=8,bg="grey",relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")
def hello():
    print("Hello Tkinter Buttons")
def name():
    print("Name is Bhaskar")
b1=Button(f1,fg="red",text="Print Now",command=hello)
b1.pack(side=LEFT)
b2=Button(f1,fg="red",text="Name",command=name)
b2.pack(side=LEFT)
root.mainloop()