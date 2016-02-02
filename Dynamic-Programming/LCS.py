#Longest Unique Subsequence

def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        #I propose we apply part of KMP's substring algo for constructing a prefix/suffix table and count longest stream of 0s
        
        table = [0 for i in range(len(s))]
        unique_char = 1 
        cbuffer = 1
        i = 0
        j = 1
        
        while j<len(s):
            if s[i] == s[j]:
                table[j] = table[j-1]+1
                i+=1
                j+=1
                cbuffer=1
            else:
                k = table[j-1]
                while k>=0:
                    if s[k] == s[j]:
                        table[j] = table[k]+1
                        break
                    elif k!=0:
                        k = table[k-1]
                    else:
                        table[j] = 0
                        cbuffer+=1
                        unique_char = max(cbuffer, unique_char)
                        break;
                i=k
                j+=1
                
        return unique_char

print lengthOfLongestSubstring('au')
