from tkinter import *
from sort import *
import random

#program in tkinter to visualize bubble sort

#global variables
lowIDs = []  #ids from lower half of canvas
upIDs = []  #ids from upper half of canvas

merge = False #merge sort flag

def draw(arr,colors):
    global lowIDs
    #draws inside canvas function, bars based off arr, colors tell colors of bars
    n = len(arr)
    horL = 560/n #length of each bar+space between next bar
    startx = 1/6 * horL  #starting x value
    y1 = 500  # guarentees rectangle fills beyond space

    can.delete(*lowIDs) #clears canvas
    lowIDs = []  # clears lowIDs
    normalize = [i/max(arr) for i in arr] #percentage of the bar that should be filled

    for i, curr in enumerate(normalize): #curr represents the current content of normalize, being an integer
        xWidth = horL * 2 / 3  # width of bar
        height = 80+(300*(1-curr)) if not merge else 180+(200*(1-curr)) #changes height if mergesorting


        recs = can.create_rectangle(startx,y1,startx+xWidth,height,fill=colors[i]) #create(x1,y1,x2,x2,col)
        #startx marks where the rectangle will start bounded, x2 is then that + the width of each bar, y is measured by content of arr
        #print(str(arr[i]) + " " + str(len(str(arr[i]))))

        fontSize = (22 - int(n/6))
        if (len(str(arr[i])) == 2):
            fontSize = int(fontSize // 1.3)
        if (len(str(arr[i])) == 3):
            fontSize = int(fontSize // 1.5)
        texts = can.create_text(startx+xWidth/2,height-15,text=arr[i], font=("Impact", fontSize),
                                fill="black")

        if merge:
            lowIDs.append(can.create_line(0,150,560,150,fill="black")) #create a line if merging and appending
        lowIDs.append(recs)
        lowIDs.append(texts) #now we can wipe only the 'bottom' half of the canvas

        startx += horL  # increment space by horL(space + width of bar)
    can.update_idletasks() #ensures canvas is updated

def draw2(arr,colors,val): #note this arr is not the sorting array, rather from mergeSort
    global upIDs
    if arr is None:
        can.delete(*upIDs)
        return
    n = len(arr)
    horL = 560 / n
    startx = 1/6 * horL
    can.delete(*upIDs)
    upIDs = []

    maxV = max(i for i in arr if i is not None) #maxValue
    normalize = [] #we have to do normalize differently for merge sort as we have 'None' values
    for i in range(0, len(arr)):
        if (arr[i] != None):
            normalize.append(arr[i] / maxV)
            print("i:" + str(i) + " maxV:" + str(maxV) + " i/maxV:" + str(i / maxV))
        else:
            normalize.append(None)
    print(normalize)

    #similar to draw1, but we have to account for 'None' values
    for i, curr in enumerate(normalize):
        if (arr[i] != None):  # only make bar if there is content
            xWidth = horL * 2 / 3
            height = 50 + (80 * (1 - curr))
            recs = can.create_rectangle(startx, 150, startx + xWidth, height, fill=colors[i])  # create(x1,y1,x2,x2,col)
            fontSize = (22 - int(n / 6))
            if (len(str(arr[i])) == 2):
                fontSize = int(fontSize // 1.3)
            if (len(str(arr[i])) == 3):
                fontSize = int(fontSize // 1.5)
            texts = can.create_text(startx + xWidth / 2, height - 15, text=arr[i], font=("Impact", fontSize),
                                fill="black")
            upIDs.append(texts)  # now we can wipe only the 'bottom' half of the canvas
            upIDs.append(recs)

        startx += horL  # increment space by horL(space + width of bar)
    can.update_idletasks()  # ensures canvas is updated
    can.update_idletasks()

def rand(length):
    #generates random arr of size length
    arr = []
    for i in range(0,length):
        arr.append(random.randint(0,100))
    return arr

def upSize(size):
    #updates size of array and redraws it
    global arr
    global can
    can.delete("all")
    arr = rand(size)
    draw(arr,['black']*size)

def upSpeed(speed):
    #called in order to change spd in sort.py
    changeSpd(speed)

def upMerge(val):
    #called to change merge flag
    global merge
    merge = val

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
speed.set(1)
size.set(10)


bWidth = 10
bfg = 'black'
bbg = 'blanched almond'


#Buttons
bsBut = Button(bFrame,text = "Bubble", height=2, width=bWidth, fg = bfg,bg = bbg,
                command = lambda: (bubSort(arr,draw)))
bsBut.grid(row=10,column=0,padx=0,pady=10)

insBut = Button(bFrame,text = "Insertion", height=2, width=bWidth, fg = bfg,bg = bbg,
                command = lambda: (insSort(arr,draw)))
insBut.grid(row=10,column=1,padx=0,pady=10)

selBut = Button(bFrame,text = "Selection", height=2, width=bWidth, fg = bfg,bg = bbg,
                command = lambda: (selSort(arr,draw)))
selBut.grid(row=10,column=2,padx=0,pady=10)

quickBut = Button(bFrame,text = "Quick", height=2, width=bWidth, fg = bfg,bg = bbg,
                command = lambda: (quickSortHelper(arr,draw)))
quickBut.grid(row=11,column=0,padx=0,pady=10)

mergeBut = Button(bFrame,text = "Merge", height=2, width=bWidth, fg = bfg,bg = bbg,
                command = lambda: (mergeSortHelper(arr,draw,draw2,upMerge)))
mergeBut.grid(row=11,column=1,padx=0,pady=10)

#i dont know how this is going to work, possible multithreading? yikerones
pause = Button(bFrame,text = "Pause", height=2, width=bWidth, fg = bfg,bg = bbg,
             command = lambda: upPause)
pause.grid(row=10,column=5,padx=(5,5),pady=10)

root.mainloop()