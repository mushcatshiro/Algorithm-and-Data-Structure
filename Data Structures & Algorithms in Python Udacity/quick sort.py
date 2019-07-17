"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def partition(arr,low,high): 
    i = ( low-1 )
    pivot = arr[high] 
  
    for j in range(low , high): 
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def quickSort(arr,low,high): 
    if low < high: 

        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)
    return arr

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
n = len(test) 

print quickSort(test,0,n-1)