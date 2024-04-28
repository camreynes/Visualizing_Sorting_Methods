import time

def insSort(arr,upCol,draw,spd,can):
    print(arr)
    for i in range(len(arr)):
        time.sleep(.1)
        can = draw(arr, ['black'] * len(arr))
        minV = arr[i]
        mindex = i

        for j in range(i, len(arr)):
            if (arr[j] < minV):
                mindex = j
                minV = arr[j]
        swap(mindex, i,arr)
        print(arr,end=" ")
        print(str(i) + " " + str(mindex))



        time.sleep(.1)

    for i in range(5):
        upCol(i, 'green2', can)
        time.sleep(.1)
        can.update_idletasks()



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