def partition(st,end,arr):

    pvtIdx=st;
    pivot=arr[pvtIdx]

    while(st<end):
        while st<len(arr) and arr[st]<=pivot:
            st+=1

        while arr[end]>pivot:
            end-=1
         
        if(st<end):
              arr[st],arr[end]=arr[end],arr[st]
    arr[end],arr[pvtIdx]=arr[pvtIdx],arr[end]
    return end

def quickSort(st,end,arr):
    if(st<end):
        p=partition(st,end,arr)
        quickSort(st,p-1,arr)
        quickSort(p+1,end,arr)

l=list(map(int,input("Enter array elements sep space").split()))
quickSort(0,len(l)-1,l)
print(l)
