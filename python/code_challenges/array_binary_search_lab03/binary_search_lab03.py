
def binarySearch(my_list,se_key):

    start = 0
    end = len(my_list)
    mid = 0
    step = 0

    while (start <= end):
        step = step+1
        mid = (start + end) // 2

        if se_key == my_list[mid]:
            return mid

        if se_key < my_list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1




my_list=[1,2,3,4,5]
se_key=1

print(binarySearch(my_list,se_key))
