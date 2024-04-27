import time

def bubSort(arr,draw,dur): #content,canvas,time interval
    n = len(arr)
    fin = False
    while not fin:
        fin = True
        for i in range(0, len(arr) - 1):
            if (arr[i + 1] < arr[i]):  # determines whether to do ascending or descending sorting
                print("!")
                cols = ['black'] * n #default bar color
                cols[i],cols[i+1] = 'green2','green2' #highlights numbers beings swapped

                swap(i, i + 1,arr)
                draw(arr,cols)

                fin = False

                time.sleep(float(dur))
            print("!")


def swap(pos1,pos2,arr):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]