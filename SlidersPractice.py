from tkinter import *
import tkinter.messagebox as tmsg
def submit():
    print(f"Thankyou for rating Us {myslider.get()}Stars")
    tmsg.showinfo("Ratings",f"Thankyou for rating Us {myslider.get()} Stars")

root=Tk()
root.geometry("654x534")
root.title("Slider practice Question")
Label(root,text="Rate Us").pack()
myslider=Scale(root,from_=0 ,to = 10,orient=HORIZONTAL)
myslider.set(5)
myslider.pack()

Button(root,text="Submit",command=submit,pady=10).pack()


myslider.pack()
root.mainloop()