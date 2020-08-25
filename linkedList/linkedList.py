# Code adapted from Udacity Data Structures Course

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    # def __repr__(self):
        # return self.data

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def iterate(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def append(self, new_node):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def get_index(self, index):
        counter = 1
        current = self.head
        if index < 1:
            return None
        while current and counter <= index:
            if counter == index:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_node, index):
        counter = 1
        current = self.head
        if index > 1:
            while current and counter < index:
                if counter == index - 1:
                    new_node.next = current.next
                    current.next = new_node
                current = current.next
                counter += 1
        elif index == 1:
            new_node.next = self.head
            self.head = new_node
    
    # def delete(self, value):
    #     current =self.head
    #     next = current.next
    #     current.value = next.value
    #     current.next = next.next

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
    
    def count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def printit(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def print_index(self, search_value):
        current = self.head
        count = 0
        while current.value != search_value:
            current = current.next
            count += 1
        if current.value == search_value:
            print(count)




# Test cases Set up some Elements
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)


# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_index
# Should print 3
# print(ll.head.next.next.value)
# Should also print 3
# print(ll.get_index(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
# print(ll.get_index(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
# print(ll.get_index(1).value)
# Should print 4 now
# print(ll.get_index(2).value)
# Should print 3 now
# print(ll.get_index(3).value)
e5 = Node(276)
ll.append(e5)
# print(ll.count())