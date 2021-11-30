from tkinter import*
def getvals():
    print(f"Firstname is {Firstnamevalue.get()}")
    print(f"Lastname is {Lastnamevalue.get()}")
    print(f"Age is {Agevalue.get()}")

root=Tk()
root.geometry("645x456")
root.title("Dance Class Form")
Firstname=Label(root,text="Firstname")
Lastname=Label(root,text="Lastname")
Age=Label(root,text="Age")
Firstname.grid(row=0)
Lastname.grid(row=1)
Age.grid(row=2)

Firstnamevalue=StringVar()
Lastnamevalue=StringVar()
Agevalue=StringVar()

Firstnameentry=Entry(root,textvariable=Firstnamevalue)
Lastnameentry=Entry(root,textvariable=Lastnamevalue)
Ageentry=Entry(root,textvariable=Agevalue)
Firstnameentry.grid(row=0,column=1)
Lastnameentry.grid(row=1,column=1)
Ageentry.grid(row=2,column=1)

Button(text="Submit",command=getvals).grid()

root.mainloop()