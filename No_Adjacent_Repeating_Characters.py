# TODO ERROR

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


def rearrangeString(s):
    char_counts = find_coutns(s)
    print(char_counts)
    if _is_possible(char_counts, len(s)):
        return_string = ''
        counter = 0
        while True:
            if len(char_counts.keys()) == 0:
                break
            number_of_keys = len(char_counts.keys())
            key = list(char_counts.keys())[counter]
            counter+=1
            counter = counter % number_of_keys
            return_string = return_string+key
            char_counts[key] = char_counts[key]-1
            if char_counts[key] == 0:
                char_counts.pop(key)
        return return_string
    else:
        return None


print(rearrangeString('aabbdddd'))
# cbcabc
