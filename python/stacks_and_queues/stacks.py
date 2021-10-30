from stacks_and_queues.node import Node
class Stacks:
    """
    Description: This class define the stack

    """
    def __init__(self,top=None):
        self.top=top

    def push(self,value):
        """
        Description: This function pushs nodes into the stack when called

        Args:
            value (int or str)
        """
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        """
        Description: This function remove a node from the stack when called
        return: the value of the removed node
        """
        if self.top==None:
            raise Exception("You cant remove, Stack is Empty")
        else:
            temp=self.top
            self.top=self.top.next
            temp.next=None
        return temp.value


    def peek(self):
        """
        Description: This function shows the top node in the stack when called
        return: the value of the top node
        """
        if self.top==None:
            raise Exception("There is no value, Stack is Empty")
        else:
            return self.top.value


    def is_empty(self):
        """
        Description: This function checks if the stack is empty
        return: True, if the stack is empty
                False, if the stack is not empty
        """
        return self.top==None



