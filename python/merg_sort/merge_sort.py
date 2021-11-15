def merge_sort(my_list):
    n=len(my_list)
    if n > 1:

        mid = n//2
        left = my_list[:mid]

        right = my_list[mid:]
        merge_sort(left)

        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
                print('r',right)
                print('l',left)
                print('mid',mid)
                print(i,j,k)
                print(my_list)
            else:
                my_list[k] = right[j]
                j += 1
            k += 1
            #

        while i < len(left):
            print('r',right)
            print('l',left)
            print('mid',mid)
            print(i,j,k)
            print(my_list)
            my_list[k] = left[i]
            i += 1
            k += 1
            # print(my_list)
        while j < len(right):
            print('r',right)
            print('l',left)
            print('mid',mid)
            print(i,j,k)
            print(my_list)
            my_list[k] = right[j]
            j += 1
            k += 1
            # print(my_list)
    return my_list

if __name__=='__main__':

    x=[2,4,1,5,7]
    print(merge_sort(x))



