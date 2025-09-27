class Node:
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1

array = [2,3,5,7]
x = Node(3)

y = x   #pointing to the adress of node x
print(y)
