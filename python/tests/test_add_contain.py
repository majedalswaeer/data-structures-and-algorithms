from trees.tree import BinaryTree, Node,BinarySearchTree
import pytest
def test_add(my_fix):
    expected=['a','b','c','d']
    actual=my_fix.pre_order()
    assert actual==expected

def test_contain(my_fix):
    expected=True
    actual=my_fix.contains('a')
    assert actual==expected
def test_contain_two(my_fix):
    expected=True
    actual=my_fix.contains('d')
    assert actual==expected

def test_contain_three(my_fix):
    expected=False
    actual=my_fix.contains('q')
    assert actual==expected

@pytest.fixture
def my_fix():
    my_class=BinarySearchTree()
    my_class.add('a')
    my_class.add('b')
    my_class.add('c')
    my_class.add('d')
    return my_class

