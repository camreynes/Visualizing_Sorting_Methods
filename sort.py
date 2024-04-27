import time
import visSort

def bubSort(arr,draw): #content,canvas,recIDS
    fin = False
    while not fin:
        fin = True
        for i in range(0, len(arr) - 1):
            if (arr[i + 1] < arr[i]):  # determines whether to do ascending or descending sorting
                print("!")

                swap(i, i + 1,arr)
                visSort.update(i,"green2")
                visSort.update(i+1, "green2")
                #can.update_idletasks()

                fin = False

                time.sleep(.5)
            print("!")
            draw(arr)


def swap(pos1,pos2,arr):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp