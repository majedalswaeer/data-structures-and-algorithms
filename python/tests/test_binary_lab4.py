from code_challenges.array_binary_search_lab03.binary_search_lab03 import binarySearch

def test_one():
    x=[1,2,3,4]
    y=3
    expected=2
    actual=binarySearch(x,y)
    assert actual==expected

def test_two():
    x=[1,2,3,4,5,6,7,8]
    y=1
    expected=0
    actual=binarySearch(x,y)
    assert actual==expected

def test_three():
    x=[1,2,3,4,5,6,7,8]
    y=8
    expected=7
    actual=binarySearch(x,y)
    assert actual==expected
