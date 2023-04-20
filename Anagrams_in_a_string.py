import re
def generatePermutation(string,start,end,list_ofways):  
    current = 0
    if(start == end-1):
       list_ofways.append(string)
    else:   
        for current in range(start,end):  
            x = list(string) 
            temp = x[start]
            x[start] = x[current]  
            x[current] = temp  

            generatePermutation("".join(x),start+1,end,list_ofways);  
            temp = x[start]
            x[start] = x[current]  
            x[current] = temp

def find_anagrams(s:str, t):
    all_ways_of_arranging_t=[]
    generatePermutation(t,0,len(t),all_ways_of_arranging_t)
    list_of_anagrams_index=[]
    for permute in all_ways_of_arranging_t:
        if permute in s:    
            list_of_anagrams_index.append(s.index(permute))
    return list_of_anagrams_index
print(find_anagrams('acdbacdacb', 'abc'))
# [3, 7]
