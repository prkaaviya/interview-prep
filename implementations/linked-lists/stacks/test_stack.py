"""test_stack.py"""
from stack import (
    Node,
    Stack,
)

def test_initial_node():
    node = Node(5)

    assert node.value == 5

def test_initial_stack():
    ll = Stack()

    assert ll.head == None

def test_push_stack():
    ll = Stack()

    ll.push(9)
    ll.push(5)
    ll.push(8)
    ll.push(2)

    assert ll.head.value == 2

def test_peek_stack():
    ll = Stack()

    ll.push(3)
    ll.push(1)
    ll.push(6)

    assert ll.peek() == 6

def test_peek_empty_stack():
    ll = Stack()

    assert ll.peek() is None

def test_display_stack():
    ll = Stack()

    ll.push(7)
    ll.push(10)
    ll.push(2)

    ll.display()

def test_pop_stack():
    ll = Stack()

    ll.push(13)
    ll.push(4)
    ll.push(9)

    assert ll.pop() == 9
    assert ll.pop() == 4

def test_pop_empty_stack():
    ll = Stack()

    assert ll.pop() is None

def test_empty_stack():
    ll = Stack()

    assert ll.is_empty()

def test_not_empty_stack():
    ll = Stack()

    ll.push(9)

    assert ll.is_empty() is False

def test_get_length_stack():
    ll = Stack()

    ll.push(4)
    ll.push(3)
    ll.push(10)
    ll.push(7)
    ll.push(15)
    ll.push(6)
    ll.push(8)

    assert ll.get_length() == 7

    ll.pop()

    assert ll.get_length() == 6