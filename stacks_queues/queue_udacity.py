class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self):
        self.head=None
        
class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        pass

    def peek(self):
        pass 

    def dequeue(self):
        pass