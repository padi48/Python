class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        printval = self.head

        while printval is not None:
            print(printval.data)
            printval = printval.next
    
    #inserting at the beginning
    def atBeginning(self, newdata):
        NewNode = Node(newdata)

        NewNode.next = self.head
        self.head = NewNode

    #inserting at the end
    def atEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        lastI = self.head
        while lastI.next:
            lastI = lastI.next
        lastI.next = NewNode

    #inserting between two Nodes
    def between(self, middle, newdata):
        if middle is None:
            print("The mentioned node is absent!")
            return

        NewNode = Node(newdata)
        NewNode.next = middle.next
        middle.next = NewNode

    def remove(self, key):
        headval = self.head

        if headval is not None:
            if headval.data == key:
                self.head = headval.next
                headval = None
                return
        while headval is not None:
            if headval.data == key:
                break
            prev = headval
            headval = headval.next

        if headval == None:
            return
        prev.next = headval.next
        headval = None

list1 = LinkedList()

list1.atBeginning("Monday")
list1.atEnd("Tuesday")
list1.atEnd("Wednesday")

list1.printList()
