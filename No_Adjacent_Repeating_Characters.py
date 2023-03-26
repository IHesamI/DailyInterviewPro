def find_coutns(s):
    char_counts = {}
    for char in s:
        if char in char_counts.keys():
            char_counts[char] = char_counts[char]+1
        else:
            char_counts[char] = 1
    return {k: v for k, v in sorted(char_counts.items(), key=lambda item: item[1], reverse=True)}


def _is_possible(char_counts: dict, s_leng):
    for value in char_counts.values():
        other_chars_count = s_leng-value
        if value-other_chars_count > 1:
            return False
    return True

def fill__list(start,end,step,string_as_list,chars_stack,char_counts):
        for i in range(start, end, step):
            string_as_list[i] = chars_stack[-1]
            char_counts[chars_stack[-1]]=char_counts[chars_stack[-1]]-1
            if char_counts[chars_stack[-1]]==0:
                char_counts.pop(chars_stack[-1])
                chars_stack.pop()

def rearrangeString(s):
    char_counts = find_coutns(s)
    if _is_possible(char_counts, len(s)):
        string_as_list = ['' for i in range(len(s))]
        chars_stack = list(char_counts.keys())
        fill__list(0,len(s),2,string_as_list,chars_stack,char_counts)
        fill__list(1,len(s),2,string_as_list,chars_stack,char_counts)
    
        return ''.join(string_as_list)
    

print(rearrangeString('aabbddcdd'))
# cbcabc
