from __future__ import annotations
from typing import Any, Optional


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
    next:
        The next node in the list, or None if there are no more nodes.
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # _first:
    #     The first node in the linked list, or None if the list is empty.
    # curr : cursor pointing to nodes during the run

    _first: Optional[_Node]

    def __init__(self) -> None:
        """Initialize an empty linked list.
        """
        self._first = None

    def __len__(self) -> int:
        """Return the number of elements in this list.

        >>> lst = LinkedList()
        >>> len(lst)              # Equivalent to lst.__len__()
        0
        >>> lst = three_items(1, 2, 3)
        >>> len(lst)
        3
        """
        cur_tot = 0
        curr = self._first
        while curr is not None:
            cur_tot += 1
            curr = curr.next
        return cur_tot

    def __contains__(self, item: Any) -> bool:
        """Return whether <item> is in this list.

        Use == to compare items.

        >>> lst = three_items(1, 2, 3)
        >>> 2 in lst                     # Equivalent to lst.__contains__(2)
        True
        >>> 4 in lst
        False
        """
        curr = self._first
        while curr is not None:
            if curr.item == item:
                return True
            curr = curr.next
        return False


class _Doubly_Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None


class Doubly_linked_list:
    def __init__(self):
        self.start_node = None
