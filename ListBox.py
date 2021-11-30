from tkinter import *
def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1

i=0
root=Tk()
root.geometry("645x453")
root.title("ListBox Tutorial")
lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"First item in the listbox")

Button(root,text="Add item",command=add).pack()



root.mainloop()