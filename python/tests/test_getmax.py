from trees.tree import BinaryTree, Node,BinarySearchTree
import pytest
def test_one(my_fix):
    #Arrange
    expected=6

    #Act
    actual=my_fix.get_max()

    #Assert
    assert actual==expected

def test_two(my_fix):
    #Arrange
    my_fix.add(100)
    expected=100

    #Act
    actual=my_fix.get_max()

    #Assert
    assert actual==expected

def test_three(my_fix):
    #Arrange
    my_fix.add(5)
    expected=6

    #Act
    actual=my_fix.get_max()

    #Assert
    assert actual==expected



@pytest.fixture

def my_fix():
  tree = BinarySearchTree()
  a_node=Node(1)
  b_node=Node(2)
  c_node=Node(3)
  d_node=Node(4)
  e_node=Node(5)
  f_node=Node(6)
  a_node.left = b_node
  a_node.right = c_node

  c_node.left=f_node

  b_node.left = d_node
  b_node.right = e_node
  tree.root=a_node
  return tree
