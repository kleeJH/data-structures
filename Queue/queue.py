""" Queue implementation. """

from abc import ABC, abstractmethod
from fixed_size_array import FixedSizeArray


class Queue[T](ABC):
    """ Abstract class for a generic Queue. """

    def __init__(self) -> None:
        self.length = 0

    @abstractmethod
    def append(self, item: T) -> None:
        """ Adds an element to the rear of the queue. """
        pass

    @abstractmethod
    def serve(self) -> T:
        """ Deletes and returns the element at the queue's front. """
        pass

    def __len__(self) -> int:
        """ Returns the number of elements in the queue. """
        return self.length

    def is_empty(self) -> bool:
        """ True if the queue is empty. """
        return len(self) == 0

    @abstractmethod
    def is_full(self) -> bool:
        """ True if the stack is full and no element can be pushed. """
        pass

    def clear(self):
        """ Clears all elements from the queue. """
        self.length = 0


class LinearQueue[T](Queue[T]):
    """ 
    Linear implementation of a queue with arrays.

    Attributes:
        - length (int): number of elements in the queue (inherited)
        - front (int): index of the element at the front of the queue
        - rear (int): index of the first empty space at the back of the queue
        - array (FixedSizeArray[T]): array storing the elements of the queue
    """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        Queue.__init__(self)
        self.front = 0
        self.rear = 0
        self.array = FixedSizeArray(max(self.MIN_CAPACITY, max_capacity))

    def append(self, item: T) -> None:
        """ Adds an element to the rear of the queue. """
        if self.is_full():
            raise Exception("Queue is full")

        self.array[self.rear] = item
        self.length += 1
        self.rear += 1

    def serve(self) -> T:
        """ Deletes and returns the element at the queue's front. """
        if self.is_empty():
            raise Exception("Queue is empty")

        self.length -= 1
        item = self.array[self.front]
        self.front += 1
        return item

    def clear(self):
        """ Clears all elements from the queue. """
        super().clear()
        self.front = 0
        self.rear = 0

    def is_full(self) -> bool:
        """ True if the queue is full and no element can be appended. """
        return self.rear == len(self.array)

    def __str__(self) -> str:
        """ Returns the elements of the queue (from left to right) as a string. """
        if self.is_empty():
            return ""
        else:
            result = "["
            for i in range(self.front, self.rear):
                if i >= self.front:
                    result += ', '
                result += str(self.array[i])
            result += ']'
            return result


class CircularQueue[T](Queue[T]):
    """ Circular implementation of a queue with arrays.

    Attributes:
        - length (int): number of elements in the queue (inherited)
        - front (int): index of the element at the front of the queue
        - rear (int): index of the first empty space at the back of the queue
        - array (FixedSizeArray[T]): array storing the elements of the queue
    """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        Queue.__init__(self)
        self.front = 0
        self.rear = 0
        self.array = FixedSizeArray(max(self.MIN_CAPACITY, max_capacity))

    def append(self, item: T) -> None:
        """ Adds an element to the rear of the queue. """
        if self.is_full():
            raise Exception("Queue is full")

        self.array[self.rear] = item
        self.length += 1
        self.rear = (self.rear + 1) % len(self.array)

    def serve(self) -> T:
        """ Deletes and returns the element at the queue's front. """
        if self.is_empty():
            raise Exception("Queue is empty")

        self.length -= 1
        item = self.array[self.front]
        self.front = (self.front + 1) % len(self.array)
        return item

    def is_full(self) -> T:
        """ True if the queue is full and no element can be appended. """
        return len(self) == len(self.array)

    def clear(self) -> None:
        """ Clears all elements from the queue. """
        Queue.__init__(self)
        self.front = 0
        self.rear = 0

    def __str__(self) -> str:
        """ Returns the elements of the queue (from left to right) as a string. """
        length = len(self)
        if length > 0:
            index = self.front
            output = str(self.array[index])
            for _ in range(len(self)-1):
                index = (index + 1) % len(self.array)
                output += ", " + str(self.array[index])
        else:
            output = ""
        return output


class Node[T]:
    def __init__(self, item: T = None) -> None:
        self.item = item
        self.next = None


class LinkQueue[T](Queue[T]):
    """
    Linked implementation of a queue with nodes.

    Attributes:
        - length (int): number of elements in the linked queue (inherited)
        - front (int): reference to the front node (None represents an empty queue)
        - rear (int): reference to the rear node (None represents an empty queue)
    """

    def __init__(self, _=None) -> None:
        Queue.__init__(self)
        self.front = None
        self.rear = None

    def clear(self) -> None:
        """ Clears the queue. """
        super().clear()
        self.front = None
        self.rear = None

    def is_full(self) -> bool:
        """ Returns true if the list is full. LinkQueue will never be full. """
        return False

    def append(self, item: T) -> None:
        """ Adds an element to the rear of the queue. """
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.length += 1

    def serve(self) -> T:
        """ Deletes and returns the element at the queue's front. """
        if self.is_empty():
            raise Exception("Queue is empty")

        temp = self.front.item
        self.front = self.front.next
        self.length -= 1
        if self.is_empty():
            self.rear = None
        return temp

    def __str__(self) -> str:
        """ Returns the elements of the queue (from left to right) as a string. """
        result = ""
        node = self.front
        while node is not None:
            result += str(node.item) + ", "
            node = node.next

        return result
