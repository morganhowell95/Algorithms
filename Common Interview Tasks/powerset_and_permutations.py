def powset(arr):
    result = []
    
    if arr:
        
        (head, tail) = (arr[:1],arr[1:])
        for unit in powset(tail):
            result.append(unit)
            result.append(head + unit)
    
    else:
        result.append([])
    return result


#print powset([1,2,3])


def permuteString(string):
    result = []
    if string:
        head = string[:1]
        tail = string[1:]
        
        for unit in permuteString(tail):
            result.append(unit)
            result.append(head + unit)
    else:
        result.append("")
                
    return result

print permuteString("abc")




def permutations(string, step = 0):

    # if we've gotten to the end, print the permutation
    if step == len(string):
        print "".join(string)

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)
