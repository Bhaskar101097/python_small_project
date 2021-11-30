from tkinter import*
def getvals():
    print(f"name is {namevalue.get()}")
    print(f"phone is {phonevalue.get()}")
    print(f"gender is {gendervalue.get()}")
    print(f"emergencyContact is {emergencyContactvalue.get()}" )
    print(f"paymentmode is {paymentmodevalue.get()}")
root=Tk()
root.geometry("645x354")
root.title("Travel Agency")
Label(root,text="Welcome to Bhaskar Travels",font="comicsansms 20 bold",pady=10).grid(row=0,column=3)
name=Label(root,text="NAME")
phone=Label(root,text="PHONE")
gender=Label(root,text="GENDER")
emergencyContact=Label(root,text="EMERGENCY CONTACT")
paymentmode=Label(root,text="PAYMENT MODE")

#pack text for our forms
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergencyContact.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

#Tkinter variables for entry 
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyContactvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

#Entries for the form
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyContactentry=Entry(root,textvariable=emergencyContactvalue)
paymentvalueentry=Entry(root,textvariable=paymentmodevalue)

#pack the entries
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyContactentry.grid(row=4,column=3)
paymentvalueentry.grid(row=5,column=3)

#CheckBox
foodservice=Checkbutton(text="Want to pre book your Meals?",variable=foodservicevalue)
foodservice.grid(row=6,column=3)

Button(text="Submit to Bhaskar Travels",command=getvals).grid(row=7,column=3)


root.mainloop()