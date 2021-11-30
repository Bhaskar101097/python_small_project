from tkinter import *
def resize():
    # print(f"The value of width is {widthvalue.get()}")
    #print(f"The value of height is {heightvalue.get()}")
    width_value=width.get()
    height_value=height.get()

    root.geometry(f"{width_value}*{height_value}")
root=Tk()
root.title("Windows Resizer")
root.geometry("653x323")

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

Button=Button(root,text="Apply",command=resize)
Button.grid()

root.mainloop()