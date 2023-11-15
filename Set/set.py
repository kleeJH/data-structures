""" Set Implementation. """

from __future__ import annotations

from abc import ABC, abstractmethod

class Set[T](ABC):
    def __init__(self) -> None:
        self.clear()

    @abstractmethod
    def __len__(self) -> int:
        """ Returns the number of elements in the set. """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """ True if the set is empty. """
        pass

    @abstractmethod
    def clear(self) -> None:
        """ Makes the set empty. """
        pass

    @abstractmethod
    def __contains__(self, item: T) -> bool:
        """ True if the set contains the item. """
        pass

    @abstractmethod
    def add(self, item: T) -> None:
        """ Adds an element to the set. """
        pass

    @abstractmethod
    def remove(self, item: T) -> None:
        """ Removes an element from the set.  """
        pass

    @abstractmethod
    def union(self, other: Set[T]) -> Set[T]:
        """ Makes a union of the set with another set. """
        pass

    @abstractmethod
    def intersection(self, other: Set[T]) -> Set[T]:
        """ Makes an intersection of the set with another set. """
        pass

    @abstractmethod
    def difference(self, other: Set[T]) -> Set[T]:
        """ Creates a difference of the set with another set. """
        pass
