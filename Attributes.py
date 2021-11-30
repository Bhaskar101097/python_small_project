from tkinter import*
root=Tk()
root.geometry("644x333")
root.title("My GUI with Harry")

#Important Label Options
#text - adds the text
#bd - background
#fg - foreground
#font - sets the font
#padx - x padding
#pady - y padding
#relief - border styling - SUNKEN , RAISED , GROOVE , RIDGE
title_label=Label(text='''Vidyut Jammwal (Hindi: विद्युत जामवाल; born 10 December 1980)[3][4] is an Indian actor, martial artist, stuntman, and action     \n choreographer who predominantly works in Indian action films. Known for his roles in the Commando film series, he is a practitioner of Kalaripayattu and also \n known as "The New Age Action Hero of Bollywood".[5] He studied the art of Kalaripayattu since from the age of three. He is a recipient of several awards \n including 1 Filmfare Award.''',bg="blue",fg="White",padx=23,pady=13,font= "comicsansms 19 bold",borderwidth=3,relief=SUNKEN
)
#Important pack options
#anchor=nw
#side=top,bottom,left,right
#fill
#padx
#pady
#title_label.pack(side=LEFT,anchor='nw',fill=X)
title_label.pack(side=BOTTOM,fill="y")

root.mainloop()