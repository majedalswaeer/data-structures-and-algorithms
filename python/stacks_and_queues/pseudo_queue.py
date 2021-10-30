from stacks_and_queues.stacks import Stacks
# from stacks import Stacks
from stacks_and_queues.node import Node
# from node import Node
class PseudoQueue:
    """
    This class defines the pseduo queue
    """

    def __init__(self):
        self.g_stack=Stacks()
        self.t_stack=Stacks()
        self.q_front=None
        self.q_rare=None

    def enqueue(self, value):
        """
        This function push the value given into the giver stack

        Args:
            value: integer or string
        """
        self.g_stack.push(value)
    def dequeue(self):
        """
        This function push the value removed from the giver stack and give it to the taker stack and adjusting the pointers for front and rare after dequeuing
        """
        if self.g_stack.top:
            while not self.g_stack.is_empty():
                g_poped=self.g_stack.pop()
                self.t_stack.push(g_poped)
            t_poped=self.t_stack.pop()
            self.q_front=self.t_stack.top.value
            while not self.t_stack.is_empty():
                self.g_stack.push(self.t_stack.pop())
            self.q_rare=self.g_stack.top.value
            return t_poped
        else:
            raise Exception("The stack is empty, so the queue is empty also")

    def __str__(self):
        """
        This function convert the pseduo queue into a string

        Returns:
            String: Pseudo queue
        """

        li = []
        cur = self.g_stack.top
        while cur!=None:
            li= li + [(f"{ { cur.value } }").replace("'", " ")]
            cur=cur.next
        return ' -> '.join(li + ["NULL"])



if __name__ == '__main__':
    my_class=PseudoQueue()
    my_class.enqueue(2)
    my_class.enqueue(3)
    my_class.enqueue(4)
    my_class.enqueue(5)
    my_class.enqueue('a')
    my_class.enqueue('b')
    my_class.enqueue('c')
    my_class.enqueue('d')

    
    print(my_class.dequeue())
    print(my_class.q_front)
    print(my_class.q_rare)
    print(str(my_class))
