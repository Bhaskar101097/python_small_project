from tkinter import*
def getvals():
    print(f"the user is {uservalue.get()}")
    print(f"the password is {passwordvalue.get()}")
root=Tk()
root.geometry("643x345")
root.title("Login Details")
Label(root,text="Enter Your Details Here",font="comicsansms 20 bold",pady=10).grid(row=0,column=3)

user=Label(root,text="USER")
password=Label(root,text="PASSWORD")
user.grid(row=1,column=2)
password.grid(row=2,column=2)

uservalue=StringVar()
passwordvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passwordentry=Entry(root,textvariable=passwordvalue)

userentry.grid(row=1,column=3)
passwordentry.grid(row=2,column=3)

Button(text="Submit your Details",command=getvals).grid(row=3,column=3)



root.mainloop()