''' 1)Traversal in a Linked List
    2)Length of Linked List
    3)Searching a Linked List
'''
class Node:
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1

class LinkedList:
    def convertArr2LL(arr):
        if not arr:
            return None
        head = Node(arr[0])
        mover = head
        for i in range(1,len(arr)):
            temp = Node(arr[i])
            mover.next = temp
            mover = temp
        return head

    def traversal(head):
        temp = head 
        while temp:
            print(temp.data, end = '->')
            temp = temp.next
        print("None")

    def LengthOfLL(head):
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def searchLL(head, value):
        temp = head 
        while temp:
            if temp.data == value: return True
            temp = temp.next
        return False



# Create an array
arr = [1, 3, 5, 6, 7, 9]

# Convert array to Linked List
head = LinkedList.convertArr2LL(arr)

# Traversal
print("Linked List:")
LinkedList.traversal(head)   # Output: 1->3->5->6->7->9->None

# Length of Linked List
print("Length:", LinkedList.LengthOfLL(head))  # Output: 6

# Search for a value
print("Search 5:", LinkedList.searchLL(head, 5))   # Output: True
print("Search 10:", LinkedList.searchLL(head, 10)) # Output: False



        



