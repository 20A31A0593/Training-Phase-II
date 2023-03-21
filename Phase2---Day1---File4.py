# Binary Search using while loop

arr=[i for i in range(1,11)]
print(arr)
key=3
low=0
high=len(arr)-1
found=False
while low<=high:
    mid=(low+high)//2
    if arr[mid]==key:
        print("found:",mid)
        found=True
        break
    elif key < arr[mid]:
        high=mid-1
    elif key > arr[mid]:
        low=mid+1
    else:
        print("element not found")
