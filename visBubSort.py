from tkinter import *

#program in tkinter to visualize bubble sort

#function to draw data
def draw():
    normalize = [i/max(arr) for i in arr]
    y1 = 500 #guarentees rectangle fills beyond space

    #create(x1,y1,x2,x2,col)
    can.create_rectangle(5,400,30,100,fill="black")


if __name__ == "__main__":
    root = Tk()
    root.title("Bubble Sort Visualization")
    root.geometry("600x500")
    root.configure(background = "white")
    #basic setup of Tk object

    arr = [0,9,3,1,5,7,4,2,10,6] #array to sort, will randomize latter

    can = Canvas(root,width=550,height =400,bg="gray92")
    can.grid(row=0,column=0,padx=25)
    draw()

    root.mainloop()