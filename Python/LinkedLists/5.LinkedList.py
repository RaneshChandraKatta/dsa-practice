'''Insertion'''

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
    def insertAtHead(head, val):
        temp = Node(val, head)
        return temp
    
    @staticmethod
    def insertAtEnd(head, val):
        if not head:
            return Node(val)
        
        temp = head
        while temp.next:
            temp = temp.next

        temp.next = Node(val)
        return head
 
    @staticmethod
    def insertAtPosition(head, el, position):
        if not head:
            if position == 1:
                return Node(el)
            else:
                print("List is empty, Insertion Failed")
                return None

        if position == 1:
            return Node(el, head)
        
        count = 1
        temp = head
        while temp and count < position - 1:
            temp = temp.next
            count += 1

        if not temp:  # Position out of range
            print("Position out of range")
            return head
        
        node_to_be_inserted = Node(el, temp.next)
        temp.next = node_to_be_inserted

        return head
    
    @staticmethod
    def insertBeforeVal(head, el, val):
        if not head:
            return None
        if head.data == val:
            return Node(el, head)
        
        temp = head
        while temp.next:
            if temp.next.data == val:
                inserted_node = Node(el, temp.next)
                temp.next = inserted_node
                break
            temp = temp.next
        return head
    
