from merg_sort.merge_sort import merge_sort


def test_merge_sort():
    x=[20,18,12,8,5,-2]
    expected=[-2,5,8,12,18,20]
    actual=merge_sort(x)
    assert actual==expected

