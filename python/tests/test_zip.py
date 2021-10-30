from linked_list.linked_list import Node,  LinkedList,zip_lists
import pytest
def test_zip():
    f_list=LinkedList()
    f_list.insert(1)
    f_list.insert(2)
    f_list.insert(3)
    s_list=LinkedList()
    s_list.insert(4)
    s_list.insert(5)
    s_list.insert(6)

    expected = "{ 3 } -> { 2 } -> { 1 } -> { 6 } -> { 5 } -> { 4 } -> NULL"

    actual = str(zip_lists(f_list, s_list))

def test_zip_2():
    f_list=LinkedList()
    f_list.insert('a')
    f_list.append('b')
    f_list.append('c')
    s_list=LinkedList()
    s_list.insert(1)
    s_list.append(2)
    s_list.append(3)

    expected = "{ a } -> { 1 } -> { b } -> { 2 } -> { c } -> { 3 } -> NULL"

    actual = str(zip_lists(f_list, s_list))

def test_zip_3():
    f_list=LinkedList()
    f_list.insert('a')
    f_list.append('b')
    f_list.append('c')
    s_list=LinkedList()

    with pytest.raises(Exception):
        assert str(zip_lists(f_list, s_list))

def test_zip_4():
    f_list=LinkedList()
    s_list=LinkedList()
    s_list.insert(1)
    s_list.append(2)
    s_list.append(3)

    with pytest.raises(Exception):
        assert str(zip_lists(f_list, s_list))

def test_zip_5():
    f_list=LinkedList()
    s_list=LinkedList()

    with pytest.raises(Exception):
        assert str(zip_lists(f_list, s_list))


