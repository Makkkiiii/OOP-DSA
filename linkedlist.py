from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional['Node'] = None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def add(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else :
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
            print(None)
            
    def search (self,data):
        current = self.head
        position = 0
        while current:
            position += 1
            if current.data == data:
                print("Available at position:", position)
                return 
            else:
                current = current.next
        print("Not Available")

            
l=LinkedList()
l.add(4)
l.add(3)
l.add(7)
l.search(3)

l.display()