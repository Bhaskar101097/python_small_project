from tkinter import *
root=Tk()
root.geometry("454x200")
root.title("ScollBar Tutorial")
# For connecting scrollbar to a widget
# 1.widget(yscrollcommand=scrollbar.set)
# 2. scrollbar.config(command=widget.yview)
scrollbar=Scrollbar(root)
scrollbar.pack(fill=Y,side=RIGHT)
#listbox=Listbox(root,yscrollcommand=scrollbar.set)
#for i in range(344):
#  listbox.insert(END,f" Item{i}")

#listbox.pack(fill="both",padx=33)
text=Text(root,yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)



scrollbar.config(command=text.yview)





root.mainloop()