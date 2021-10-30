from stacks_and_queues.shelter import AnimalShelter

def test_one():
    my_dog=AnimalShelter()
    my_dog.enqueue_Q('dog')
    expected="{ dog } -> NULL"

    actual=str(my_dog)
    assert actual == expected

def test_two():
    my_cat=AnimalShelter()
    my_cat.enqueue_Q('cat')
    expected="{ cat } -> NULL"

    actual=str(my_cat)
    assert actual == expected

def test_three():
    my_dog=AnimalShelter()
    my_dog.enqueue_Q('mouse')
    expected="NULL"

    actual=str(my_dog)
    assert actual == expected
