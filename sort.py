import time

def insSort(arr,draw,spd):
    print(arr)
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


def bubSort(arr,draw,spd): #content,canvas,time interval
    n = len(arr)
    fin = False
    while not fin:
        fin = True
        for i in range(0, len(arr) - 1):
            if (arr[i + 1] < arr[i]):  # determines whether to do ascending or descending sorting
                cols = ['black'] * n #default bar color
                cols[i],cols[i+1] = 'green2','green2' #highlights numbers beings swapped

                #swaps and redraws
                swap(i, i + 1,arr)
                draw(arr,cols)
                fin = False
                time.sleep(float(spd))
            print("!")


def swap(pos1,pos2,arr):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]