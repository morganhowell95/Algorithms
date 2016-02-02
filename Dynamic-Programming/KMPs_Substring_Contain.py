#Knuth-Morris-Pratt's pattern matching Algo
#Final Complexity: O(m+n)


#Subroutine to calculate the prefix/suffix mapping of the pattern
#Time complexity: O(n)
#Space complexity: O(n)
def sconst(pattern):
    p_relation = [0 for i in range(len(pattern))]
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            p_relation[j] = p_relation[j-1] + 1
            i+=1
            j+=1
        else:
            k = p_relation[j-1]
            while k>=0:
                if pattern[k] == pattern[j]:
                    p_relation[j] = p_relation[k]+1
                    break;
                elif k!=0:
                    k = p_relation[k-1]
                else:
                    p_relation[j] = 0
                    break;
            i=k
            j+=1
    return p_relation

#check to see if given string contains a given substring
#Final Complexity: O(m+n)
def contains(s1, pattern):
    #p_relation is an array describing the prefix suffix relation
    #at a given index
    p_relation = sconst(pattern)
    
    i = 0
    j = 0
    
    while i<len(s1) and j<len(pattern):
        if s1[i] == pattern[j]:
            i+=1
            j+=1
	elif j!=0:
            j=p_relation[j-1]
	else:
	    i+=1
            
    return j>=len(pattern)


print sconst('aab')
