# Merge Sort
def merge(arr,left,right,middle):
    left_arr=arr[left:middle+1]
    right_arr=arr[middle+1:right+1]

    left_ind=0
    right_ind=0
    ind=left
    while(left_ind<len(left_arr) and right_ind<len(right_arr)):
        if(left_arr[left_ind]<right_arr[right_ind]):
            arr[ind]=left_arr[left_ind]
            left_ind+=1
        else:
            arr[ind]=right_arr[right_ind]
            right_ind+=1
        ind+=1
    while(left_ind<len(left_arr)):
        arr[ind]=left_arr[left_ind]
        left_ind+=1
        ind+=1
    while(right_ind<len(right_arr)):
        arr[ind]=right_arr[right_ind]
        right_ind+=1
        ind+=1
def merge_sort(arr,left,right):
    if(left>=right):
        return
    else:
        mid=(left+right)//2
        merge_sort(arr,left,mid)
        merge_sort(arr,mid+1,right)
        merge(arr,left,right,mid)

arr=list(map(int,input().split()))
print(arr)
n=len(arr)
x=merge_sort(arr,0,n-1)
print(arr)

