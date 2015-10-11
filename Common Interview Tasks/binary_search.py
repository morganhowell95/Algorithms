

import random

def merge_sort(arr):
    
    if(len(arr)>1):
    
        mid = len(arr)//2
    
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])
        
        
        i=0
        j=0
        k=0
        
        
        while(i<len(left_half) and j<len(right_half)):
            if (left_half[i]<=right_half[j]):
                arr[k] = left_half[i]
                i = i+1
            else:
                arr[k] = right_half[j]
                j=j+1
            k = k+1
    
        while(i<len(left_half)):
            arr[k] = left_half[i]
            i=i+1
            k=k+1
        
        while(j<len(right_half)):
            arr[k] = right_half[j]
            j=j+1
            k=k+1
            
    return arr


def quick_sort(arr):
    less = []
    piv = []
    more = []
    
    if len(arr)>1:
        pivot = arr[0]
        
        for x in arr:
            
            if x<pivot:
                less.append(x)
                
            if x is pivot:
                piv.append(x)
                
            if x>pivot:
                more.append(x)
        
        return quick_sort(less) + piv + quick_sort(more)
    else:
        return arr
    
    
    
def binary_search(arr, num):
    i = 0
    j = len(arr)-1
    found = False
    
    while(not found and i<=j):
        mid = (i+j)//2
        if(arr[mid] is num):
            found = True
        else:
            if(arr[mid]>num): 
                j = mid-1
            if(arr[mid]<num):
                i = mid+1
                
    return found

arr = []
for i in xrange(100):
    a = random.randint(-100, 100)
    arr.append(a)
    
arr = quick_sort(arr)

print arr
print binary_search(arr, 50)





