class Node:
  def __init__ (self,data,left=None,right=None):
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

  def bfs(self):
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

  def pre_order(self):
    """
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items

    sub method : walk () to make the recursion staff
    """
    list_of_items = []
    def walk(node):
      if node:
        list_of_items.append(node.data)
        if node.left:
          walk(node.left)
        if node.right:
          walk(node.right)

    walk(self.root)
    return list_of_items

  def in_order(self):
    """
    function to in order the list using Trees
    """
    list_of_items = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        list_of_items.append(node.data)
        if node.right:
          walk(node.right)

    walk(self.root)
    return list_of_items

  def post_order(self):
    """
    A binary tree method which returns a list of items in post order

    input: None

    output: tree items
    """
    list_of_items = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        if node.right:
          walk(node.right)
        list_of_items.append(node.data)

    walk(self.root)
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
                if not cur.left:
                    cur.left=Node(value)
                    break
                cur=cur.left

                if not cur.right:
                    cur.right=Node(value)
                    break
                cur=cur.right

    def contains(self,value):
        """
        This function checks if a value existed in the binary tree or not

        Args:
            value : Str or int
        return: True or False
        """

        if not self.root:
            raise Exception("Binary tree has no babas nor children")
        else:
            cur=self.root
            while cur:
                if value == cur.data:
                    return True
                else:
                    if cur.left:
                        if value==cur.left.data:
                            return True
                        else:
                            cur=cur.left
                    elif cur.right:

                        if value==cur.right.data:
                            return True
                        else:
                            cur=cur.right
                    else: return False


    




if __name__ == "__main__":
  tree = BinarySearchTree()
  # tree.add(1)
  # tree.add(2)
  # tree.add(3)
  # tree.add(4)
  # tree.add(5)
  # tree.add(5)
  # ss=BinaryTree()
#   a_node.left = b_node
#   a_node.right = c_node

#   c_node.left=f_node

#   b_node.left = d_node
#   b_node.right = e_node

#   Add Root node to tree
#   tree.root=a_node
#   tree.add('1')
#   tree.add('2')
#   tree.add('3')
#   tree.add('4')

  print(tree.find_maximum_value())


