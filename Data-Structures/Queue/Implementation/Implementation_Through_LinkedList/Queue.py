import threading
from enum import nonmember
from typing import Generic , TypeVar , Optional

T = TypeVar("T")

# Node Class
class Node(Generic[T]):
    def __init__(self , data: T):
        self.data: T = data
        self.next: Optional["Node[T]"] = None


class Queue(Generic[T]):
    def __init__(self , capcity: int):
        if capcity <= 0:
            raise ValueError("value should be greater than zero")

        self.capacity = capcity
        self.front: Optional["Node[T]"] = None
        self.rear: Optional["Node[T]"] = None
        self._size = 0

        # Lock for thread safety
        self.Lock = threading.Lock()

        # Conditions for Blocking Behaviour
        self.not_empty = threading.Condition(self.Lock)
        self.not_full = threading.Condition(self.Lock)


    # Enqueue : Producer
    def enqueue(self , data: T) -> None:
        if data is None:
            raise ValueError("Values are not allowed")

        with self.Lock:
            # Wait if queue is full
            while self._size == self.capacity:
                self.not_full.wait()

            new_node = Node(data)

            if self.is_Empty():
                self.front = self.rear = new_node
            else:
                assert self.rear is None
                self.rear.next = new_node
                self.rear = new_node

            self._size += 1

            # Signal that queue is not empty
            self.not_empty.notify()


    # Dequeue (Consumer)
    def dequeue(self) -> T:
        with self.Lock:

            # Wait if queue is empty
            while self.is_empty():
                self.not_empty.wait()

            assert self.front is not None

            data = self.front.data

            front = self.front.next

            if self.front is None:
                self.rear = None

            self._size -= 1

            # Signal that queue has space now
            self.not_empty.notify()

            return data

    def peek(self) -> T:
        with (self.Lock):
            if self.is_Empty():
                raise IndexError("Queue is Empty")

            assert self.front is not None

            return self.front.data


    def is_empty(self) -> bool:
        return self._size == 0

    def size(self):
        with self.Lock:
            return self._size

    def clear(self):
        with self.Lock:
            self.front = self.rear = None
            self._size = 0
            self.not_full.notify_all()

            











