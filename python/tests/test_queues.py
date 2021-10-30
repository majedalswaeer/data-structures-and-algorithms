from stacks_and_queues.queues import Queues
import pytest

def test_enqueue():
    # Arrange
    my_class=Queues()
    my_class.enqueue(1)
    expected=1

    #Act
    actual=my_class.rear.value

    #Assert
    assert actual == expected

def test_enqueue_two(queues):
    # Arrange
    expected="d"

    #Act
    actual=queues.rear.value

    #Assert
    assert actual == expected
# _________________________________

def test_dequeue(queues):
    # Arrange
    expected="m"

    #Act
    actual=queues.dequeue()

    #Assert
    assert actual == expected

# _________________________________

def test_peek(queues):
    # Arrange
    expected="m"

    #Act
    actual=queues.peek()

    #Assert
    assert actual == expected


def test_peek_two():
    my_class=Queues()
    with pytest.raises(ValueError):
        my_class.peek()

# _________________________________

def test_is_empty_queue(queues):
    # Arrange
    expected=False


    #Act
    actual=queues.is_empty_queue()

    #Assert

    assert actual==expected


def test_is_empty_queue_two():
    # Arrange

    my_class=Queues()
    expected=True


    #Act
    actual=my_class.is_empty_queue()

    #Assert

    assert actual==expected


@pytest.fixture
def queues():
    my_class=Queues()
    my_class.enqueue("m")
    my_class.enqueue("a")
    my_class.enqueue("j")
    my_class.enqueue("e")
    my_class.enqueue("d")
    return my_class

