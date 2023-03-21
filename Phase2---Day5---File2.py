# Quick Sort

def quick_sort(arr):
    if(len(arr)<=1):
        return arr
    else:
        pivot=arr[0]
        left_arr=[i for i in arr[1:] if i<=pivot]
        right_arr=[i for i in arr[1:] if i>pivot]
        return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)
        

arr=list(map(int,input().split()))
print(arr)
print(quick_sort(arr))
