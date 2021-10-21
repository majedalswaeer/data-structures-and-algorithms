from stacks_and_queues.stacks import Stacks
import pytest

def test_push(my_stack):
    # Arrange
    expected=3

    #Act
    actual=my_stack.top.value

    #Assert
    assert actual==expected

def test_push_two():

    # Arrange
    my_class=Stacks()
    my_class.push(1)
    expected=1

    #Act

    actual=my_class.top.value

    #Assert

    assert actual==expected

# ______________________________

def test_pop(my_stack):

    expected=3
    actual=my_stack.pop()
    assert actual==expected

def test_pop_exception():
    with pytest.raises(Exception):
        Stacks.pop()
# ______________________________

def test_peek(my_stack):
    # Arrange
    expected=3


    #Act
    actual=my_stack.peek()

    #Assert

    assert actual==expected

def test_peek_exception():
    # Check if the function will give an exception
    my_class=Stacks()
    with pytest.raises(Exception):
        my_class.peek()

# ______________________________

def test_is_empty(my_stack):
    # Arrange
    expected=False


    #Act
    actual=my_stack.is_empty()

    #Assert

    assert actual==expected

def test_is_empty_two():
    # Arrange

    my_class=Stacks()
    expected=True


    #Act
    actual=my_class.is_empty()

    #Assert

    assert actual==expected



@pytest.fixture
def my_stack():
    my_class=Stacks()
    my_class.push(1)
    my_class.push(2)
    my_class.push(3)
    return my_class

