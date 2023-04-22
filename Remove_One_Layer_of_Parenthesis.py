import re
def remove_outermost_parenthesis(s):
    regex=r'\((\(\))*\)'
    matches=re.finditer(regex,s) 
    list_of_groups=[ match.group() for match in matches]
    result=''
    for group in list_of_groups:
        result+=group[1:-1]
    return result

print(remove_outermost_parenthesis('(())()'))
# ()

print(remove_outermost_parenthesis('(()())'))
# ()()

print(remove_outermost_parenthesis('()()()'))
# ' '