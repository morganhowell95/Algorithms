
#calculate the final number with depth of given 
def calculate_depth(arr, depth):
    sum = 0
    for i in range(0,len(arr)):
        if(type(arr[i]) is int):
            sum = sum + (arr[i]*depth)
        else:
            sum = sum + calculate_depth(arr[i],depth+1)
    return sum
            
        


a = [1,[1,[1,5]]]
sum = 58
print calculate_depth(a,1)
