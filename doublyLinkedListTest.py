class Node:
    def __init__(self, data):
        self.item = data
        self.prev = None
        self.next = None

class doublyLinkedList:
    def __init__(self):
        self.start_node = None
    
    def InsertToEmptyList(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is empty")
    
    def InsertToEnd(self, data):
        #Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        #Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
    
    #Delete the elements from the start
    def DeleteAtStart(self):
        #Check if list is empty
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        #If there is only 1 element in the list, delete it
        if self.start_node.next is None:
            self.start_node = None
            return
        #Sinon décaller la liste de 1, en supprimant le 1er élément
        self.start_node = self.start_node.next
        self.start_prev = None
    
    #Delete element from the end
    def DeleteAtEnd(self):
        #Check if list is empty
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        #If there is only 1 element in the list, delete it
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        #Sinon décaller la liste de 1, en supprimant le dernier élément
        while n.next is not None:
            n = n.next
        n.prev.next = None

    #Traversing and Displaying each element of the list
    def Display(self):
        #If list empty, dont print
        if self.start_node is None:
            print("Nothing to display in here")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")

    def FindDeepestChildren(self):
        n = self.start_node
        while n is not None:
            lastn = n.item
            n = n.next
        print("Last element of the list: ",lastn)
        return

# Create a new Doubly Linked List
NewDoublyLinkedList = doublyLinkedList()
# Insert the element to empty list
NewDoublyLinkedList.InsertToEmptyList(10)
# Insert the element at the end
NewDoublyLinkedList.InsertToEnd(20)
NewDoublyLinkedList.InsertToEnd(30)
NewDoublyLinkedList.InsertToEnd(40)
NewDoublyLinkedList.InsertToEnd(50)
NewDoublyLinkedList.InsertToEnd(60)
# Display Data
#NewDoublyLinkedList.Display()
# Delete elements from start
NewDoublyLinkedList.DeleteAtStart()
# Delete elements from end
NewDoublyLinkedList.DeleteAtEnd()
# Display Data
#NewDoublyLinkedList.Display()

#NewDoublyLinkedList.FindDeepestChildren()

amogus=doublyLinkedList()
amogus.InsertToEmptyList(1)
amogus.InsertToEnd(2)
amogus.InsertToEnd(3)
amogus.Display()
amogus.FindDeepestChildren()