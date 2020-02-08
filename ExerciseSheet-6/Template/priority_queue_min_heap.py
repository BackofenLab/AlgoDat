#!/usr/bin/python3

class PriorityQueueItem:
    """ Provides a handle for a queue item.
    A simple class implementing a key-value pair,
    where the key is an integer, and the value can
    be an arbitrary object. Index is the heap array
    index of the item.
    """
    def __init__(self, key, value, index):
        self._key = key
        self._value = value
        self._index = index

    def __lt__(self, other):
        """ Enables us to compare two items with a < b.
        The __lt__ method defines the behavior of the
        < (less than) operator when applied to two
        objects of this class. When using the code a < b,
        a.__lt__(b) gets evaluated.
        There are many other such special methods in Python.
        See "python operator overloading" for more details.
        """
        return self._key < other._key

    def get_heap_index(self):
        """ Return heap index of item."""
        return self._index

    def set_heap_index(self, index):
        """ Update heap index of item."""
        self._index = index


class PriorityQueueMinHeap:
    """Priority queue implemented as min heap."""

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._list = []

    """
    TO DO:
    Create methods:
    insert(self, key, value) -> return inserted item object
    get_min(self) -> return item._key and item._value
    delete_min(self) -> return item._key an item._value
    change_key(item, new_key), no return value
    size() -> return current heap size

    Plus your choice of additional helper (private) methods
    Helpful would be e.g.
    _repair_heap_up(), _repair_heap_down(), _swap_items() ...

    Use private methods (_method_name) if they only get accessed within the class.
    Private methods have a leading underscore:
    def _swap_items(self, i, j):
        # Swap items with indices i,j (also swap their indices!)
        ...

    """

if __name__ == "__main__":
    # Create priority queue object.
    pq1 = PriorityQueueMinHeap()
    # Insert some flights into queue.
    pq1_item1 = pq1.insert(1, "Airforce One")
    pq1_item2 = pq1.insert(45,"Bermuda Triangle Blues (Flight 45)")
    pq1_item3 = pq1.insert(666,"Flight 666")
    # ....


