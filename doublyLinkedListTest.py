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