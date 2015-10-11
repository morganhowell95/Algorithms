A = [200,6,5,4,2,1,4,9,0,-20,3,5]

#i =2 j=1 key=5
#A[j]>key, so A[2]=A[1], then j=0
# A[1] = A[0]

print "Instance of problem:"
print A


#Insertion Sort
#AVG: O(n^2)
#worse: O(n^2)
#best: O(n^2)

for i in range(2,len(A)):
	j =  i - 1
	key = A[i]
	while j>=0 and A[j]>key:
		A[j+1] = A[j]
		j= j-1
	A[j+1] = key

print "Sorted Array"
print A

