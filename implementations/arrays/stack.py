"""stack.py"""
import sys

def log_stack_operation(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        print(f"[{func.__name__.upper()}] stack: {self._data}")
        return result
    return wrapper

class Stack:
    def __init__(self):
        self._data = []

    @log_stack_operation
    def push(self, *item):
        for s in item:
            self._data.append(s)

    @log_stack_operation
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    @log_stack_operation
    def peek(self):
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._data[-1]

    def is_empty(self):
        return not self._data

    @log_stack_operation
    def reset(self):
        self._data = []

    def length(self):
        return len(self._data)

    def __str__(self):
        return f"stack: {self._data}"

    def __eq__(self, other):
        return self._data == other._data

    def __hash__(self):
        return hash(tuple(self._data))


stack = Stack()

try:
    stack.peek()
except IndexError as e:
    print(f"Caught exception: {str(e)}, moving on...")

try:
    stack.pop()
except IndexError as e:
    print(f"Caught exception: {str(e)}, moving on...")

stack.push(6, 9, 7, 3, 1, 8, 10)

stack2 = Stack()
stack2.push(6, 9, 7, 3, 1, 8, 10)

print(id(stack) == id(stack2))
print(stack is stack2)
print(stack == stack2)

stack3 = stack
print(stack is stack3)

print(sys.getsizeof(stack), sys.getsizeof(stack2))
print(sys.getrefcount(stack), sys.getrefcount(stack2))

my_set = {stack, stack2}
print(len(my_set))

stack2.pop()
stack.reset()
print(stack.is_empty())