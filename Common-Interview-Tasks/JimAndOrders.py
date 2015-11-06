import sys

#merge sort in a stable form taking into account order time
def mergesort(arr):
    if len(arr)>1:
        midpoint = len(arr)//2
        left_half = arr[:midpoint]
        right_half = arr[midpoint:]
        
        
        mergesort(left_half)
        mergesort(right_half)
        
        i = 0
        j = 0
        k = 0
        
        while(i<len(left_half) and j<len(right_half)):
            if(left_half[i][3] == right_half[j][3]):
                if left_half[i][0] <= right_half[i][0]:
                    arr[k] = left_half[i]
                    i+=1
                else:
                    arr[k] = right_half[j]
                    j+=1 
            elif(left_half[i][3] <= right_half[j][3]):
                arr[k] = left_half[i]
                i+=1
            else:
                arr[k] = right_half[j]
                j+=1
            k+=1
            
        while(i<len(left_half)):
            arr[k] = left_half[i]
            i+=1
            k+=1
            
        while(j<len(right_half)):
            arr[k] = right_half[j]
            j+=1
            k+=1
            
    return arr



# Enter your code here. Read input from STDIN. Print output to STDOUT
count = raw_input()

#appropriate data into list of tuples
customers = []
for i in range(1,int(count)+1):
    serve = raw_input().split()
    time = int(serve[0])
    process = int(serve[1])
    customers.append((i,time, process, time+process))
    
customers = mergesort(customers)

for i in customers:
    sys.stdout.write(str(i[0]))
    sys.stdout.write(" ")
    

            
           
                
        
