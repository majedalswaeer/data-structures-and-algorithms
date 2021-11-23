def insertionSort(list):
    """
    This function takes a list as an input and return the same array with sorted values

    Args:
        list

    Return:
        Sorted list
    """
    i=1
    for i in range(len(list)):
        j=i-1 #0
        temp=list[i] #5
        while j>=0 and temp<list[j]:
            list[j+1]=list[j]
            j=j-1
        list[j+1]=temp
    return list


if __name__ == '__main__':
    x=[2,4,1,5,7]
    print(insertionSort(x))
