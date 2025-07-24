"""stack.py"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def peek(self):
        return self.head.value if self.head else None

    def display(self):
        current = self.head
        while current:
            print(f"{current.value} ->", end=" ")
            current = current.next
        print("None")

    def pop(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

    def is_empty(self):
        return self.head is None

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
