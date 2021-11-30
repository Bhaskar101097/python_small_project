from tkinter import *
import tkinter.messagebox as tmsg
def getdollars():
    print(f"We have credited {myslider2.get()} dollars in your bank Account")
    tmsg.showinfo("Amount Credited",f"We have credited {myslider2.get()} dollars in your bank Account")
root=Tk()
root.geometry("645x435")
root.title("Sliders tutorial")
#myslider=Scale(root,from_=0, to=100)
#myslider.pack()

Label(root,text="How many dollars do you want?").pack()

myslider2=Scale(root,from_=0, to=100,orient=HORIZONTAL,tickinterval=50)
myslider2.set(34)
myslider2.pack()

Button(root,text="Get Dollars",pady=10,command=getdollars).pack()

root.mainloop()