def has_character_map(str1, str2):
    map_of_str1_to_str2={}
    for i in range(len(str1)):
        char=str1[i]
        if char in map_of_str1_to_str2.keys():
            map_of_str1_to_str2[char]:set()
            map_of_str1_to_str2[char].add(str2[i])
        else:
            map_of_str1_to_str2[char]=set(str2[i])
    for value in map_of_str1_to_str2.values():
        if len(value)!=1:
            return False
    return True


print(has_character_map('abc', 'def'))
# True
print(has_character_map('aac', 'def'))
# False