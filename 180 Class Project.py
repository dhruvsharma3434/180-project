from tkinter import *
from tkinter import ttk
from googletrans import Translator

root = Tk()
root.geometry("500x500")
root.config(bg = "Light Blue")

Language_Translator = Label(root,text="Language Translator",bg = "Light Blue",font = ("Arial CE",15,"bold"))
Language_Translator.place(relx = 0.5,rely = 0.5,anchor = CENTER)

input_label = Label(root,text = "Entry Text",bg = "Light Blue",font = ("Arial",11,"bold"))
input_label(relx =0.02,rely =0.2,anchor = W)
input_label = Entry(root,bg = "Light Blue",font =("Arial",11,"bold"),height= = 50,wrap = WORD,width = 60,padx =10,pady =1,border =0)

input_Text.place(relx =0.02,rely =0.5,anchor = W)
root.mainloop()
