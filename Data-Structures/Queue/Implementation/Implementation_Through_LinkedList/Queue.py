import threading
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
    def enqueue(self , data: T):





