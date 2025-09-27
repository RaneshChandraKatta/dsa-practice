'''Deletion'''

class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

class LinkedList:
    @staticmethod
    def convertArr2LL(arr):
        if not arr:
            return None
        head = Node(arr[0])
        mover = head
        for i in range(1, len(arr)):
            temp = Node(arr[i])
            mover.next = temp
            mover = temp
        return head

    @staticmethod
    def traversal(head):
        temp = head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

    @staticmethod
    def removeHead(head):
        if not head:
            return None
        head = head.next
        return head
    
    @staticmethod
    def removeTail(head):
        if not head:
            return None
        if not head.next:
            return None   #returns none if the linked list contains only one node
        temp = head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        return head
    
    @staticmethod
    def delAtPosition(head, position):
        if not head:
            return None
        
        # Case 1: Deleting head
        if position == 1:
            return head.next
        
        count = 1
        temp = head
        prev = None
        
        # Traverse until position is reached
        while temp and count < position:
            prev = temp
            temp = temp.next
            count += 1
        
        # If position is out of range
        if not temp:
            print("Position out of range")
            return head
        
        # Delete the node
        prev.next = temp.next
        return head
    
    @staticmethod
    def delValue(head, val):
        if not head:
            return None
        
        if head.data == val:
            return head.next
        
        temp = head
        prev = None
        
        while temp and  temp.data != val:
            prev = temp
            temp = temp.next

        if not temp:
            print("value not found in the linked list")
            return head
        
        prev.next = temp.next
        return head





arr = [1, 3, 5, 7, 9, 11, 13]

head = LinkedList.convertArr2LL(arr)

'''
Test input for removing head and tail:

print("Before removing head:")
LinkedList.traversal(head)   


head = LinkedList.removeHead(head)

print("After removing head:")
LinkedList.traversal(head)   

head = LinkedList.removeTail(head)

print("After removing tail:")
LinkedList.traversal(head)  '''


'''
Test input for deleting based on the value

head = LinkedList.delAtPosition(head, 2)
LinkedList.traversal(head) 


head = LinkedList.delAtPosition(head, 3)
LinkedList.traversal(head)  

# Delete out of range
head = LinkedList.delAtPosition(head, 5)  
LinkedList.traversal(head)'''

head = LinkedList.delValue(head, 1)
LinkedList.traversal(head)

head = LinkedList.delValue(head, 5)
LinkedList.traversal(head)

head = LinkedList.delValue(head, 7)
LinkedList.traversal(head)

head = LinkedList.delValue(head, 100)
LinkedList.traversal(head)
