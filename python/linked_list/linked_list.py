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

    def __iter__(self):

        while self.head != None:
            yield self.head
            self.head = self.head.next

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

    def insert_after(self,value,new_value):
        """
        Insert_after is a method adds a new node with the given new value immediately after the first node that has the value specified

        Arguments: value, new value

        Returns: a list with added node after the value specified

        """
        n = self.cur
        while n is not None:
            if n.value == value:
                break
            n = n.next
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(new_value)
            new_node.next = n.next
            n.next = new_node

    def append(self, new_value):
        """
        Append function adds a node to the end of the list

        Arguments: new value

        Returns: list with a new node in its ending
        """
        n=self.cur
        if n is None:
            print("empty list")
        while n != None:
            if n.next == None:
                n.next = Node(new_value)
                break
            n = n.next


    def insert_before(self,value,new_value):
        """
        Insert_before is a method adds a new node with the given new value immediately before the first node that has the value specified

        Arguments: value, new value

        Returns: a list with added node before the value specified
        """
        n = self.cur
        if n is None:
            print("item not in the list")
        while n is not None:
            if n.value == value:
                self.insert(new_value)
                break
            if n.next.value == value:
                n.next = Node(new_value, n.next)
                break
            n = n.next


    def kthFromEnd(self,k):
        """
        kthFromEnd is a function that return the node’s value that is k places from the tail of the linked list


        Arguments:
        Input: value
        Returns: the the node’s value that is k places from the tail
        """
        n=self.cur
        n = self.head
        l = 0
        while n.next:
            l += 1
            n = n.next
        n = self.head

        if k<0:
            return "It has to be zero and above"

        if k>l:
            return "This index is empty of nodes or the length is smaller than the integer you enterd"

        diff = l-k
        for i in range(l+1):
            print(1)
            if i == diff:
                return n.value
            n = n.next

def zip_lists(list1, list2):
    """
    Description: This function takes two linked lists and zip them togather

    Args:
        list1 : Linked List
        list2 : Linked List

    Raises:
        Exception: Raised if the first list is empty.
        Exception: Raised if the second list is empty.
        Exception: Raised two lists are empty.

    Returns:
        a new ziped linked list
    """
    if not (list1.head):
        raise Exception('First linked list is empty')
    if not (list2.head):
        raise Exception('Second linked list is empty')
    if not (list2.head and list1.head):
        raise Exception('Both linked lists are empty')

    new_list = LinkedList()
    
    list1.cur = list1.head
    list2.cur = list2.head
    new_list.insert(list1.cur.value)
    list1.cur = list1.cur.next
    while list1.cur or list2.cur:
        if list2.cur:
            new_list.append(list2.cur.value)
            list2.cur = list2.cur.next
        if list1.cur:
            new_list.append(list1.cur.value)
            list1.cur = list1.cur.next

        if not (list2.cur or list1.cur):
            return new_list





if __name__ == "__main__":

    f_ll = LinkedList()
    f_ll.insert("a")
    f_ll.append("b")
    f_ll.append("c")
    s_ll = LinkedList()
    s_ll.insert("1")
    s_ll.append("2")
    s_ll.append("3")

    print(s_ll.__str__())
    print(f_ll.__str__())
    print(str(zip_lists(f_ll,s_ll)))














