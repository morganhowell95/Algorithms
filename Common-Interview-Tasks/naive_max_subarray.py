def max_subarray(arr):
    current_sum = 0
    current_index = -1
    best_sum = 0
    best_first_index = -1
    best_last_index = -1
    
    for i in xrange(len(arr)):
        val = current_sum + arr[i]
        if val > 0:
            if current_sum is 0:
                current_index = i
            current_sum = val
        else:
            current_sum = 0
            
        if(current_sum>best_sum):
            best_sum=current_sum
            best_first_index = current_index
            best_last_index = i
            
    return arr[best_first_index:best_last_index+1]

arr = [1,-10,5,9,-100,3,4,5,6,7,-1000]
print max_subarray(arr)
                
                
