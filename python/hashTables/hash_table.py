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

    # def __str__(self):
    #     """
    #     Stringfy function that return the linked list with it nodes's values in formated way

    #     Returns:
    #         Formated Linked list: String
    #     """
    #     self.cur=self.head
    #     li=[]
    #     while self.cur!=None:
    #         li= li + [(f"{ { self.cur.value } }").replace("'", " ")]
    #         self.cur=self.cur.next_
    #     return ' -> '.join(li + ["NULL"])

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

def left_join(hashTable_f,hashTable_s):
    """
    This function takes two hash tables and return a list or lists that contain keys and its corresponding values

    Args:
        hashTable_f: Hash Table
        hashTable_s: Hash Table

    Returns:
        k_coress_value: list containing strings or integers
    """
    k_coress_value=[]
    for i in hashTable_f._HashTable__buckets:
        for j in hashTable_s._HashTable__buckets:
            if i and j:
                cur=i.head
                cur1=j.head
                while cur and cur1:
                    if cur.value[0]==cur1.value[0]:
                        res=[cur.value[0],cur.value[1],cur1.value[1]]
                        k_coress_value.append(res)
                    cur=cur.next_
                    cur1=cur1.next_
    return k_coress_value


if __name__ =='__main__':
    hash_1=HashTable()
    hash_2=HashTable()
    hash_1.add('majed','whats')
    hash_1.add('ahmed','going')
    hash_1.add('zaid','on')
    hash_2.add('majed','the')
    hash_2.add('ahmed','meaning')
    hash_2.add('zaid','of')
    print(left_join(hash_1,hash_2))

