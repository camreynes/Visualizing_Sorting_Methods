import copy
import time

#global vars
spd = 1/10

def mergeSortHelper(arr,draw,draw2,upMerge):
    upMerge(1)
    mergeSort(arr,0,len(arr)-1,draw,draw2)
    upMerge(0) #turns off merge slice
    time.sleep(spd*2)
    draw(arr,['black' for x in range(len(arr))]) #reset colors


    draw(arr,['black' for x in range(len(arr))]) #reset colors
def mergeSort(arr,lo,hi,draw,draw2):
    if lo < hi:
        #first portion displays the range of bars being split up/merged
        draw(arr,['black' for x in range(len(arr))]) #reset colors
        time.sleep(spd)
        draw(arr,['dodger blue' if x >= lo and x <= hi else 'black' for x in range(len(arr))]) #highlight range of bars being sorted
        time.sleep(spd)

        mid = lo+(hi-lo) // 2 #good practice
        mergeSort(arr,lo,mid,draw,draw2)
        mergeSort(arr,mid+1,hi,draw,draw2)
        merge(arr,lo,mid,hi,draw,draw2)

def merge(arr,lo,mid,hi,draw,draw2):
    cols1 = ['black' if x >= lo and x <= hi else 'black' for x in range(len(arr))] #highlighting the range of bars being merged

    #merge method for mergeSort
    a = arr[lo:mid+1]
    b = arr[mid+1:hi+1] #slicing exclusive

    arr2 = [None] * len(arr)
    arr2[lo:hi+1] = arr[lo:hi+1]

    cols2 = ['maroon1' if x >= lo and x <= mid else 'gold2' if x >= mid+1 and x <= hi else 'None' for x in range(len(arr))]

    draw(arr,cols1)
    draw2(arr2,cols2,lo)
    time.sleep(spd) #initial draw and sleep

    aI,bI = 0,0 #left and right arrays
    cI = lo
    while aI < len(a) and bI < len(b):
        #compare put into left or right
        if a[aI] <= b[bI]: #if left is smaller, put in left
            arr[cI] = a[aI]
            disChange(arr, arr2, draw, draw2, cols1, cols2, lo + aI, cI)
            aI += 1
        else:
            arr[cI] = b[bI]
            disChange(arr, arr2, draw, draw2, cols1, cols2, lo + bI + len(a), cI)
            bI += 1
        cI += 1
    #dump rest of calues
    while aI < len(a):
        arr[cI] = a[aI]
        disChange(arr, arr2, draw, draw2, cols1, cols2, lo + aI, cI)
        aI += 1
        cI += 1
    while bI < len(b):
        arr[cI] = b[bI]
        disChange(arr, arr2, draw, draw2, cols1, cols2, lo + bI + len(a), cI)
        bI += 1
        cI += 1
    draw2(None,None,None) #wipe the second canvas

def disChange(arr,arr2,draw,draw2,cols1,cols2,offset,cI):
    #displays the change in arr and arr2, offset is where we should represesnt color in arr2
        #i is aI or bI
    cols2[offset] = 'red1'  # bar in arr2 that is being compared to a[aI]
    cols1[cI] = 'red1'
    draw(arr, cols1)
    draw2(arr2, cols2, offset)
    time.sleep(spd)
        #we are 'done' with these colors
    cols2[offset] = 'gray38'  # bar in arr2 that is being compared to a[aI]
    cols1[cI] = 'gray38'
    draw(arr, cols1)
    draw2(arr2, cols2, offset)
    time.sleep(spd)

def quickSortHelper(arr,draw):
    global spd #only need this global within this method of QS
    #spd /= 4
    quickSort(arr,0,len(arr)-1,draw)

def quickSort(arr,lo,hi,draw):
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
        quickSort(arr,lo,part-1,draw)
        quickSort(arr,part+1,hi,draw)
    print(arr)

def shellSort(arr,draw):
    # code here
    n = len(arr)
    gap = n // 2

    while gap > 0:
        j = gap
        while n > j: #make sure we are not out of bounds
            i = j - gap
            while i >= 0: #compare, break early if already 'sorted'
                cols = ['black' for x in range(len(arr))]  # default color
                cols[i], cols[i + gap] = 'green2', 'green2'  # highlights bars being compared
                draw(arr, cols)
                time.sleep(spd)

                if arr[i] < arr[i + gap]:
                    break
                else:
                    swap(i+gap,i,arr)
                    cols[i], cols[i + gap] = 'red', 'red'  # highlights bars being swapped
                    draw(arr, cols)
                    time.sleep(spd)

                i = i - gap #decrement
            j += 1
        gap = gap // 2

    cols = ['black' for x in range(len(arr))]  # default color
    time.sleep(spd)
    draw(arr, cols)  # reset colors

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

    cols = ['black' for x in range(len(arr))]  # default color
    time.sleep(spd)
    draw(arr, cols)  # reset colors

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

    cols = ['black' for x in range(len(arr))]  # default color
    time.sleep(spd)
    draw(arr, cols)  # reset colors

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

    cols = ['black' for x in range(len(arr))]  # default color
    time.sleep(spd)
    draw(arr, cols)  # reset colors

def swap(pos1,pos2,arr):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]


def changeSpd(newSpd):
    global spd
    spd = newSpd


#to be implemented
def wait(spd):
    # global pause
    time.sleep(spd)
    # while pause:
    #     time.sleep(spd)

def upPause():
    global pause
    pause = not pause
