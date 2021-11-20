from insertion_sort.insertion_sort import  insertionSort
def test_1():
    #Arrange
    x=[1,3,4,2]
    expected=[1,2,3,4]

    #Act
    actual=insertionSort(x)

    #Assert
    assert actual==expected


def test_2():
    #Arrange
    x=[7,2]
    expected=[2,7]

    #Act
    actual=insertionSort(x)

    #Assert
    assert actual==expected
