""" Heap Implementation. """

from fixed_size_array import FixedSizeArray
from collections.abc import Sequence
from abc import ABC, abstractmethod


class Heap[T](ABC):
    MIN_CAPACITY = 1

    def __init__(self, max_size: int = MIN_CAPACITY) -> None:
        self.length = 0
        # Add +1 in the array for readability
        self.the_array = FixedSizeArray(max(self.MIN_CAPACITY, max_size) + 1)

    def __len__(self) -> int:
        return self.length

    def is_full(self) -> bool:
        return self.length + 1 == len(self.the_array)

    def swap(self, i: int, j: int) -> None:
        """ Swap the element of index i and index j around. """
        temp_i = self.the_array[i]
        self.the_array[i] = self.the_array[j]
        self.the_array[j] = temp_i

    @abstractmethod
    def rise(self, k: int) -> None:
        """ Raise element at index k to its correct position. """
        pass

    def add(self, element: T) -> bool:
        """ Add an element in to the Heap. `rise` function is used in conjunction with `add` to swap and raise element. """
        has_space_left = not self.is_full()

        if has_space_left:
            self.length += 1
            self.the_array[self.length] = element
            self.rise(self.length)

        return has_space_left

    @abstractmethod
    def rise2(self, k: int, element: T) -> int:
        """ Raise element at index k to its correct position. """
        pass

    def add2(self, element: T) -> bool:
        """ Add an element in to the Heap. This alternative implementation shuffles the items down the heap using `rise2` and adds the new item in it's correct position at the end. """
        has_space_left = not self.is_full()
        if has_space_left:
            self.length += 1
            self.the_array[self.rise2(self.length, element)] = element
        return has_space_left

    @abstractmethod
    def priotized_child(self, k: int) -> int:
        """ Returns the index of the priotized child of k. """
        pass

    @abstractmethod
    def sink(self, k: int) -> None:
        """ Make the element at index k sink to the correct position. """
        pass

    def get_most_priotized(self) -> int:
        " Get the priotized element from the heap. "
        temp_priotized = self.the_array[1]
        # Swap root and last available node
        self.the_array[1] = self.the_array[len(self)]
        self.length -= 1
        self.sink(1)
        return temp_priotized

    def create_heap(self, max_size: int, an_array: Sequence = None) -> None:
        """ Bottom-up heap construction. Create the heap by heap-ordering each parent (from the bottom up) using a given array. It makes initialization of heap faster. """
        self.the_array = FixedSizeArray(
            max(len(an_array), max_size, self.MIN_CAPACITY) + 1)
        self.length = len(an_array)

        if an_array is not None:
            # Copy an_array to self.the_array (shift by 1 for readability)
            for i in range(len(an_array)):
                self.the_array[i+1] = an_array[i]

            # Heapify every parent
            for i in range(max_size//2, 0, -1):
                self.sink(i)


class MaxHeap[T](Heap[T]):

    def rise(self, k: int) -> None:
        """ Raise element at index k to its correct position. """
        while k > 1 and self.the_array[k] > self.the_array[k // 2]:
            self.swap(k, k // 2)
            k = k // 2

    def rise2(self, k: int, element: T) -> int:
        """ Raise element at index k to its correct position. """
        while k > 1 and element > self.the_array[k // 2]:
            self.the_array[k] = self.the_array[k // 2]
            k = k//2
        return k

    def priotized_child(self, k: int) -> int:
        """ Returns the index of the largest child of k. """
        if 2 * k == self.length or self.the_array[2 * k] > self.the_array[2 * k + 1]:
            return 2*k
        else:
            return 2*k+1

    def sink(self, k: int) -> None:
        """ Make the element at index k sink to the correct position. """
        while 2*k <= self.length:
            child = self.priotized_child(k)
            if self.the_array[k] >= self.the_array[child]:
                break
            self.swap(child, k)
            k = child


class MinHeap[T](Heap[T]):

    def rise(self, k: int) -> None:
        """ Raise element at index k to its correct position. """
        while k > 1 and self.the_array[k] < self.the_array[k // 2]:
            self.swap(k, k // 2)
            k = k // 2

    def rise2(self, k: int, element: T) -> int:
        """ Raise element at index k to its correct position. """
        while k > 1 and element < self.the_array[k // 2]:
            self.the_array[k] = self.the_array[k // 2]
            k = k//2
        return k

    def priotized_child(self, k: int) -> int:
        """ Returns the index of the smallest child of k. """
        if 2 * k == self.length or self.the_array[2 * k] < self.the_array[2 * k + 1]:
            return 2*k
        else:
            return 2*k+1

    def sink(self, k: int) -> None:
        """ Make the element at index k sink to the correct position. """
        while 2*k <= self.length:
            child = self.priotized_child(k)
            if self.the_array[k] <= self.the_array[child]:
                break
            self.swap(child, k)
            k = child
