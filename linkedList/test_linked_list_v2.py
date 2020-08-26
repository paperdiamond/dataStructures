from linked_list_v2 import *

def test_start():
    lst = SinglyLinkedList()
    lst.append('Fantastic')
    assert lst.count() == 1

def test_append():
    lst = SinglyLinkedList()
    lst.append('Fantastic')
    lst.append('105')
    lst.append(105)

def test_prepend():
    lst = SinglyLinkedList()
    lst.prepend(23)
    lst.prepend('Word choice')
    lst.prepend('150')
    lst.prepend(1000)

def test_count():
    lst = SinglyLinkedList()
    lst.append('Fantastic')
    lst.append('105')
    lst.append(105)
    lst.count()

def test_reverse():
    lst = SinglyLinkedList()
    lst.append('Fantastic')
    lst.append('105')
    lst.append(105)
    lst.reverse()

def test_find():
    lst = SinglyLinkedList()
    lst.append('Fantastic')
    lst.append('105')
    lst.append(105)
    lst.find('105')
