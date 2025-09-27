#INSERTION IN A HEAP

def insertHeap(arr, n):
    i = n
    temp = arr[n]
    while i > 0 and temp > arr[(i-1) // 2]:
        arr[i] = arr[(i-1) // 2]
        i = (i-1) // 2
    arr[i] = temp

#CREATING A HEAP 

def createHeap(arr):
    for i in range(len(arr)):
        insertHeap(arr,i)

#SWAPPING ELEMNETS IN AN ARRAY

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

#DELETION IN A HEAP

def delHeap(arr, n):
    arr[0] = arr[n - 1]
    i = 0 
    j = (2 * i) + 1

    while j < (n - 1):

        if j + 1 < (n - 1) and arr[j + 1] > arr[j]:
            j += 1
        if arr[i] < arr[j]:
            swap(arr, i, j)
            i = j
            j = (2 * i) + 1
        else:
            break
    arr.pop()



            

