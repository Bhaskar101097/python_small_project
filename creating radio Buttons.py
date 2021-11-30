from tkinter import *
import tkinter.messagebox as tmsg
def Done():
    tmsg.showinfo("Order Recieved",f"We have recieved your Order {var.get()},Thanks for Ordering")
root=Tk()
root.geometry("645x432")
root.title("Radio Buttons Tutorial")
#var=IntVar()
#var.set(1)
var=StringVar()
Label(root,text="What would you like to have sir?",font="lucida 19 bold",justify=LEFT,pady=14).pack()

radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio=Radiobutton(root,text="idly",padx=14,variable=var,value="idly").pack(anchor="w")
radio=Radiobutton(root,text="Burger",padx=14,variable=var,value="Burger").pack(anchor="w")
radio=Radiobutton(root,text="Egg Roll",padx=14,variable=var,value="Egg Roll").pack(anchor="w")
radio=Radiobutton(root,text="French Fries",padx=14,variable=var,value="French Fries").pack(anchor="w")



Button(root,text="Thankyou for your Order",command=Done).pack()


root.mainloop()