lfrom tkinter import *
def Update():
    print("Updating the GUI")
    root.geometry(f"{widthvalue.get()}x{heightvalue.get()}")

root=Tk()
root.title("Window Resizer")
root.geometry("435x234")
width=Label(root,text="width")
height=Label(root,text="height")
width.grid()
height.grid()

widthvalue=StringVar()
heightvalue=StringVar()
widthentry=Entry(root,textvariable=widthvalue)
heightentry=Entry(root,textvariable=heightvalue)
widthentry.grid(row=0,column=2)
heightentry.grid(row=1,column=2)

button=Button(root,text="Apply",command=Update)
button.grid()



root.mainloop()