from code_challenges.array_reverse_lab01.reverse_lab01 import reverse_list


def test_reverse():
    l=[1,2,3,4,5]
    expected=[5,4,3,2,1]
    actual=reverse_list(l)
    assert actual==expected

def test_reverse_two():
    l=[1,2,3]
    expected=[3,2,1]
    actual=reverse_list(l)
    assert actual==expected
