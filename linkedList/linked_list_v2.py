class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None
        self.tail = None
        self.index = 0

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        self.head = Node(data=data, next=self.head)

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """

        node = Node(data=data)
        if self.index == 0:
            self.head = node
        else:
            self.tail.next= node
        self.tail = node
        self.index += 1
            
        

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        # Find the element and keep a
        # reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        # Unlink it from the list
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node
    
    def count(self):
        """
        Counts the number of elements in the list.
        Takes O(n) time.
        """
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count
    
    def middle(self):
        """
        Finds the middle element of the list.
        If two, it uses the second. 
        Takes O(n) time. 
        N = number of nodes
        Takes O(1) space
        """
        fast = slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def popfirst(self):
        temp = self.head
        if self.head == None:
            return
        else: 
            self.head = temp.next
            temp = None
            return
    
    def deleteNode(self, position): 
        # If linked list is empty 
        if self.head == None: 
            return 
        # Store head node 
        temp = self.head 
        # If head needs to be removed 
        if position == 0: 
            self.head = temp.next
            temp = None
            return 
        # Find previous node of the node to be deleted 
        for i in range(position -1 ): 
            temp = temp.next
            if temp is None: 
                break
        # If position is more than number of nodes 
        if temp is None: 
            return 
        if temp.next is None: 
            return 
        # Node temp.next is the node to be deleted 
        # store pointer to the next of node to be deleted 
        next = temp.next.next
        # Unlink the node from linked list 
        temp.next = None
        temp.next = next 
    
    def get(self,index):
        curr = self.head
        count = 0
        while count < index:
            count += 1
            curr = curr.next
        return curr.data


            



ll = SinglyLinkedList()
ll.append('Here')
ll.append('is')
ll.append('some')
ll.append('test')
ll.append('text')

