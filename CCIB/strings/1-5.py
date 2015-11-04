def compressString(string):

        if not string: return string
        
        past_letter = string[0]
        letter_count = 1
        stored_counts = []
        for i in range(1, len(string)):
                current_letter = string[i]
                
                if(current_letter == past_letter):
                        letter_count = letter_count+1
                        if i == len(string)-1:
                            stored_counts.append((i,letter_count))
                else:
                        stored_counts.append((i-1,letter_count))
                        letter_count=1
                        
                past_letter = string[i]
        
        padding=0
        for i in range(len(stored_counts)):
                
                if(stored_counts[i][1] != 1 and stored_counts[i][0] is len(string)-1):
                        string = string + str(stored_counts[i][1])
                        
                elif(stored_counts[i][1] != 1):
                        string = string[:stored_counts[i][0]+1+padding] + str(stored_counts[i][1]) + string[stored_counts[i][0]+1+padding:]
                if(stored_counts[i][1] != 1):
                    padding=padding+1
            
        return string

