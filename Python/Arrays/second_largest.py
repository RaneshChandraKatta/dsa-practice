def second_largest(arr):
    arr.sort()
    largest = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] != largest:
            second_largest = arr[i]
            break
    return second_largest

def better_second_largest(arr):
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    second_largest = -1      # only positive allowed (your condition)
    for i in range(len(arr)):
        if arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    return second_largest

def optimal_second_largest(arr):
    largest = arr[0]
    second_largest = float('-inf')
    for i in range(len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > second_largest:
            second_largest = arr[i]
    return second_largest

            
            

