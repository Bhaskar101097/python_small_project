from tkinter import *
root=Tk()
root.geometry("745x456")
root.title("Pycharm")
def myfunc():
    print("Main Bahut hi mst function hoon")

#Use these to create non drop down menu
mymenu=Menu(root)
mymenu.add_command(label='File',command=myfunc)
mymenu.add_command(label='Exit',command=quit)
root.config(menu=mymenu)

mainmenu=Menu(root)

m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="New Project",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_separator()
m1.add_command(label="Save As",command=myfunc)
m1.add_command(label="Print",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="file",menu=m1)


m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Undo",command=myfunc)
m2.add_command(label="Redo",command=myfunc)
m2.add_separator()
m2.add_command(label="Cut",command=myfunc)
m2.add_command(label="Copy",command=myfunc)
root.config(menu=mainmenu)


mainmenu.add_cascade(label="Exit",menu=m2)

f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN,pady=160,padx=100)
f1.pack(side=LEFT,fill=X)
f2=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN,pady=160,padx=100)
f2.pack(side=TOP,fill=X)

l=Label(f1,text="Trying to do something new")
l.pack()
l1=Label(f2,text="Gotcha")
l1.pack()

root.mainloop() 