import sys
sys.path.append("./refactor/")
from doubly_linked_list import *


def test_add_element():
    assert str(Node(1)) == '(1, None)'


def test_create_doubly_linked_list():
    """Create a test function for building a sample DoublyLinkedList"""
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    assert str(dL) == "(0, (1, (2, (3, ('Trailer', None)))))"  # Adjust the expected string representation


def test_size_method():
    """Test the size method"""
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    assert dL.size() == 4


def test_is_empty_method():
    """Test the is_empty method"""
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    assert not dL.is_empty()

    dL2 = DoublyLinkedList()
    assert dL2.is_empty()


def test_get_first_and_get_last_methods():
    """ Test the get_first and get_last methods"""
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    assert str(dL.get_first()) == "(0, (1, (2, (3, ('Trailer', None)))))"
    assert str(dL.get_last()) == "(3, ('Trailer', None))"


def test_get_previous():
    """ Test  get_previous """
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    assert str(dL.get_last().get_previous()) == "(2, (3, ('Trailer', None)))"


def test_get_next():
    """Test  get_next method"""
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    assert str(dL.get_first().get_next()) == "(1, (2, (3, ('Trailer', None))))"


def test_remove_method():
    """ Test the remove method"""
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    dL.remove(dL.get_first())
    assert dL.get_first().get_element() == 1


def test_map_method():
    """ Test the map method """
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    dL.map(lambda x: x ** 2)
    assert str(dL) == "(0, (1, (4, (9, ('Trailer', None)))))"


# Test the add_before and add_after methods
def test_add_before_and_add_after_methods():
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    dL.add_after(Node(42), dL.get_first())
    dL.add_before(Node(34), dL.get_last())
    assert str(dL) == "(0, (42, (1, (2, (34, (3, ('Trailer', None))))))"


def test_get_first():
    """ Test the get_first method"""
    lst = DoublyLinkedList()
    lst.add_first(Node(10))
    node = lst.get_first()
    assert node.get_element() == 10


def test_get_last(self):
    """ Test the get_last_method"""
    list = DoublyLinkedList()
    list.add_last(Node(10))
    node = list.get_last()
    assert node.get_element() == 10


