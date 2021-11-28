class Node:
  def __init__ (self,data,left=None,right=None,):
    self.data = data
    self.left = left
    self.right = right
class Queue:
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False

  def enqueue(self,item):
    self.data.append(item)

  def dequeue(self):
    return self.data.pop(0)
class BinaryTree:

  def __init__(self):
    self.root = None

  def tree_breadth_first(self):
    """
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items
    """
    # Queue breadth <-- new Queue()
    breadth = Queue()
    # breadth.enqueue(root)
    breadth.enqueue(self.root)

    list_of_items = []

    while breadth.peek():
      front = breadth.dequeue()
      list_of_items += [front.data]

      if front.left:
        breadth.enqueue(front.left)

      if front.right:
        breadth.enqueue(front.right)

    return list_of_items


class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def add(self,value):
        """
        This function adds a node to the binary tree

        Args:
            value : Str or int
        """
        if not self.root:
            self.root=Node(value)

        else:
            cur=self.root
            while cur:
                if value < cur.data:
                    if not cur.left:
                        cur.left=Node(value)
                        break
                    cur=cur.left
                else:
                    if not cur.right:
                        cur.right=Node(value)
                        break
                    cur=cur.right
