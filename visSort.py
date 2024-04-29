from tkinter import *
from sort import *
import random

#program in tkinter to visualize bubble sort

#global variables
recIDS = []  # list of rectangle ids, is appended after each rectangle is created, can.create returns rec ID

def draw(arr,colors):
    #draws inside canvas function, bars based off arr, colors tell colors of bars
    n = len(arr)
    horL = 540/n #length of each bar+space between next bar
    startx = 5  #starts at 5, allows 5 padding on the right
    y1 = 500  # guarentees rectangle fills beyond space


    can.delete("all") #clears canvas
    normalize = [i/max(arr) for i in arr] #percentage of the bar that should be filled


    list = []
    for i, curr in enumerate(normalize): #curr represents the current content of normalize, being an integer
        y2 = 380-(300*curr) #height using pct rect height
        xWidth = horL * 2 / 3  # width of bar
        recs = can.create_rectangle(startx,y1,startx+xWidth,380-(300*curr),fill=colors[i]) #create(x1,y1,x2,x2,col)
            #startx marks where the rectangle will start bounded, x2 is then that + the width of each bar, y is measured by content of arr

        recIDS.append(recs) #rec is an integer, then is added to the list, recIDS
        can.create_text(startx+xWidth/2,y2-15,text=arr[i],font=("Impact",22-int(n/6)),fill="black"); #create_text(x,y,text,font=("",23),fill) - similar nature to createRect

        startx += horL #increment space by horL(space + width of bar)
    can.update_idletasks() #ensures canvas is updated

def press():
    #function for bubblesort
    upSpeed(1 / (4 * speed.get()))
    bubSort(arr, draw)

    #quickSort(arr,draw)
    #selSort(arr, draw)

def rand(length):
    #generates random arr of size length
    arr = []
    for i in range(0,length):
        arr.append(random.randint(0,10))
    return arr

def upSize(size):
    #updates size of array and redraws it
   global arr
   arr = rand(size)
   draw(arr,['black']*size)

def upSpeed(speed):
    #called in order to change spd in sort.py
    changeSpd(speed)

root = Tk()
root.title("Sort Visualizer - @camreynes")
root.geometry("600x620")
root.configure(background = "white")
#basic setup of Tk object

#main canvas
arr = rand(10)
arr = [4,7,6,8,9,0,1,3,2,5]
can = Canvas(root, width=560, height=400, bg="gray92")
can.grid(row=0,column=0,padx=25)
draw(arr,['black']*10)

# frame for scalers - two frames are easier to manage given the spacing for buttons and scalers differ
sFrame = Frame(root,width=500,height=200,bg="gray95") #height doesnt matter much since nsticky is used
sFrame.grid(row=10,column=0, sticky="nsew",padx=40,pady=(10,0))
sFrame.grid_columnconfigure((0,1), weight=1)

#frame for buttons
bFrame = Frame(root,width=500,height=200,bg="gray95")
bFrame.grid(row=12,column=0, sticky="nsew",padx=40)
bFrame.grid_columnconfigure((0,1,2,3,4), weight=1)

#sliders in frame
speed = Scale(sFrame,from_=.25,to=10,orient=HORIZONTAL, #SPEED
             label="Speed", digits=3,resolution=.25,length=100)
speed.grid(row=0,column=0,pady=5)
speed.bind("<ButtonRelease>", lambda value: upSpeed(1/(4*speed.get()))) #a wrapper in sort could have worked
            ## but would be less efficient and need to import visSort which break things

size = Scale(sFrame,from_=3,to=50,orient=HORIZONTAL, #SIZE
             label="Size",length=100)
size.grid(row=0,column=1,pady=5)
size.bind("<ButtonRelease>", lambda value: upSize(size.get()))

#default values sliders
speed.set(10)
size.set(10)


bWidth = 10
bfg = 'black'
bbg = 'blanched almond'


#Buttons
bsBut = Button(bFrame,text = "Bubble", height=2, width=bWidth, fg = bfg,bg = bbg,
                command = lambda: (bubSort(arr,draw),press()))
bsBut.grid(row=10,column=0,padx=0,pady=10)

insBut = Button(bFrame,text = "Insertion", height=2, width=bWidth, fg = bfg,bg = bbg,
                command = lambda: (insSort(arr,draw),press()))
insBut.grid(row=10,column=1,padx=0,pady=10)

selBut = Button(bFrame,text = "Selection", height=2, width=bWidth, fg = bfg,bg = bbg,
                command = lambda: (selSort(arr,draw),press()))
selBut.grid(row=10,column=2,padx=0,pady=10)

quickBut = Button(bFrame,text = "Quick", height=2, width=bWidth, fg = bfg,bg = bbg,
                command = lambda: (quickSort(arr,draw),press()))
quickBut.grid(row=11,column=0,padx=0,pady=10)

#i dont know how this is going to work, possible multithreading? yikerones
pause = Button(bFrame,text = "Pause", height=2, width=bWidth, fg = bfg,bg = bbg,
             command = lambda: upPause)
pause.grid(row=10,column=5,padx=(5,5),pady=10)

root.mainloop()