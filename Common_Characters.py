def common_characters(strs):
    map_of_chars={}
    number_of_words=len(strs)
    for word in strs:
        chars_set=set()
        for char in word:
            if char not in chars_set:
                chars_set.add(char)
        for each_char in chars_set:
            if each_char in map_of_chars.keys():
                map_of_chars[each_char]=map_of_chars[each_char]+1
            else :
                map_of_chars[each_char]=1
    return [char for char,count in map_of_chars.items() if count == number_of_words]
        

print(common_characters(['google', 'facebook', 'youtube']))
# ['e', 'o']
