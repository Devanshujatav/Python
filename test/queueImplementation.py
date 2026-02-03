import threading
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


# Node class (same logic as Java)
class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional["Node[T]"] = None


class Queue(Generic[T]):

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")

        self.capacity = capacity
        self.front: Optional[Node[T]] = None
        self.rear: Optional[Node[T]] = None
        self._size = 0

        # Lock for thread safety
        self.lock = threading.Lock()

        # Conditions for blocking behavior
        self.not_empty = threading.Condition(self.lock)
        self.not_full = threading.Condition(self.lock)

    # Enqueue (Producer)
    def enqueue(self, data: T) -> None:
        if data is None:
            raise ValueError("Null values are not allowed")

        with self.lock:
            # Wait if queue is full
            while self._size == self.capacity:
                self.not_full.wait()

            new_node = Node(data)

            if self.is_empty():
                self.front = self.rear = new_node
            else:
                assert self.rear is not None
                self.rear.next = new_node
                self.rear = new_node

            self._size += 1

            # Signal that queue is no longer empty
            self.not_empty.notify()

    # Dequeue (Consumer)
    def dequeue(self) -> T:
        with self.lock:
            # Wait if queue is empty
            while self.is_empty():
                self.not_empty.wait()

            assert self.front is not None
            data = self.front.data
            self.front = self.front.next

            if self.front is None:
                self.rear = None

            self._size -= 1

            # Signal that queue has space now
            self.not_full.notify()

            return data

    def peek(self) -> T:
        with self.lock:
            if self.is_empty():
                raise IndexError("Queue is Empty")
            assert self.front is not None
            return self.front.data

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        with self.lock:
            return self._size

    def clear(self) -> None:
        with self.lock:
            self.front = self.rear = None
            self._size = 0
            self.not_full.notify_all()
