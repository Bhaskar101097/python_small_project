from tkinter import *
root=Tk()
root.title("Canvas Widget")
canvas_width=800
canvas_height=200
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()


#The Line goes from x1 y1 to x2 y2
#can_widget.create_line(0,0,800,200,fill="red")
#can_widget.create_line(0,200,800,0,fill="red")

#To Create a rectangle specify parameters in this order-coors of top left and coors of bottom right.

#can_widget.create_rectangle(3,5,700,300,fill="Blue")
#can_widget.create_text(400,100,text="Python")
#can_widget.create_oval(333,210,232,323)
root.mainloop()