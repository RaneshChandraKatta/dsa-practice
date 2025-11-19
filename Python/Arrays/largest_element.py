#Brute force method : Sort the array and print the last element in the array , time complexity - o(NlogN)

#Opimal method:
def largest_element_in_array(arr):
    largest = arr[0]
    for i in len(arr):
        if arr[i] > largest:
            largest = arr[i]
    return largest

#time complexity - o(n)
