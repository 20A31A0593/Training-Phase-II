# Selection Sort 

def selection_sort(arr):
    for i in range(len(arr)):
        min_ind=i
        for j in range(i+1, len(arr)):
            if(arr[min_ind]>arr[j]):
                min_ind=j
        (arr[i],arr[min_ind])=(arr[min_ind],arr[i])      #swap(arr[i], rr[min_ind])
    return arr
     
arr=list(map(int,input().split()))
print(arr)
print(selection_sort(arr))
