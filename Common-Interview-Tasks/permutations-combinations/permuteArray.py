def permute(arr):
    
    results = []
    def auxpermut(remaining, result):
        if len(remaining)>0:
            for i in range(len(remaining)):
                auxpermut(remaining[:i] + remaining[i+1:],
                         result + [remaining[i]])
        else:
            results.append(result)
            return result
        
    auxpermut(arr, [])
        
    return results


    
    
print permute([1,2,3])



