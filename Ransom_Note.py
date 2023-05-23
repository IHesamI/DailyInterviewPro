class Solution(object):
  def canSpell(self, magazine, note):
        
    if len(note)>len(magazine):
        return False
    
    dict_of_chars={}
    for i in range(len(magazine)):
        char_inlist=magazine[i]
        if char_inlist in dict_of_chars.keys():
            dict_of_chars[char_inlist]=dict_of_chars[char_inlist]+1
        else:
            dict_of_chars[char_inlist]=1
        try:
            char_in_str=note[i]
            if char_in_str in dict_of_chars.keys():
                dict_of_chars[char_in_str]=dict_of_chars[char_in_str]-1
            else:
                dict_of_chars[char_in_str]= -1
        except Exception:
            continue    
    return len(list(filter(lambda x : x<0,list(dict_of_chars.values()))) )==0

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
# True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
# False
