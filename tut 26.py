from tkinter import *
root=Tk()
root.geometry("645x534")
root.title("Code with Bhaskar")
root.configure(bg="grey")

# If we want to know the height and width of the window in which we are working
width=root.winfo_screenwidth()
height=root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="close",command=root.destroy,padx=15).pack(fill=X,anchor="w")



root.mainloop()