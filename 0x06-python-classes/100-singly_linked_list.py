#!/usr/bin/python3

"""This class represents a node of a singly linked listt."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """
        Initializes a node instance with the specified data and next_node.

        Parameters:
        - data: The data of the node (must be an integer)
        - next_node: The next node in the linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Set data to value."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next_node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Set next_node to value."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Simple instantiation of a singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.

        Parameters:
        - value: The value of the new Node (must be an integer)
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """String representation of the entire linked list."""
        result = []
        tmp = self.__head
        while tmp is not None:
            result.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(result))
