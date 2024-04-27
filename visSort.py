from tkinter import *
from sort import *
import random

#program in tkinter to visualize bubble sort

#function to draw data, colors is a list that will be used to determine each bars color
def draw(arr,colors):
    print(arr)

    n = len(arr) #length of array, have 540x space to work with total
    horL = 540/n #length of each bar+space between next bar
    startx = 5  #starts at 5, allows 5 padding on the right
    y1 = 500  # guarentees rectangle fills beyond space


    recIDS = []  # list of rectangle ids, is appended after each rectangle is created, can.create returns rec ID
    can.delete("all") #clears canvas
    normalize = [i/max(arr) for i in arr] #percentage of the bar that should be filled


    list = []
    for i, curr in enumerate(normalize): #curr represents the current content of normalize, being an integer
        y2 = 380-(300*curr) #height using pct rect height
        xWidth = horL * 2 / 3  # width of bar
        xSpace = horL * 1 / 3  # space between bars
        recs = can.create_rectangle(startx,y1,startx+xWidth,380-(300*curr),fill=colors[i]) #create(x1,y1,x2,x2,col)
            #startx marks where the rectangle will start bounded, x2 is then that + the width of each bar, y is measured by content of arr


        recIDS.append(recs) #rec is an integer, then is added to the list, recIDS
        print(22-int(n/7))
        can.create_text(startx+xWidth/2,y2-15,text=arr[i],font=("Impact",22-int(n/6)),fill="black"); #create_text(x,y,text,font=("",23),fill) - similar nature to createRect

        startx += horL #increment space by horL(space + width of bar)
    root.update_idletasks() #ensures canvas is updated

def press():
    print(arr)
    spd = 1/(6*speed.get())
    bubSort(arr,draw,spd)

def rand(length):
    arr = []
    for i in range(0,length):
        arr.append(random.randint(0,10))
    return arr

def upSize(size):
   global arr
   arr = rand(size)
   draw(arr,['black']*size)

root = Tk()
root.title("Bubble Sort Visualization")
root.geometry("600x550")
root.configure(background = "white")
#basic setup of Tk object

#main canvas
arr = rand(10)
can = Canvas(root, width=550, height=400, bg="gray92")
can.grid(row=0,column=0,padx=25)
draw(arr,['black']*10)

#frame for options
frame = Frame(root,width=600,height=100,bg="white")
frame.grid(row=10,column=0)

#sliders in frame
speed = Scale(frame,from_=.5,to=5,orient=HORIZONTAL,
             label="Speed", digits=2,resolution=.1) #size scaler
speed.grid(row=0,column=0,pady=5)

size = Scale(frame,from_=3,to=50,orient=HORIZONTAL,
             label="Size")
size.grid(row=0,column=1,pady=5,padx=15)
size.bind("<ButtonRelease>", lambda value: upSize(size.get()))
#size.config(command=lambda value: upSize(size.get()))

#test button
but = Button(frame,text = "sort", height=2, width=5, fg = 'white',bg = 'black',
             command = press)
but.grid(row=10,column=0,padx=10,pady=10)

root.mainloop()


#bubSort(arr,can)