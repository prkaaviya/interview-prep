"""queue.py"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.head: # queue is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if not self.head: # queue is empty
            return None
        value = self.head.value
        self.head = self.head.next
        if not self.head: # queue became empty
            self.tail = None
        return value

    def display(self):
        current = self.head
        while current:
            print(f"{current.value} ->", end=" ")
            current = current.next
        print("None")

    def peek(self):
        return self.head.value if self.head else None

    def is_empty(self):
        return self.head is None

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next

        return count
