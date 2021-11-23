
def quick_sort(my_list, left, right):
    """
    This function takes a list as an input and return the same array with sorted values

    Args:
        list
        left
        right

    Return:
        Sorted list
    """
    if left < right:
        position = partition(my_list, left, right)
        quick_sort(my_list, left, position-1)
        quick_sort(my_list, position+1, right)
    return my_list


def partition(my_list, left, right):

    pivot = my_list[right]
    low = left -1

    for i in range(left, right):
        if my_list[i] <= pivot:
            low += 1
            swap(my_list, i, low)

    swap(my_list, right, low+1)
    return low +1


def swap(my_list, i, low):

    temp = my_list[i]
    my_list[i] = my_list[low]
    my_list[low] = temp


if __name__ =='__main__':
    x=[2,4,1,6,9,7]
    print(quick_sort(x,0,len(x)-1))
