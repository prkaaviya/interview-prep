"""lru.py"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"\"node_value: {self.value}\""


class LRUCache:
    """LRUCache implementation."""

    def __init__(self, capacity):
        self._capacity = capacity
        self._cache = {}
        self._cache_head = None
        self._cache_tail = None

    def _is_cache_empty(self):
        return not len(self._cache)

    def _is_cache_full(self):
        return len(self._cache) == self._capacity

    def _remove_node(self, node):
        """Removes a node."""
        if node.prev:
            node.prev.next = node.next
        else:
            self._cache_head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self._cache_tail = node.prev

        node.next = node.prev = None

    def _append_node_to_tail(self, node):
        """Adds a node to the tail (most recently used)."""
        if not self._cache_tail:
            self._cache_head = self._cache_tail = node
            return

        self._cache_tail.next = node
        node.prev = self._cache_tail
        self._cache_tail = node

    def display(self):
        print("From head")
        current = self._cache_head
        while current:
            print(f"{current.key, current.value} ->", end=" ")
            current = current.next
        print("None")

    def get_cache_size(self):
        size = 0
        current = self._cache_head
        while current:
            size += 1
            current = current.next
        return size

    def get_cache_capacity(self):
        return self._capacity

    def put(self, key, value):
        if key in self._cache:
            node = self._cache[key]
            node.value = value
            self._remove_node(node)
            self._append_node_to_tail(node)
        else:
            if self._is_cache_full():
                lru_node = self._cache_head
                self._remove_node(lru_node)
                del self._cache[lru_node.key]

            new_node = Node(key, value)
            self._append_node_to_tail(new_node)
            self._cache[key] = new_node

    def get(self, key):
        if key not in self._cache:
            return -1

        node = self._cache[key]
        self._remove_node(node)
        self._append_node_to_tail(node)
        return node.value
