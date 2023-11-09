""" Stack implementation."""

from abc import ABC, abstractmethod
from fixed_size_array import FixedSizeArray


class Stack[T](ABC):
    def __init__(self) -> None:
        self.length = 0

    @abstractmethod
    def push(self, item: T) -> None:
        """ Pushes an element to the top of the stack. """
        pass

    @abstractmethod
    def pop(self) -> T:
        """ Pops an element from the top of the stack. """
        pass

    @abstractmethod
    def peek(self) -> T:
        """ Pops the element at the top of the stack. """
        pass

    def __len__(self) -> int:
        """ Returns the number of elements in the stack. """
        return self.length

    def is_empty(self) -> bool:
        """ True if the stack is empty. """
        return len(self) == 0

    @abstractmethod
    def is_full(self) -> bool:
        """ True if the stack is full and no element can be pushed. """
        pass

    def clear(self):
        """ Clears all elements from the stack. """
        self.length = 0


class ArrayStack[T](Stack[T]):
    """ Implementation of a stack with arrays.
    
    Attributes:
        - length (int): number of elements in the stack (inherited)
        - array (FixedSizeArray[T]): array storing the elements of the queue

    NOTE: Stack requires a capacity of ONE
    """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        """ 
        Initialises the length and the array with the given capacity.
        If max_capacity is 0, the array is created with MIN_CAPACITY.
        """
        Stack.__init__(self)
        self.array = FixedSizeArray(max(self.MIN_CAPACITY, max_capacity))
        
    def is_full(self) -> bool:
        """ True if the stack is full and no element can be pushed. """
        return len(self) == len(self.array)

    def push(self, item: T) -> None:
        """ Pushes an element to the top of the stack. """
        if self.is_full():
            raise Exception("Stack is full")
        self.array[len(self)] = item
        self.length += 1

    def pop(self) -> T:
        """ Pops the element at the top of the stack. """
        if self.is_empty():
            raise Exception("Stack is empty")
        self.length -= 1
        return self.array[self.length]

    def peek(self) -> T:
        """ Returns the element at the top, without popping it from stack. """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.array[self.length-1]
 
    def __str__(self) -> str:
        """ Returns the elements of the stack (from top to bottom) as a string. """
        length = len(self)
        if length > 0:
            output = str(self.array[length-1])
            for i in range(length-2, -1, -1):
                output += ", " + str(self.array[i])
        else:
            output = ""
        return output


class Node[T]:
    def __init__(self, item: T = None) -> None:
        self.item = item
        self.link = None


class LinkStack[T](Stack[T]):
    """ Implementation of a stack with linked nodes.

    Attributes:
        - length (int): number of elements in the stack (inherited)
    """

    def __init__(self, _=None) -> None:
        Stack.__init__(self)
        self.top = None

    def clear(self) -> None:
        """" Clears all elements from the stack. """
        super().clear()
        self.top = None

    def is_empty(self) -> bool:
        """ Returns whether the stack is empty. """
        return self.top is None

    def is_full(self) -> bool:
        """ Returns whether the stack is full. """
        return False

    def push(self, item: T) -> None:
        """ Pushes an element to the top of the stack. """
        new_node = Node(item)
        new_node.link = self.top
        self.top = new_node
        self.length += 1

    def pop(self) -> T:
        """ Pops the element at the top of the stack. """
        if self.is_empty():
            raise Exception("Stack is empty")

        item = self.top.item
        self.top = self.top.link
        self.length -= 1
        return item

    def peek(self) -> T:
        """ Returns the element at the top, without popping it from stack. """
        if self.is_empty(self):
            raise Exception("Stack is empty")
        return self.top.item

    def __str__(self) -> str:
        """ Returns the elements of the stack (from top to bottom) as a string. """
        current = self.top
        output = ''
        while current is not None:
            if output != '':
                output += ', '
            output += str(current.item)
            current = current.link

        return output