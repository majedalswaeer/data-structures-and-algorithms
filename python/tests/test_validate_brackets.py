from stacks_and_queues.validate_brackets import validate_brackets

def test_one():
    # Arrange

    char="{}{Code}[Fellows](())"
    expected=True

    #Act
    actual=validate_brackets(char)

    #Assert
    assert actual==expected

def test_two():
    # Arrange

    char="{(})"
    expected=False

    #Act
    actual=validate_brackets(char)

    #Assert
    assert actual==expected

def test_three():
    # Arrange

    char="{"
    expected=False

    #Act
    actual=validate_brackets(char)

    #Assert
    assert actual==expected

def test_three():
    # Arrange

    char="(){}[[]]"
    expected=True

    #Act
    actual=validate_brackets(char)

    #Assert
    assert actual==expected

