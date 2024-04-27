from tkinter import *
from sort import *

#program in tkinter to visualize bubble sort


#function to draw data
def draw(arr):
    recIDS = []  # list of rectangle ids, is appended after each rectangle is created, can.create returns rec ID
    normalize = [i/max(arr) for i in arr] #percentage of the bar that should be filled
    y1 = 500  #guarentees rectangle fills beyond space
    xspace = 5  # space between each bar, iterates +50 each time

    list = []
    for i, curr in enumerate(normalize): #curr represents the current content of normalize, being an integer
        y2 = 380-(300*curr) #height using pct rect height
        recs = can.create_rectangle(xspace,y1,xspace+25,380-(300*curr),fill="black") #create(x1,y1,x2,x2,col)

        recIDS.append(recs) #rec is an integer, then is added to the list, recIDS
        can.create_text(xspace+12.5,y2-15,text=arr[i],font=("Impact",20),fill="black"); #create_text(x,y,text,font=("",23),fill)

        xspace += 50 #increment spacing for next rect


    #can.itemconfig(recs[2], fill="purple")

def update(id,color): #updates color of bar > ID
    can.itemconfig(id, fill=color)

def press():
    bubSort(arr,draw)

if __name__ == "__main__":
    root = Tk()
    root.title("Bubble Sort Visualization")
    root.geometry("600x500")
    root.configure(background = "white")
    #basic setup of Tk object

    arr = [0,9,3,1,5,7,4,2,10,6] #array to sort, will randomize latter
    #can.itemconfig(rectangle_ids[1], fill="purple")

    can = Canvas(root, width=550, height=400, bg="gray92")
    can.grid(row=0,column=0,padx=25)
    draw(arr)

    but = Button(root,text = "test", height=2, width=5, fg = 'white',bg = 'black',
                 command = press)
    but.grid(row=10,column=0,padx=10,pady=10)
    root.mainloop()

    #bubSort(arr,can)