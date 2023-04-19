def remove_adjacent_dup(s):
  
    list_of_chars=list(s)
    index=0

    while True:
        try:
            if list_of_chars[index]==list_of_chars[index+1]:
                del list_of_chars[index:index+2]
                index=0
                continue
            index+=1
            if index==len(list_of_chars):
                break
        except Exception:
            break
    return "".join(list_of_chars)

print(remove_adjacent_dup("cabba"))
# Start with cabba
# After remove bb: caa
# After remove aa: c
# print c
