
'''

Given an array with a mix of strings and other arrays (of strings and/or arrays), flatten it into a single array of strings using the programming language of your choice.
'''

#recursively flatten embedded arrays of arbitrary elements
#Solution in Python 2.7
# - Morgan J. Howell

def flatten_array(arr):
    result = []
    for element in arr:
        if type(element) is list:
            result.extend(flatten_array(element))
        else:
            result.append(element)
    return result


#a few test cases to ease the spirits!

failed_tests = False

arr1= [1]
arr2=["hello",5,4,3,2,[5,4,3,[3,4,5,[1]]]]
arr3=[[[],[[4]]],4,5,6,3,[3,4,5,"yo"],0]
arr4=[]

if(len(flatten_array(arr1)) != 1):
    failed_tests=True

if(len(flatten_array(arr2)) != 12):
    failed_tests=True
    
if(len(flatten_array(arr3)) != 10):
    failed_tests=True
    
if(len(flatten_array(arr4)) != 0):
    failed_tests=True

if(failed_tests):
    print "some test cases failed :("
else:
    print "Success - I think you're ready for Weebly!"
        
