from stacks_and_queues.node import Node
# from node import Node
class Queues:
    """
    Description: This class define the queue

    """
    def __init__(self,front=None):
        self.front = front
        self.rear=None

    def enqueue(self,value):
        """
        Description: This function pushs nodes into the end of the queue when called

        Args:
            value (int or str)
        """
        new_node=Node(value)
        if not self.front:
            self.front = new_node
            self.rear=new_node
        else:
            self.rear=new_node
            new_node.next==None


    def dequeue(self):
        """
        Description: This function remove a node from the front of the queue when called

        """
        if not self.front:
            raise Exception('You cant remove, its empty queue')
        else:
            temp=self.front
            self.front=self.front.next
            temp.next=None
        return temp.value

    def peek(self):
        """
        Description: This function shows the front node in the queue when called
        return: the value of the top node
        """
        if self.front==None:
            raise ValueError('The queue is empty')
        else:
            return self.front.value

    def is_empty_queue(self):
        """
        Description: This function queue if the stack is empty
        return: True, if the queue is empty
                False, if the queue is not empty
        """
        return self.front==None
