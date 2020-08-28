from linked_list_v2 import *

lst = SinglyLinkedList()
lst.prepend(23)
lst.prepend('Word choice')
lst.prepend('150')
lst.prepend(1000)

def test_append():
    lst.append('Fantastic')
    lst.append('105')
    lst.append(105)

def test_prepend():
    lst.prepend(23)
    lst.prepend('Word choice')
    lst.prepend('150')
    lst.prepend(1000)

def test_count():
    lst.count()

def test_reverse():
    lst.reverse()

def test_find():
    lst.find('105')


def test_middle():
    lst.middle()