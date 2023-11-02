""" Basic class implementation of an array of references"""

from ctypes import py_object


class FixedSizeArray[T]:
    def __init__(self, length: int) -> None:
        """ 
        Creates an array of references to objects of the given length

        The instance variables holding the physical array is constructed
        using the ctypes library to create a py_object (an object that can hold
        a reference to any python object).
        """
        if length <= 0:
            raise ValueError("Array length should be larger than 0.")
        self.array = (length * py_object)()  # initialises the space
        self.array[:] = [None for _ in range(length)] # make every element in space None

    def __len__(self) -> int:
        """ Returns the length of the array"""
        return len(self.array)

    def __getitem__(self, index: int) -> T:
        """ Returns the object in position index."""
        return self.array[index]

    def __setitem__(self, index: int, value: T) -> None:
        """ Sets the object in position index to value"""
        self.array[index] = value
