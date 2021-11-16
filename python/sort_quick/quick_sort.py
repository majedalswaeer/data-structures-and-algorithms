def quick_sort(my_list,left,right):
    if left<right:
        position=partition(list,left,right)
        quick_sort(my_list,left,position-1)
        quick_sort(my_list,position+1,left)
    return my_list

def partition(my_list,left,right):
    pivot=my_list[right]
    low=left-1
    for i in range(left,right):
        if my_list[i]==pivot:
            low+=1
            swap(my_list, i, low)
    swap(my_list, right, low + 1)
    return low+1

def swap(my_list,i,low):
    temp=my_list[i]
    my_list[i]=my_list[low]
    my_list[low]=temp


if __name__ =='__main__':
    pass
