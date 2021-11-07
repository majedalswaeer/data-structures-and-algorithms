import pytest
from trees.tree import BinaryTree,fizzBuzzTree, K_Node, bffirst_k_tree

def test_one(fixxx):
    #Arrange
    expected = [2, 'fizz', 'fizzBuzz', 'buzz', 1, 'fizz', 22]
    new_tree = fizzBuzzTree(fixxx)

    #Act
    actual = bffirst_k_tree(new_tree)

    #Assert
    assert actual == expected


@pytest.fixture
def fixxx():
  tree = BinaryTree
  a_node = K_Node(2)
  b_node = K_Node(3)
  c_node = K_Node(15)
  d_node = K_Node(85)
  e_node = K_Node(1)
  f_node = K_Node(33)
  g_node = K_Node(22)
  a_node.children.append( b_node)
  a_node.children.append( c_node)
  a_node.children.append( d_node)
  b_node.children.append( e_node)
  b_node.children.append( f_node)
  c_node.children.append( g_node)
  tree.root = a_node
  return tree
