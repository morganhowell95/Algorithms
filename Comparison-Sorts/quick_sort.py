


#nonpython implementation of quick-sort
#Expected runtime of quicksort is : O(nlogn), however worsecase time is O(n^2)
#Keep in mind however, quicksort is an inplace sorting algorithm

#Quick sort can be described by the following recurrence equations:
#worst case: T(n)= T(n-1) + O(n)
#best case: T(n) = 2T(n/2) + O(n)

def quicksort(arr, beg, end):
	if beg<end:
		pivot = partition(arr, beg, end) 
		quicksort(arr, beg, pivot-1)
		quicksort(arr, pivot+1, end)
	return arr

def partition(arr, beg, end):
	#we can vastly improve our algorithm by either making the pivot the median
	#or randomly choosing our pivto to arrive at the expected time
	#here we are simplifying things a bit and choosing our pivot to be the last element
	pivot = arr[end]
	i = beg - 1
	for j in range(beg, end):
		if(arr[j]<=pivot):
			i = i+1
			swap(arr, i, j)
	swap(arr, i+1,end)
	return i+1

def swap(arr, i , j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

arr = [12,-123,23,124,4,525,45,1,232,-1,0]
print quicksort(arr,0,len(arr)-1)

#The more pythonic way of doing quick sort:


def quicker_sort(array=[12,4,5,6,7,3,1,15]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quicker_sort(less)+equal+quicker_sort(greater)  
    else: 
        return array
