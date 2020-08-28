from stack_udacity_quiz import *
# Test cases

# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
def test_push():
    stack.push(e2)
    stack.push(e3)

def test_pop():
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop())
