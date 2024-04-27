from tkinter import *

expression = "" #global expression we will use to update current expression

#after we update a variable we use the set("") method to update the gui

# used to update expression given the numebr provided
# ex. if exp = "4 + " and num 5 then exp = "4 + 5" afterwards
def press(num):
    global expression
    expression += num;
    equation.set(expression)

#function to attempt to execute the expression
#try eval(String)
#then update equation to display on gui
def equalpress():
    try:
        global expression
        total = str(eval(expression)) #uses str() to convert value to expression
        equation.set(total)
        #reset expression as we just computed what was in expression
        expression = str(total)

    except:
        equation.set("error")
        expression = ""


#clear method to reset eq and exp
def clear():
    global expression
    expression = ""
    equation.set("")

def newB(symbol): #simple function that returns a new button, we use this because most the code is the same for each buttton except the text
    return Button(gui, text= symbol, fg = 'black', bg = 'white', height=1, width=4,
                     command= lambda: press(symbol))
def place(but,r,c,p,padx):
    but.grid(row=r, column=c, pady=(p,0), padx=(padx,0), ipadx=0,sticky="nsew") #stick = "nsew" removes padding horizontally

if __name__ == "__main__": #code will run only if program is executed, similar to main function of java
    gui = Tk()
    #main gui window using Tk() class

    #simple methods we can run on the gui
    gui.title("calculator using tkinter")
    gui.configure(background = "light blue")
    gui.geometry("270x150") #sets default resolution of gui, WxH

    #define equation here, can still be used in outside methods
    equation = StringVar()

    expField = Entry(gui, textvariable=equation) #entry object gets text user input
    expField.grid(columnspan=6,ipadx=80) #.grid places entry within the gui (size of txt box, x padding)

    #lambda is a way to create a small function, we use this so we don't have to define one seperately
    #we use a helper method to condense this process
    b0 = newB("0")
    b1 = newB("1")
    b2 = newB("2")
    b3 = newB("3")
    b4 = newB("4")
    b5 = newB("5")
    b6 = newB("6")
    b7 = newB("7")
    b8 = newB("8")
    b9 = newB("9")
    bPl = newB("+")
    bMi = newB("-")
    bTi = newB("*")
    bDi = newB("/")

    #custom buttons for enter and clear
    bE = Button(gui, text = "=", fg = 'black', bg = 'white', height=1, width=4,
                command= lambda: equalpress())
    bCl = Button(gui, text = "Clear", fg = 'black', bg = 'white', height=1, width=4,
                 command= lambda: clear())

    #now that we have created the buttons we will display them on the screen
    #col 0
    place(b7,1,0,10,15)
    place(b4,2,0,0,15)
    place(b1, 3, 0, 0,15)
    #col 1
    place(b8,1,1,10,0)
    place(b5, 2, 1, 0,0)
    place(b2, 3, 1, 0,0)
    place(b0, 4, 1, 0,0)
    # col 2
    place(b9, 1, 2, 10,0)
    place(b6, 2, 2, 0,0)
    place(b3, 3, 2, 0,0)
    #col 3
    place(bDi, 1, 3, 10,0)
    place(bTi, 2, 3, 0,0)
    place(bMi, 3, 3, 0,0)
    place(bPl, 4, 3, 0,0)

    # = and clear
    #place(b1, 4, 0, 0)
    place(bE, 4, 0, 0,15)
    place(bCl, 4,2,0,0)

    gui.mainloop()