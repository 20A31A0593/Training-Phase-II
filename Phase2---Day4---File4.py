# Insertion Sort 

def insertion_sort(arr):
    
    for i in range(1,len(arr)):
        j=i    #temp=j
        while (arr[j-1]>arr[j] and j>0):
            (arr[j-1], arr[j])=(arr[j],arr[j-1])
            j-=1
    return arr

arr=list(map(int,input().split()))
print(arr)
print(insertion_sort(arr))
