from .hash_table import HashTable
from .helper_classes import BinarySearchTree

def tt(tree1,tree2):
    l1=tree1.tree_breadth_first()
    l2=tree2.tree_breadth_first()
    hashh_table=HashTable()
    results=[]
    for i in l1:
        hashh_table.add(i,1)
    for j in l2:
        if hashh_table.contains(j):
            results.append(j)
    return results


if __name__ == "__main__":
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
  print(tt(tree,tree2))

