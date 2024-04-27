from tkinter import *
from tkinter.ttk import * #different collection than line 1

#main window of application
root = Tk()

#changing title
root.title("first program!")

#example label, displaying text in window
lab = Label(root, text = "display") #(parent, text)
lab.pack() #auto-adjusts widget and displays it

#to start program
root.mainloop()