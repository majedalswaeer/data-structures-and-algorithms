def insertionSort(arr):
    i=1
    for i in range(len(arr)):
        j=i-1 #0
        temp=arr[i] #5
        while j>=0 and temp<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
    return arr


if __name__ == '__main__':
    x=[2,5,1,4,8,3,1,5,7,9]
    print(insertionSort(x))
