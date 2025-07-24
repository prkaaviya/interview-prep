"""test_queue.py"""
from queue import (
    Node,
    Queue,
)

def test_init_node():
    node = Node(5)

    assert node.value == 5
    assert node.next is None

def test_init_queue():
    ll = Queue()

    assert ll.head is None
    assert ll.tail is None

def test_enqueue_queue():
    ll = Queue()

    ll.enqueue(5)
    ll.enqueue(9)
    ll.enqueue(3)
    ll.enqueue(8)

    assert ll.head.value == 5
    assert ll.tail.value == 8

def test_dequeue_queue():
    ll = Queue()

    ll.enqueue(5)
    ll.enqueue(9)
    ll.enqueue(3)
    ll.enqueue(8)

    assert ll.dequeue() == 5
    assert ll.dequeue() == 9

def test_full_dequeue_queue():
    ll = Queue()

    ll.enqueue(5)
    ll.enqueue(9)
    ll.enqueue(3)
    ll.enqueue(8)

    assert ll.dequeue() == 5
    assert ll.dequeue() == 9
    assert ll.dequeue() == 3
    assert ll.dequeue() == 8
    assert ll.head is None
    assert ll.tail is None

def test_display_queue():
    ll = Queue()

    ll.enqueue(5)
    ll.enqueue(9)
    ll.enqueue(3)
    ll.enqueue(8)

    ll.display()

def test_peek_queue():
    ll = Queue()

    ll.enqueue(7)
    ll.enqueue(9)
    ll.enqueue(8)

    assert ll.peek() == 7

def test_empty_queue():
    ll = Queue()

    assert ll.is_empty()

def test_not_empty_queue():
    ll = Queue()

    ll.enqueue(5)

    assert ll.is_empty() is False

    ll.dequeue()

    assert ll.is_empty()

def test_get_length_queue():
    ll = Queue()

    assert ll.get_length() == 0

    ll.enqueue(5)
    ll.enqueue(9)
    ll.enqueue(3)
    ll.enqueue(8)

    assert ll.get_length() == 4
