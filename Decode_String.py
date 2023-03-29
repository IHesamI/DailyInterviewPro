import re


def decodeString(s):
    pattern = re.compile(r'\d\[\w*\]')
    while re.findall(pattern, s):
        for matched in re.findall(pattern, s):
            count = int(matched[0])
            matched:str
            newmatched=matched[1:]
            newmatched=newmatched.replace(']', '')
            newmatched=newmatched.replace('[', '')
            newstring=newmatched*count
            s=s.replace(matched,newstring)
    return s

print(decodeString('2[a2[b]c]'))
# abbcabbc
