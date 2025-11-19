def sedond_smallest(arr):
    smallest = arr[0]
    second_smallest = float('inf')
    for i in range(len(arr)):
        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]
        elif arr[i] != smallest and arr[i] < second_smallest:
            second_smallest = arr[i]
    return second_smallest
