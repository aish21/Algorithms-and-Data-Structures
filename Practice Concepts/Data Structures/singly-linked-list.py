# Python implementation of Singly Linked List

class Node:
    # Create a node
    def __init__(self, item):
        self.item = item
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

# Driver code
if __name__ == '__main__':
    linkedList = LinkedList()

    # Assign Data
    linkedList.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Connect the nodes
    linkedList.head.next = second
    second.next = third

    # Print the Linked List
    while linkedList.head != None:
        print(linkedList.head.item, end=' ')
        linkedList.head = linkedList.head.next