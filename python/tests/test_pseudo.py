from stacks_and_queues.pseudo_queue import PseudoQueue
import pytest


def test_pseudo_enqueue(pseudos):

    # Arrange
    expected="{ d } -> { c } -> { b } -> { a } -> {5} -> {4} -> {3} -> {2} -> NULL"

    #Act
    actual=str(pseudos)

    #assert
    assert actual==expected

def test_pseudo_dequeue(pseudos):

    # Arrange
    expected="{ d } -> { c } -> { b } -> { a } -> {5} -> {4} -> {3} -> NULL"
    pseudos.dequeue()

    #Act
    actual=str(pseudos)

    #assert
    assert actual==expected

def test_pseudo_three(pseudos):

    # Arrange
    expected="{ d } -> { c } -> { b } -> { a } -> {5} -> NULL"
    pseudos.dequeue()
    pseudos.dequeue()
    pseudos.dequeue()

    #Act
    actual=str(pseudos)

    #assert
    assert actual==expected

def test_pseudo_exception():

    # Arrange
    my_class=PseudoQueue()

    #assert
    with pytest.raises(Exception):
        pseudos.dequeue()

def test_pseudo_front_rare(pseudos):

    # Arrange
    my_class=PseudoQueue()
    expected_front=3
    expected_rare='d'
    pseudos.dequeue()

    #Act
    actual_front=pseudos.q_front
    actual_rare=pseudos.q_rare

    # Assert
    assert actual_front==expected_front
    assert actual_rare==expected_rare







@pytest.fixture
def pseudos():
    my_class=PseudoQueue()
    my_class.enqueue(2)
    my_class.enqueue(3)
    my_class.enqueue(4)
    my_class.enqueue(5)
    my_class.enqueue('a')
    my_class.enqueue('b')
    my_class.enqueue('c')
    my_class.enqueue('d')
    return my_class
