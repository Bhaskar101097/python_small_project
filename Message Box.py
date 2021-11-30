from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("745x456")
root.title("Pycharm")
def myfunc():
    print("Main Bahut hi mst function hoon")
def Help():
    print("I will Help You")
    a=tmsg.showinfo("Help","Harry will help you with this GUi")

def rate():
    print("Rate Us")
    value=tmsg.askquestion("Was your Experience Good?","You used this GUI...was your experience good?")
    print(value)
    if value=="yes":
        msg="Great.Rate us on App store Please"
    else:
        msg="Tell us what went wrong.We will call you soon"
    tmsg.showinfo("Experience",msg)

def divya():
    ans=tmsg.askretrycancel("Divya se dosti karlo","Sorry divya nahi banegi aapki dost")
    if ans:
        print("Retry karne par bhi nahi hoga")
    else:
        print("Sahi kra bhai cancel kr diya warna bohot maar khaate")


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

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=Help)
m3.add_command(label="Rate Us",command=rate)
m3.add_command(label="Befriend Divya",command=divya)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="help",menu=m3)


root.mainloop() 