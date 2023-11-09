""" List implementation. """

from abc import ABC, abstractmethod
from fixed_size_array import FixedSizeArray


class List[T](ABC):
    def __init__(self) -> None:
        """ Initialises the length of an empty list to be 0. """
        self.length = 0

    @abstractmethod
    def __setitem__(self, index: int, item: T) -> None:
        """ Sets the value of the element at position index to be item. """
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        """ Returns the value of the element at position index. """
        pass

    def __len__(self) -> int:
        """ Returns the length of the list. """
        return self.length

    @abstractmethod
    def is_full(self) -> bool:
        """ Returns True iff the list is full. """
        pass

    def is_empty(self) -> bool:
        """ Returns True iff the list is empty. """
        return len(self) == 0

    def clear(self):
        """ Sets the list back to empty. """
        self.length = 0

    @abstractmethod
    def insert(self, index: int, item: T) -> None:
        """ Insert an element at a specific index (with certain constraints) """
        pass

    def append(self, item: T) -> None:
        """ Adds the item to the end of the list. """
        self.insert(len(self), item)

    @abstractmethod
    def delete_at_index(self, index: int) -> T:
        """ Delete an element at a specific index (with certain constraints) and returns the element. """
        pass

    @abstractmethod
    def get_index(self, item: T) -> int:
        """ Returns the position of the first occurrence of item in the list. """
        pass

    def remove(self, item: T) -> None:
        """ Removes the first occurrence of the item from the list. """
        index = self.get_index(item)
        self.delete_at_index(index)

    def __str__(self) -> str:
        """ Returns the elements of the list in order as a string. """
        result = "["
        for i in range(len(self)):
            if i > 0:
                result += ', '
            result += str(self[i])
        result += ']'
        return result


class ArrayList[T](List[T]):
    """ 
    Implementation of a generic list with arrays.

    Attributes:
         length (int): number of elements in the list (inherited)\n
         array (FixedSizeArray[T]): array storing the elements of the list
    """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        List.__init__(self)
        self.array = FixedSizeArray(max(self.MIN_CAPACITY, max_capacity))

    def __getitem__(self, index: int) -> T:
        """ Returns the value of the element at an index. """
        return self.array[index]

    def __setitem__(self, index: int, value: T) -> None:
        """ Sets the value of the element at position index. """
        self.array[index] = value

    def __shuffle_right(self, index: int) -> None:
        """ Shuffles all the items to the right from index. """
        for i in range(len(self), index, -1):
            self.array[i] = self.array[i - 1]

    def __shuffle_left(self, index: int) -> None:
        """ Shuffles all the items to the left from index. """
        for i in range(index, len(self)):
            self.array[i] = self.array[i+1]

    def is_full(self):
        """ Returns true if the list is full. """
        return len(self) >= len(self.array)

    def get_index(self, item: T) -> int:
        """ Returns the position of the first occurrence of item. """
        for i in range(len(self)):
            if item == self[i]:
                return i
        raise ValueError("Item not in list")

    def delete_at_index(self, index: int) -> T:
        """ Deletes the element from index and move remaining elements to the left. """
        if index < 0 or index > len(self):
            raise IndexError("Out of bounds")
        item = self.array[index]
        self.length -= 1
        self.__shuffle_left(index)
        return item

    def insert(self, index: int, item: T) -> None:
        """ Moves element from index to the right by one position and inserts the element in index. """
        if self.is_full():
            raise Exception("List is full")
        self.__shuffle_right(index)
        self.array[index] = item
        self.length += 1

class SortedArrayList[T](ArrayList[T]):
    """ 
    Implementation of a sorted list with arrays.

    Attributes:
         length (int): number of elements in the list (inherited)\n
         array (FixedSizeArray[T]): array storing the elements of the list  (inherited)

    Note: This class is to take advantage on the binary search time complexity.
    """

    def __init__(self, max_capacity: int) -> None:
        super().__init__(max_capacity)

    def __setitem__(self, index: int, value: T) -> None:
        """ Sets the value of the element at position index and sorts the list. """
        super().__setitem__(index, value)
        self.array.sort()

    def get_index(self, item: T) -> int:
        """ Returns the position of the first occurrence of item. """
        self.binary_search(item)
    
    def insert(self, index: int, item: T) -> None:
        """ Moves element from index to the right by one position, insert the element in index and sort the list. """
        super().insert(index, item)
        self.array.sort()

    def binary_search(self, item: T) -> int:
        """ Does binary search on a sorted list. """
        low = 0
        high = len(self) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.array[mid] > item:
                high = mid - 1
            elif self.array[mid] == item:
                return mid
            else:
                low = mid + 1
        raise ValueError("Item not in list")


