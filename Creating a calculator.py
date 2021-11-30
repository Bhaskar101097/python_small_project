from tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text== "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        scvalue.update()





root=Tk()
root.geometry("543x900")
root.title("My Calculator")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X)

f1=Frame(root,bg="grey")
b=Button(f1,text="9",padx=25,pady=12,font="lucida 35 bold")
b.pack(side="left",padx=18,pady=12)
b.bind("<Button-1>",click)
b=Button(f1,text="8",padx=25,pady=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)
b=Button(f1,text="7",padx=25,pady=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)
b=Button(f1,text="*",padx=5,pady=7,font="lucida 35 bold")
b.pack(padx=18,pady=12)
b.bind("<Button-1>",click)

f1.pack()


f1=Frame(root,bg="grey")
b=Button(f1,text="6",padx=22,pady=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)
b=Button(f1,text="5",padx=22,pady=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)
b=Button(f1,text="4",padx=22,pady=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)
b=Button(f1,text="+",padx=5,pady=7,font="lucida 35 bold")
b.pack(padx=18,pady=12)
b.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="grey")
b=Button(f1,text="4",padx=21,pady=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)
b=Button(f1,text="3",padx=21,pady=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)
b=Button(f1,text="2",padx=21,pady=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)
b=Button(f1,text="%",padx=5,pady=7,font="lucida 35 bold")
b.pack(padx=18,pady=12)
b.bind("<Button-1>",click)
f1.pack()


f1=Frame(root,bg="grey")
b=Button(f1,text="1",padx=25,pady=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)
b=Button(f1,text="0",padx=25,pady=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)
b=Button(f1,text="=",padx=25,pady=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)
b=Button(f1,text="/",padx=5,pady=7,font="lucida 35 bold")
b.pack(padx=18,pady=12)
b.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="grey")
b=Button(f1,text="+",padx=19,pady=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)
b=Button(f1,text="-",padx=19,pady=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)
b=Button(f1,text="C",padx=19,pady=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)
b=Button(f1,text="00",padx=5,pady=7,font="lucida 35 bold")
b.pack(padx=18,pady=12)
b.bind("<Button-1>",click)
f1.pack()

root.mainloop()