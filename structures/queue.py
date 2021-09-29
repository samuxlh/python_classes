import time # this library will make it easier for us to see data

class Node: # defining node structure
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None
class linkedList: # defining list structure
    def __init__(self):
        self.head = None
        self.last = None
    def printList(self): # prints entire list
        temp=self.head
        while temp is not None:
            print(temp.data,end=">")
            time.sleep(0.5)
            temp=temp.next
        print('\n')
    def insertNode(self, data): # adds new element to list
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev = self.last
            self.last = self.last.next
    def removeNode(self): # removes element at the top of list
        if self.head is None:
            return ("list is empty")
        else:
            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
            
    def first_node(self): # shows what's on top of the list
        return self.head.data
    def is_empty(self): # true if empty
        if self.head is None:
            return True
        else:
            return False

myList = linkedList() # declaring myList as a linkedList type

opt = int(input("How many values do you want to insert? ")) # this will define how many nodes it will have

print("Starting list...")
time.sleep(0.5)
for i in range(opt):
    x = int(input("insert value: "))
    myList.insertNode(x) 

print("\nList after inserting:")
time.sleep(0.5)
myList.printList()
time.sleep(2)

print("\nIs list empty? ")
time.sleep(0.5)
print(myList.is_empty()) 
time.sleep(2)

print("\nWho's on top? ")
time.sleep(0.5)
print(myList.first_node()) 
time.sleep(2)

print("\nNow removing all elements...\n")
time.sleep(0.5)
for n in range(opt):
    myList.printList()
    time.sleep(0.5)
    myList.removeNode()
time.sleep(2)

print("Is list empty? ")
time.sleep(0.5)
print(myList.is_empty())
time.sleep(2)