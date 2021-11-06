import pytest
from trees.tree import BinaryTree, Node,BinarySearchTree,fizzBuzzTree

def test_one(fix):

    expected=[1, 2, 4, 'buzz', 'fizz', 'fizz', 'fizzBuzz']
    actual=fizzBuzzTree(fix).pre_order()

    assert actual==expected




@pytest.fixture
def fix():
  tree = BinarySearchTree()
  a_node=Node(1)
  b_node=Node(2)
  c_node=Node(3)
  d_node=Node(4)
  e_node=Node(5)
  f_node=Node(6)
  node_15=Node(15)

  a_node.left = b_node
  a_node.right = c_node

  c_node.left=f_node
  c_node.right=node_15

  b_node.left = d_node
  b_node.right = e_node
  tree.root=a_node
  return tree
