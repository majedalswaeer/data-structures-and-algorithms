class Node:
    """
    Class to initialize a node
    """
    def __init__(self,value):
        """
        Constructor to initialize a node's value

        Args:
            value ([type]): Any
        """
        self.value=value
        self.next_=None

class LinkedList:
    def __init__(self):
        """
        Constructor method for the linked list. To Initializes the head of a linked list.

        """
        self.head=None

    def insert(self,value):
        """
        Description:Insert function inserts a node at the beganning of the linked list

        Args:
            value: String or integers
        """
        new_node=Node(value)
        new_node.next_=self.head
        self.head=new_node

    def __str__(self):
        """
        Stringfy function that return the linked list with it nodes's values in formated way

        Returns:
            Formated Linked list: String
        """
        self.cur=self.head
        li=[]
        while self.cur!=None:
            li= li + [(f"{ { self.cur.value } }").replace("'", " ")]
            self.cur=self.cur.next_
        return ' -> '.join(li + ["NULL"])

class HashTable:
    """
    Class to crate a hash table

    """
    def __init__(self,size=1024):
        """
        Constructor of the hash table to Initializes the size and buckets

        Args:
            size (int, optional)[description]. Defaults to 1024.
        """
        self.__size=size
        self.__buckets=[None]*size

    def __hash(self,key):
        """
        Hash function which hash the given key with specfic number

        Args:
            key ([type]): Any

        Returns:
            Integer
        """
        return sum([ord(char) for char in str(key)]) * 599 % self.__size


    def add(self,key,value):
        """
        Add function adds a key/value pair into the hash table

        Args:
            key ([type]): Any
            value ([type]): Any
        """
        index=self.__hash(key)

        if not self.__buckets[index]:
            self.__buckets[index]=LinkedList()
        self.__buckets[index].insert([key,value])

    def get(self,key):
        """
        Get function retrive a value that is associated with the given key

        Args:
            key ([type]): Any

        Returns:
            Value if existed (Any type of data)
            Exception if the key does not exist
        """

        index=self.__hash(key)
        if self.__buckets[index]:
            cur=self.__buckets[index].head
            while cur:
                if cur.value[0]==key:
                    return cur.value[1]
                cur=cur.next_
            return Exception('The key given is not exicted in the hashmap')

    def contains(self,key):
        """
        Contain function checks whether if the key given existed or not in the hash table

        Args:
            key ([type]): Any

        Returns:
            [type]: Boolean
        """
        index=self.__hash(key)
        if self.__buckets[index]:
            cur=self.__buckets[index].head
            while cur:
                if cur.value[0]==key:
                    return True
                cur=cur.next_
        return False

if __name__ =='__main__':
    l1=LinkedList()
    q=HashTable()
    l1.insert(1)
    l1.insert(2)
    l1.insert(3)
    print(q.__hash(l1.head.value))

