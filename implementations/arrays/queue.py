"""queue.py"""

def log_queue_operation(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        print(f"queue after {func.__name__.upper()}: {self._data}")
        return result
    return wrapper


class Queue:
    def __init__(self):
        self._data = []

    def __str__(self):
        return f"queue: {self._data}"

    @log_queue_operation
    def insert(self, *item):
        for s in item:
            self._data.append(s)

    @log_queue_operation
    def remove(self):
        if self.is_empty():
            raise IndexError("remove from empty queue")
        item = self._data.pop(0)
        return item

    @log_queue_operation
    def reset(self):
        self._data = []

    def is_empty(self):
        return not self._data

queue = Queue()

try:
    print(queue.remove())
except IndexError as e:
    print(f"Caught exception: {str(e)}, moving on...")

queue.insert(2, 7, 3, 4)
queue.insert(10, 1, 5, 18, 6)

print(queue.remove())

queue.reset()

print(queue.is_empty())
