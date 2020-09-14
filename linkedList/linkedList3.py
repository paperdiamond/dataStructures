# Code originally created by @Bizdak for Auckland Data Structure and & Algo group
# One of the biggest advantage of a linkedlist is the ability to insert random data in the chain
# I added a repr, middle, 
# Pop_last is not emptying the repr list

class LinkedList:

    class Node:
        def __init__(self, data):
            self.next = None
            self.prev = None
            self.data = data
        
        def __repr__(self):
            return repr(self.data)

    class Iter:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node is None:
                raise StopIteration()
            data = self.node.data
            self.node = self.node.next
            return data

    def __iter__(self):
        return LinkedList.Iter(self.head)

    def __init__(self):
        self.head, self.tail = None, None
        self.len = 0  # keep track, expensive to traverse for length

    def __len__(self):
        return self.len
    
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

    def append(self, data):
        node = LinkedList.Node(data)
        if self.tail is None:
            assert(self.head is None)
            self.head = self.tail = node
        else:
            self.tail.next, node.prev = node, self.tail
            self.tail = node
        self.len += 1

    def prepend(self, data):
        node = LinkedList.Node(data)
        if self.head is None:
            assert(self.tail is None)
            self.head = self.tail = node
        else:
            self.head.prev, node.next = node, self.head
            self.head = node
        self.len += 1

    def pop_first(self):
        if self.head is None:
            raise IndexError()
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        self.len -= 1
        return data

    def pop_last(self):
        if self.tail is None:
            raise IndexError()
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        self.len -= 1
        return data

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


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.prepend(4)
    ll.prepend(3)
#     for n in ll:
#         print(n)
#     print("len: %d" % len(ll))
#     print("pop_first: %d" % ll.pop_first())
#     print("pop_last: %d" % ll.pop_last())
#     print("len: %d" % len(ll))
#     for n in ll:
#         print(n)
#     ll.pop_last()
#     ll.pop_last()
#     print("len: %d" % len(ll))
#     ll.pop_last()
#     print("len: %d" % len(ll))
#     ll.pop_last()