import time

def bubSort(arr,draw,ids): #content,canvas,recIDS
    fin = False
    while not fin:
        fin = True
        for i in range(0, len(arr) - 1):
            if (arr[i + 1] < arr[i]):  # determines whether to do ascending or descending sorting
                print("!")
                cols = ['black'] * 10 #default bar color
                cols[i],cols[i+1] = 'red','red' #highlights numbers beings swapped

                swap(i, i + 1,arr)
                draw(arr,cols)

                fin = False

                time.sleep(.5)
            print("!")


def swap(pos1,pos2,arr):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]