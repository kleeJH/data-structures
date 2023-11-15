""" Array-based Set implementation. """

from __future__ import annotations
from set import *
from fixed_size_array import FixedSizeArray

class ArrayBasedSet[T](Set[T]):
    """Simple array-based implementation.

    Attributes:
        - size (int): number of elements in the set
        - array (FixedSizeArray[T]): array storing the elements of the set
    """

    MIN_CAPACITY = 1

    def __init__(self, capacity: int = 1) -> None:
        Set.__init__(self)
        self.array = FixedSizeArray(max(self.MIN_CAPACITY, capacity))
        pass

    def __len__(self) -> int:
        """ Returns the number of elements in the set. """
        return self.size

    def is_empty(self) -> bool:
        """ True if the set is empty. """
        return len(self) == 0

    def __contains__(self, item: T) -> bool:
        """ True if the set contains the item. """
        for i in range(self.size):
            if item == self.array[i]:
                return True
        return False

    def clear(self) -> None:
        """ Makes the set empty. """
        self.size = 0

    def is_full(self) -> bool:
        """ True if the set is full and no element can be added. """
        return len(self) == len(self.array)

    def add(self, item: T) -> None:
        """ Adds an element to the set. """
        if self.is_full():
            raise Exception("Set is full")
        elif item not in self:
            self.array[self.size] = item
            self.size += 1

    def remove(self, item: T) -> None:
        """ Removes an element from the set. """
        if item not in self:
            raise KeyError("Item is not found")
        else:
            # Find the item, then shifts left to fill up empty space
            for i in range(len(self)):
                if self.array[i] == item:
                    self.array[i] = self.array[self.size - 1]
                    self.size -= 1
                    break

    def union(self, other: ArrayBasedSet[T]) -> ArrayBasedSet[T]:
        """ 
        Creates a new set equal to the union with another one.
        The new set should contains the elements of `self` and `other`.
        """
        maxcapacity = len(self.array) + len(other.array)
        res = ArrayBasedSet(maxcapacity)
        for the_set in [self, other]:
            for i in range(len(the_set)):
                res.add(the_set.array[i])
        return res

    def intersection(self, other: ArrayBasedSet[T]) -> ArrayBasedSet[T]:
        """ 
        Creates a new set equal to the intersection with another one.
        The new set should contain the elements that are both in `self` and `other`.
        """
        res = ArrayBasedSet(min(len(self), len(other)))
        for i in range(len(self)):
            if self.array[i] in other:
                res.add(self.array[i])
        return res

    def difference(self, other: ArrayBasedSet[T]) -> ArrayBasedSet[T]:
        """ 
        Creates a new set equal to the difference with another one.
        The new set should contain the elements of `self` that are not in `other`.
        """
        res = ArrayBasedSet(len(self))
        for i in range(len(self)):
            if self.array[i] not in other:
                res.add(self.array[i])
        return res