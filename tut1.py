from tkinter import*
from PIL import Image,ImageTk

bhaskar_root=Tk()

bhaskar_root.geometry("435x234")
#photo= photoimage(files="index.jpeg")

#for jpeg Images

image=image.open("index.jpeg")
photo=ImageTk.photoImage(Image)
class_label=label(image=photo)
class_label.pack()

bhaskar_root.mainloop()