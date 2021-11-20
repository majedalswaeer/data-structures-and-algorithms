from sort_quick.quick_sort import quick_sort
def test_1():
    expected=[1, 2, 4, 6, 7, 9]
    x=[2, 4, 1, 6, 9, 7]

    actual=quick_sort(x,0,len(x)-1)
    assert actual==expected

