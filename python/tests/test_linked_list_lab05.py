from linked_list.linked_list import Node,  LinkedList

def test_new_linked_list_is_empty():
    #Arrange
    my_class = LinkedList()
    expected = None

    #Act
    actual = my_class.head

    #Assert
    assert actual == expected

def test_insert_into_the_linked_list():
    # Arrange any data that you need to run your test
    expected = 1

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = node.value

    # Assert
    assert actual == expected


def test_head_pointer():
    # Arrange
    my_class=LinkedList()
    my_class.insert("10")
    my_class.insert("9")
    expected = "9"

    # Act
    actual=my_class.head.value

    # assert
    assert actual == expected

def test_insert_multiple():
    #Arrange
    my_class = LinkedList()
    my_class.insert("4")
    my_class.insert("3")
    my_class.insert("2")
    my_class.insert("1")
    expected_1 = "1"
    expected_2 = "2"
    expected_3 = "3"
    expected_4 = "4"

    #Act
    actual_1 = my_class.head.value
    actual_2 = my_class.head.next.value
    actual_3 = my_class.head.next.next.value
    actual_4 = my_class.head.next.next.next.value

    #Assert
    assert actual_1 == expected_1
    assert actual_2 == expected_2
    assert actual_3 == expected_3
    assert actual_4 == expected_4

def test_includes_return_true():
    # Arrange
    my_class = LinkedList()
    my_class.insert("4")
    my_class.insert("3")
    my_class.insert("2")
    my_class.insert("1")
    expected=True

    # Act
    actual=my_class.includes("4")

    # assert
    assert actual==expected

def test_includes_return_falsee():
    # Arrange
    my_class = LinkedList()
    my_class.insert("4")
    my_class.insert("3")
    my_class.insert("2")
    my_class.insert("1")
    expected=False

    # Act
    actual=my_class.includes("9")

    # assert
    assert actual==expected

def test_toString():
    # Arrange
    my_class = LinkedList()
    my_class.insert("3")
    my_class.insert("2")
    my_class.insert("1")
    expected="{ 1 } -> { 2 } -> { 3 } -> NULL"

    # Act
    actual=my_class.to_string()

    # assert
    assert actual==expected
