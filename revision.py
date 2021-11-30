from tkinter import*
root=Tk()
root.geometry("653x345")

root.title("My first GUI with Harry")
f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")
f2=Frame(root,bg="grey",borderwidth=8,relief=SUNKEN)
f2.pack(side=TOP,fill="x")


l=Label(f1,text="Welcome to the Tkinter Project")
l.pack()
l=Label(f2,text="Here we learn How to use Tkinter")
l.pack(pady=160)
root.mainloop()