from tkinter import *
root=Tk()
root.title("India News-Aapka Apna Akhbar")
root.geometry("1000x800 ")
for i in range(0,3):
    with open(f"{i+1}.odt") as f:
        

root.mainloop()