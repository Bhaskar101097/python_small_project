from tkinter import*
root=Tk()
root.geometry("633x433")
f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")
f2=Frame(root,bg="grey",borderwidth=8,relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l=Label(f1,text="Project Tkinter - Pycharm")
l.pack(pady=142)
l=Label(f2,text="Welcome to the Sublime Project",font="Helvetica 16 bold",fg="red")
l.pack(pady=160)


root.mainloop()