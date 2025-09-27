'''converting an array to linked list'''

class Node:
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1

def convertArr2LL(arr):
    head = Node(arr[0])
    mover = head
    for i in range(len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    
    return head

arr = [1,3,5,6,7,9]
head = convertArr2LL(arr)
print(head.data)
print(head.next)
        



