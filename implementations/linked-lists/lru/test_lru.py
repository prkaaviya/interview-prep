"""test_lru.py"""
import pytest
from lru import (
    Node,
    LRUCache,
)


def test_initial_cache_node():
    node = Node(5, "kevin")

    assert node.key == 5
    assert node.value == "kevin"
    assert node.prev is None
    assert node.next is None

def test_initial_lru():
    capacity = 5
    lru = LRUCache(capacity)

    assert lru.get_cache_size() == 0
    assert lru.get_cache_capacity() == capacity
    assert lru._is_cache_empty()
    assert not lru._is_cache_full()

def test_put_lru():
    capacity = 5
    lru = LRUCache(capacity)

    lru.put(4, "david")
    lru.put(2, "alice")
    lru.put(7, "kevin")
    lru.put(3, "madison")
    lru.put(5, "jon")
    lru.display()

    lru.put(5, "kate")
    lru.display()

    lru.get(2)
    lru.display()

    lru.get(7)
    lru.display()


def test_get_lru():
    capacity = 2
    lru = LRUCache(capacity)

    lru.put(4, "david")
    lru.put(2, "alice")

    assert lru.get(2) == "alice"
    assert lru.get(3) == -1