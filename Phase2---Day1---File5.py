# Binary Search using recursive function

def binary_search(arr,low,high,key):
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]<key):
            low=mid+1
            return binary_search(arr,low,high,key)
        elif(arr[mid]>key):
            high=mid-1
            return binary_search(arr,low,high,key)
        else:
            print("Element is found at position:",mid)
            c=1
            return 
    print("Element is not found")
    return
arr=list(map(int,input().split()))
low=0
high=len(arr)-1
key=int(input())
res=binary_search(arr,low,high,key)
