import re
def parse_number(num):
    pattern=r'^(-?[0-9]*\.?[0-9]*[e[0-9]*$]?)'
    regex=re.compile(pattern=pattern)   
    return True if regex.match(num) else False
    
num=input()

print(parse_number(num))
# True
