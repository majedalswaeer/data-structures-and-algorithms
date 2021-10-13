def insertShiftArray(my_list,middle):
    """
    this function takes two arguments, the first one is a list, the second is the value that you want to put it in the middle in the array_insert_shift
    first will check if the length of the array is odd or even.
    then it will insert the desigred value in the middle of the array
    """
    if len(my_list)%2==0:
        mid_length=int(len(my_list)/2)
        print('even')
        modifed_list=my_list[0:mid_length]+[middle]+my_list[mid_length:]
        return modifed_list
    if len(my_list)%2!=0:
        mid_length=(len(my_list)//2)+1
        print('odd')
        modifed_list=my_list[0:mid_length]+[middle]+my_list[mid_length:]
        return modifed_list






if __name__=="__main__":
    my_list=[1,2,3,4,5,6,7,8]
    middle=0
    print(insertShiftArray(my_list,middle))
