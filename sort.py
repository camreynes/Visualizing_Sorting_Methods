import copy
import time

#global vars
spd = 1

def changeSpd(newSpd):
    global spd
    spd = newSpd

def quickSort(arr,draw):
    global spd #only need this global within this method of QS
    #spd /= 4
    sort(arr,0,len(arr)-1,draw)

def sort(arr,lo,hi,draw):
    cols = ['black'] * len(arr)
    for i in range(lo,hi+1):
        cols[i] = 'dodger blue' #highlighting the range of bars being sorted
    draw(arr,cols)
    time.sleep(spd)
    cols = ['black'] * len(arr)
    draw(arr,cols) #flashes colors highlited, then resets to black
    time.sleep(spd)

    #quick sort, uses quickSort() as a helper method
    if (lo < hi):
        part = partition(arr,lo,hi,draw)
        sort(arr,lo,part-1,draw)
        sort(arr,part+1,hi,draw)
    print(arr)

def partition(arr,low,high,draw):
    # partition method for quicksort
    if low >= high:
        return low #early return

    i = low - 1
    pivot = arr[high]
    for j in range(low,high):
        cols = ['black'] * len(arr)
        cols[high] = 'green2'  # comparing to pivot, so we highlight pivot as green2

        # cols = ['black'] * len(arr)
        for colIndex in range(i+1,j):
            if i != -1:
                cols[colIndex] = 'gray38' #if not getting compared, highlight grey

        cols[j] = 'green2' #highlight bar being compared to pivot
        draw(arr,cols)
        time.sleep(spd)
        if arr[j] < pivot:
            i += 1
            cols[i] = 'red' #highlight bars being swapped
            cols[j] = 'red'
            swap(i,j,arr)
            draw(arr, cols)
            time.sleep(spd)
            cols = ['black'] * len(arr) #reset colors
    swap(i+1,high,arr)
    draw(arr, cols) #cols will be defined, returned otherwise
    time.sleep(spd)
    return i+1

def insSort(arr,draw):
    global spd
    print(spd)
    for i in range(1,len(arr)):
        cols = ['dodger blue' if k <= i-1 else 'black' for k in range(len(arr))] #highlights bars that are already sorted
        j = i
        cols[j] = 'green2' #highlight bar being compared
        draw(arr,cols) #initial draw & reset
        time.sleep(spd)
        #visualizing insSort, we use a deepcopy so we can visualize the swap without a swap at each step
            #we could visualize each swap, however, i believe this implementation is cleaner, albiet, less accurate
        visIn = i
        visNum = arr[j]
        copyArr = copy.deepcopy(arr)
        while(visIn-1 != -1 and visNum <= arr[visIn-1]): #
            swap(visIn,visIn-1,copyArr)
            visIn -= 1
            cols[visIn] = 'gray38' if cols[visIn] != 'green2' else 'gray38' #gray bars until we reach the correct position
            draw(arr,cols)
            time.sleep(spd)
        j = i #actual swapping
        while (j - 1 != -1 and arr[j] <= arr[j - 1]):
            swap(j,j-1,arr)
            j -= 1
        #vcisualized at the end
        cols[j] = 'green2'
        draw(arr, cols)
        time.sleep(spd)

def selSort(arr,draw):
    global spd
    for i in range(len(arr)):
        cols = ['black'] * len(arr); #default color is black for all recs
        cols[i] = 'cyan' #highlight current bar (i)
        draw(arr, cols)
        minV = arr[i]
        mindex = i
        for j in range(i+1, len(arr)):
            if (arr[j] < minV):
                cols[mindex] = 'gray38' if cols[mindex] != 'cyan' else 'cyan'
                    #if bar at mindex is not the ith bar (if it snot the cyan bar), then we change its color to grey
                cols[j] = 'green2' #highlight bar being compared to minV
                mindex = j
                minV = arr[j]
            else:
                cols[j] = 'gray38' #if not being compared, then it is gray
            time.sleep(spd)
            draw(arr, cols)
        swap(mindex, i,arr)
        time.sleep(spd)

def bubSort(arr,draw): #content,canvas,time interval
    global spd
    n = len(arr)
    fin = False
    while not fin:
        fin = True
        for i in range(0, len(arr) - 1):
            cols = ['black'] * n  # default bar color
            cols[i], cols[i + 1] = 'green2', 'green2'  # highlights bars being compared
            draw(arr, cols)
            if (arr[i + 1] < arr[i]):  # determines whether to do ascending or descending sorting
                time.sleep(spd)
                cols[i], cols[i + 1] = 'red', 'red' #highlights bars being swapped
                # swaps and redraws
                swap(i, i + 1, arr)
                draw(arr, cols)
                fin = False
            time.sleep(float(spd))

def swap(pos1,pos2,arr):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]




#to be implemented
def wait(spd):
    # global pause
    time.sleep(spd)
    # while pause:
    #     time.sleep(spd)

def upPause():
    global pause
    pause = not pause