class Node[T]:
    def __init__(self, item: T = None) -> None:
        self.item = item
        self.link = None


class LinkListIterator[T]:
    """ 
    Implementation of a the methods to make LinkList iterable

    Attributes:
         current (Node[T]): the node whose item will be returned next
    """

    def __init__(self, node: Node[T]) -> None:
        """ Initialises self.current to the node given as input. """
        self.current = node

    def __iter__(self) -> 'LinkListIterator': # Forward reference type hint, the return in quotes. Ref: https://peps.python.org/pep-0484/#forward-references
        """ Returns itself, as required to be iterable. """
        return self

    def __next__(self) -> T:
        """ Returns the current item and moves to the next node """
        if self.current is not None:
            item = self.current.item
            self.current = self.current.link
            return item
        else:
            raise StopIteration


class LinkList[T](List[T]):
    """ 
    Implementation of a generic list with linked nodes.

    Attributes:
         length (int): number of elements in the list (inherited)
         head (Node[T]): node at the head of the list
    """

    def __init__(self) -> None:
        List.__init__(self)
        self.head = None

    def __iter__(self) -> LinkListIterator[T]:
        """ Computes and returns an iterator for the current list. """
        return LinkListIterator(self.head)

    def __setitem__(self, index: int, item: T) -> None:
        """ Sets the value of the element at position index to be item. """
        node_at_index = self.__get_node_at_index(index)
        node_at_index.item = item

    def __getitem__(self, index: int) -> T:
        """ Returns the value of the element at position index. """
        node_at_index = self.__get_node_at_index(index)
        return node_at_index.item

    def is_full(self):
        """ Returns true if the list is full. """
        return False

    def __get_node_at_index(self, index: int) -> Node[T]:
        """ Returns the node in the list at position index. """
        if 0 <= index < len(self):
            current = self.head
            for _ in range(index):
                current = current.link
            return current
        else:
            raise ValueError("Index out of bounds")

    def insert(self, index: int, item: T) -> None:
        """ Insert an item at a specific index position. """
        new_node = Node(item)
        if index == 0:
            new_node.link = self.head
            self.head = new_node
        else:
            previous_node = self.__get_node_at_index(index-1)
            new_node.link = previous_node.link
            previous_node.link = new_node
        self.length += 1

    def get_index(self, item: T) -> int:
        """ Returns the position of the first occurrence of item. """
        current = self.head
        index = 0
        while current is not None and current.item != item:
            current = current.link
            index += 1

        # After going through the link list, if not yet found, current will be None
        if current is None:
            raise ValueError("Item is not in list")
        else:
            return index

    def delete_at_index(self, index: int) -> T:
        """ Delete an element at the index position and returns the item. """
        try:
            previous_node = self.__get_node_at_index(index-1)
        except ValueError as e:
            if self.is_empty():
                raise ValueError("List is empty")
            elif index == 0:
                item = self.head.item
                self.head = self.head.link
            else:
                raise e
        else:
            item = previous_node.link.item
            previous_node.link = previous_node.link.link
        self.length -= 1
        return item

    def delete_negative(self):
        """ Deletes all nodes with a negative item. """
        previous = self.head
        for _ in range(1, self.length):  # delete negative nodes from index 1
            current = previous.link
            if current.item < 0:
                previous.link = current.link    # delete the node
                self.length -= 1
            else:
                previous = current              # move previous along

        if self.length > 0 and self.head.item < 0:  # check node at index 0
            self.head = self.head.link             # move the head
            self.length -= 1

    def clear(self):
        """ Clears the link list. """
        List.clear(self)
        self.head = None