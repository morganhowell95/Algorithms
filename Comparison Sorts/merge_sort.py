#Implementation of merge sort, worst O(nlog) however requires O(n) space complexity
#Merge sort can be described by the following reccurrence: T(n) = 2T(n/2)+c
#This sorting algorithm describes the textbook "divide and conquer" strategy

arr = []
uinput = raw_input("Enter elements of array:\n")
while(uinput):
        arr.append(uinput)
        uinput=raw_input()

# 0 1 2 3 4
#[9,8,7,6,5]
# beg = 0 mid =2 end =4
#left_count = 3 right_count =2
# sub1 = [none,none,none] sub2=[none,none]
# sub1= [9,8,7] sub2=[6,5]
def merge(A, beg, mid, end):
        left_count = (mid-beg)+1
        right_count = (end-mid)
        
        sub_array1 = [None] * left_count
        sub_array2 = [None] * right_count

	for i in range(0, left_count):
		sub_array1[i] = A[beg+i]

	for i in range(0, right_count):
		sub_array2[i] = A[mid+i+1] 		
	
	left_index=0
	right_index=0
	for k in range(beg, end+1):

		sub1_empty = not left_index<len(sub_array1)
		sub2_empty = not right_index<len(sub_array2)

		if (sub2_empty or not sub1_empty and (sub_array1[left_index] <= sub_array2[right_index])):
			A[k] = sub_array1[left_index]
			left_index = left_index + 1
		elif:
			A[k] = sub_array2[right_index]
			right_index = right_index + 1
	return A

#first index should be labeled by index 0
def mergesort(A,start,end):
	a=[]
	if (start<end):
		middle = (start+end)/2
		A = mergesort(A,start,middle)
		A = mergesort(A,middle+1,end)
		A = merge(A,start, middle, end)
	return A
	
#print mergesort(arr,0,len(arr)-1)


#More elegant pythonic solution

list = [3,6,1,4,22222]

def mergeSort(list):
    if len(list) > 1:
        midpoint = len(list)//2
        leftHalf = list[:midpoint]
        rightHalf = list[midpoint:]
        
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        
        i=0
        j=0
        k=0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                list[k] = leftHalf[i]
                i+=1
            else:
                list[k] = rightHalf[j]
                j+=1
            k+=1

        while i < len(leftHalf):
            list[k] = leftHalf[i]
            i+=1
            k+=1
        while j < len(rightHalf):
            list[k] = rightHalf[j]
            j+=1
            k+=1
    return list
    
print mergeSort(list)

