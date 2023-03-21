# Bubble Sort

def bubble_sort(arr):
    for i in range(len(arr)-1):
        flag=0
        for j in range(0,len(arr)-1-i):
            if(arr[j]>arr[j+1]):
                flag=1
                (arr[j],arr[j+1])=(arr[j+1],arr[j])
        if(flag==0):
            break
    return arr

arr=list(map(int,input().split()))
print(arr)
print(bubble_sort(arr))
