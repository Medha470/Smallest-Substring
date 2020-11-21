from collections import defaultdict 
  
MAX_CHAR = 256
# Function to find smallest window 
# containing all distinct characters 
def findSubString(strs): 
      
    p = len(strs)
    #Counting all distinct characters
    dist_count = len(set([x for x in strs])) 
      
    curr_count = defaultdict(lambda: 0) 
    count = 0
    start = 0
    min_len = p
    #maintaining a window of characters that contains all characters of given string. 
    for i in range(p): 
        curr_count[strs[i]] += 1
        # If any distinct character matched,then increment count
        if curr_count[strs[i]] == 1: 
            count += 1
        # Trying to minimize the window i.e., check if any character is occurring more no. of times than its occurrence in pattern, if ythen remove it from starting and also remove the useless characters.
        if count == dist_count: 
            while curr_count[strs[start]] > 1: 
                if curr_count[strs[start]] > 1: 
                    curr_count[strs[start]] -= 1
                      
                start += 1
            #updating window size
            len_window = i - start + 1
              
            if min_len > len_window: 
                min_len = len_window 
                start_index = start
    # Return substring starting from start_index and length min_len
    return str(strs[start_index: start_index +
                                 min_len]) 
                                   
# Driver code 
if __name__=='__main__': 
      
    string = input()
    print(len(findSubString(string)))
  
  
