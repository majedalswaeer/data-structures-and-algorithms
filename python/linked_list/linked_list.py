class Node:
    """
    A class representing a Node

    Attributes
    ----------


    Methods
    -------
    __init__(data, next_):
        the constructor method for the class, it takes two parameters, the data parameter is the a reference to the data the node will hold, and the next_

    """

    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class LinkedList:
    """
    A class for creating instances of a Linked List.

    Data and other attributes defined here:

    head: Node | None

    Methods defined here:

    1- insert(value: any)

    2- includes(value: any) return boolean value

    3- to_string return formatted string
    """

    def __init__(self):
        self.head = None
        self.cur = None

    def insert(self, value):
        """
        Insert creates a Node with the value that was passed and adds
        it to the head of the linked list shifting all other values down

        Arguments:
        value : any

        Returns: None
        """
        self.head = Node(value, self.head)
        self.cur = self.head

    def includes(self, value):
        """
        Includes Indicates whether that value exists as a Node’s value somewhere within the list.

        Arguments:
        value : value

        Returns: Boolean
        """
        self.cur = self.head

        while self.cur != None:
            if self.cur.value == value:
                return True
            next_node=self.cur.next
            self.cur =next_node
        return False

    def __str__(self):
        """
        Includes Indicates whether that value exists as a Node’s value somewhere within the list.

        Arguments: none

        Returns: a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL"
        """
        li = []
        self.cur = self.head
        while self.cur!=None:
            li= li + [(f"{ { self.cur.value } }").replace("'", " ")]
            self.cur=self.cur.next
        return ' -> '.join(li + ["NULL"])
