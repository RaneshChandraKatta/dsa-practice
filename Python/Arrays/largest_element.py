def largest_element_arr(arr):
    largest = 0
    for i in range(0, len(arr)):
        if largest < arr[i]:
            largest = arr[i]

    return largest


arr = [2,37,65,3,1]
print(largest_element_arr(arr))




# time complexity - O(N)