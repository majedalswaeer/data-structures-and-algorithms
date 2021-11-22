from hashTables import hashtable_inetersection
from hashTables.helper_classes import BinarySearchTree

def test_1():
  tree = BinarySearchTree()
  tree.add('a')
  tree.add('b')
  tree.add('c')
  tree.add('d')
  tree.add('e')
  tree.add('f')
  tree2 = BinarySearchTree()
  tree2.add('A')
  tree2.add('B')
  tree2.add('c')
  tree2.add('d')
  tree2.add('e')
  tree2.add('f')
