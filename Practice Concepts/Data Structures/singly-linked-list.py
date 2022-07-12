# Python implementation of Singly Linked List and its operations

class Node:
    # Create a node
    def __init__(self, item):
        self.item = item
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Insert: Beginning
    def insertBeg(self, newItem):
        newNode = Node(newItem)
        newNode.next = self.head
        self.head = newNode
    
    # Insert: End
    def insertEnd(self, newItem):
        newNode = Node(newItem)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = newNode
    
    # Insert: After a node
    def insertAfterNode(self, prevNode, newItem):
        if prevNode is None:
            print('The given previous node must be in the Linked List')
            return       
        newNode = Node(newItem)
        newNode.next = prevNode.next
        prevNode.next = newNode
    
    # Deleting a node
    def deleteNode(self, position):
        if self.head is None:
            return 
        
        temp = self.head
        
        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        
        if temp is None:
            return
        
        if temp.next is None:
            return
        
        next = temp.next.next
        temp.next = None
        temp.next = next
    
    # Search for an element
    def search(self, key):
        current = self.head

        while current is not None:
            if current.item == key:
                return True
            current = current.next
        return False
    
    # Sort Linked List
    def sort(self, head):
        current = head
        index = Node(None)
        
        if head is None:
            return 
        
        else:
            while current is not None:
                index = current.next

                while index is not None:
                    if current.item > index.item:
                        current.item, index.item = index.item, current.item
                    index = index.next

                current = current.next
    
    # Print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.item) + " ", end="")
            temp = temp.next

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
    
    llist = LinkedList()
    llist.insertEnd(1)
    llist.insertBeg(2)
    llist.insertBeg(3)
    llist.insertEnd(4)
    llist.insertAfterNode(llist.head.next, 5)

    print('Linked List:')
    llist.printList()

    print("\nAfter deleting an element:")
    llist.deleteNode(3)
    llist.printList()

    print()
    item_to_find = 3
    if llist.search(item_to_find):
        print(str(item_to_find) + " is found")
    else:
        print(str(item_to_find) + " is not found")

    llist.sort(llist.head)
    print("Sorted List: ")
    llist.printList()